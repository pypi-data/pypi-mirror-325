"""

The interceptor gives us access to the flow of requests and responses.

It uses a local HTTP proxy to intercept outgoing web requests. The proxy hands
intercepted requests to a request handler callback, which handles our application
logic, somehow services the request (varies by signing mode), and hands back a
response to the requestor.
"""

from typing import Callable

from .iproxy import InterceptingProxy


class Interceptor:
    """Interceptor component

    The interceptor gives us access to the flow of requests and responses.
    """

    def __init__(self, request_handler: Callable, port: int | None):
        self.port = port
        self.iproxy = InterceptingProxy(port=port, request_handler=request_handler)

    def start(self):
        """Start the interceptor."""

        # Start proxy
        self.iproxy.start()

    def stop(self):
        """Stop the interceptor."""

        # Stop proxy
        self.iproxy.stop()
