"""HarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_method_call_overload,
    pythonnet_property_get,
)
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7698

_PART_TO_PART_SHEAR_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "PartToPartShearCouplingConnection",
)
_CLUTCH_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "ClutchConnection"
)
_CONCEPT_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "ConceptCouplingConnection",
)
_COUPLING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "CouplingConnection"
)
_SPRING_DAMPER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperConnection"
)
_TORQUE_CONVERTER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings",
    "TorqueConverterConnection",
)
_PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingConnectionLoadCase",
)
_CLUTCH_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ClutchConnectionLoadCase",
)
_CONCEPT_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConceptCouplingConnectionLoadCase",
)
_COUPLING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CouplingConnectionLoadCase",
)
_SPRING_DAMPER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperConnectionLoadCase",
)
_TORQUE_CONVERTER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterConnectionLoadCase",
)
_STRAIGHT_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearLoadCase",
)
_STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearSetLoadCase",
)
_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelPlanetGearLoadCase",
)
_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelSunGearLoadCase",
)
_WORM_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearLoadCase"
)
_WORM_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearSetLoadCase"
)
_ZEROL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ZerolBevelGearLoadCase"
)
_ZEROL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ZerolBevelGearSetLoadCase",
)
_CYCLOIDAL_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalAssemblyLoadCase",
)
_CYCLOIDAL_DISC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CycloidalDiscLoadCase"
)
_RING_PINS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RingPinsLoadCase"
)
_PART_TO_PART_SHEAR_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingLoadCase",
)
_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PartToPartShearCouplingHalfLoadCase",
)
_BELT_DRIVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BeltDriveLoadCase"
)
_CLUTCH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ClutchLoadCase"
)
_CLUTCH_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ClutchHalfLoadCase"
)
_CONCEPT_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptCouplingLoadCase"
)
_CONCEPT_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ConceptCouplingHalfLoadCase",
)
_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingLoadCase"
)
_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingHalfLoadCase"
)
_CVT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CVTLoadCase"
)
_CVT_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CVTPulleyLoadCase"
)
_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PulleyLoadCase"
)
_SHAFT_HUB_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftHubConnectionLoadCase",
)
_ROLLING_RING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RollingRingLoadCase"
)
_ROLLING_RING_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RollingRingAssemblyLoadCase",
)
_SPRING_DAMPER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpringDamperLoadCase"
)
_SPRING_DAMPER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpringDamperHalfLoadCase",
)
_SYNCHRONISER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SynchroniserLoadCase"
)
_SYNCHRONISER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserHalfLoadCase",
)
_SYNCHRONISER_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserPartLoadCase",
)
_SYNCHRONISER_SLEEVE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserSleeveLoadCase",
)
_TORQUE_CONVERTER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "TorqueConverterLoadCase"
)
_TORQUE_CONVERTER_PUMP_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterPumpLoadCase",
)
_TORQUE_CONVERTER_TURBINE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterTurbineLoadCase",
)
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftToMountableComponentConnectionLoadCase",
)
_CVT_BELT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CVTBeltConnectionLoadCase",
)
_BELT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BeltConnectionLoadCase"
)
_COAXIAL_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CoaxialConnectionLoadCase",
)
_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectionLoadCase"
)
_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "InterMountableComponentConnectionLoadCase",
)
_PLANETARY_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PlanetaryConnectionLoadCase",
)
_ROLLING_RING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RollingRingConnectionLoadCase",
)
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftToMountableComponentConnectionLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearMeshLoadCase",
)
_CONCEPT_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearMeshLoadCase"
)
_FACE_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearMeshLoadCase"
)
_STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearMeshLoadCase",
)
_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearMeshLoadCase"
)
_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearMeshLoadCase"
)
_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearMeshLoadCase",
)
_CYLINDRICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearMeshLoadCase",
)
_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearMeshLoadCase"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearMeshLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
)
_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearMeshLoadCase",
)
_STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelGearMeshLoadCase",
)
_WORM_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "WormGearMeshLoadCase"
)
_ZEROL_BEVEL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ZerolBevelGearMeshLoadCase",
)
_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearMeshLoadCase"
)
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalDiscCentralBearingConnectionLoadCase",
)
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CycloidalDiscPlanetaryBearingConnectionLoadCase",
)
_RING_PINS_TO_DISC_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "RingPinsToDiscConnectionLoadCase",
)
_ABSTRACT_SHAFT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "AbstractShaftLoadCase"
)
_MICROPHONE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "MicrophoneLoadCase"
)
_MICROPHONE_ARRAY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "MicrophoneArrayLoadCase"
)
_ABSTRACT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractAssemblyLoadCase",
)
_ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftOrHousingLoadCase",
)
_BEARING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BearingLoadCase"
)
_BOLT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltLoadCase"
)
_BOLTED_JOINT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltedJointLoadCase"
)
_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ComponentLoadCase"
)
_CONNECTOR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectorLoadCase"
)
_DATUM_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "DatumLoadCase"
)
_EXTERNAL_CAD_MODEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ExternalCADModelLoadCase",
)
_FE_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FEPartLoadCase"
)
_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "FlexiblePinAssemblyLoadCase",
)
_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "AssemblyLoadCase"
)
_GUIDE_DXF_MODEL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GuideDxfModelLoadCase"
)
_MASS_DISC_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "MassDiscLoadCase"
)
_MEASUREMENT_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MeasurementComponentLoadCase",
)
_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MountableComponentLoadCase",
)
_OIL_SEAL_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "OilSealLoadCase"
)
_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PartLoadCase"
)
_PLANET_CARRIER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PlanetCarrierLoadCase"
)
_POINT_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PointLoadLoadCase"
)
_POWER_LOAD_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PowerLoadLoadCase"
)
_ROOT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "RootAssemblyLoadCase"
)
_SPECIALISED_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpecialisedAssemblyLoadCase",
)
_UNBALANCED_MASS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "UnbalancedMassLoadCase"
)
_VIRTUAL_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "VirtualComponentLoadCase",
)
_SHAFT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ShaftLoadCase"
)
_CONCEPT_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearLoadCase"
)
_CONCEPT_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConceptGearSetLoadCase"
)
_FACE_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearLoadCase"
)
_FACE_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearSetLoadCase"
)
_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearLoadCase",
)
_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AGMAGleasonConicalGearSetLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearLoadCase",
)
_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearSetLoadCase",
)
_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialPlanetGearLoadCase",
)
_BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialSunGearLoadCase",
)
_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearLoadCase"
)
_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearSetLoadCase"
)
_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearLoadCase"
)
_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearSetLoadCase"
)
_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CylindricalGearLoadCase"
)
_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalGearSetLoadCase",
)
_CYLINDRICAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "CylindricalPlanetGearLoadCase",
)
_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearLoadCase"
)
_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearSetLoadCase"
)
_HYPOID_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearLoadCase"
)
_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearSetLoadCase"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearSetLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
)
_PLANETARY_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "PlanetaryGearSetLoadCase",
)
_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "SpiralBevelGearLoadCase"
)
_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearSetLoadCase",
)
_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearLoadCase",
)
_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearSetLoadCase",
)
_STRAIGHT_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGear"
)
_STRAIGHT_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGearSet"
)
_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelPlanetGear"
)
_STRAIGHT_BEVEL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelSunGear"
)
_WORM_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGear")
_WORM_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "WormGearSet"
)
_ZEROL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGear"
)
_ZEROL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ZerolBevelGearSet"
)
_CONCEPT_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGear"
)
_CONCEPT_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConceptGearSet"
)
_FACE_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGear")
_FACE_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "FaceGearSet"
)
_AGMA_GLEASON_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGear"
)
_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)
_BEVEL_DIFFERENTIAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGear"
)
_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialGearSet"
)
_BEVEL_DIFFERENTIAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialPlanetGear"
)
_BEVEL_DIFFERENTIAL_SUN_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelDifferentialSunGear"
)
_BEVEL_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear")
_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGearSet"
)
_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
)
_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
)
_CYLINDRICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGear"
)
_CYLINDRICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalGearSet"
)
_CYLINDRICAL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "CylindricalPlanetGear"
)
_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "Gear")
_GEAR_SET = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "GearSet")
_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGear"
)
_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGear"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidConicalGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGear"
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "KlingelnbergCycloPalloidHypoidGearSet"
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGear",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearSet",
)
_PLANETARY_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "PlanetaryGearSet"
)
_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGear"
)
_SPIRAL_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGearSet"
)
_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGear"
)
_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
)
_CYCLOIDAL_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalAssembly"
)
_CYCLOIDAL_DISC = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "CycloidalDisc"
)
_RING_PINS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Cycloidal", "RingPins"
)
_PART_TO_PART_SHEAR_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCoupling"
)
_PART_TO_PART_SHEAR_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "PartToPartShearCouplingHalf"
)
_BELT_DRIVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "BeltDrive"
)
_CLUTCH = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Clutch")
_CLUTCH_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ClutchHalf"
)
_CONCEPT_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCoupling"
)
_CONCEPT_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ConceptCouplingHalf"
)
_COUPLING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Coupling"
)
_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
)
_CVT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVT")
_CVT_PULLEY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVTPulley"
)
_PULLEY = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Couplings", "Pulley")
_SHAFT_HUB_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "ShaftHubConnection"
)
_ROLLING_RING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRing"
)
_ROLLING_RING_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "RollingRingAssembly"
)
_SPRING_DAMPER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamper"
)
_SPRING_DAMPER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SpringDamperHalf"
)
_SYNCHRONISER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "Synchroniser"
)
_SYNCHRONISER_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserHalf"
)
_SYNCHRONISER_PART = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserPart"
)
_SYNCHRONISER_SLEEVE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserSleeve"
)
_TORQUE_CONVERTER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverter"
)
_TORQUE_CONVERTER_PUMP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterPump"
)
_TORQUE_CONVERTER_TURBINE = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "TorqueConverterTurbine"
)
_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "ShaftToMountableComponentConnection",
)
_CVT_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CVTBeltConnection"
)
_BELT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "BeltConnection"
)
_COAXIAL_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CoaxialConnection"
)
_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Connection"
)
_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)
_PLANETARY_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "PlanetaryConnection"
)
_ROLLING_RING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "RollingRingConnection"
)
_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "AbstractShaftToMountableComponentConnection",
)
_BEVEL_DIFFERENTIAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelDifferentialGearMesh"
)
_CONCEPT_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConceptGearMesh"
)
_FACE_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "FaceGearMesh"
)
_STRAIGHT_BEVEL_DIFF_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelDiffGearMesh"
)
_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearMesh"
)
_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearMesh"
)
_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "AGMAGleasonConicalGearMesh"
)
_CYLINDRICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "CylindricalGearMesh"
)
_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "HypoidGearMesh"
)
_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidConicalGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidHypoidGearMesh",
)
_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
)
_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "SpiralBevelGearMesh"
)
_STRAIGHT_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelGearMesh"
)
_WORM_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "WormGearMesh"
)
_ZEROL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ZerolBevelGearMesh"
)
_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "GearMesh"
)
_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscCentralBearingConnection",
)
_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscPlanetaryBearingConnection",
)
_RING_PINS_TO_DISC_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "RingPinsToDiscConnection",
)
_ABSTRACT_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaft"
)
_MICROPHONE = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Microphone")
_MICROPHONE_ARRAY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MicrophoneArray"
)
_ABSTRACT_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractAssembly"
)
_ABSTRACT_SHAFT_OR_HOUSING = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaftOrHousing"
)
_BEARING = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bearing")
_BOLT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Bolt")
_BOLTED_JOINT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "BoltedJoint")
_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_CONNECTOR = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Connector")
_DATUM = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Datum")
_EXTERNAL_CAD_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "ExternalCADModel"
)
_FE_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "FEPart")
_FLEXIBLE_PIN_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "FlexiblePinAssembly"
)
_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Assembly")
_GUIDE_DXF_MODEL = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "GuideDxfModel"
)
_MASS_DISC = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "MassDisc")
_MEASUREMENT_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MeasurementComponent"
)
_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)
_OIL_SEAL = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "OilSeal")
_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")
_PLANET_CARRIER = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "PlanetCarrier"
)
_POINT_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PointLoad")
_POWER_LOAD = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "PowerLoad")
_ROOT_ASSEMBLY = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "RootAssembly")
_SPECIALISED_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "SpecialisedAssembly"
)
_UNBALANCED_MASS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "UnbalancedMass"
)
_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)
_SHAFT = python_net_import("SMT.MastaAPI.SystemModel.PartModel.ShaftModel", "Shaft")
_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses", "HarmonicAnalysis"
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2725
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses import (
        _7484,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7696,
        _7711,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5800,
        _5802,
        _5803,
        _5804,
        _5805,
        _5806,
        _5807,
        _5808,
        _5809,
        _5810,
        _5811,
        _5812,
        _5813,
        _5814,
        _5815,
        _5816,
        _5817,
        _5818,
        _5819,
        _5820,
        _5821,
        _5822,
        _5823,
        _5824,
        _5825,
        _5827,
        _5828,
        _5829,
        _5830,
        _5831,
        _5832,
        _5833,
        _5834,
        _5835,
        _5836,
        _5837,
        _5838,
        _5839,
        _5840,
        _5841,
        _5842,
        _5843,
        _5844,
        _5845,
        _5846,
        _5847,
        _5848,
        _5849,
        _5850,
        _5851,
        _5852,
        _5854,
        _5869,
        _5870,
        _5871,
        _5872,
        _5873,
        _5874,
        _5876,
        _5878,
        _5881,
        _5883,
        _5888,
        _5894,
        _5895,
        _5896,
        _5897,
        _5898,
        _5899,
        _5900,
        _5901,
        _5902,
        _5903,
        _5904,
        _5905,
        _5906,
        _5907,
        _5908,
        _5909,
        _5910,
        _5911,
        _5912,
        _5913,
        _5914,
        _5915,
        _5916,
        _5918,
        _5919,
        _5920,
        _5921,
        _5922,
        _5923,
        _5925,
        _5926,
        _5927,
        _5928,
        _5929,
        _5930,
        _5931,
        _5932,
        _5933,
        _5935,
        _5937,
        _5938,
        _5939,
        _5940,
        _5941,
        _5942,
        _5944,
        _5945,
        _5946,
        _5947,
        _5948,
        _5949,
        _5950,
        _5951,
        _5952,
        _5953,
        _5954,
        _5955,
        _5956,
        _5957,
        _5958,
        _5959,
        _5961,
        _5962,
        _5963,
        _5964,
        _5965,
        _5966,
        _5967,
        _5968,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6197,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7494,
        _7495,
        _7496,
        _7497,
        _7501,
        _7502,
        _7503,
        _7506,
        _7507,
        _7508,
        _7509,
        _7510,
        _7511,
        _7512,
        _7513,
        _7514,
        _7515,
        _7516,
        _7517,
        _7518,
        _7519,
        _7520,
        _7521,
        _7522,
        _7524,
        _7525,
        _7526,
        _7527,
        _7528,
        _7529,
        _7530,
        _7531,
        _7532,
        _7534,
        _7536,
        _7537,
        _7538,
        _7539,
        _7540,
        _7541,
        _7542,
        _7543,
        _7544,
        _7545,
        _7546,
        _7547,
        _7548,
        _7549,
        _7551,
        _7553,
        _7554,
        _7557,
        _7571,
        _7572,
        _7573,
        _7574,
        _7575,
        _7576,
        _7578,
        _7580,
        _7583,
        _7584,
        _7593,
        _7594,
        _7595,
        _7599,
        _7600,
        _7601,
        _7602,
        _7603,
        _7604,
        _7605,
        _7606,
        _7607,
        _7608,
        _7609,
        _7610,
        _7612,
        _7613,
        _7614,
        _7616,
        _7618,
        _7619,
        _7620,
        _7621,
        _7622,
        _7623,
        _7625,
        _7628,
        _7629,
        _7630,
        _7633,
        _7634,
        _7635,
        _7636,
        _7637,
        _7638,
        _7639,
        _7640,
        _7641,
        _7642,
        _7643,
        _7644,
        _7645,
        _7646,
        _7647,
        _7648,
        _7649,
        _7650,
        _7651,
        _7652,
        _7653,
        _7654,
        _7655,
        _7656,
        _7657,
        _7658,
        _7659,
        _7660,
        _7663,
        _7664,
        _7665,
        _7666,
        _7671,
        _7672,
        _7673,
        _7674,
        _7675,
        _7676,
        _7677,
        _7678,
    )
    from mastapy._private.system_model.connections_and_sockets import (
        _2331,
        _2334,
        _2335,
        _2338,
        _2339,
        _2347,
        _2353,
        _2358,
        _2361,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings import (
        _2408,
        _2410,
        _2412,
        _2414,
        _2416,
        _2418,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal import (
        _2401,
        _2404,
        _2407,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import (
        _2365,
        _2367,
        _2369,
        _2371,
        _2373,
        _2375,
        _2377,
        _2379,
        _2381,
        _2384,
        _2385,
        _2386,
        _2389,
        _2391,
        _2393,
        _2395,
        _2397,
    )
    from mastapy._private.system_model.part_model import (
        _2500,
        _2501,
        _2502,
        _2503,
        _2506,
        _2509,
        _2510,
        _2511,
        _2514,
        _2515,
        _2519,
        _2520,
        _2521,
        _2522,
        _2529,
        _2530,
        _2531,
        _2532,
        _2533,
        _2535,
        _2537,
        _2538,
        _2540,
        _2541,
        _2544,
        _2546,
        _2547,
        _2549,
    )
    from mastapy._private.system_model.part_model.couplings import (
        _2649,
        _2651,
        _2652,
        _2654,
        _2655,
        _2657,
        _2658,
        _2660,
        _2661,
        _2662,
        _2663,
        _2665,
        _2672,
        _2673,
        _2674,
        _2680,
        _2681,
        _2682,
        _2684,
        _2685,
        _2686,
        _2687,
        _2688,
        _2690,
    )
    from mastapy._private.system_model.part_model.cycloidal import _2640, _2641, _2642
    from mastapy._private.system_model.part_model.gears import (
        _2585,
        _2586,
        _2587,
        _2588,
        _2589,
        _2590,
        _2591,
        _2592,
        _2593,
        _2594,
        _2595,
        _2596,
        _2597,
        _2598,
        _2599,
        _2600,
        _2601,
        _2602,
        _2604,
        _2606,
        _2607,
        _2608,
        _2609,
        _2610,
        _2611,
        _2612,
        _2613,
        _2614,
        _2615,
        _2616,
        _2617,
        _2618,
        _2619,
        _2620,
        _2621,
        _2622,
        _2623,
        _2624,
        _2625,
        _2626,
    )
    from mastapy._private.system_model.part_model.shaft_model import _2552

    Self = TypeVar("Self", bound="HarmonicAnalysis")
    CastSelf = TypeVar("CastSelf", bound="HarmonicAnalysis._Cast_HarmonicAnalysis")


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HarmonicAnalysis:
    """Special nested class for casting HarmonicAnalysis to subclasses."""

    __parent__: "HarmonicAnalysis"

    @property
    def compound_analysis_case(self: "CastSelf") -> "_7698.CompoundAnalysisCase":
        return self.__parent__._cast(_7698.CompoundAnalysisCase)

    @property
    def static_load_analysis_case(self: "CastSelf") -> "_7711.StaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7711,
        )

        return self.__parent__._cast(_7711.StaticLoadAnalysisCase)

    @property
    def analysis_case(self: "CastSelf") -> "_7696.AnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7696,
        )

        return self.__parent__._cast(_7696.AnalysisCase)

    @property
    def context(self: "CastSelf") -> "_2725.Context":
        from mastapy._private.system_model.analyses_and_results import _2725

        return self.__parent__._cast(_2725.Context)

    @property
    def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_5888.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5888,
        )

        return self.__parent__._cast(
            _5888.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def harmonic_analysis(self: "CastSelf") -> "HarmonicAnalysis":
        return self.__parent__

    def __getattr__(self: "CastSelf", name: str) -> "Any":
        try:
            return self.__getattribute__(name)
        except AttributeError:
            class_name = utility.camel(name)
            raise CastException(
                f'Detected an invalid cast. Cannot cast to type "{class_name}"'
            ) from None


@extended_dataclass(frozen=True, slots=True, weakref_slot=True, eq=False)
class HarmonicAnalysis(_7698.CompoundAnalysisCase):
    """HarmonicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _HARMONIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def time_for_modal_analysis(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "TimeForModalAnalysis")

        if temp is None:
            return 0.0

        return temp

    @property
    def time_for_single_excitations_post_analysis(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "TimeForSingleExcitationsPostAnalysis"
        )

        if temp is None:
            return 0.0

        return temp

    @property
    def time_to_run_single_excitations(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "TimeToRunSingleExcitations")

        if temp is None:
            return 0.0

        return temp

    @property
    def acoustic_analysis(self: "Self") -> "_7484.HarmonicAcousticAnalysis":
        """mastapy.system_model.analyses_and_results.acoustic_analyses.HarmonicAcousticAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AcousticAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analyses_of_single_excitations(
        self: "Self",
    ) -> "List[_6197.HarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "HarmonicAnalysesOfSingleExcitations"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection(
        self: "Self", design_entity: "_2414.PartToPartShearCouplingConnection"
    ) -> "_5914.PartToPartShearCouplingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.PartToPartShearCouplingConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PART_TO_PART_SHEAR_COUPLING_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7619.PartToPartShearCouplingConnectionLoadCase",
    ) -> "_5914.PartToPartShearCouplingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PART_TO_PART_SHEAR_COUPLING_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_connection(
        self: "Self", design_entity: "_2408.ClutchConnection"
    ) -> "_5822.ClutchConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ClutchConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CLUTCH_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_connection_load_case(
        self: "Self", design_entity_analysis: "_7520.ClutchConnectionLoadCase"
    ) -> "_5822.ClutchConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ClutchConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CLUTCH_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_connection(
        self: "Self", design_entity: "_2410.ConceptCouplingConnection"
    ) -> "_5828.ConceptCouplingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_COUPLING_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_connection_load_case(
        self: "Self", design_entity_analysis: "_7526.ConceptCouplingConnectionLoadCase"
    ) -> "_5828.ConceptCouplingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_COUPLING_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_connection(
        self: "Self", design_entity: "_2412.CouplingConnection"
    ) -> "_5839.CouplingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_COUPLING_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_connection_load_case(
        self: "Self", design_entity_analysis: "_7539.CouplingConnectionLoadCase"
    ) -> "_5839.CouplingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_COUPLING_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_connection(
        self: "Self", design_entity: "_2416.SpringDamperConnection"
    ) -> "_5940.SpringDamperConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpringDamperConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPRING_DAMPER_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_connection_load_case(
        self: "Self", design_entity_analysis: "_7646.SpringDamperConnectionLoadCase"
    ) -> "_5940.SpringDamperConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpringDamperConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPRING_DAMPER_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection(
        self: "Self", design_entity: "_2418.TorqueConverterConnection"
    ) -> "_5956.TorqueConverterConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_TORQUE_CONVERTER_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_connection_load_case(
        self: "Self", design_entity_analysis: "_7663.TorqueConverterConnectionLoadCase"
    ) -> "_5956.TorqueConverterConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_TORQUE_CONVERTER_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear(
        self: "Self", design_entity: "_2619.StraightBevelGear"
    ) -> "_5947.StraightBevelGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_load_case(
        self: "Self", design_entity_analysis: "_7652.StraightBevelGearLoadCase"
    ) -> "_5947.StraightBevelGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set(
        self: "Self", design_entity: "_2620.StraightBevelGearSet"
    ) -> "_5949.StraightBevelGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7654.StraightBevelGearSetLoadCase"
    ) -> "_5949.StraightBevelGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear(
        self: "Self", design_entity: "_2621.StraightBevelPlanetGear"
    ) -> "_5950.StraightBevelPlanetGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelPlanetGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_PLANET_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_planet_gear_load_case(
        self: "Self", design_entity_analysis: "_7655.StraightBevelPlanetGearLoadCase"
    ) -> "_5950.StraightBevelPlanetGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelPlanetGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear(
        self: "Self", design_entity: "_2622.StraightBevelSunGear"
    ) -> "_5951.StraightBevelSunGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelSunGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_SUN_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_sun_gear_load_case(
        self: "Self", design_entity_analysis: "_7656.StraightBevelSunGearLoadCase"
    ) -> "_5951.StraightBevelSunGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelSunGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_SUN_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear(
        self: "Self", design_entity: "_2623.WormGear"
    ) -> "_5963.WormGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_WORM_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_load_case(
        self: "Self", design_entity_analysis: "_7673.WormGearLoadCase"
    ) -> "_5963.WormGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_WORM_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_set(
        self: "Self", design_entity: "_2624.WormGearSet"
    ) -> "_5965.WormGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_WORM_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7675.WormGearSetLoadCase"
    ) -> "_5965.WormGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_WORM_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear(
        self: "Self", design_entity: "_2625.ZerolBevelGear"
    ) -> "_5966.ZerolBevelGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ZEROL_BEVEL_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_load_case(
        self: "Self", design_entity_analysis: "_7676.ZerolBevelGearLoadCase"
    ) -> "_5966.ZerolBevelGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ZEROL_BEVEL_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set(
        self: "Self", design_entity: "_2626.ZerolBevelGearSet"
    ) -> "_5968.ZerolBevelGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ZEROL_BEVEL_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7678.ZerolBevelGearSetLoadCase"
    ) -> "_5968.ZerolBevelGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ZEROL_BEVEL_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly(
        self: "Self", design_entity: "_2640.CycloidalAssembly"
    ) -> "_5845.CycloidalAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalAssemblyHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalAssembly)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYCLOIDAL_ASSEMBLY],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_assembly_load_case(
        self: "Self", design_entity_analysis: "_7545.CycloidalAssemblyLoadCase"
    ) -> "_5845.CycloidalAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalAssemblyHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYCLOIDAL_ASSEMBLY_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc(
        self: "Self", design_entity: "_2641.CycloidalDisc"
    ) -> "_5847.CycloidalDiscHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.CycloidalDisc)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYCLOIDAL_DISC],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_load_case(
        self: "Self", design_entity_analysis: "_7547.CycloidalDiscLoadCase"
    ) -> "_5847.CycloidalDiscHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYCLOIDAL_DISC_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins(
        self: "Self", design_entity: "_2642.RingPins"
    ) -> "_5925.RingPinsHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RingPinsHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.cycloidal.RingPins)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_RING_PINS],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_load_case(
        self: "Self", design_entity_analysis: "_7633.RingPinsLoadCase"
    ) -> "_5925.RingPinsHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RingPinsHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_RING_PINS_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling(
        self: "Self", design_entity: "_2662.PartToPartShearCoupling"
    ) -> "_5916.PartToPartShearCouplingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCoupling)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PART_TO_PART_SHEAR_COUPLING],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_load_case(
        self: "Self", design_entity_analysis: "_7621.PartToPartShearCouplingLoadCase"
    ) -> "_5916.PartToPartShearCouplingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PART_TO_PART_SHEAR_COUPLING_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half(
        self: "Self", design_entity: "_2663.PartToPartShearCouplingHalf"
    ) -> "_5915.PartToPartShearCouplingHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingHalfHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PART_TO_PART_SHEAR_COUPLING_HALF],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_to_part_shear_coupling_half_load_case(
        self: "Self",
        design_entity_analysis: "_7620.PartToPartShearCouplingHalfLoadCase",
    ) -> "_5915.PartToPartShearCouplingHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PartToPartShearCouplingHalfHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PART_TO_PART_SHEAR_COUPLING_HALF_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_drive(
        self: "Self", design_entity: "_2649.BeltDrive"
    ) -> "_5811.BeltDriveHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BeltDriveHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BELT_DRIVE],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_drive_load_case(
        self: "Self", design_entity_analysis: "_7509.BeltDriveLoadCase"
    ) -> "_5811.BeltDriveHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BeltDriveHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BELT_DRIVE_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch(
        self: "Self", design_entity: "_2651.Clutch"
    ) -> "_5824.ClutchHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ClutchHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CLUTCH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_load_case(
        self: "Self", design_entity_analysis: "_7522.ClutchLoadCase"
    ) -> "_5824.ClutchHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ClutchHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CLUTCH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_half(
        self: "Self", design_entity: "_2652.ClutchHalf"
    ) -> "_5823.ClutchHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ClutchHalfHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CLUTCH_HALF],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_clutch_half_load_case(
        self: "Self", design_entity_analysis: "_7521.ClutchHalfLoadCase"
    ) -> "_5823.ClutchHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ClutchHalfHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CLUTCH_HALF_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling(
        self: "Self", design_entity: "_2654.ConceptCoupling"
    ) -> "_5830.ConceptCouplingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_COUPLING],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_load_case(
        self: "Self", design_entity_analysis: "_7528.ConceptCouplingLoadCase"
    ) -> "_5830.ConceptCouplingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_COUPLING_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half(
        self: "Self", design_entity: "_2655.ConceptCouplingHalf"
    ) -> "_5829.ConceptCouplingHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHalfHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_COUPLING_HALF],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_coupling_half_load_case(
        self: "Self", design_entity_analysis: "_7527.ConceptCouplingHalfLoadCase"
    ) -> "_5829.ConceptCouplingHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptCouplingHalfHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_COUPLING_HALF_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling(
        self: "Self", design_entity: "_2657.Coupling"
    ) -> "_5841.CouplingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_COUPLING],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_load_case(
        self: "Self", design_entity_analysis: "_7541.CouplingLoadCase"
    ) -> "_5841.CouplingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_COUPLING_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_half(
        self: "Self", design_entity: "_2658.CouplingHalf"
    ) -> "_5840.CouplingHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHalfHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_COUPLING_HALF],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coupling_half_load_case(
        self: "Self", design_entity_analysis: "_7540.CouplingHalfLoadCase"
    ) -> "_5840.CouplingHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHalfHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_COUPLING_HALF_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt(
        self: "Self", design_entity: "_2660.CVT"
    ) -> "_5843.CVTHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CVTHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CVT],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_load_case(
        self: "Self", design_entity_analysis: "_7543.CVTLoadCase"
    ) -> "_5843.CVTHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CVTHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CVT_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_pulley(
        self: "Self", design_entity: "_2661.CVTPulley"
    ) -> "_5844.CVTPulleyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CVTPulleyHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CVT_PULLEY],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_pulley_load_case(
        self: "Self", design_entity_analysis: "_7544.CVTPulleyLoadCase"
    ) -> "_5844.CVTPulleyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CVTPulleyHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CVT_PULLEY_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_pulley(
        self: "Self", design_entity: "_2665.Pulley"
    ) -> "_5923.PulleyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PulleyHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PULLEY],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_pulley_load_case(
        self: "Self", design_entity_analysis: "_7630.PulleyLoadCase"
    ) -> "_5923.PulleyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PulleyHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PULLEY_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection(
        self: "Self", design_entity: "_2674.ShaftHubConnection"
    ) -> "_5932.ShaftHubConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftHubConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SHAFT_HUB_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_hub_connection_load_case(
        self: "Self", design_entity_analysis: "_7639.ShaftHubConnectionLoadCase"
    ) -> "_5932.ShaftHubConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftHubConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SHAFT_HUB_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring(
        self: "Self", design_entity: "_2672.RollingRing"
    ) -> "_5929.RollingRingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RollingRingHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ROLLING_RING],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_load_case(
        self: "Self", design_entity_analysis: "_7637.RollingRingLoadCase"
    ) -> "_5929.RollingRingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RollingRingHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ROLLING_RING_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly(
        self: "Self", design_entity: "_2673.RollingRingAssembly"
    ) -> "_5927.RollingRingAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RollingRingAssemblyHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ROLLING_RING_ASSEMBLY],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_assembly_load_case(
        self: "Self", design_entity_analysis: "_7635.RollingRingAssemblyLoadCase"
    ) -> "_5927.RollingRingAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RollingRingAssemblyHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ROLLING_RING_ASSEMBLY_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper(
        self: "Self", design_entity: "_2680.SpringDamper"
    ) -> "_5942.SpringDamperHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpringDamperHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPRING_DAMPER],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_load_case(
        self: "Self", design_entity_analysis: "_7648.SpringDamperLoadCase"
    ) -> "_5942.SpringDamperHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpringDamperHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPRING_DAMPER_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_half(
        self: "Self", design_entity: "_2681.SpringDamperHalf"
    ) -> "_5941.SpringDamperHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpringDamperHalfHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPRING_DAMPER_HALF],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spring_damper_half_load_case(
        self: "Self", design_entity_analysis: "_7647.SpringDamperHalfLoadCase"
    ) -> "_5941.SpringDamperHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpringDamperHalfHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPRING_DAMPER_HALF_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser(
        self: "Self", design_entity: "_2682.Synchroniser"
    ) -> "_5953.SynchroniserHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SYNCHRONISER],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_load_case(
        self: "Self", design_entity_analysis: "_7658.SynchroniserLoadCase"
    ) -> "_5953.SynchroniserHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SYNCHRONISER_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_half(
        self: "Self", design_entity: "_2684.SynchroniserHalf"
    ) -> "_5952.SynchroniserHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserHalfHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SYNCHRONISER_HALF],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_half_load_case(
        self: "Self", design_entity_analysis: "_7657.SynchroniserHalfLoadCase"
    ) -> "_5952.SynchroniserHalfHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserHalfHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SYNCHRONISER_HALF_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_part(
        self: "Self", design_entity: "_2685.SynchroniserPart"
    ) -> "_5954.SynchroniserPartHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserPartHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SYNCHRONISER_PART],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_part_load_case(
        self: "Self", design_entity_analysis: "_7659.SynchroniserPartLoadCase"
    ) -> "_5954.SynchroniserPartHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserPartHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SYNCHRONISER_PART_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve(
        self: "Self", design_entity: "_2686.SynchroniserSleeve"
    ) -> "_5955.SynchroniserSleeveHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserSleeveHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SYNCHRONISER_SLEEVE],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_synchroniser_sleeve_load_case(
        self: "Self", design_entity_analysis: "_7660.SynchroniserSleeveLoadCase"
    ) -> "_5955.SynchroniserSleeveHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SynchroniserSleeveHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SYNCHRONISER_SLEEVE_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter(
        self: "Self", design_entity: "_2687.TorqueConverter"
    ) -> "_5957.TorqueConverterHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_TORQUE_CONVERTER],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_load_case(
        self: "Self", design_entity_analysis: "_7664.TorqueConverterLoadCase"
    ) -> "_5957.TorqueConverterHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_TORQUE_CONVERTER_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump(
        self: "Self", design_entity: "_2688.TorqueConverterPump"
    ) -> "_5958.TorqueConverterPumpHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterPumpHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_TORQUE_CONVERTER_PUMP],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_pump_load_case(
        self: "Self", design_entity_analysis: "_7665.TorqueConverterPumpLoadCase"
    ) -> "_5958.TorqueConverterPumpHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterPumpHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_TORQUE_CONVERTER_PUMP_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine(
        self: "Self", design_entity: "_2690.TorqueConverterTurbine"
    ) -> "_5959.TorqueConverterTurbineHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterTurbineHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_TORQUE_CONVERTER_TURBINE],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_torque_converter_turbine_load_case(
        self: "Self", design_entity_analysis: "_7666.TorqueConverterTurbineLoadCase"
    ) -> "_5959.TorqueConverterTurbineHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.TorqueConverterTurbineHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_TORQUE_CONVERTER_TURBINE_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection(
        self: "Self", design_entity: "_2361.ShaftToMountableComponentConnection"
    ) -> "_5933.ShaftToMountableComponentConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftToMountableComponentConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_to_mountable_component_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7641.ShaftToMountableComponentConnectionLoadCase",
    ) -> "_5933.ShaftToMountableComponentConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftToMountableComponentConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection(
        self: "Self", design_entity: "_2339.CVTBeltConnection"
    ) -> "_5842.CVTBeltConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CVTBeltConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CVT_BELT_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cvt_belt_connection_load_case(
        self: "Self", design_entity_analysis: "_7542.CVTBeltConnectionLoadCase"
    ) -> "_5842.CVTBeltConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CVTBeltConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CVT_BELT_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_connection(
        self: "Self", design_entity: "_2334.BeltConnection"
    ) -> "_5810.BeltConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BeltConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BELT_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_belt_connection_load_case(
        self: "Self", design_entity_analysis: "_7508.BeltConnectionLoadCase"
    ) -> "_5810.BeltConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BeltConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BELT_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coaxial_connection(
        self: "Self", design_entity: "_2335.CoaxialConnection"
    ) -> "_5825.CoaxialConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CoaxialConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_COAXIAL_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_coaxial_connection_load_case(
        self: "Self", design_entity_analysis: "_7524.CoaxialConnectionLoadCase"
    ) -> "_5825.CoaxialConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CoaxialConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_COAXIAL_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connection(
        self: "Self", design_entity: "_2338.Connection"
    ) -> "_5837.ConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connection_load_case(
        self: "Self", design_entity_analysis: "_7537.ConnectionLoadCase"
    ) -> "_5837.ConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection(
        self: "Self", design_entity: "_2347.InterMountableComponentConnection"
    ) -> "_5897.InterMountableComponentConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.InterMountableComponentConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_INTER_MOUNTABLE_COMPONENT_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_inter_mountable_component_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7599.InterMountableComponentConnectionLoadCase",
    ) -> "_5897.InterMountableComponentConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.InterMountableComponentConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_connection(
        self: "Self", design_entity: "_2353.PlanetaryConnection"
    ) -> "_5918.PlanetaryConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetaryConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PLANETARY_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_connection_load_case(
        self: "Self", design_entity_analysis: "_7622.PlanetaryConnectionLoadCase"
    ) -> "_5918.PlanetaryConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetaryConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PLANETARY_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection(
        self: "Self", design_entity: "_2358.RollingRingConnection"
    ) -> "_5928.RollingRingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RollingRingConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ROLLING_RING_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_rolling_ring_connection_load_case(
        self: "Self", design_entity_analysis: "_7636.RollingRingConnectionLoadCase"
    ) -> "_5928.RollingRingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RollingRingConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ROLLING_RING_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection(
        self: "Self", design_entity: "_2331.AbstractShaftToMountableComponentConnection"
    ) -> "_5804.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftToMountableComponentConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_to_mountable_component_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7497.AbstractShaftToMountableComponentConnectionLoadCase",
    ) -> "_5804.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftToMountableComponentConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftToMountableComponentConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh(
        self: "Self", design_entity: "_2367.BevelDifferentialGearMesh"
    ) -> "_5813.BevelDifferentialGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_DIFFERENTIAL_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7511.BevelDifferentialGearMeshLoadCase"
    ) -> "_5813.BevelDifferentialGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh(
        self: "Self", design_entity: "_2371.ConceptGearMesh"
    ) -> "_5832.ConceptGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7530.ConceptGearMeshLoadCase"
    ) -> "_5832.ConceptGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh(
        self: "Self", design_entity: "_2377.FaceGearMesh"
    ) -> "_5871.FaceGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_FACE_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7573.FaceGearMeshLoadCase"
    ) -> "_5871.FaceGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_FACE_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh(
        self: "Self", design_entity: "_2391.StraightBevelDiffGearMesh"
    ) -> "_5945.StraightBevelDiffGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_DIFF_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7650.StraightBevelDiffGearMeshLoadCase"
    ) -> "_5945.StraightBevelDiffGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh(
        self: "Self", design_entity: "_2369.BevelGearMesh"
    ) -> "_5818.BevelGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7516.BevelGearMeshLoadCase"
    ) -> "_5818.BevelGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh(
        self: "Self", design_entity: "_2373.ConicalGearMesh"
    ) -> "_5835.ConicalGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONICAL_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7534.ConicalGearMeshLoadCase"
    ) -> "_5835.ConicalGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONICAL_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh(
        self: "Self", design_entity: "_2365.AGMAGleasonConicalGearMesh"
    ) -> "_5806.AGMAGleasonConicalGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_AGMA_GLEASON_CONICAL_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7502.AGMAGleasonConicalGearMeshLoadCase"
    ) -> "_5806.AGMAGleasonConicalGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_AGMA_GLEASON_CONICAL_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh(
        self: "Self", design_entity: "_2375.CylindricalGearMesh"
    ) -> "_5850.CylindricalGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYLINDRICAL_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7551.CylindricalGearMeshLoadCase"
    ) -> "_5850.CylindricalGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYLINDRICAL_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh(
        self: "Self", design_entity: "_2381.HypoidGearMesh"
    ) -> "_5895.HypoidGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_HYPOID_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7594.HypoidGearMeshLoadCase"
    ) -> "_5895.HypoidGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_HYPOID_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: "Self", design_entity: "_2384.KlingelnbergCycloPalloidConicalGearMesh"
    ) -> "_5899.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
        self: "Self",
        design_entity_analysis: "_7601.KlingelnbergCycloPalloidConicalGearMeshLoadCase",
    ) -> "_5899.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: "Self", design_entity: "_2385.KlingelnbergCycloPalloidHypoidGearMesh"
    ) -> "_5902.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
        self: "Self",
        design_entity_analysis: "_7604.KlingelnbergCycloPalloidHypoidGearMeshLoadCase",
    ) -> "_5902.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: "Self", design_entity: "_2386.KlingelnbergCycloPalloidSpiralBevelGearMesh"
    ) -> "_5905.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
        self: "Self",
        design_entity_analysis: "_7607.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase",
    ) -> "_5905.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh(
        self: "Self", design_entity: "_2389.SpiralBevelGearMesh"
    ) -> "_5938.SpiralBevelGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPIRAL_BEVEL_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7644.SpiralBevelGearMeshLoadCase"
    ) -> "_5938.SpiralBevelGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPIRAL_BEVEL_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh(
        self: "Self", design_entity: "_2393.StraightBevelGearMesh"
    ) -> "_5948.StraightBevelGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7653.StraightBevelGearMeshLoadCase"
    ) -> "_5948.StraightBevelGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh(
        self: "Self", design_entity: "_2395.WormGearMesh"
    ) -> "_5964.WormGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_WORM_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_worm_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7674.WormGearMeshLoadCase"
    ) -> "_5964.WormGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.WormGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_WORM_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh(
        self: "Self", design_entity: "_2397.ZerolBevelGearMesh"
    ) -> "_5967.ZerolBevelGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ZEROL_BEVEL_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_zerol_bevel_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7677.ZerolBevelGearMeshLoadCase"
    ) -> "_5967.ZerolBevelGearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ZerolBevelGearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ZEROL_BEVEL_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_mesh(
        self: "Self", design_entity: "_2379.GearMesh"
    ) -> "_5878.GearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.GearMeshHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_GEAR_MESH],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_mesh_load_case(
        self: "Self", design_entity_analysis: "_7580.GearMeshLoadCase"
    ) -> "_5878.GearMeshHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.GearMeshHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_GEAR_MESH_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection(
        self: "Self", design_entity: "_2401.CycloidalDiscCentralBearingConnection"
    ) -> "_5846.CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscCentralBearingConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_central_bearing_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7546.CycloidalDiscCentralBearingConnectionLoadCase",
    ) -> "_5846.CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscCentralBearingConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscCentralBearingConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection(
        self: "Self", design_entity: "_2404.CycloidalDiscPlanetaryBearingConnection"
    ) -> "_5848.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cycloidal_disc_planetary_bearing_connection_load_case(
        self: "Self",
        design_entity_analysis: "_7548.CycloidalDiscPlanetaryBearingConnectionLoadCase",
    ) -> "_5848.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection(
        self: "Self", design_entity: "_2407.RingPinsToDiscConnection"
    ) -> "_5926.RingPinsToDiscConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RingPinsToDiscConnectionHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_RING_PINS_TO_DISC_CONNECTION],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_ring_pins_to_disc_connection_load_case(
        self: "Self", design_entity_analysis: "_7634.RingPinsToDiscConnectionLoadCase"
    ) -> "_5926.RingPinsToDiscConnectionHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RingPinsToDiscConnectionHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_RING_PINS_TO_DISC_CONNECTION_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft(
        self: "Self", design_entity: "_2502.AbstractShaft"
    ) -> "_5802.AbstractShaftHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaft)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ABSTRACT_SHAFT],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_load_case(
        self: "Self", design_entity_analysis: "_7495.AbstractShaftLoadCase"
    ) -> "_5802.AbstractShaftHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ABSTRACT_SHAFT_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_microphone(
        self: "Self", design_entity: "_2531.Microphone"
    ) -> "_5910.MicrophoneHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.MicrophoneHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Microphone)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_MICROPHONE],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_microphone_load_case(
        self: "Self", design_entity_analysis: "_7613.MicrophoneLoadCase"
    ) -> "_5910.MicrophoneHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.MicrophoneHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MicrophoneLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_MICROPHONE_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_microphone_array(
        self: "Self", design_entity: "_2532.MicrophoneArray"
    ) -> "_5909.MicrophoneArrayHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.MicrophoneArrayHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.MicrophoneArray)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_MICROPHONE_ARRAY],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_microphone_array_load_case(
        self: "Self", design_entity_analysis: "_7612.MicrophoneArrayLoadCase"
    ) -> "_5909.MicrophoneArrayHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.MicrophoneArrayHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MicrophoneArrayLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_MICROPHONE_ARRAY_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_assembly(
        self: "Self", design_entity: "_2501.AbstractAssembly"
    ) -> "_5800.AbstractAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractAssemblyHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ABSTRACT_ASSEMBLY],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_assembly_load_case(
        self: "Self", design_entity_analysis: "_7494.AbstractAssemblyLoadCase"
    ) -> "_5800.AbstractAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractAssemblyHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ABSTRACT_ASSEMBLY_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing(
        self: "Self", design_entity: "_2503.AbstractShaftOrHousing"
    ) -> "_5803.AbstractShaftOrHousingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftOrHousingHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ABSTRACT_SHAFT_OR_HOUSING],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_abstract_shaft_or_housing_load_case(
        self: "Self", design_entity_analysis: "_7496.AbstractShaftOrHousingLoadCase"
    ) -> "_5803.AbstractShaftOrHousingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AbstractShaftOrHousingHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ABSTRACT_SHAFT_OR_HOUSING_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bearing(
        self: "Self", design_entity: "_2506.Bearing"
    ) -> "_5809.BearingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BearingHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEARING],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bearing_load_case(
        self: "Self", design_entity_analysis: "_7507.BearingLoadCase"
    ) -> "_5809.BearingHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BearingHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEARING_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolt(
        self: "Self", design_entity: "_2509.Bolt"
    ) -> "_5821.BoltHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BoltHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BOLT],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolt_load_case(
        self: "Self", design_entity_analysis: "_7519.BoltLoadCase"
    ) -> "_5821.BoltHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BoltHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BOLT_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolted_joint(
        self: "Self", design_entity: "_2510.BoltedJoint"
    ) -> "_5820.BoltedJointHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BoltedJointHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BOLTED_JOINT],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bolted_joint_load_case(
        self: "Self", design_entity_analysis: "_7518.BoltedJointLoadCase"
    ) -> "_5820.BoltedJointHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BoltedJointHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BOLTED_JOINT_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_component(
        self: "Self", design_entity: "_2511.Component"
    ) -> "_5827.ComponentHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ComponentHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Component)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_COMPONENT],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_component_load_case(
        self: "Self", design_entity_analysis: "_7525.ComponentLoadCase"
    ) -> "_5827.ComponentHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ComponentHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_COMPONENT_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connector(
        self: "Self", design_entity: "_2514.Connector"
    ) -> "_5838.ConnectorHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConnectorHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Connector)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONNECTOR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_connector_load_case(
        self: "Self", design_entity_analysis: "_7538.ConnectorLoadCase"
    ) -> "_5838.ConnectorHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConnectorHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONNECTOR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_datum(
        self: "Self", design_entity: "_2515.Datum"
    ) -> "_5854.DatumHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.DatumHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Datum)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_DATUM],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_datum_load_case(
        self: "Self", design_entity_analysis: "_7557.DatumLoadCase"
    ) -> "_5854.DatumHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.DatumHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_DATUM_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_external_cad_model(
        self: "Self", design_entity: "_2519.ExternalCADModel"
    ) -> "_5869.ExternalCADModelHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ExternalCADModelHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_EXTERNAL_CAD_MODEL],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_external_cad_model_load_case(
        self: "Self", design_entity_analysis: "_7571.ExternalCADModelLoadCase"
    ) -> "_5869.ExternalCADModelHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ExternalCADModelHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_EXTERNAL_CAD_MODEL_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_fe_part(
        self: "Self", design_entity: "_2520.FEPart"
    ) -> "_5873.FEPartHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FEPartHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.FEPart)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_FE_PART],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_fe_part_load_case(
        self: "Self", design_entity_analysis: "_7575.FEPartLoadCase"
    ) -> "_5873.FEPartHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FEPartHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_FE_PART_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly(
        self: "Self", design_entity: "_2521.FlexiblePinAssembly"
    ) -> "_5874.FlexiblePinAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FlexiblePinAssemblyHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_FLEXIBLE_PIN_ASSEMBLY],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_flexible_pin_assembly_load_case(
        self: "Self", design_entity_analysis: "_7576.FlexiblePinAssemblyLoadCase"
    ) -> "_5874.FlexiblePinAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FlexiblePinAssemblyHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_assembly(
        self: "Self", design_entity: "_2500.Assembly"
    ) -> "_5808.AssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AssemblyHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ASSEMBLY],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_assembly_load_case(
        self: "Self", design_entity_analysis: "_7506.AssemblyLoadCase"
    ) -> "_5808.AssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AssemblyHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ASSEMBLY_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model(
        self: "Self", design_entity: "_2522.GuideDxfModel"
    ) -> "_5883.GuideDxfModelHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.GuideDxfModelHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_GUIDE_DXF_MODEL],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_guide_dxf_model_load_case(
        self: "Self", design_entity_analysis: "_7584.GuideDxfModelLoadCase"
    ) -> "_5883.GuideDxfModelHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.GuideDxfModelHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_GUIDE_DXF_MODEL_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mass_disc(
        self: "Self", design_entity: "_2529.MassDisc"
    ) -> "_5907.MassDiscHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.MassDiscHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_MASS_DISC],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mass_disc_load_case(
        self: "Self", design_entity_analysis: "_7609.MassDiscLoadCase"
    ) -> "_5907.MassDiscHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.MassDiscHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_MASS_DISC_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_measurement_component(
        self: "Self", design_entity: "_2530.MeasurementComponent"
    ) -> "_5908.MeasurementComponentHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.MeasurementComponentHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_MEASUREMENT_COMPONENT],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_measurement_component_load_case(
        self: "Self", design_entity_analysis: "_7610.MeasurementComponentLoadCase"
    ) -> "_5908.MeasurementComponentHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.MeasurementComponentHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_MEASUREMENT_COMPONENT_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mountable_component(
        self: "Self", design_entity: "_2533.MountableComponent"
    ) -> "_5911.MountableComponentHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.MountableComponentHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_MOUNTABLE_COMPONENT],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_mountable_component_load_case(
        self: "Self", design_entity_analysis: "_7614.MountableComponentLoadCase"
    ) -> "_5911.MountableComponentHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.MountableComponentHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_MOUNTABLE_COMPONENT_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_oil_seal(
        self: "Self", design_entity: "_2535.OilSeal"
    ) -> "_5912.OilSealHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.OilSealHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_OIL_SEAL],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_oil_seal_load_case(
        self: "Self", design_entity_analysis: "_7616.OilSealLoadCase"
    ) -> "_5912.OilSealHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.OilSealHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_OIL_SEAL_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part(
        self: "Self", design_entity: "_2537.Part"
    ) -> "_5913.PartHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PartHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.Part)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PART],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_part_load_case(
        self: "Self", design_entity_analysis: "_7618.PartLoadCase"
    ) -> "_5913.PartHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PartHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PartLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PART_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planet_carrier(
        self: "Self", design_entity: "_2538.PlanetCarrier"
    ) -> "_5920.PlanetCarrierHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetCarrierHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PLANET_CARRIER],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planet_carrier_load_case(
        self: "Self", design_entity_analysis: "_7625.PlanetCarrierLoadCase"
    ) -> "_5920.PlanetCarrierHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetCarrierHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PLANET_CARRIER_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_point_load(
        self: "Self", design_entity: "_2540.PointLoad"
    ) -> "_5921.PointLoadHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PointLoadHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_POINT_LOAD],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_point_load_load_case(
        self: "Self", design_entity_analysis: "_7628.PointLoadLoadCase"
    ) -> "_5921.PointLoadHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PointLoadHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_POINT_LOAD_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_power_load(
        self: "Self", design_entity: "_2541.PowerLoad"
    ) -> "_5922.PowerLoadHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PowerLoadHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_POWER_LOAD],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_power_load_load_case(
        self: "Self", design_entity_analysis: "_7629.PowerLoadLoadCase"
    ) -> "_5922.PowerLoadHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PowerLoadHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_POWER_LOAD_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_root_assembly(
        self: "Self", design_entity: "_2544.RootAssembly"
    ) -> "_5930.RootAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RootAssemblyHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ROOT_ASSEMBLY],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_root_assembly_load_case(
        self: "Self", design_entity_analysis: "_7638.RootAssemblyLoadCase"
    ) -> "_5930.RootAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.RootAssemblyHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_ROOT_ASSEMBLY_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_specialised_assembly(
        self: "Self", design_entity: "_2546.SpecialisedAssembly"
    ) -> "_5935.SpecialisedAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpecialisedAssemblyHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPECIALISED_ASSEMBLY],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_specialised_assembly_load_case(
        self: "Self", design_entity_analysis: "_7642.SpecialisedAssemblyLoadCase"
    ) -> "_5935.SpecialisedAssemblyHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpecialisedAssemblyHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPECIALISED_ASSEMBLY_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass(
        self: "Self", design_entity: "_2547.UnbalancedMass"
    ) -> "_5961.UnbalancedMassHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.UnbalancedMassHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_UNBALANCED_MASS],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_unbalanced_mass_load_case(
        self: "Self", design_entity_analysis: "_7671.UnbalancedMassLoadCase"
    ) -> "_5961.UnbalancedMassHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.UnbalancedMassHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_UNBALANCED_MASS_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_virtual_component(
        self: "Self", design_entity: "_2549.VirtualComponent"
    ) -> "_5962.VirtualComponentHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.VirtualComponentHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_VIRTUAL_COMPONENT],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_virtual_component_load_case(
        self: "Self", design_entity_analysis: "_7672.VirtualComponentLoadCase"
    ) -> "_5962.VirtualComponentHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.VirtualComponentHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_VIRTUAL_COMPONENT_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft(
        self: "Self", design_entity: "_2552.Shaft"
    ) -> "_5931.ShaftHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SHAFT],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_shaft_load_case(
        self: "Self", design_entity_analysis: "_7640.ShaftLoadCase"
    ) -> "_5931.ShaftHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ShaftHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SHAFT_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear(
        self: "Self", design_entity: "_2593.ConceptGear"
    ) -> "_5831.ConceptGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_load_case(
        self: "Self", design_entity_analysis: "_7529.ConceptGearLoadCase"
    ) -> "_5831.ConceptGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_set(
        self: "Self", design_entity: "_2594.ConceptGearSet"
    ) -> "_5833.ConceptGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_concept_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7531.ConceptGearSetLoadCase"
    ) -> "_5833.ConceptGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConceptGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONCEPT_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear(
        self: "Self", design_entity: "_2600.FaceGear"
    ) -> "_5870.FaceGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_FACE_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_load_case(
        self: "Self", design_entity_analysis: "_7572.FaceGearLoadCase"
    ) -> "_5870.FaceGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_FACE_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_set(
        self: "Self", design_entity: "_2601.FaceGearSet"
    ) -> "_5872.FaceGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_FACE_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_face_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7574.FaceGearSetLoadCase"
    ) -> "_5872.FaceGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.FaceGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_FACE_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear(
        self: "Self", design_entity: "_2585.AGMAGleasonConicalGear"
    ) -> "_5805.AGMAGleasonConicalGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_AGMA_GLEASON_CONICAL_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_load_case(
        self: "Self", design_entity_analysis: "_7501.AGMAGleasonConicalGearLoadCase"
    ) -> "_5805.AGMAGleasonConicalGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_AGMA_GLEASON_CONICAL_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set(
        self: "Self", design_entity: "_2586.AGMAGleasonConicalGearSet"
    ) -> "_5807.AGMAGleasonConicalGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_AGMA_GLEASON_CONICAL_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_agma_gleason_conical_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7503.AGMAGleasonConicalGearSetLoadCase"
    ) -> "_5807.AGMAGleasonConicalGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear(
        self: "Self", design_entity: "_2587.BevelDifferentialGear"
    ) -> "_5812.BevelDifferentialGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_DIFFERENTIAL_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_load_case(
        self: "Self", design_entity_analysis: "_7510.BevelDifferentialGearLoadCase"
    ) -> "_5812.BevelDifferentialGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set(
        self: "Self", design_entity: "_2588.BevelDifferentialGearSet"
    ) -> "_5814.BevelDifferentialGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_DIFFERENTIAL_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7512.BevelDifferentialGearSetLoadCase"
    ) -> "_5814.BevelDifferentialGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear(
        self: "Self", design_entity: "_2589.BevelDifferentialPlanetGear"
    ) -> "_5815.BevelDifferentialPlanetGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialPlanetGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_DIFFERENTIAL_PLANET_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_planet_gear_load_case(
        self: "Self",
        design_entity_analysis: "_7513.BevelDifferentialPlanetGearLoadCase",
    ) -> "_5815.BevelDifferentialPlanetGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialPlanetGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear(
        self: "Self", design_entity: "_2590.BevelDifferentialSunGear"
    ) -> "_5816.BevelDifferentialSunGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialSunGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_DIFFERENTIAL_SUN_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_differential_sun_gear_load_case(
        self: "Self", design_entity_analysis: "_7514.BevelDifferentialSunGearLoadCase"
    ) -> "_5816.BevelDifferentialSunGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelDifferentialSunGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_DIFFERENTIAL_SUN_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear(
        self: "Self", design_entity: "_2591.BevelGear"
    ) -> "_5817.BevelGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_load_case(
        self: "Self", design_entity_analysis: "_7515.BevelGearLoadCase"
    ) -> "_5817.BevelGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set(
        self: "Self", design_entity: "_2592.BevelGearSet"
    ) -> "_5819.BevelGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_bevel_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7517.BevelGearSetLoadCase"
    ) -> "_5819.BevelGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.BevelGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_BEVEL_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear(
        self: "Self", design_entity: "_2595.ConicalGear"
    ) -> "_5834.ConicalGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONICAL_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_load_case(
        self: "Self", design_entity_analysis: "_7532.ConicalGearLoadCase"
    ) -> "_5834.ConicalGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONICAL_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_set(
        self: "Self", design_entity: "_2596.ConicalGearSet"
    ) -> "_5836.ConicalGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONICAL_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_conical_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7536.ConicalGearSetLoadCase"
    ) -> "_5836.ConicalGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CONICAL_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear(
        self: "Self", design_entity: "_2597.CylindricalGear"
    ) -> "_5849.CylindricalGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYLINDRICAL_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_load_case(
        self: "Self", design_entity_analysis: "_7549.CylindricalGearLoadCase"
    ) -> "_5849.CylindricalGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYLINDRICAL_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set(
        self: "Self", design_entity: "_2598.CylindricalGearSet"
    ) -> "_5851.CylindricalGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYLINDRICAL_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7553.CylindricalGearSetLoadCase"
    ) -> "_5851.CylindricalGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYLINDRICAL_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear(
        self: "Self", design_entity: "_2599.CylindricalPlanetGear"
    ) -> "_5852.CylindricalPlanetGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalPlanetGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYLINDRICAL_PLANET_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_cylindrical_planet_gear_load_case(
        self: "Self", design_entity_analysis: "_7554.CylindricalPlanetGearLoadCase"
    ) -> "_5852.CylindricalPlanetGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalPlanetGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_CYLINDRICAL_PLANET_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear(
        self: "Self", design_entity: "_2602.Gear"
    ) -> "_5876.GearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.GearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_load_case(
        self: "Self", design_entity_analysis: "_7578.GearLoadCase"
    ) -> "_5876.GearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.GearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_set(
        self: "Self", design_entity: "_2604.GearSet"
    ) -> "_5881.GearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.GearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7583.GearSetLoadCase"
    ) -> "_5881.GearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.GearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear(
        self: "Self", design_entity: "_2606.HypoidGear"
    ) -> "_5894.HypoidGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_HYPOID_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_load_case(
        self: "Self", design_entity_analysis: "_7593.HypoidGearLoadCase"
    ) -> "_5894.HypoidGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_HYPOID_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set(
        self: "Self", design_entity: "_2607.HypoidGearSet"
    ) -> "_5896.HypoidGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_HYPOID_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_hypoid_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7595.HypoidGearSetLoadCase"
    ) -> "_5896.HypoidGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HypoidGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_HYPOID_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear(
        self: "Self", design_entity: "_2608.KlingelnbergCycloPalloidConicalGear"
    ) -> "_5898.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_load_case(
        self: "Self",
        design_entity_analysis: "_7600.KlingelnbergCycloPalloidConicalGearLoadCase",
    ) -> "_5898.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set(
        self: "Self", design_entity: "_2609.KlingelnbergCycloPalloidConicalGearSet"
    ) -> "_5900.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_conical_gear_set_load_case(
        self: "Self",
        design_entity_analysis: "_7602.KlingelnbergCycloPalloidConicalGearSetLoadCase",
    ) -> "_5900.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear(
        self: "Self", design_entity: "_2610.KlingelnbergCycloPalloidHypoidGear"
    ) -> "_5901.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_load_case(
        self: "Self",
        design_entity_analysis: "_7603.KlingelnbergCycloPalloidHypoidGearLoadCase",
    ) -> "_5901.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: "Self", design_entity: "_2611.KlingelnbergCycloPalloidHypoidGearSet"
    ) -> "_5903.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
        self: "Self",
        design_entity_analysis: "_7605.KlingelnbergCycloPalloidHypoidGearSetLoadCase",
    ) -> "_5903.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: "Self", design_entity: "_2612.KlingelnbergCycloPalloidSpiralBevelGear"
    ) -> "_5904.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
        self: "Self",
        design_entity_analysis: "_7606.KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
    ) -> "_5904.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: "Self", design_entity: "_2613.KlingelnbergCycloPalloidSpiralBevelGearSet"
    ) -> "_5906.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
        self: "Self",
        design_entity_analysis: "_7608.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase",
    ) -> "_5906.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set(
        self: "Self", design_entity: "_2614.PlanetaryGearSet"
    ) -> "_5919.PlanetaryGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetaryGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PLANETARY_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_planetary_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7623.PlanetaryGearSetLoadCase"
    ) -> "_5919.PlanetaryGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetaryGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_PLANETARY_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear(
        self: "Self", design_entity: "_2615.SpiralBevelGear"
    ) -> "_5937.SpiralBevelGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPIRAL_BEVEL_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_load_case(
        self: "Self", design_entity_analysis: "_7643.SpiralBevelGearLoadCase"
    ) -> "_5937.SpiralBevelGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPIRAL_BEVEL_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set(
        self: "Self", design_entity: "_2616.SpiralBevelGearSet"
    ) -> "_5939.SpiralBevelGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPIRAL_BEVEL_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_spiral_bevel_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7645.SpiralBevelGearSetLoadCase"
    ) -> "_5939.SpiralBevelGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear(
        self: "Self", design_entity: "_2617.StraightBevelDiffGear"
    ) -> "_5944.StraightBevelDiffGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_DIFF_GEAR],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_load_case(
        self: "Self", design_entity_analysis: "_7649.StraightBevelDiffGearLoadCase"
    ) -> "_5944.StraightBevelDiffGearHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_DIFF_GEAR_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set(
        self: "Self", design_entity: "_2618.StraightBevelDiffGearSet"
    ) -> "_5946.StraightBevelDiffGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearSetHarmonicAnalysis

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_DIFF_GEAR_SET],
            design_entity.wrapped if design_entity else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def results_for_straight_bevel_diff_gear_set_load_case(
        self: "Self", design_entity_analysis: "_7651.StraightBevelDiffGearSetLoadCase"
    ) -> "_5946.StraightBevelDiffGearSetHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.StraightBevelDiffGearSetHarmonicAnalysis

        Args:
            design_entity_analysis (mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ResultsFor",
            [_STRAIGHT_BEVEL_DIFF_GEAR_SET_LOAD_CASE],
            design_entity_analysis.wrapped if design_entity_analysis else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_HarmonicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_HarmonicAnalysis
        """
        return _Cast_HarmonicAnalysis(self)
