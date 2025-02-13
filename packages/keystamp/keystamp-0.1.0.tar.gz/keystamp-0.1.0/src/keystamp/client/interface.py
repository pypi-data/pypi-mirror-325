"""Keystamp client interface

This component is responsible for user interface: To the user, config, and to all
subcomponents (setting up, etc.).

To be more specific, we provide two interfaces:
    keystamp.sign() for usage from within Python
    A command-line interface for signing arbitrary command-line operations

This typically results in running the user's code within a SigningContext.
"""

import contextlib
import importlib.util
import logging
import os
import runpy
import sys
from collections import ChainMap
from pathlib import Path
from typing import Any, ContextManager, Dict, List, Literal, Optional, Union

import click
from typeguard import check_type
from dotenv import load_dotenv
from keystamp.client.sign import SigningContext
from keystamp.client.verify import Keychain, verify_transcript_dir
from keystamp_common import config
from keystamp_common.config import (
    DEFAULT_LOCAL_KEY_FILENAME_PUB,
    DEFAULT_PROXY_PORT,
    DEFAULT_KEYSTAMP_DIR,
)


# --------------------------------------------------------------------------
# Global setup
# --------------------------------------------------------------------------

# Load environment variables for entire process
load_dotenv()

# Set up logging
logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------
# Shared config validation
# --------------------------------------------------------------------------


def validate_transcript_dir(
    transcript_dir: Optional[Union[str, Path]],
    source: Literal["cli", "python"],
) -> Path:
    if transcript_dir is None:
        transcript_dir = config.DEFAULT_OFFICIAL_TS_DIR

    # Create transcript dir if it doesn't exist
    transcript_dir = Path(transcript_dir)
    transcript_dir.mkdir(parents=True, exist_ok=True)

    return transcript_dir


def validate_target_proxy_port(target_proxy_port: Optional[int]) -> int | None:
    if target_proxy_port is not None:
        assert isinstance(target_proxy_port, int)
        assert 0 <= target_proxy_port <= 65535

    return target_proxy_port


# --------------------------------------------------------------------------
# Unified validation and context manager setup
# --------------------------------------------------------------------------


def get_sign_cm(
    locals: Dict[str, Any],
    source: Literal["cli", "python"],
) -> ContextManager[SigningContext]:
    """Returns a context manager for signing API calls.

    The CLI and Python interfaces are very similar, so we use the same function
    to validate user inputs and initialize the context manager.
    """

    # Validate user config
    transcript_dir = validate_transcript_dir(locals["transcript_dir"], source)
    target_port = validate_target_proxy_port(locals["port"])
    assert locals["signing_mode"] in ["local", "official", "none"]

    # User config is now validated: create context manager
    return SigningContext(
        transcript_dir=transcript_dir,
        signing_mode=locals["signing_mode"],
        target_port=target_port,
    )


def verify_validate_and_call(
    transcript_dir: Path,
    public_key: Path | None,
    verbose: bool,
) -> bool:
    # Ensure that transcript_dir exists and is a directory
    transcript_dir = Path(transcript_dir)
    if not transcript_dir.exists():
        raise click.UsageError(f"Transcript directory {transcript_dir} does not exist")
    if not transcript_dir.is_dir():
        raise click.UsageError(
            f"Transcript directory {transcript_dir} is not a directory"
        )

    print(f"\nKeystamp: Verifying transcripts at `{transcript_dir}`:")

    # If public_key is provided, ensure it exists and is a file
    if public_key is not None:
        public_key = Path(public_key)
        if not public_key.exists():
            raise click.UsageError(f"Public key {public_key} does not exist")
        if not public_key.is_file():
            raise click.UsageError(f"Public key {public_key} is not a file")

    # If public_key is not provided, ensure default keys exist
    if public_key is None:
        local_key_path = (
            Path(config.DEFAULT_KEYSTAMP_DIR) / DEFAULT_LOCAL_KEY_FILENAME_PUB
        )
        if not local_key_path.exists():
            raise click.UsageError(f"Local key {local_key_path} does not exist")

        # TODO
        # official_key_path = Path(config.DEFAULT_KEYSTAMP_DIR) / DEFAULT_OFFICIAL_KEY_FILENAME_PUB
        # if not official_key_path.exists():
        #     raise click.UsageError(f"Official key {official_key_path} does not exist")

    all_verified = verify_transcript_dir(
        transcript_dir,
        public_key=public_key,
        verbose=verbose,
    )

    if all_verified:
        print(f"    Verification successful: All transcripts verified!\n")
    else:
        print(f"    Verification failed: Some transcripts did not match their digital signatures.\n")

    return all_verified


# --------------------------------------------------------------------------
# Frontend code: Python and CLI
#
# Some duplication of documentation below, so that CLI and Python users both
# have a usable interface.
# --------------------------------------------------------------------------


@contextlib.contextmanager
def sign_from_python(
    # Core options
    transcript_dir: Optional[Union[str, Path]] = config.DEFAULT_OFFICIAL_TS_DIR,
    signing_mode: Literal["local", "official", "none"] = "local",
    port: Optional[int] = None,
) -> None:  # ContextManager[SigningContext]:
    """Start capturing and signing web requests.

    Creates a context that automatically handles setup and cleanup of the proxy
    and transcript management. When the context exits, any buffered transcripts
    are saved and the proxy is shut down.

    This interface is currently experimental and subject to change.

    Args:
        transcript_dir: Directory to save signed transcripts to
        signing_mode: Which signer to use for signing. Use 'official' to send to Keystamp's signing server, 'local' for self-signing (during development), or 'none' to skip signing.
        port: Local Keystamp proxy port, auto-assigned if not specified
    """
    cm = get_sign_cm(locals(), "python")
    with cm as context:
        yield context


def verify_from_python(
    transcript_dir: Path = Path(config.DEFAULT_OFFICIAL_TS_DIR),
    public_key: Path | None = None,
    verbose: bool = False,
) -> bool:
    """Verify the transcripts in a directory.

    Args:
        transcript_dir: Directory that contains transcripts to verify
        public_key: Verify against a specific public key. If not provided, uses .keystamp/local_key.pub and .keystamp/official_key.pub
    """
    return verify_validate_and_call(
        transcript_dir,
        public_key,
        verbose,
    )


@click.group()
def main():
    pass


@main.command(
    name="sign",
    help="Sign the execution of a Python module or file",
    context_settings={
        "ignore_unknown_options": True,
        "allow_extra_args": True,
    },
)
@click.option(
    "--transcript-dir",
    type=click.Path(exists=False, file_okay=False, writable=True),
    default=config.DEFAULT_OFFICIAL_TS_DIR,
    show_default=True,
    help="Directory to save signed transcripts to",
)
@click.option(
    "--signing-mode",
    "-s",
    type=click.Choice(["local", "official", "none"]),
    default="official",
    show_default=True,
    help="Which signer to use for signing. Use 'official' to send to Keystamp's signing server, 'local' for self-signing (during development), or 'none' to skip signing.",
)
@click.option(
    "--port",
    "-p",
    type=click.INT,
    default=DEFAULT_PROXY_PORT,
    help="Local Keystamp proxy port to use",
)
@click.argument(
    "target",
    required=False,
    # help="Python module or file to sign",
)
@click.option(
    "--module",
    "-m",
    is_flag=True,
    required=False,
    help="Run target as a module",
)
# Collects the args to run the command with
@click.argument(
    "target_args",
    nargs=-1,
    type=click.UNPROCESSED,
    # help="Arguments to run the target with",
)  # Collects the command user wants to sign (keystamp sign -- <command>)
def sign_from_cli(
    transcript_dir: Path,
    signing_mode: Literal["local", "official", "none"],
    port: int | None,
    target: str,
    module: bool,
    target_args: List[str],
):
    """
    Signs the entire run of a Python module or file.

    Examples:
        'keystamp sign your_script.py --your_args'
        'keystamp sign -m your_module --your_args'

    Todo:
        Handle target args which overlap with keystamp CLI args. Can be done by
            manually parsing sys.argv. Deferred for now.
    """

    cm = get_sign_cm(locals(), "cli")

    # Validate target
    if not target:
        raise click.UsageError("No target provided")

    # Without -m, we must be able to locate the target file
    if not module:
        if not Path(target).exists():
            raise click.UsageError(f"Target file {target} does not exist")

    # With -m, we must be able to locate the target module
    if module:
        if not importlib.util.find_spec(target):
            raise click.UsageError(f"Target module {target} does not exist")

    # Run target within context using runpy
    with cm as sign:
        runstring = f"Keystamp: Signing command: `python {target}`"
        if target_args:
            runstring += f" {' '.join(target_args)}"
        click.echo(runstring)

        # Save outer argv, setup inner argv
        outer_argv = sys.argv
        sys.argv = [target, *target_args]

        if module:
            runpy.run_module(target, run_name="__main__")
        else:
            runpy.run_path(target, run_name="__main__")

        # Restore sys.argv
        sys.argv = outer_argv

        click.echo(f"Keystamp: Done: Transcripts saved to `{sign.transcript_dir}`")


@main.command(
    name="verify",
    help="Verify the transcripts in a directory",
)
@click.argument(
    "transcript_dir",
    type=click.Path(exists=True, file_okay=False, writable=False),
)
@click.option(
    "--public-key",
    type=click.Path(exists=True, file_okay=True, writable=False),
    help="Verify against a specific public key. If not provided, uses .keystamp/local_key.pub and .keystamp/official_key.pub",
)
@click.option(
    "--concise",
    is_flag=True,
    default=False,
    help="Print concise output",
)
def verify_from_cli(
    transcript_dir: Path,
    public_key: Path | None,
    concise: bool,
):
    all_verified = verify_validate_and_call(
        transcript_dir,
        public_key,
        verbose=not concise,
    )

    if all_verified:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
