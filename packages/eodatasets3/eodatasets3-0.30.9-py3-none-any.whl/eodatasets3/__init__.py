from . import _version
from ._version import get_versions
from .assemble import DatasetAssembler, DatasetPrepare, IfExists, IncompleteDatasetError
from .images import GridSpec, ValidDataMethod
from .model import DatasetDoc
from .names import NamingConventions, namer
from .properties import Eo3Dict

REPO_URL = "https://github.com/GeoscienceAustralia/eo-datasets.git"

__version__ = get_versions()["version"]
del get_versions

__all__ = (
    "REPO_URL",
    "DatasetAssembler",
    "DatasetDoc",
    "DatasetPrepare",
    "Eo3Dict",
    "GridSpec",
    "IfExists",
    "IncompleteDatasetError",
    "NamingConventions",
    "ValidDataMethod",
    "__version__",
    "namer",
)

__version__ = _version.get_versions()["version"]
