"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.bearings.tolerances._1965 import BearingConnectionComponent
    from mastapy._private.bearings.tolerances._1966 import InternalClearanceClass
    from mastapy._private.bearings.tolerances._1967 import BearingToleranceClass
    from mastapy._private.bearings.tolerances._1968 import (
        BearingToleranceDefinitionOptions,
    )
    from mastapy._private.bearings.tolerances._1969 import FitType
    from mastapy._private.bearings.tolerances._1970 import InnerRingTolerance
    from mastapy._private.bearings.tolerances._1971 import InnerSupportTolerance
    from mastapy._private.bearings.tolerances._1972 import InterferenceDetail
    from mastapy._private.bearings.tolerances._1973 import InterferenceTolerance
    from mastapy._private.bearings.tolerances._1974 import ITDesignation
    from mastapy._private.bearings.tolerances._1975 import MountingSleeveDiameterDetail
    from mastapy._private.bearings.tolerances._1976 import OuterRingTolerance
    from mastapy._private.bearings.tolerances._1977 import OuterSupportTolerance
    from mastapy._private.bearings.tolerances._1978 import RaceRoundnessAtAngle
    from mastapy._private.bearings.tolerances._1979 import RadialSpecificationMethod
    from mastapy._private.bearings.tolerances._1980 import RingDetail
    from mastapy._private.bearings.tolerances._1981 import RingTolerance
    from mastapy._private.bearings.tolerances._1982 import RoundnessSpecification
    from mastapy._private.bearings.tolerances._1983 import RoundnessSpecificationType
    from mastapy._private.bearings.tolerances._1984 import SupportDetail
    from mastapy._private.bearings.tolerances._1985 import SupportMaterialSource
    from mastapy._private.bearings.tolerances._1986 import SupportTolerance
    from mastapy._private.bearings.tolerances._1987 import (
        SupportToleranceLocationDesignation,
    )
    from mastapy._private.bearings.tolerances._1988 import ToleranceCombination
    from mastapy._private.bearings.tolerances._1989 import TypeOfFit
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.bearings.tolerances._1965": ["BearingConnectionComponent"],
        "_private.bearings.tolerances._1966": ["InternalClearanceClass"],
        "_private.bearings.tolerances._1967": ["BearingToleranceClass"],
        "_private.bearings.tolerances._1968": ["BearingToleranceDefinitionOptions"],
        "_private.bearings.tolerances._1969": ["FitType"],
        "_private.bearings.tolerances._1970": ["InnerRingTolerance"],
        "_private.bearings.tolerances._1971": ["InnerSupportTolerance"],
        "_private.bearings.tolerances._1972": ["InterferenceDetail"],
        "_private.bearings.tolerances._1973": ["InterferenceTolerance"],
        "_private.bearings.tolerances._1974": ["ITDesignation"],
        "_private.bearings.tolerances._1975": ["MountingSleeveDiameterDetail"],
        "_private.bearings.tolerances._1976": ["OuterRingTolerance"],
        "_private.bearings.tolerances._1977": ["OuterSupportTolerance"],
        "_private.bearings.tolerances._1978": ["RaceRoundnessAtAngle"],
        "_private.bearings.tolerances._1979": ["RadialSpecificationMethod"],
        "_private.bearings.tolerances._1980": ["RingDetail"],
        "_private.bearings.tolerances._1981": ["RingTolerance"],
        "_private.bearings.tolerances._1982": ["RoundnessSpecification"],
        "_private.bearings.tolerances._1983": ["RoundnessSpecificationType"],
        "_private.bearings.tolerances._1984": ["SupportDetail"],
        "_private.bearings.tolerances._1985": ["SupportMaterialSource"],
        "_private.bearings.tolerances._1986": ["SupportTolerance"],
        "_private.bearings.tolerances._1987": ["SupportToleranceLocationDesignation"],
        "_private.bearings.tolerances._1988": ["ToleranceCombination"],
        "_private.bearings.tolerances._1989": ["TypeOfFit"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BearingConnectionComponent",
    "InternalClearanceClass",
    "BearingToleranceClass",
    "BearingToleranceDefinitionOptions",
    "FitType",
    "InnerRingTolerance",
    "InnerSupportTolerance",
    "InterferenceDetail",
    "InterferenceTolerance",
    "ITDesignation",
    "MountingSleeveDiameterDetail",
    "OuterRingTolerance",
    "OuterSupportTolerance",
    "RaceRoundnessAtAngle",
    "RadialSpecificationMethod",
    "RingDetail",
    "RingTolerance",
    "RoundnessSpecification",
    "RoundnessSpecificationType",
    "SupportDetail",
    "SupportMaterialSource",
    "SupportTolerance",
    "SupportToleranceLocationDesignation",
    "ToleranceCombination",
    "TypeOfFit",
)
