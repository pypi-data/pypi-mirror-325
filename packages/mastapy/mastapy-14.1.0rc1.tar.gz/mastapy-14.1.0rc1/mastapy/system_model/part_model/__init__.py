"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.part_model._2500 import Assembly
    from mastapy._private.system_model.part_model._2501 import AbstractAssembly
    from mastapy._private.system_model.part_model._2502 import AbstractShaft
    from mastapy._private.system_model.part_model._2503 import AbstractShaftOrHousing
    from mastapy._private.system_model.part_model._2504 import (
        AGMALoadSharingTableApplicationLevel,
    )
    from mastapy._private.system_model.part_model._2505 import (
        AxialInternalClearanceTolerance,
    )
    from mastapy._private.system_model.part_model._2506 import Bearing
    from mastapy._private.system_model.part_model._2507 import BearingF0InputMethod
    from mastapy._private.system_model.part_model._2508 import (
        BearingRaceMountingOptions,
    )
    from mastapy._private.system_model.part_model._2509 import Bolt
    from mastapy._private.system_model.part_model._2510 import BoltedJoint
    from mastapy._private.system_model.part_model._2511 import Component
    from mastapy._private.system_model.part_model._2512 import ComponentsConnectedResult
    from mastapy._private.system_model.part_model._2513 import ConnectedSockets
    from mastapy._private.system_model.part_model._2514 import Connector
    from mastapy._private.system_model.part_model._2515 import Datum
    from mastapy._private.system_model.part_model._2516 import (
        ElectricMachineSearchRegionSpecificationMethod,
    )
    from mastapy._private.system_model.part_model._2517 import EnginePartLoad
    from mastapy._private.system_model.part_model._2518 import EngineSpeed
    from mastapy._private.system_model.part_model._2519 import ExternalCADModel
    from mastapy._private.system_model.part_model._2520 import FEPart
    from mastapy._private.system_model.part_model._2521 import FlexiblePinAssembly
    from mastapy._private.system_model.part_model._2522 import GuideDxfModel
    from mastapy._private.system_model.part_model._2523 import GuideImage
    from mastapy._private.system_model.part_model._2524 import GuideModelUsage
    from mastapy._private.system_model.part_model._2525 import (
        InnerBearingRaceMountingOptions,
    )
    from mastapy._private.system_model.part_model._2526 import (
        InternalClearanceTolerance,
    )
    from mastapy._private.system_model.part_model._2527 import LoadSharingModes
    from mastapy._private.system_model.part_model._2528 import LoadSharingSettings
    from mastapy._private.system_model.part_model._2529 import MassDisc
    from mastapy._private.system_model.part_model._2530 import MeasurementComponent
    from mastapy._private.system_model.part_model._2531 import Microphone
    from mastapy._private.system_model.part_model._2532 import MicrophoneArray
    from mastapy._private.system_model.part_model._2533 import MountableComponent
    from mastapy._private.system_model.part_model._2534 import OilLevelSpecification
    from mastapy._private.system_model.part_model._2535 import OilSeal
    from mastapy._private.system_model.part_model._2536 import (
        OuterBearingRaceMountingOptions,
    )
    from mastapy._private.system_model.part_model._2537 import Part
    from mastapy._private.system_model.part_model._2538 import PlanetCarrier
    from mastapy._private.system_model.part_model._2539 import PlanetCarrierSettings
    from mastapy._private.system_model.part_model._2540 import PointLoad
    from mastapy._private.system_model.part_model._2541 import PowerLoad
    from mastapy._private.system_model.part_model._2542 import (
        RadialInternalClearanceTolerance,
    )
    from mastapy._private.system_model.part_model._2543 import (
        RollingBearingElementLoadCase,
    )
    from mastapy._private.system_model.part_model._2544 import RootAssembly
    from mastapy._private.system_model.part_model._2545 import (
        ShaftDiameterModificationDueToRollingBearingRing,
    )
    from mastapy._private.system_model.part_model._2546 import SpecialisedAssembly
    from mastapy._private.system_model.part_model._2547 import UnbalancedMass
    from mastapy._private.system_model.part_model._2548 import (
        UnbalancedMassInclusionOption,
    )
    from mastapy._private.system_model.part_model._2549 import VirtualComponent
    from mastapy._private.system_model.part_model._2550 import (
        WindTurbineBladeModeDetails,
    )
    from mastapy._private.system_model.part_model._2551 import (
        WindTurbineSingleBladeDetails,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model._2500": ["Assembly"],
        "_private.system_model.part_model._2501": ["AbstractAssembly"],
        "_private.system_model.part_model._2502": ["AbstractShaft"],
        "_private.system_model.part_model._2503": ["AbstractShaftOrHousing"],
        "_private.system_model.part_model._2504": [
            "AGMALoadSharingTableApplicationLevel"
        ],
        "_private.system_model.part_model._2505": ["AxialInternalClearanceTolerance"],
        "_private.system_model.part_model._2506": ["Bearing"],
        "_private.system_model.part_model._2507": ["BearingF0InputMethod"],
        "_private.system_model.part_model._2508": ["BearingRaceMountingOptions"],
        "_private.system_model.part_model._2509": ["Bolt"],
        "_private.system_model.part_model._2510": ["BoltedJoint"],
        "_private.system_model.part_model._2511": ["Component"],
        "_private.system_model.part_model._2512": ["ComponentsConnectedResult"],
        "_private.system_model.part_model._2513": ["ConnectedSockets"],
        "_private.system_model.part_model._2514": ["Connector"],
        "_private.system_model.part_model._2515": ["Datum"],
        "_private.system_model.part_model._2516": [
            "ElectricMachineSearchRegionSpecificationMethod"
        ],
        "_private.system_model.part_model._2517": ["EnginePartLoad"],
        "_private.system_model.part_model._2518": ["EngineSpeed"],
        "_private.system_model.part_model._2519": ["ExternalCADModel"],
        "_private.system_model.part_model._2520": ["FEPart"],
        "_private.system_model.part_model._2521": ["FlexiblePinAssembly"],
        "_private.system_model.part_model._2522": ["GuideDxfModel"],
        "_private.system_model.part_model._2523": ["GuideImage"],
        "_private.system_model.part_model._2524": ["GuideModelUsage"],
        "_private.system_model.part_model._2525": ["InnerBearingRaceMountingOptions"],
        "_private.system_model.part_model._2526": ["InternalClearanceTolerance"],
        "_private.system_model.part_model._2527": ["LoadSharingModes"],
        "_private.system_model.part_model._2528": ["LoadSharingSettings"],
        "_private.system_model.part_model._2529": ["MassDisc"],
        "_private.system_model.part_model._2530": ["MeasurementComponent"],
        "_private.system_model.part_model._2531": ["Microphone"],
        "_private.system_model.part_model._2532": ["MicrophoneArray"],
        "_private.system_model.part_model._2533": ["MountableComponent"],
        "_private.system_model.part_model._2534": ["OilLevelSpecification"],
        "_private.system_model.part_model._2535": ["OilSeal"],
        "_private.system_model.part_model._2536": ["OuterBearingRaceMountingOptions"],
        "_private.system_model.part_model._2537": ["Part"],
        "_private.system_model.part_model._2538": ["PlanetCarrier"],
        "_private.system_model.part_model._2539": ["PlanetCarrierSettings"],
        "_private.system_model.part_model._2540": ["PointLoad"],
        "_private.system_model.part_model._2541": ["PowerLoad"],
        "_private.system_model.part_model._2542": ["RadialInternalClearanceTolerance"],
        "_private.system_model.part_model._2543": ["RollingBearingElementLoadCase"],
        "_private.system_model.part_model._2544": ["RootAssembly"],
        "_private.system_model.part_model._2545": [
            "ShaftDiameterModificationDueToRollingBearingRing"
        ],
        "_private.system_model.part_model._2546": ["SpecialisedAssembly"],
        "_private.system_model.part_model._2547": ["UnbalancedMass"],
        "_private.system_model.part_model._2548": ["UnbalancedMassInclusionOption"],
        "_private.system_model.part_model._2549": ["VirtualComponent"],
        "_private.system_model.part_model._2550": ["WindTurbineBladeModeDetails"],
        "_private.system_model.part_model._2551": ["WindTurbineSingleBladeDetails"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "Assembly",
    "AbstractAssembly",
    "AbstractShaft",
    "AbstractShaftOrHousing",
    "AGMALoadSharingTableApplicationLevel",
    "AxialInternalClearanceTolerance",
    "Bearing",
    "BearingF0InputMethod",
    "BearingRaceMountingOptions",
    "Bolt",
    "BoltedJoint",
    "Component",
    "ComponentsConnectedResult",
    "ConnectedSockets",
    "Connector",
    "Datum",
    "ElectricMachineSearchRegionSpecificationMethod",
    "EnginePartLoad",
    "EngineSpeed",
    "ExternalCADModel",
    "FEPart",
    "FlexiblePinAssembly",
    "GuideDxfModel",
    "GuideImage",
    "GuideModelUsage",
    "InnerBearingRaceMountingOptions",
    "InternalClearanceTolerance",
    "LoadSharingModes",
    "LoadSharingSettings",
    "MassDisc",
    "MeasurementComponent",
    "Microphone",
    "MicrophoneArray",
    "MountableComponent",
    "OilLevelSpecification",
    "OilSeal",
    "OuterBearingRaceMountingOptions",
    "Part",
    "PlanetCarrier",
    "PlanetCarrierSettings",
    "PointLoad",
    "PowerLoad",
    "RadialInternalClearanceTolerance",
    "RollingBearingElementLoadCase",
    "RootAssembly",
    "ShaftDiameterModificationDueToRollingBearingRing",
    "SpecialisedAssembly",
    "UnbalancedMass",
    "UnbalancedMassInclusionOption",
    "VirtualComponent",
    "WindTurbineBladeModeDetails",
    "WindTurbineSingleBladeDetails",
)
