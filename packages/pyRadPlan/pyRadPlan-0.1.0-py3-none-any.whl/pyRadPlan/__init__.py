from importlib.metadata import version, PackageNotFoundError
import logging

from .plan._plans import Plan, validate_pln, IonPlan, PhotonPlan
from .ct._ct import CT, validate_ct
from .cst._cst import StructureSet, validate_cst
from .stf._generate_stf import generate_stf
from .stf import SteeringInformation, validate_stf
from .dose._calc_dose import calc_dose_influence, calc_dose_forward
from .optimization._fluence_optimization import fluence_optimization

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    pass

# Logging is not exposed by default and needs to be configured by the user.
logging.getLogger(__name__).addHandler(logging.NullHandler())

__all__ = [
    "__version__",
    "Plan",
    "IonPlan",
    "PhotonPlan",
    "validate_pln",
    "CT",
    "validate_ct",
    "StructureSet",
    "validate_cst",
    "generate_stf",
    "calc_dose_influence",
    "calc_dose_forward",
    "fluence_optimization",
    "SteeringInformation",
    "validate_stf",
]
