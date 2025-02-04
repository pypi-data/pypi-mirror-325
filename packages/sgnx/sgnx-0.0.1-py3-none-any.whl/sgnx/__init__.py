"""Top-level package for sgnx.

import flattening and version handling
"""

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "?.?.?"

# Import flattening
from sgnx.transforms import Power
