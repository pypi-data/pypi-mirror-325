# Supply __version__ from pyproject.toml
try:
    from importlib.metadata import version as _version
except ImportError:
    # Python < 3.8: Use backported solution
    from importlib_metadata import version as _version

try:
    __version__ = _version("keystamp")
except Exception:
    # Fallback for dev environments
    from keystamp_common.versions import CLIENT_VERSION_DEV
    __version__ = CLIENT_VERSION_DEV

# Main client interfaces
from keystamp.client.interface import sign_from_python as sign
from keystamp.client.interface import verify_from_python as verify
