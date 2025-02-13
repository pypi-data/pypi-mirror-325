"""Local signing component

When Keystamp is run with signer="local", we use this component to sign requests
and responses locally, instead of farming out to a signing server.

Relay calls this component with a request and response, and this component
returns the SignedTranscript bundle for saving.
"""

import json
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import List
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from mitmproxy.http import Request, Response
from typeguard import check_type

from keystamp_common.config import (
    DEFAULT_LOCAL_KEY_FILENAME_PEM,
    DEFAULT_LOCAL_KEY_FILENAME_PUB,
)
from keystamp_common.signing import transcript_from_message_pair
from keystamp_common.types import SignedTranscript, Transcript, Signature
from keystamp_common.versions import SIGNED_TRANSCRIPT_VERSION

# --------------------------------------------------------------------------
# Local signing component
# --------------------------------------------------------------------------

class LocalSigner:
    """Local signing component"""

    def __init__(self, local_key_dir: str):

        # Ensure the key directory exists
        os.makedirs(local_key_dir, exist_ok=True)

        # Load or generate keys
        pem_path = os.path.join(local_key_dir, DEFAULT_LOCAL_KEY_FILENAME_PEM)
        pub_path = os.path.join(local_key_dir, DEFAULT_LOCAL_KEY_FILENAME_PUB)

        if not os.path.exists(pem_path) and not os.path.exists(pub_path):
            # Generate a new Ed25519 key pair for signing
            self._private_key = ed25519.Ed25519PrivateKey.generate()
            self._public_key = self._private_key.public_key()

            # Save the keys to disk
            with open(pem_path, "wb") as f:
                f.write(
                    self._private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.PKCS8,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )
            with open(pub_path, "wb") as f:
                f.write(
                    self._public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo,
                    )
                )

        elif os.path.exists(pem_path) and os.path.exists(pub_path):
            # Load existing keys
            with open(pem_path, "rb") as f:
                pem_data = f.read()

            self._private_key = serialization.load_pem_private_key(pem_data, None)
            if not isinstance(self._private_key, ed25519.Ed25519PrivateKey):
                raise ValueError("Invalid private key file")
            self._public_key = self._private_key.public_key()
        else:
            # We don't want to accidentally overwrite a private key,
            # so let's raise an error if one is missing
            raise ValueError(
                f"Either both or neither of {pem_path} and {pub_path} must exist"
            )

    def sign(self, request: Request, response: Response) -> SignedTranscript:
        transcript: Transcript = transcript_from_message_pair(request, response)
        signature = self.sign_transcript(transcript)
        return SignedTranscript(
            transcript=transcript,
            signature=signature,
        )

    def sign_transcript(self, transcript: Transcript) -> Signature:
        """Sign a transcript using Ed25519 signing.

        Args:
            transcript: The transcript to sign

        Returns:
            Signature: The signature of the transcript
        """
        # Validate: Transcript should match type
        check_type(transcript, Transcript)

        # Convert transcript to bytes for signing
        # We use json.dumps with sort_keys=True to ensure consistent byte representation
        transcript_bytes = json.dumps(transcript.to_dict(), sort_keys=True).encode()

        # Hash and sign the transcript bytes, get base64 encoded signature
        transcript_digest = hashlib.sha256(transcript_bytes).digest()
        signature_bytes = self._private_key.sign(transcript_digest)
        signature = signature_bytes.hex()

        # Compile full signature
        signature = Signature(
            version=SIGNED_TRANSCRIPT_VERSION,
            keypair_id="local",
            timestamp=datetime.now().isoformat(),
            signature=signature,
            algorithm="ed25519", # TODO: Is there some programmatic field?
        )

        return signature

