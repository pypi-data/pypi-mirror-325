"""Transcript vault"""

import json
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from typing import Dict, List

from keystamp_common.types import SignedTranscript, Transcript, Signature


class Vault:
    """Transcript vault: Manages storage and retrieval of transcripts"""

    def __init__(self, transcript_dir: Path):

        # Create the transcript directory if it doesn't exist
        self.transcript_dir = transcript_dir
        self.transcript_dir.mkdir(parents=True, exist_ok=True)

        # Build transcript index
        self.transcript_hashes: Dict[str, str] = self._index_transcripts()

    # --------------------------------------------------------------------------
    # Public interface
    # --------------------------------------------------------------------------

    def contains(self, transcript_hash: str) -> bool:
        """Check if a transcript with the given hash exists in the vault"""
        return transcript_hash in self.transcript_hashes

    def load_transcript(self, transcript_hash: str) -> SignedTranscript:
        """Load a transcript from the vault, or raise an error if it doesn't exist

        Raises:
            FileNotFoundError: If the transcript doesn't exist.
        """
        if transcript_hash not in self.transcript_hashes:
            raise FileNotFoundError(f"Transcript {transcript_hash} not found in vault")

        # Get the date directory where the transcript is stored
        date_dir = self.transcript_hashes[transcript_hash]
        transcript_dir = self.transcript_dir / date_dir

        # Load the transcript and signature files
        with open(
            transcript_dir / f"{transcript_hash}.json", "r", encoding="utf-8"
        ) as f:
            transcript_json = json.load(f)
            transcript = Transcript(**transcript_json)
        with open(
            transcript_dir / f"{transcript_hash}.sig", "r", encoding="utf-8"
        ) as f:
            signature = json.load(f)
            signature = Signature(**signature)

        return SignedTranscript(
            transcript=transcript,
            signature=signature,
        )

    def save_transcript(self, signed_transcript: SignedTranscript):
        """Save a transcript to the vault"""

        # Setup save
        save_date = datetime.now().strftime("%Y-%m-%d")
        save_dir = self.transcript_dir / save_date
        save_dir.mkdir(parents=True, exist_ok=True)

        # Calculate transcript hash
        transcript_json = json.dumps(
            signed_transcript.transcript.to_dict(), sort_keys=True
        )
        transcript_hash = signed_transcript.transcript.hash_sha256()

        # Save transcript and signature
        with open(save_dir / f"{transcript_hash}.json", "w", encoding="utf-8") as f:
            f.write(transcript_json)
        with open(save_dir / f"{transcript_hash}.sig", "w", encoding="utf-8") as f:
            f.write(json.dumps(signed_transcript.signature.to_dict()))

        # Add to transcript index
        self.transcript_hashes[transcript_hash] = save_date

    # --------------------------------------------------------------------------
    # Helper functions
    # --------------------------------------------------------------------------

    def _index_transcripts(self) -> Dict[str, str]:
        """Index transcripts in the transcript directory

        Transcript folders are organized as:
            transcript_dir/YYYY-MM-DD/transcript_hash.(json,sig)
        """

        transcript_hashes: Dict[str, str] = {}  # transcript_hash -> YYYY-MM-DD

        # Iterate over all
        for transcript_dir in self.transcript_dir.iterdir():
            if not transcript_dir.is_dir():
                continue

            for transcript_file in transcript_dir.iterdir():
                if transcript_file.name.endswith(".sig"):
                    transcript_hash = transcript_file.name[:-4]
                    transcript_date = transcript_dir.name
                    transcript_hashes[transcript_hash] = transcript_date

        return transcript_hashes
