"""Core application logic for the signing process

This component is the main internal-facing interface for the signing process.
It starts key subcomponents and provides the context manager used for signing
requests.
"""

import logging
from pathlib import Path
from typing import Literal
from urllib.parse import urlparse

from mitmproxy.http import Request

from keystamp.client.intercept.mpatch.core import Interceptor
from keystamp.client.relay import RequestRelay
from keystamp.client.local import LocalSigner
from keystamp.client.vault import Vault
from keystamp_common.config import DEFAULT_KEYSTAMP_DIR
from keystamp_common.types import SignedTranscript
from keystamp_common.config import get_whitelisted_domains

class SigningContext:
    """Context manager for signing web requests.

    This class is responsible for orchestrating the signing process. It assumes
    inputs have been validated (via interface.py).
    """

    def __init__(
        self,
        transcript_dir: Path,
        signing_mode: Literal["local", "official", "none"],
        target_port: int | None,
    ):
        """Initialize the signing context.

        Components are initialized here and started at __enter__ below.
        """

        # Store inputs and basic state
        self.nesting_depth = 0  # For nested metadata annotation calls
        self.transcript_dir = transcript_dir
        self.signing_mode = signing_mode
        self.target_port = target_port

        # Vault
        self.vault = Vault(
            transcript_dir=transcript_dir,
        )

        # Signer
        self.local_signer = LocalSigner(local_key_dir=DEFAULT_KEYSTAMP_DIR)

        # Relay
        self.relay = RequestRelay(
            signing_mode=signing_mode,
            sign_eligible_checker=self.is_signable,
            signed_transcript_handler=self.store_signed_transcript,
            local_signer=self.local_signer,
        )

        # Interceptor: Catches requests and passes them to Relay
        self.interceptor = Interceptor(
            request_handler=self.relay.handle_request,
            port=target_port,
        )

    # --------------------------------------------------------------------------
    # Context manager enter/exit
    # --------------------------------------------------------------------------

    def __enter__(self) -> "SigningContext":
        """Start the proxy when entering the context."""

        self.nesting_depth += 1

        if self.nesting_depth == 1:
            # First time entering the context: start underlying components

            # Start proxy and wait for it to be ready (sets environment variables)
            self.interceptor.start()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Stop the proxy when exiting the context."""

        self.nesting_depth -= 1
        if self.nesting_depth == 0:
            # We've exited the outermost context: Restore environment

            # Stop proxy (restores environment variables)
            self.interceptor.stop()

    # --------------------------------------------------------------------------
    # Hooks
    # --------------------------------------------------------------------------

    def is_signable(self, request: Request) -> bool:
        """Does this request need to be signed?

        Kept here to separate signing application logic from relay logic.
        """
        # Get the whitelisted domains
        whitelisted_domains = get_whitelisted_domains()

        # Check if the request URL is whitelisted
        parsed_url = urlparse(request.url)
        return parsed_url.netloc.split(":")[0] in whitelisted_domains

    def store_signed_transcript(self, signed_transcript: SignedTranscript) -> None:
        """Save a signed transcript to the vault."""

        self.vault.save_transcript(signed_transcript)
        logging.debug(f"Saved transcript to vault: {signed_transcript}")
