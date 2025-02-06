import pkg_resources  # part of setuptools

from .analyse import *
from .generate import *
from .main import *
from .plotting import *

__version__ = pkg_resources.require("orientationpy")[0].version
