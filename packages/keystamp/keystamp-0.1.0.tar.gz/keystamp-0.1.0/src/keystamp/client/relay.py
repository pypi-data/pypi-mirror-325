"""
Request relay
"""

import json
import copy
import logging
import time
import os
from typing import Callable, Literal, Tuple
from dataclasses import asdict
from datetime import datetime
import httpx
from mitmproxy.http import Headers, HTTPFlow, Request, Response

from keystamp.client.local import LocalSigner
from keystamp_common.types import (
    SignedTranscript,
    Signature,
    HTTPRequest,
)
from keystamp_common.config import (
    get_keystamp_sign_path,
    KS_RELAY_OFFICIAL_TIMEOUT_SECS,
)
from keystamp_common.versions import SIGNED_TRANSCRIPT_VERSION, API_PROTOCOL_VERSION
from keystamp_common.signing import transcript_from_message_pair

logger = logging.getLogger(__name__)


class RequestRelay:
    """Request relay component

    The request relay accepts intercepted requests, relays them to their
    final destinations, and hands back a signed Transcript bundle.

    This is either:
        If we don't need to sign the request, put https back on the URL,
        make the request, and return the response.

        If we do need to sign the request, pass request to a Keystamp signing
        server, and return the response.

    Args:
        check_sign_eligible: A callback that returns True if the request
            respresents content that is eligible for signing. This doesn't
            necessarily mean we need to sign it, e.g. if it already exists
            in the vault.
    """

    def __init__(
        self,
        signing_mode: Literal["local", "official", "none"],
        sign_eligible_checker: Callable[[Request], bool],
        signed_transcript_handler: Callable[[SignedTranscript], None],
        local_signer: LocalSigner,
    ):
        self.signing_mode = signing_mode
        self.sign_eligible_checker = sign_eligible_checker
        self.signed_transcript_handler = signed_transcript_handler

        # Signing component
        self.local_signer = local_signer

    # --------------------------------------------------------------------------
    # Main interface: Called by iproxy to give us intercepted requests
    # --------------------------------------------------------------------------

    def handle_request(self, flow: HTTPFlow) -> Response:
        """Handle a request intercepted by the interceptor.

        Once the intercepting proxy has intercepted a request, it runs this
        method to actually do something with it. Typically, this involves
        fulfilling the request, signing and saving a transcript, and returning
        the response.

        Do not change its interface: this format is required by mitmproxy.
        """


        try:
            if not self.sign_eligible_checker(flow.request):
                return self.local_passthrough(flow)

            # TODO: Call out to check_transcript_exists and return this instead
            # if it does. (To start, let's sign everything that reaches this)

            if self.signing_mode == "local":
                response = self.local_passthrough(flow)
                signed_transcript = self.local_signer.sign(flow.request, response)
                self.signed_transcript_handler(signed_transcript)
                return response

            elif self.signing_mode == "official":
                response, signature = self.official_proxy(flow)

                if signature is not None:

                    # Package up a SignedTranscript
                    transcript = transcript_from_message_pair(
                        flow.request,
                        response,
                    )

                    signed_transcript = SignedTranscript(
                        transcript=transcript,
                        signature=signature,
                    )

                    self.signed_transcript_handler(signed_transcript)

                return response

            else:  # Signing disabled
                response = self.local_passthrough(flow)
                return response

        except Exception as e:
            # If our processing fails for any reason, mitmproxy's default behavior
            # is to continue processing the request as if we didn't exist.
            # This is bad UX: Users need to be informed that signing failed.
            # We translate any top-level exceptions into a 500 error.

            flow.response = Response.make(
                status_code=500,
                content=str(e).encode("utf-8"),
                headers=Headers([(b"Content-Type", b"text/plain")]),
            )
            flow.response.reason = b"Internal Server Error (Keystamp relay exception)"

            logger.error(f"Error relaying request: {e}")
            raise e


    # --------------------------------------------------------------------------
    # Main operations
    # --------------------------------------------------------------------------

    def local_passthrough(self, flow: HTTPFlow) -> Response:
        """Pass a request through to its intended destination."""

        # Assemble request in httpx
        client = httpx.Client(
            trust_env=False,
            timeout=30.0,
        ) # Ignore env vars, e.g. HTTP_PROXY
        req = client.build_request(
            method=str(flow.request.method),
            url=str(flow.request.url),
            headers=flow.request.headers,
            content=flow.request.content,
        )

        resp = client.send(req)

        # Package the response as mitmproxy Response
        if "content-encoding" in resp.headers:
            # Proxy will have already decompressed the response
            resp.headers.pop("content-encoding")
        headers_mitm = tuple(
            (k.encode("utf-8"), v.encode("utf-8")) for k, v in resp.headers.items()
        )

        mitm_resp = Response(
            http_version=resp.extensions["http_version"],
            status_code=resp.status_code,
            reason=resp.extensions["reason_phrase"],
            headers=headers_mitm,
            content=resp.content,
            trailers=None,
            timestamp_start=time.time(),
            timestamp_end=None,
        )

        return mitm_resp

    def official_proxy(self, flow: HTTPFlow) -> Tuple[Response, Signature | None]:
        """Relay a request to the official proxy.
        
        This is a slightly involved process:

        1. Package the request into JSON format required by official signing servers
        2. Fire off the request to the signing server
        3. Receive the response, which contains a signature in the HTTP header
        4. Return the response and official signature for packaging into a
           SignedTranscript
        """

        # Package and fire off request

        # Outer request components
        inner_request_obj = self._format_request_for_proxy(flow.request)
        outer_request_body = json.dumps(asdict(inner_request_obj))
        outer_request_url = get_keystamp_sign_path()
        outer_request_method = "POST"

        # Build the request
        client = httpx.Client(
            trust_env=False,
            timeout=KS_RELAY_OFFICIAL_TIMEOUT_SECS,
        ) # Ignore env vars, e.g. HTTP_PROXY
        outer_request = client.build_request(
            method=outer_request_method,
            url=outer_request_url,
            content=outer_request_body,
        )

        # Add API protocol version to the request
        outer_request.headers["Keystamp-API-Version"] = str(API_PROTOCOL_VERSION)

        # Send the request
        outer_response = client.send(outer_request)

        # Handle non-200 outer responses
        if outer_response.status_code != 200:
            if outer_response.status_code == 403:
                raise Exception(
                    "Keystamp: Rate limit exceeded: "
                    "See GitHub for rate limit increases")
            else:
                raise Exception(f"Keystamp: Unexpected server error: {outer_response.status_code}")

        # Unpack the inner response
        inner_response_dict = json.loads(outer_response.content.decode())
        
        # Handle non-200 inner responses
        if inner_response_dict["status_code"] == 200:

            # Remove content-encoding header if present
            # (Proxy will have already decompressed the response)
            if "content-encoding" in inner_response_dict["headers"]:
                inner_response_dict["headers"].pop("content-encoding")

            # Extract Keystamp signature
            assert "Keystamp-Signature" in inner_response_dict["headers"]
            signature_str = inner_response_dict["headers"]["Keystamp-Signature"]
            signature_json = json.loads(signature_str)
            signature = Signature(**signature_json)
            inner_response_dict["headers"].pop("Keystamp-Signature")

        else:
            signature = None

        # Convert headers to mitmproxy format
        header_tuples = [
            (k.encode(), v.encode())
            for k, v in inner_response_dict["headers"].items()
        ]

        # Package this into a mitmproxy Response
        mitm_resp = Response(
            http_version=outer_response.extensions["http_version"],
            status_code=inner_response_dict["status_code"],
            reason=outer_response.extensions["reason_phrase"],
            headers=header_tuples,
            content=inner_response_dict["body"].encode(),
            trailers=None,
            timestamp_start=time.time(),
            timestamp_end=None,
        )

        # Hand this back to the user's calling code
        return mitm_resp, signature


    # --------------------------------------------------------------------------
    # Helper functions
    # --------------------------------------------------------------------------

    def _format_request_for_proxy(self, request: Request) -> HTTPRequest:
        """Package a request for transmission to the official proxy.
        
        Returns:
            An HTTPRequest object
        """

        # Build URL with port if not standard
        scheme = request.scheme
        host = request.host
        port = request.port
        path = request.path if isinstance(request.path, str) else request.path.decode()
        
        # Include port in URL unless it's standard for the scheme
        if (scheme == "http" and port != 80) or (scheme == "https" and port != 443):
            url = f"{scheme}://{host}:{port}{path}"
        else:
            url = f"{scheme}://{host}{path}"

        request_dict = {}
        request_dict["url"] = url
        request_dict["method"] = str(request.method)
        request_dict["headers"] = dict(request.headers)
        request_dict["body"] = request.content.decode() # Bytes to string
        return HTTPRequest(**request_dict)