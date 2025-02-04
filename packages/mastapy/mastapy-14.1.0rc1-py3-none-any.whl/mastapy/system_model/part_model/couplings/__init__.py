"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.part_model.couplings._2649 import BeltDrive
    from mastapy._private.system_model.part_model.couplings._2650 import BeltDriveType
    from mastapy._private.system_model.part_model.couplings._2651 import Clutch
    from mastapy._private.system_model.part_model.couplings._2652 import ClutchHalf
    from mastapy._private.system_model.part_model.couplings._2653 import ClutchType
    from mastapy._private.system_model.part_model.couplings._2654 import ConceptCoupling
    from mastapy._private.system_model.part_model.couplings._2655 import (
        ConceptCouplingHalf,
    )
    from mastapy._private.system_model.part_model.couplings._2656 import (
        ConceptCouplingHalfPositioning,
    )
    from mastapy._private.system_model.part_model.couplings._2657 import Coupling
    from mastapy._private.system_model.part_model.couplings._2658 import CouplingHalf
    from mastapy._private.system_model.part_model.couplings._2659 import (
        CrowningSpecification,
    )
    from mastapy._private.system_model.part_model.couplings._2660 import CVT
    from mastapy._private.system_model.part_model.couplings._2661 import CVTPulley
    from mastapy._private.system_model.part_model.couplings._2662 import (
        PartToPartShearCoupling,
    )
    from mastapy._private.system_model.part_model.couplings._2663 import (
        PartToPartShearCouplingHalf,
    )
    from mastapy._private.system_model.part_model.couplings._2664 import (
        PitchErrorFlankOptions,
    )
    from mastapy._private.system_model.part_model.couplings._2665 import Pulley
    from mastapy._private.system_model.part_model.couplings._2666 import (
        RigidConnectorSettings,
    )
    from mastapy._private.system_model.part_model.couplings._2667 import (
        RigidConnectorStiffnessType,
    )
    from mastapy._private.system_model.part_model.couplings._2668 import (
        RigidConnectorTiltStiffnessTypes,
    )
    from mastapy._private.system_model.part_model.couplings._2669 import (
        RigidConnectorToothLocation,
    )
    from mastapy._private.system_model.part_model.couplings._2670 import (
        RigidConnectorToothSpacingType,
    )
    from mastapy._private.system_model.part_model.couplings._2671 import (
        RigidConnectorTypes,
    )
    from mastapy._private.system_model.part_model.couplings._2672 import RollingRing
    from mastapy._private.system_model.part_model.couplings._2673 import (
        RollingRingAssembly,
    )
    from mastapy._private.system_model.part_model.couplings._2674 import (
        ShaftHubConnection,
    )
    from mastapy._private.system_model.part_model.couplings._2675 import (
        SplineFitOptions,
    )
    from mastapy._private.system_model.part_model.couplings._2676 import (
        SplineHalfManufacturingError,
    )
    from mastapy._private.system_model.part_model.couplings._2677 import (
        SplineLeadRelief,
    )
    from mastapy._private.system_model.part_model.couplings._2678 import (
        SplinePitchErrorInputType,
    )
    from mastapy._private.system_model.part_model.couplings._2679 import (
        SplinePitchErrorOptions,
    )
    from mastapy._private.system_model.part_model.couplings._2680 import SpringDamper
    from mastapy._private.system_model.part_model.couplings._2681 import (
        SpringDamperHalf,
    )
    from mastapy._private.system_model.part_model.couplings._2682 import Synchroniser
    from mastapy._private.system_model.part_model.couplings._2683 import (
        SynchroniserCone,
    )
    from mastapy._private.system_model.part_model.couplings._2684 import (
        SynchroniserHalf,
    )
    from mastapy._private.system_model.part_model.couplings._2685 import (
        SynchroniserPart,
    )
    from mastapy._private.system_model.part_model.couplings._2686 import (
        SynchroniserSleeve,
    )
    from mastapy._private.system_model.part_model.couplings._2687 import TorqueConverter
    from mastapy._private.system_model.part_model.couplings._2688 import (
        TorqueConverterPump,
    )
    from mastapy._private.system_model.part_model.couplings._2689 import (
        TorqueConverterSpeedRatio,
    )
    from mastapy._private.system_model.part_model.couplings._2690 import (
        TorqueConverterTurbine,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model.couplings._2649": ["BeltDrive"],
        "_private.system_model.part_model.couplings._2650": ["BeltDriveType"],
        "_private.system_model.part_model.couplings._2651": ["Clutch"],
        "_private.system_model.part_model.couplings._2652": ["ClutchHalf"],
        "_private.system_model.part_model.couplings._2653": ["ClutchType"],
        "_private.system_model.part_model.couplings._2654": ["ConceptCoupling"],
        "_private.system_model.part_model.couplings._2655": ["ConceptCouplingHalf"],
        "_private.system_model.part_model.couplings._2656": [
            "ConceptCouplingHalfPositioning"
        ],
        "_private.system_model.part_model.couplings._2657": ["Coupling"],
        "_private.system_model.part_model.couplings._2658": ["CouplingHalf"],
        "_private.system_model.part_model.couplings._2659": ["CrowningSpecification"],
        "_private.system_model.part_model.couplings._2660": ["CVT"],
        "_private.system_model.part_model.couplings._2661": ["CVTPulley"],
        "_private.system_model.part_model.couplings._2662": ["PartToPartShearCoupling"],
        "_private.system_model.part_model.couplings._2663": [
            "PartToPartShearCouplingHalf"
        ],
        "_private.system_model.part_model.couplings._2664": ["PitchErrorFlankOptions"],
        "_private.system_model.part_model.couplings._2665": ["Pulley"],
        "_private.system_model.part_model.couplings._2666": ["RigidConnectorSettings"],
        "_private.system_model.part_model.couplings._2667": [
            "RigidConnectorStiffnessType"
        ],
        "_private.system_model.part_model.couplings._2668": [
            "RigidConnectorTiltStiffnessTypes"
        ],
        "_private.system_model.part_model.couplings._2669": [
            "RigidConnectorToothLocation"
        ],
        "_private.system_model.part_model.couplings._2670": [
            "RigidConnectorToothSpacingType"
        ],
        "_private.system_model.part_model.couplings._2671": ["RigidConnectorTypes"],
        "_private.system_model.part_model.couplings._2672": ["RollingRing"],
        "_private.system_model.part_model.couplings._2673": ["RollingRingAssembly"],
        "_private.system_model.part_model.couplings._2674": ["ShaftHubConnection"],
        "_private.system_model.part_model.couplings._2675": ["SplineFitOptions"],
        "_private.system_model.part_model.couplings._2676": [
            "SplineHalfManufacturingError"
        ],
        "_private.system_model.part_model.couplings._2677": ["SplineLeadRelief"],
        "_private.system_model.part_model.couplings._2678": [
            "SplinePitchErrorInputType"
        ],
        "_private.system_model.part_model.couplings._2679": ["SplinePitchErrorOptions"],
        "_private.system_model.part_model.couplings._2680": ["SpringDamper"],
        "_private.system_model.part_model.couplings._2681": ["SpringDamperHalf"],
        "_private.system_model.part_model.couplings._2682": ["Synchroniser"],
        "_private.system_model.part_model.couplings._2683": ["SynchroniserCone"],
        "_private.system_model.part_model.couplings._2684": ["SynchroniserHalf"],
        "_private.system_model.part_model.couplings._2685": ["SynchroniserPart"],
        "_private.system_model.part_model.couplings._2686": ["SynchroniserSleeve"],
        "_private.system_model.part_model.couplings._2687": ["TorqueConverter"],
        "_private.system_model.part_model.couplings._2688": ["TorqueConverterPump"],
        "_private.system_model.part_model.couplings._2689": [
            "TorqueConverterSpeedRatio"
        ],
        "_private.system_model.part_model.couplings._2690": ["TorqueConverterTurbine"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BeltDrive",
    "BeltDriveType",
    "Clutch",
    "ClutchHalf",
    "ClutchType",
    "ConceptCoupling",
    "ConceptCouplingHalf",
    "ConceptCouplingHalfPositioning",
    "Coupling",
    "CouplingHalf",
    "CrowningSpecification",
    "CVT",
    "CVTPulley",
    "PartToPartShearCoupling",
    "PartToPartShearCouplingHalf",
    "PitchErrorFlankOptions",
    "Pulley",
    "RigidConnectorSettings",
    "RigidConnectorStiffnessType",
    "RigidConnectorTiltStiffnessTypes",
    "RigidConnectorToothLocation",
    "RigidConnectorToothSpacingType",
    "RigidConnectorTypes",
    "RollingRing",
    "RollingRingAssembly",
    "ShaftHubConnection",
    "SplineFitOptions",
    "SplineHalfManufacturingError",
    "SplineLeadRelief",
    "SplinePitchErrorInputType",
    "SplinePitchErrorOptions",
    "SpringDamper",
    "SpringDamperHalf",
    "Synchroniser",
    "SynchroniserCone",
    "SynchroniserHalf",
    "SynchroniserPart",
    "SynchroniserSleeve",
    "TorqueConverter",
    "TorqueConverterPump",
    "TorqueConverterSpeedRatio",
    "TorqueConverterTurbine",
)
