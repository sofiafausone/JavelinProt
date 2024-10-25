"""pkmodel is a Pharmokinetic modelling library.

It contains functionality for creating, solving, and visualising the solution
of Parmokinetic (PK) models

"""
# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from .model import Model    # noqa
from .Model2 import *
from .protocol2 import *
from .protocol import Protocol    # noqa
from .example import Solution     # noqa
from .utils import *

