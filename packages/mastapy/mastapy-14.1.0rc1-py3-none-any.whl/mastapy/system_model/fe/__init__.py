"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.fe._2421 import AlignConnectedComponentOptions
    from mastapy._private.system_model.fe._2422 import AlignmentMethod
    from mastapy._private.system_model.fe._2423 import AlignmentMethodForRaceBearing
    from mastapy._private.system_model.fe._2424 import AlignmentUsingAxialNodePositions
    from mastapy._private.system_model.fe._2425 import AngleSource
    from mastapy._private.system_model.fe._2426 import BaseFEWithSelection
    from mastapy._private.system_model.fe._2427 import BatchOperations
    from mastapy._private.system_model.fe._2428 import BearingNodeAlignmentOption
    from mastapy._private.system_model.fe._2429 import BearingNodeOption
    from mastapy._private.system_model.fe._2430 import BearingRaceNodeLink
    from mastapy._private.system_model.fe._2431 import BearingRacePosition
    from mastapy._private.system_model.fe._2432 import ComponentOrientationOption
    from mastapy._private.system_model.fe._2433 import ContactPairWithSelection
    from mastapy._private.system_model.fe._2434 import CoordinateSystemWithSelection
    from mastapy._private.system_model.fe._2435 import CreateConnectedComponentOptions
    from mastapy._private.system_model.fe._2436 import (
        CreateMicrophoneNormalToSurfaceOptions,
    )
    from mastapy._private.system_model.fe._2437 import DegreeOfFreedomBoundaryCondition
    from mastapy._private.system_model.fe._2438 import (
        DegreeOfFreedomBoundaryConditionAngular,
    )
    from mastapy._private.system_model.fe._2439 import (
        DegreeOfFreedomBoundaryConditionLinear,
    )
    from mastapy._private.system_model.fe._2440 import ElectricMachineDataSet
    from mastapy._private.system_model.fe._2441 import ElectricMachineDynamicLoadData
    from mastapy._private.system_model.fe._2442 import ElementFaceGroupWithSelection
    from mastapy._private.system_model.fe._2443 import ElementPropertiesWithSelection
    from mastapy._private.system_model.fe._2444 import FEEntityGroupWithSelection
    from mastapy._private.system_model.fe._2445 import FEExportSettings
    from mastapy._private.system_model.fe._2446 import FEPartDRIVASurfaceSelection
    from mastapy._private.system_model.fe._2447 import FEPartWithBatchOptions
    from mastapy._private.system_model.fe._2448 import FEStiffnessGeometry
    from mastapy._private.system_model.fe._2449 import FEStiffnessTester
    from mastapy._private.system_model.fe._2450 import FESubstructure
    from mastapy._private.system_model.fe._2451 import FESubstructureExportOptions
    from mastapy._private.system_model.fe._2452 import FESubstructureNode
    from mastapy._private.system_model.fe._2453 import FESubstructureNodeModeShape
    from mastapy._private.system_model.fe._2454 import FESubstructureNodeModeShapes
    from mastapy._private.system_model.fe._2455 import FESubstructureType
    from mastapy._private.system_model.fe._2456 import FESubstructureWithBatchOptions
    from mastapy._private.system_model.fe._2457 import FESubstructureWithSelection
    from mastapy._private.system_model.fe._2458 import (
        FESubstructureWithSelectionComponents,
    )
    from mastapy._private.system_model.fe._2459 import (
        FESubstructureWithSelectionForHarmonicAnalysis,
    )
    from mastapy._private.system_model.fe._2460 import (
        FESubstructureWithSelectionForModalAnalysis,
    )
    from mastapy._private.system_model.fe._2461 import (
        FESubstructureWithSelectionForStaticAnalysis,
    )
    from mastapy._private.system_model.fe._2462 import GearMeshingOptions
    from mastapy._private.system_model.fe._2463 import (
        IndependentMASTACreatedCondensationNode,
    )
    from mastapy._private.system_model.fe._2464 import (
        LinkComponentAxialPositionErrorReporter,
    )
    from mastapy._private.system_model.fe._2465 import LinkNodeSource
    from mastapy._private.system_model.fe._2466 import MaterialPropertiesWithSelection
    from mastapy._private.system_model.fe._2467 import (
        NodeBoundaryConditionStaticAnalysis,
    )
    from mastapy._private.system_model.fe._2468 import NodeGroupWithSelection
    from mastapy._private.system_model.fe._2469 import NodeSelectionDepthOption
    from mastapy._private.system_model.fe._2470 import (
        OptionsWhenExternalFEFileAlreadyExists,
    )
    from mastapy._private.system_model.fe._2471 import PerLinkExportOptions
    from mastapy._private.system_model.fe._2472 import PerNodeExportOptions
    from mastapy._private.system_model.fe._2473 import RaceBearingFE
    from mastapy._private.system_model.fe._2474 import RaceBearingFESystemDeflection
    from mastapy._private.system_model.fe._2475 import RaceBearingFEWithSelection
    from mastapy._private.system_model.fe._2476 import ReplacedShaftSelectionHelper
    from mastapy._private.system_model.fe._2477 import SystemDeflectionFEExportOptions
    from mastapy._private.system_model.fe._2478 import ThermalExpansionOption
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.fe._2421": ["AlignConnectedComponentOptions"],
        "_private.system_model.fe._2422": ["AlignmentMethod"],
        "_private.system_model.fe._2423": ["AlignmentMethodForRaceBearing"],
        "_private.system_model.fe._2424": ["AlignmentUsingAxialNodePositions"],
        "_private.system_model.fe._2425": ["AngleSource"],
        "_private.system_model.fe._2426": ["BaseFEWithSelection"],
        "_private.system_model.fe._2427": ["BatchOperations"],
        "_private.system_model.fe._2428": ["BearingNodeAlignmentOption"],
        "_private.system_model.fe._2429": ["BearingNodeOption"],
        "_private.system_model.fe._2430": ["BearingRaceNodeLink"],
        "_private.system_model.fe._2431": ["BearingRacePosition"],
        "_private.system_model.fe._2432": ["ComponentOrientationOption"],
        "_private.system_model.fe._2433": ["ContactPairWithSelection"],
        "_private.system_model.fe._2434": ["CoordinateSystemWithSelection"],
        "_private.system_model.fe._2435": ["CreateConnectedComponentOptions"],
        "_private.system_model.fe._2436": ["CreateMicrophoneNormalToSurfaceOptions"],
        "_private.system_model.fe._2437": ["DegreeOfFreedomBoundaryCondition"],
        "_private.system_model.fe._2438": ["DegreeOfFreedomBoundaryConditionAngular"],
        "_private.system_model.fe._2439": ["DegreeOfFreedomBoundaryConditionLinear"],
        "_private.system_model.fe._2440": ["ElectricMachineDataSet"],
        "_private.system_model.fe._2441": ["ElectricMachineDynamicLoadData"],
        "_private.system_model.fe._2442": ["ElementFaceGroupWithSelection"],
        "_private.system_model.fe._2443": ["ElementPropertiesWithSelection"],
        "_private.system_model.fe._2444": ["FEEntityGroupWithSelection"],
        "_private.system_model.fe._2445": ["FEExportSettings"],
        "_private.system_model.fe._2446": ["FEPartDRIVASurfaceSelection"],
        "_private.system_model.fe._2447": ["FEPartWithBatchOptions"],
        "_private.system_model.fe._2448": ["FEStiffnessGeometry"],
        "_private.system_model.fe._2449": ["FEStiffnessTester"],
        "_private.system_model.fe._2450": ["FESubstructure"],
        "_private.system_model.fe._2451": ["FESubstructureExportOptions"],
        "_private.system_model.fe._2452": ["FESubstructureNode"],
        "_private.system_model.fe._2453": ["FESubstructureNodeModeShape"],
        "_private.system_model.fe._2454": ["FESubstructureNodeModeShapes"],
        "_private.system_model.fe._2455": ["FESubstructureType"],
        "_private.system_model.fe._2456": ["FESubstructureWithBatchOptions"],
        "_private.system_model.fe._2457": ["FESubstructureWithSelection"],
        "_private.system_model.fe._2458": ["FESubstructureWithSelectionComponents"],
        "_private.system_model.fe._2459": [
            "FESubstructureWithSelectionForHarmonicAnalysis"
        ],
        "_private.system_model.fe._2460": [
            "FESubstructureWithSelectionForModalAnalysis"
        ],
        "_private.system_model.fe._2461": [
            "FESubstructureWithSelectionForStaticAnalysis"
        ],
        "_private.system_model.fe._2462": ["GearMeshingOptions"],
        "_private.system_model.fe._2463": ["IndependentMASTACreatedCondensationNode"],
        "_private.system_model.fe._2464": ["LinkComponentAxialPositionErrorReporter"],
        "_private.system_model.fe._2465": ["LinkNodeSource"],
        "_private.system_model.fe._2466": ["MaterialPropertiesWithSelection"],
        "_private.system_model.fe._2467": ["NodeBoundaryConditionStaticAnalysis"],
        "_private.system_model.fe._2468": ["NodeGroupWithSelection"],
        "_private.system_model.fe._2469": ["NodeSelectionDepthOption"],
        "_private.system_model.fe._2470": ["OptionsWhenExternalFEFileAlreadyExists"],
        "_private.system_model.fe._2471": ["PerLinkExportOptions"],
        "_private.system_model.fe._2472": ["PerNodeExportOptions"],
        "_private.system_model.fe._2473": ["RaceBearingFE"],
        "_private.system_model.fe._2474": ["RaceBearingFESystemDeflection"],
        "_private.system_model.fe._2475": ["RaceBearingFEWithSelection"],
        "_private.system_model.fe._2476": ["ReplacedShaftSelectionHelper"],
        "_private.system_model.fe._2477": ["SystemDeflectionFEExportOptions"],
        "_private.system_model.fe._2478": ["ThermalExpansionOption"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AlignConnectedComponentOptions",
    "AlignmentMethod",
    "AlignmentMethodForRaceBearing",
    "AlignmentUsingAxialNodePositions",
    "AngleSource",
    "BaseFEWithSelection",
    "BatchOperations",
    "BearingNodeAlignmentOption",
    "BearingNodeOption",
    "BearingRaceNodeLink",
    "BearingRacePosition",
    "ComponentOrientationOption",
    "ContactPairWithSelection",
    "CoordinateSystemWithSelection",
    "CreateConnectedComponentOptions",
    "CreateMicrophoneNormalToSurfaceOptions",
    "DegreeOfFreedomBoundaryCondition",
    "DegreeOfFreedomBoundaryConditionAngular",
    "DegreeOfFreedomBoundaryConditionLinear",
    "ElectricMachineDataSet",
    "ElectricMachineDynamicLoadData",
    "ElementFaceGroupWithSelection",
    "ElementPropertiesWithSelection",
    "FEEntityGroupWithSelection",
    "FEExportSettings",
    "FEPartDRIVASurfaceSelection",
    "FEPartWithBatchOptions",
    "FEStiffnessGeometry",
    "FEStiffnessTester",
    "FESubstructure",
    "FESubstructureExportOptions",
    "FESubstructureNode",
    "FESubstructureNodeModeShape",
    "FESubstructureNodeModeShapes",
    "FESubstructureType",
    "FESubstructureWithBatchOptions",
    "FESubstructureWithSelection",
    "FESubstructureWithSelectionComponents",
    "FESubstructureWithSelectionForHarmonicAnalysis",
    "FESubstructureWithSelectionForModalAnalysis",
    "FESubstructureWithSelectionForStaticAnalysis",
    "GearMeshingOptions",
    "IndependentMASTACreatedCondensationNode",
    "LinkComponentAxialPositionErrorReporter",
    "LinkNodeSource",
    "MaterialPropertiesWithSelection",
    "NodeBoundaryConditionStaticAnalysis",
    "NodeGroupWithSelection",
    "NodeSelectionDepthOption",
    "OptionsWhenExternalFEFileAlreadyExists",
    "PerLinkExportOptions",
    "PerNodeExportOptions",
    "RaceBearingFE",
    "RaceBearingFESystemDeflection",
    "RaceBearingFEWithSelection",
    "ReplacedShaftSelectionHelper",
    "SystemDeflectionFEExportOptions",
    "ThermalExpansionOption",
)
