from importlib.metadata import version
from packaging.version import Version


_PYFAI_VERSION = version("pyFAI")
PYFAI_HAS_ORIENTATION = Version(_PYFAI_VERSION) >= Version("2024.1.0")
