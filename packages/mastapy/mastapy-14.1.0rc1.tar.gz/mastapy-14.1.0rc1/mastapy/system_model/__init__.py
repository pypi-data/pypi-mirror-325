"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model._2266 import Design
    from mastapy._private.system_model._2267 import ComponentDampingOption
    from mastapy._private.system_model._2268 import (
        ConceptCouplingSpeedRatioSpecificationMethod,
    )
    from mastapy._private.system_model._2269 import DesignEntity
    from mastapy._private.system_model._2270 import DesignEntityId
    from mastapy._private.system_model._2271 import DesignSettings
    from mastapy._private.system_model._2272 import DutyCycleImporter
    from mastapy._private.system_model._2273 import DutyCycleImporterDesignEntityMatch
    from mastapy._private.system_model._2274 import ExternalFullFELoader
    from mastapy._private.system_model._2275 import HypoidWindUpRemovalMethod
    from mastapy._private.system_model._2276 import IncludeDutyCycleOption
    from mastapy._private.system_model._2277 import MAAElectricMachineGroup
    from mastapy._private.system_model._2278 import MASTASettings
    from mastapy._private.system_model._2279 import MemorySummary
    from mastapy._private.system_model._2280 import MeshStiffnessModel
    from mastapy._private.system_model._2281 import (
        PlanetPinManufacturingErrorsCoordinateSystem,
    )
    from mastapy._private.system_model._2282 import (
        PowerLoadDragTorqueSpecificationMethod,
    )
    from mastapy._private.system_model._2283 import (
        PowerLoadInputTorqueSpecificationMethod,
    )
    from mastapy._private.system_model._2284 import PowerLoadPIDControlSpeedInputType
    from mastapy._private.system_model._2285 import PowerLoadType
    from mastapy._private.system_model._2286 import RelativeComponentAlignment
    from mastapy._private.system_model._2287 import RelativeOffsetOption
    from mastapy._private.system_model._2288 import SystemReporting
    from mastapy._private.system_model._2289 import (
        ThermalExpansionOptionForGroundedNodes,
    )
    from mastapy._private.system_model._2290 import TransmissionTemperatureSet
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model._2266": ["Design"],
        "_private.system_model._2267": ["ComponentDampingOption"],
        "_private.system_model._2268": ["ConceptCouplingSpeedRatioSpecificationMethod"],
        "_private.system_model._2269": ["DesignEntity"],
        "_private.system_model._2270": ["DesignEntityId"],
        "_private.system_model._2271": ["DesignSettings"],
        "_private.system_model._2272": ["DutyCycleImporter"],
        "_private.system_model._2273": ["DutyCycleImporterDesignEntityMatch"],
        "_private.system_model._2274": ["ExternalFullFELoader"],
        "_private.system_model._2275": ["HypoidWindUpRemovalMethod"],
        "_private.system_model._2276": ["IncludeDutyCycleOption"],
        "_private.system_model._2277": ["MAAElectricMachineGroup"],
        "_private.system_model._2278": ["MASTASettings"],
        "_private.system_model._2279": ["MemorySummary"],
        "_private.system_model._2280": ["MeshStiffnessModel"],
        "_private.system_model._2281": ["PlanetPinManufacturingErrorsCoordinateSystem"],
        "_private.system_model._2282": ["PowerLoadDragTorqueSpecificationMethod"],
        "_private.system_model._2283": ["PowerLoadInputTorqueSpecificationMethod"],
        "_private.system_model._2284": ["PowerLoadPIDControlSpeedInputType"],
        "_private.system_model._2285": ["PowerLoadType"],
        "_private.system_model._2286": ["RelativeComponentAlignment"],
        "_private.system_model._2287": ["RelativeOffsetOption"],
        "_private.system_model._2288": ["SystemReporting"],
        "_private.system_model._2289": ["ThermalExpansionOptionForGroundedNodes"],
        "_private.system_model._2290": ["TransmissionTemperatureSet"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "Design",
    "ComponentDampingOption",
    "ConceptCouplingSpeedRatioSpecificationMethod",
    "DesignEntity",
    "DesignEntityId",
    "DesignSettings",
    "DutyCycleImporter",
    "DutyCycleImporterDesignEntityMatch",
    "ExternalFullFELoader",
    "HypoidWindUpRemovalMethod",
    "IncludeDutyCycleOption",
    "MAAElectricMachineGroup",
    "MASTASettings",
    "MemorySummary",
    "MeshStiffnessModel",
    "PlanetPinManufacturingErrorsCoordinateSystem",
    "PowerLoadDragTorqueSpecificationMethod",
    "PowerLoadInputTorqueSpecificationMethod",
    "PowerLoadPIDControlSpeedInputType",
    "PowerLoadType",
    "RelativeComponentAlignment",
    "RelativeOffsetOption",
    "SystemReporting",
    "ThermalExpansionOptionForGroundedNodes",
    "TransmissionTemperatureSet",
)
