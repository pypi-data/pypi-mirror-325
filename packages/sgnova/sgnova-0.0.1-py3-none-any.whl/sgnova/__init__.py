"""Top-level package for sgnova.

import flattening and version handling
"""

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "?.?.?"

# Import flattening
from sgnova.transforms import Power
