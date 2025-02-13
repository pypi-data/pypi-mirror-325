"""

Local proxy for intercepting requests.

- Listens for HTTP proxy requests via os.environ['HTTP_PROXY']
- Relays them to our handlers for fulfillment and signing
- Collects responses from handlers, hands back to client

"""

import asyncio
import logging
import os
import socket
import threading
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Mapping, Optional, Union

from mitmproxy import options
from mitmproxy.http import HTTPFlow
from mitmproxy.tools.dump import DumpMaster

from keystamp_common.config import (
    DEFAULT_PROXY_DIR,
    DEFAULT_PROXY_HOST,
    DEFAULT_PROXY_PORT,
    DEFAULT_PROXY_SETUP_TIMEOUT_SECS,
    DEFAULT_PROXY_CA_CERT_FILENAME,
)

logger = logging.getLogger(__name__)


class ProxyEnvironment:
    """Manages proxy-related environment variables."""

    def __init__(self):
        # Store original environment values
        self._original_env = {
            "HTTP_PROXY": os.environ.get("HTTP_PROXY"),
            'HTTPS_PROXY': os.environ.get('HTTPS_PROXY'),
            "http_proxy": os.environ.get("http_proxy"),
            'https_proxy': os.environ.get('https_proxy'),
            "NO_PROXY": os.environ.get("NO_PROXY"),
            "no_proxy": os.environ.get("no_proxy"),
            "SSL_CERT_FILE": os.environ.get("SSL_CERT_FILE"),
        }

    def set_proxy(
        self,
        host: str,
        port: int,
        no_proxy: Optional[List[str]] = None,
        proxy_ca_cert_path: Optional[Path] = None,
    ):
        """Set proxy-related environment variables."""
        proxy_url = f"http://{host}:{port}"

        # Set proxy variables (both upper and lower case for compatibility)
        os.environ["HTTP_PROXY"] = proxy_url
        os.environ['HTTPS_PROXY'] = proxy_url
        os.environ["http_proxy"] = proxy_url
        os.environ['https_proxy'] = proxy_url
        os.environ["SSL_CERT_FILE"] = str(proxy_ca_cert_path)

        # Set NO_PROXY if specified
        if no_proxy:
            no_proxy_str = ",".join(no_proxy)
            os.environ["NO_PROXY"] = no_proxy_str
            os.environ["no_proxy"] = no_proxy_str

    def restore(self):
        """Restore original environment variables."""
        for key, value in self._original_env.items():
            if value is None: # No original value
                os.environ.pop(key, None)  # Remove entirely
            else:
                os.environ[key] = value


class CallbackAddon:
    """Addon that calls a callback function."""

    def __init__(
        self,
        request_handler: Callable,
    ):
        self.request_handler = request_handler

    def request(self, flow: HTTPFlow) -> None:
        # Result always provided by handler
        # (Required because even if we want to pass through,
        #  we need to put HTTPS back onto the request)
        flow.response = self.request_handler(flow)

    def response(self, flow: HTTPFlow) -> None:
        pass


class InterceptingProxy:
    """Proxy that intercepts requests to HTTP_PROXY."""

    def __init__(
        self,
        port: int | None = DEFAULT_PROXY_PORT,
        request_handler: Callable = None,
    ):
        logger.debug("Initializing KeystampProxy")
        self.port: int | None = port or DEFAULT_PROXY_PORT
        self.host = DEFAULT_PROXY_HOST
        self.socket = None
        self.running = False
        self.addons = [CallbackAddon(request_handler=request_handler)]
        self._proxy_thread = None
        self._ready = threading.Event()
        self.loop = None

        # Initialize environment manager
        self.env_manager = ProxyEnvironment()

        self.proxy_dir = Path(DEFAULT_PROXY_DIR)
        self.proxy_dir.mkdir(parents=True, exist_ok=True)
        self.proxy_ca_cert_path = self.proxy_dir / DEFAULT_PROXY_CA_CERT_FILENAME

        # Set up mitmproxy options
        self.opts = options.Options(
            listen_port=self.port,
            listen_host=self.host,
            confdir=str(self.proxy_dir),
        )
        logger.debug(
            f"Configured mitmproxy options: host={self.host}, port={self.port}"
        )

        # Initialize master but don't start
        self.master = None

    def _run_proxy(self):
        """Run the proxy in a separate thread."""

        # Create a new event loop for the proxy
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        try:
            # Initialize master and start in event loop
            self.master = DumpMaster(
                self.opts,
                loop=self.loop,
                with_termlog=False,
                with_dumper=False,
            )
            self.master.addons.add(*self.addons)
            proxy_task = self.loop.create_task(self.master.run())
            self.loop.run_forever()
            self.loop.run_until_complete(proxy_task)
        except Exception as e:
            logger.error(f"Error in proxy thread: {e}")
        finally:
            # Clean up the loop in this thread
            tasks = asyncio.all_tasks(self.loop)
            for t in tasks:
                if not t.done() and not t.cancelled():
                    t.cancel()

            self.loop.run_until_complete(
                asyncio.gather(
                    *tasks,
                    return_exceptions=True,
                )
            )
            self.loop.close()

    def start(self):
        """Start the proxy server and wait until it's ready."""
        if self.running:
            logger.debug("Proxy already running")
            return

        logger.debug("Starting proxy server")

        # Start proxy in a background thread
        logger.debug("Starting proxy thread")
        self._proxy_thread = threading.Thread(target=self._run_proxy)
        self._proxy_thread.daemon = True
        self._proxy_thread.start()
        self.running = True

        # Wait for proxy to be ready by attempting to connect
        logger.debug("Waiting for proxy to be ready")
        start_time = time.time()
        started = False
        while time.time() - start_time < DEFAULT_PROXY_SETUP_TIMEOUT_SECS:
            try:
                with socket.create_connection((self.host, self.port), timeout=0.1):
                    logger.debug("Proxy is ready")
                    self._ready.set()
                    started = True
                    break
            except (socket.timeout, ConnectionRefusedError) as e:
                logger.debug(f"Connection attempt failed: {e}")
                time.sleep(0.1)

        if not started:
            logger.error("Proxy failed to start within setup timeout")
            raise TimeoutError("Proxy failed to start within setup timeout")

        # Set up environment
        logger.debug("Setting up proxy environment")
        self.env_manager.set_proxy(
            self.host,
            self.port,
            proxy_ca_cert_path=self.proxy_ca_cert_path,
        )

    def wait_ready(
        self, timeout: Optional[float] = DEFAULT_PROXY_SETUP_TIMEOUT_SECS
    ) -> bool:
        """Wait until the proxy is ready to handle requests.

        Args:
            timeout: Maximum time to wait in seconds. None means wait forever.

        Returns:
            True if proxy is ready, False if timeout occurred.
        """
        return self._ready.wait(timeout=timeout)

    def is_ready(self) -> bool:
        """Check if proxy is ready to handle requests."""
        return self._ready.is_set()

    def stop(self):
        """Stop the proxy server and clean up."""
        if not self.running:
            return

        # Shutdown master using the event loop's thread-safe scheduler.
        if self.master:
            try:
                # Schedule the shutdown on the proxy thread's event loop.
                self.loop.call_soon_threadsafe(self.master.shutdown)
                # Also stop the event loop to exit run_forever().
                self.loop.call_soon_threadsafe(self.loop.stop)
            except Exception as e:
                logger.error(f"Error shutting down proxy master: {e}")
            self.master = None

        # Wait for the background thread to finish.
        if self._proxy_thread and self._proxy_thread.is_alive():
            self._proxy_thread.join(timeout=DEFAULT_PROXY_SETUP_TIMEOUT_SECS)

        if self._proxy_thread and self._proxy_thread.is_alive():
            logger.error("Proxy thread failed to stop")
            raise RuntimeError("Proxy thread failed to stop")

        # Restore the original environment.
        self.env_manager.restore()

        self._ready.clear()
        self.running = False

    def wait_stop(
        self, timeout: Optional[float] = DEFAULT_PROXY_SETUP_TIMEOUT_SECS
    ) -> bool:
        """Wait until the proxy is stopped."""
        if not self._proxy_thread:
            return True

        self._proxy_thread.join(timeout=timeout)
        return not self._proxy_thread.is_alive()

    def is_running(self) -> bool:
        """Check if proxy is running."""
        return self.running
