"""Transcript verification

This module handles verifying signed transcripts.
"""

import os
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Tuple
from enum import Enum
import importlib.resources
import hashlib
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.types import PublicKeyTypes
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import padding, utils
from keystamp_common import config
from keystamp_common.types import Signature
from keystamp_common.versions import SIGNED_TRANSCRIPT_VERSION

# --------------------------------------------------------------------------
# Main public interface
# --------------------------------------------------------------------------

def verify_transcript_dir(
    transcript_dir: Path,
    public_key: Path | None = None,
    verbose: bool = False,
) -> bool:
    """Verify the transcripts in a directory.

    Basic input validation done in interface.py.

    Args:
        transcript_dir: Directory containing transcripts to verify
        public_key: Verify against a specific public key.
        verbose: Whether to emit detailed verification output

    Returns:
        True if all transcripts are verified, False otherwise
    """

    # Setup keychain with appropriate configuration based on public_key
    keychain = Keychain(
        custom_key_paths=[] if public_key is None else [public_key],
        use_local_keychain=public_key is None,  # Only use local keychain if no specific key
        use_official_keychain=public_key is None,  # Only use official keychain if no specific key
    )

    return verify_transcript_dir_inner(transcript_dir, keychain, verbose)

# --------------------------------------------------------------------------
# Keychain
# --------------------------------------------------------------------------

class KeyType(Enum):
    CUSTOM = "custom"
    OFFICIAL = "official"
    LOCAL = "local"

KeyID = str

class Keychain:
    """Represents a specific set of public keys to be used for verification.

    Public keys are stored as dictionaries of key IDs to key bytes. Key IDs
    vary by key type:
        - Custom keys: Absolute path to key file
        - Official keys: Filename of key file in .resources/keys
        - Local key: Absolute path to key file

    Args:
        custom_key_paths: If provided, add these keys to keychain
        use_local_keychain: If True, add local keys to keychain from .keystamp
            directory, if it exists
        use_official_keychain: If True, add official Keystamp keys to keychain
    """

    def __init__(
            self,
            custom_key_paths: List[Path],
            use_local_keychain: bool = True,
            use_official_keychain: bool = True,
        ):

        # Setup
        self.custom_keys: Dict[str, PublicKeyTypes] = {}
        self.local_keys: Dict[str, PublicKeyTypes] = {}
        self.official_keys: Dict[str, PublicKeyTypes] = {}

        # Add custom keys
        for path in custom_key_paths:
            key = self._load_public_key(path)
            self.custom_keys[str(path.absolute())] = key

        # Add local keys
        if use_local_keychain:
            local_key_path = Path(config.DEFAULT_KEYSTAMP_DIR) / \
                config.DEFAULT_LOCAL_KEY_FILENAME_PUB
            if local_key_path.exists():
                key = self._load_public_key(local_key_path)
                self.local_keys[str(local_key_path.absolute())] = key

        # Add official keys
        if use_official_keychain:
            try:
                keys_dir = importlib.resources.files(
                    "keystamp.resources").joinpath("keys")
                for key_file in keys_dir.iterdir():
                    if key_file.name.endswith(".pub"):
                        key_id = key_file.name[:-4]  # Remove .pub extension
                        key_bytes = key_file.read_bytes()
                        key = serialization.load_pem_public_key(key_bytes)
                        self.official_keys[key_id] = key
            except (FileNotFoundError, ImportError) as e:
                logging.warning(f"Failed to load official keys: {e}")
            except Exception as e:
                logging.error(f"Unexpected error loading official keys: {e}")

    def verify_transcript(
            self, 
            transcript_path: Path,
            signature_path: Path,
            verbose: bool,
        ) -> Tuple[bool, Tuple[KeyType, KeyID] | None]:
        """Verify a signed transcript against the current keychain.

        Tries keys in the following order:
            - Custom keys: Specifically provided by user
            - Local keys: In .keystamp directory
            - Official keys: Within package

        Args:
            transcript_path: Path to the transcript to verify
            signature_path: Path to the signature to verify
            verbose: Whether to emit detailed verification output

        Returns:
            (False, None) if verification fails for all keys
            (True, (KeyType, KeyID)) for the first key that verifies successfully
        """
        
        # Load transcript and signature
        transcript_bytes_raw = transcript_path.read_bytes()
        transcript_digest = hashlib.sha256(transcript_bytes_raw).digest()

        try:
            signature_json = json.loads(signature_path.read_text())
        except json.JSONDecodeError as e:
            if verbose:
                logging.error(f"Invalid signature file: {e}")
            return False, None

        # Check that signature version <= current signing protocol version
        # (Do this with raw json, in case the data structure has changed)
        if int(signature_json["version"]) > SIGNED_TRANSCRIPT_VERSION:
            raise ValueError(
                f"Transcript was signed with a newer signing protocol version "
                f"({signature_json['version']}) than your client "
                f"supports ({SIGNED_TRANSCRIPT_VERSION}). Please update Keystamp."
            )

        # Parse into Signature object and bytes
        try:
            signature = Signature(**signature_json)
            signature_bytes = bytes.fromhex(signature.signature)
        except (ValueError, TypeError) as e:
            print(f"    Error: Failed to parse signature file: {e}")
            return False, None

        MAX_PATH_DISPLAY_LENGTH = 60
        PATH_RHS_CHARS = 8
        transcript_path_display = str(transcript_path)
        if len(transcript_path_display) > MAX_PATH_DISPLAY_LENGTH:
            transcript_path_display = transcript_path_display[
                :MAX_PATH_DISPLAY_LENGTH - PATH_RHS_CHARS
            ] + "..." + transcript_path_display[-PATH_RHS_CHARS:]
        
        # Did the user ask to use a specific key?
        if len(self.custom_keys) > 0:
            for key_id, key in self.custom_keys.items():
                try:
                    key.verify(signature_bytes, transcript_digest)
                    print(f"    ✅ CUSTOM KEY:   {transcript_path_display}")
                    return True, (KeyType.CUSTOM, key_id)
                except InvalidSignature:
                    print(f"    ❌ CUSTOM KEY:   {transcript_path_display}")

            # Failed to verify with any custom key
            print(f"    Error: Failed to verify with any custom key: {transcript_path}")
            return False, None

        # Does the signature specify that it's a local key?
        elif signature.keypair_id == "local":
            for key_id, key in self.local_keys.items():
                try:
                    key.verify(signature_bytes, transcript_digest)
                    print(f"    👉 LOCAL KEY:    {transcript_path_display}\n" + 
                          f"                     Self-signed transcript: Not verified by Keystamp")
                    return True, (KeyType.LOCAL, key_id)
                except InvalidSignature:
                    print(f"    ❌ LOCAL KEY:    {transcript_path_display}")
                    return False, None

        # Is the keypair ID on our official key list?
        elif signature.keypair_id in self.official_keys:
            try:
                self.official_keys[signature.keypair_id].verify(
                    signature=signature_bytes,
                    data=transcript_digest,
                    padding=padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    algorithm=utils.Prehashed(hashes.SHA256()),
                )
                print(f"    ✅ OFFICIAL KEY: {transcript_path_display}")
                return True, (KeyType.OFFICIAL, signature.keypair_id)
            except InvalidSignature:
                print(f"    ❌ OFFICIAL KEY: {transcript_path_display}")
                return False, None

        # Otherwise, we have no idea what to do
        else:
            print(f"    Warning: Unknown keypair ID: {signature.keypair_id}")
            return False, None
        

    def _load_public_key(self, public_key_path: Path) -> PublicKeyTypes:
        """Load a public key from a file."""
        with open(public_key_path, "rb") as f:
            key_raw = f.read()

        key = serialization.load_pem_public_key(key_raw)
        return key

# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def verify_transcript_dir_inner(
    transcript_dir: Path,
    keychain: Keychain,
    verbose: bool,
) -> bool:
    """Verify the transcripts in a directory.

    Basic input validation done in interface.py.

    Args:
        transcript_dir: Directory containing transcripts to verify
        keychain: Keychain to use for verification
        verbose: Whether to emit detailed verification output

    Returns:
        True if all transcripts are verified, False otherwise
    """

    all_pass = True

    # Recurse through transcript directory, looking for any JSON files
    for path_child in transcript_dir.iterdir():

        # Folder: Recurse
        if path_child.is_dir():
            all_pass &= verify_transcript_dir_inner(path_child, keychain, verbose)

        # File: Verify
        elif path_child.is_file():
            if path_child.suffix == ".json":
                # There must be a matching .sig file
                sig_path = path_child.with_suffix(".sig")
                if not sig_path.exists():
                    all_pass = False
                    print(f"    Error: No matching signature file found for {path_child}")
                    continue

                # Verify transcript
                success, key_info = keychain.verify_transcript(
                    path_child, sig_path, verbose
                )
                if not success:
                    all_pass = False

    return all_pass

