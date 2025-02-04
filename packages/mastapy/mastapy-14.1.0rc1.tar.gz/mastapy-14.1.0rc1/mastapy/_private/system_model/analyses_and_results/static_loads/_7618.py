"""PartLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import (
    constructor,
    conversion,
    enum_with_selected_value_runtime,
    utility,
)
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.implicit import (
    enum_with_selected_value,
    list_with_selected_item,
)
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_method_call,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.system_model.analyses_and_results import _2732
from mastapy._private.system_model.analyses_and_results.static_loads import _7493, _7585

_PART_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PartLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.electric_machines.harmonic_load_data import _1438
    from mastapy._private.system_model.analyses_and_results import _2726, _2728
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7494,
        _7495,
        _7496,
        _7501,
        _7503,
        _7506,
        _7507,
        _7509,
        _7510,
        _7512,
        _7513,
        _7514,
        _7515,
        _7517,
        _7518,
        _7519,
        _7521,
        _7522,
        _7525,
        _7527,
        _7528,
        _7529,
        _7531,
        _7532,
        _7536,
        _7538,
        _7540,
        _7541,
        _7543,
        _7544,
        _7545,
        _7547,
        _7549,
        _7553,
        _7554,
        _7557,
        _7571,
        _7572,
        _7574,
        _7575,
        _7576,
        _7578,
        _7583,
        _7584,
        _7593,
        _7595,
        _7600,
        _7602,
        _7603,
        _7605,
        _7606,
        _7608,
        _7609,
        _7610,
        _7612,
        _7613,
        _7614,
        _7616,
        _7620,
        _7621,
        _7623,
        _7625,
        _7628,
        _7629,
        _7630,
        _7633,
        _7635,
        _7637,
        _7638,
        _7639,
        _7640,
        _7642,
        _7643,
        _7645,
        _7647,
        _7648,
        _7649,
        _7651,
        _7652,
        _7654,
        _7655,
        _7656,
        _7657,
        _7658,
        _7659,
        _7660,
        _7662,
        _7664,
        _7665,
        _7666,
        _7671,
        _7672,
        _7673,
        _7675,
        _7676,
        _7678,
    )
    from mastapy._private.system_model.part_model import _2537

    Self = TypeVar("Self", bound="PartLoadCase")
    CastSelf = TypeVar("CastSelf", bound="PartLoadCase._Cast_PartLoadCase")


__docformat__ = "restructuredtext en"
__all__ = ("PartLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartLoadCase:
    """Special nested class for casting PartLoadCase to subclasses."""

    __parent__: "PartLoadCase"

    @property
    def part_analysis(self: "CastSelf") -> "_2732.PartAnalysis":
        return self.__parent__._cast(_2732.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2728.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2728

        return self.__parent__._cast(_2728.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2726.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2726

        return self.__parent__._cast(_2726.DesignEntityAnalysis)

    @property
    def abstract_assembly_load_case(
        self: "CastSelf",
    ) -> "_7494.AbstractAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7494,
        )

        return self.__parent__._cast(_7494.AbstractAssemblyLoadCase)

    @property
    def abstract_shaft_load_case(self: "CastSelf") -> "_7495.AbstractShaftLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7495,
        )

        return self.__parent__._cast(_7495.AbstractShaftLoadCase)

    @property
    def abstract_shaft_or_housing_load_case(
        self: "CastSelf",
    ) -> "_7496.AbstractShaftOrHousingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7496,
        )

        return self.__parent__._cast(_7496.AbstractShaftOrHousingLoadCase)

    @property
    def agma_gleason_conical_gear_load_case(
        self: "CastSelf",
    ) -> "_7501.AGMAGleasonConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7501,
        )

        return self.__parent__._cast(_7501.AGMAGleasonConicalGearLoadCase)

    @property
    def agma_gleason_conical_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7503.AGMAGleasonConicalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7503,
        )

        return self.__parent__._cast(_7503.AGMAGleasonConicalGearSetLoadCase)

    @property
    def assembly_load_case(self: "CastSelf") -> "_7506.AssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7506,
        )

        return self.__parent__._cast(_7506.AssemblyLoadCase)

    @property
    def bearing_load_case(self: "CastSelf") -> "_7507.BearingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7507,
        )

        return self.__parent__._cast(_7507.BearingLoadCase)

    @property
    def belt_drive_load_case(self: "CastSelf") -> "_7509.BeltDriveLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7509,
        )

        return self.__parent__._cast(_7509.BeltDriveLoadCase)

    @property
    def bevel_differential_gear_load_case(
        self: "CastSelf",
    ) -> "_7510.BevelDifferentialGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7510,
        )

        return self.__parent__._cast(_7510.BevelDifferentialGearLoadCase)

    @property
    def bevel_differential_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7512.BevelDifferentialGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7512,
        )

        return self.__parent__._cast(_7512.BevelDifferentialGearSetLoadCase)

    @property
    def bevel_differential_planet_gear_load_case(
        self: "CastSelf",
    ) -> "_7513.BevelDifferentialPlanetGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7513,
        )

        return self.__parent__._cast(_7513.BevelDifferentialPlanetGearLoadCase)

    @property
    def bevel_differential_sun_gear_load_case(
        self: "CastSelf",
    ) -> "_7514.BevelDifferentialSunGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7514,
        )

        return self.__parent__._cast(_7514.BevelDifferentialSunGearLoadCase)

    @property
    def bevel_gear_load_case(self: "CastSelf") -> "_7515.BevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7515,
        )

        return self.__parent__._cast(_7515.BevelGearLoadCase)

    @property
    def bevel_gear_set_load_case(self: "CastSelf") -> "_7517.BevelGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7517,
        )

        return self.__parent__._cast(_7517.BevelGearSetLoadCase)

    @property
    def bolted_joint_load_case(self: "CastSelf") -> "_7518.BoltedJointLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7518,
        )

        return self.__parent__._cast(_7518.BoltedJointLoadCase)

    @property
    def bolt_load_case(self: "CastSelf") -> "_7519.BoltLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7519,
        )

        return self.__parent__._cast(_7519.BoltLoadCase)

    @property
    def clutch_half_load_case(self: "CastSelf") -> "_7521.ClutchHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7521,
        )

        return self.__parent__._cast(_7521.ClutchHalfLoadCase)

    @property
    def clutch_load_case(self: "CastSelf") -> "_7522.ClutchLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7522,
        )

        return self.__parent__._cast(_7522.ClutchLoadCase)

    @property
    def component_load_case(self: "CastSelf") -> "_7525.ComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7525,
        )

        return self.__parent__._cast(_7525.ComponentLoadCase)

    @property
    def concept_coupling_half_load_case(
        self: "CastSelf",
    ) -> "_7527.ConceptCouplingHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7527,
        )

        return self.__parent__._cast(_7527.ConceptCouplingHalfLoadCase)

    @property
    def concept_coupling_load_case(self: "CastSelf") -> "_7528.ConceptCouplingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7528,
        )

        return self.__parent__._cast(_7528.ConceptCouplingLoadCase)

    @property
    def concept_gear_load_case(self: "CastSelf") -> "_7529.ConceptGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7529,
        )

        return self.__parent__._cast(_7529.ConceptGearLoadCase)

    @property
    def concept_gear_set_load_case(self: "CastSelf") -> "_7531.ConceptGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7531,
        )

        return self.__parent__._cast(_7531.ConceptGearSetLoadCase)

    @property
    def conical_gear_load_case(self: "CastSelf") -> "_7532.ConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7532,
        )

        return self.__parent__._cast(_7532.ConicalGearLoadCase)

    @property
    def conical_gear_set_load_case(self: "CastSelf") -> "_7536.ConicalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7536,
        )

        return self.__parent__._cast(_7536.ConicalGearSetLoadCase)

    @property
    def connector_load_case(self: "CastSelf") -> "_7538.ConnectorLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7538,
        )

        return self.__parent__._cast(_7538.ConnectorLoadCase)

    @property
    def coupling_half_load_case(self: "CastSelf") -> "_7540.CouplingHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7540,
        )

        return self.__parent__._cast(_7540.CouplingHalfLoadCase)

    @property
    def coupling_load_case(self: "CastSelf") -> "_7541.CouplingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7541,
        )

        return self.__parent__._cast(_7541.CouplingLoadCase)

    @property
    def cvt_load_case(self: "CastSelf") -> "_7543.CVTLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7543,
        )

        return self.__parent__._cast(_7543.CVTLoadCase)

    @property
    def cvt_pulley_load_case(self: "CastSelf") -> "_7544.CVTPulleyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7544,
        )

        return self.__parent__._cast(_7544.CVTPulleyLoadCase)

    @property
    def cycloidal_assembly_load_case(
        self: "CastSelf",
    ) -> "_7545.CycloidalAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7545,
        )

        return self.__parent__._cast(_7545.CycloidalAssemblyLoadCase)

    @property
    def cycloidal_disc_load_case(self: "CastSelf") -> "_7547.CycloidalDiscLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7547,
        )

        return self.__parent__._cast(_7547.CycloidalDiscLoadCase)

    @property
    def cylindrical_gear_load_case(self: "CastSelf") -> "_7549.CylindricalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7549,
        )

        return self.__parent__._cast(_7549.CylindricalGearLoadCase)

    @property
    def cylindrical_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7553.CylindricalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7553,
        )

        return self.__parent__._cast(_7553.CylindricalGearSetLoadCase)

    @property
    def cylindrical_planet_gear_load_case(
        self: "CastSelf",
    ) -> "_7554.CylindricalPlanetGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7554,
        )

        return self.__parent__._cast(_7554.CylindricalPlanetGearLoadCase)

    @property
    def datum_load_case(self: "CastSelf") -> "_7557.DatumLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7557,
        )

        return self.__parent__._cast(_7557.DatumLoadCase)

    @property
    def external_cad_model_load_case(
        self: "CastSelf",
    ) -> "_7571.ExternalCADModelLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7571,
        )

        return self.__parent__._cast(_7571.ExternalCADModelLoadCase)

    @property
    def face_gear_load_case(self: "CastSelf") -> "_7572.FaceGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7572,
        )

        return self.__parent__._cast(_7572.FaceGearLoadCase)

    @property
    def face_gear_set_load_case(self: "CastSelf") -> "_7574.FaceGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7574,
        )

        return self.__parent__._cast(_7574.FaceGearSetLoadCase)

    @property
    def fe_part_load_case(self: "CastSelf") -> "_7575.FEPartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7575,
        )

        return self.__parent__._cast(_7575.FEPartLoadCase)

    @property
    def flexible_pin_assembly_load_case(
        self: "CastSelf",
    ) -> "_7576.FlexiblePinAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7576,
        )

        return self.__parent__._cast(_7576.FlexiblePinAssemblyLoadCase)

    @property
    def gear_load_case(self: "CastSelf") -> "_7578.GearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7578,
        )

        return self.__parent__._cast(_7578.GearLoadCase)

    @property
    def gear_set_load_case(self: "CastSelf") -> "_7583.GearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7583,
        )

        return self.__parent__._cast(_7583.GearSetLoadCase)

    @property
    def guide_dxf_model_load_case(self: "CastSelf") -> "_7584.GuideDxfModelLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7584,
        )

        return self.__parent__._cast(_7584.GuideDxfModelLoadCase)

    @property
    def hypoid_gear_load_case(self: "CastSelf") -> "_7593.HypoidGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7593,
        )

        return self.__parent__._cast(_7593.HypoidGearLoadCase)

    @property
    def hypoid_gear_set_load_case(self: "CastSelf") -> "_7595.HypoidGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7595,
        )

        return self.__parent__._cast(_7595.HypoidGearSetLoadCase)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_load_case(
        self: "CastSelf",
    ) -> "_7600.KlingelnbergCycloPalloidConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7600,
        )

        return self.__parent__._cast(_7600.KlingelnbergCycloPalloidConicalGearLoadCase)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7602.KlingelnbergCycloPalloidConicalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7602,
        )

        return self.__parent__._cast(
            _7602.KlingelnbergCycloPalloidConicalGearSetLoadCase
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
        self: "CastSelf",
    ) -> "_7603.KlingelnbergCycloPalloidHypoidGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7603,
        )

        return self.__parent__._cast(_7603.KlingelnbergCycloPalloidHypoidGearLoadCase)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7605.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7605,
        )

        return self.__parent__._cast(
            _7605.KlingelnbergCycloPalloidHypoidGearSetLoadCase
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
        self: "CastSelf",
    ) -> "_7606.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7606,
        )

        return self.__parent__._cast(
            _7606.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7608.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7608,
        )

        return self.__parent__._cast(
            _7608.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
        )

    @property
    def mass_disc_load_case(self: "CastSelf") -> "_7609.MassDiscLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7609,
        )

        return self.__parent__._cast(_7609.MassDiscLoadCase)

    @property
    def measurement_component_load_case(
        self: "CastSelf",
    ) -> "_7610.MeasurementComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7610,
        )

        return self.__parent__._cast(_7610.MeasurementComponentLoadCase)

    @property
    def microphone_array_load_case(self: "CastSelf") -> "_7612.MicrophoneArrayLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7612,
        )

        return self.__parent__._cast(_7612.MicrophoneArrayLoadCase)

    @property
    def microphone_load_case(self: "CastSelf") -> "_7613.MicrophoneLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7613,
        )

        return self.__parent__._cast(_7613.MicrophoneLoadCase)

    @property
    def mountable_component_load_case(
        self: "CastSelf",
    ) -> "_7614.MountableComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7614,
        )

        return self.__parent__._cast(_7614.MountableComponentLoadCase)

    @property
    def oil_seal_load_case(self: "CastSelf") -> "_7616.OilSealLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7616,
        )

        return self.__parent__._cast(_7616.OilSealLoadCase)

    @property
    def part_to_part_shear_coupling_half_load_case(
        self: "CastSelf",
    ) -> "_7620.PartToPartShearCouplingHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7620,
        )

        return self.__parent__._cast(_7620.PartToPartShearCouplingHalfLoadCase)

    @property
    def part_to_part_shear_coupling_load_case(
        self: "CastSelf",
    ) -> "_7621.PartToPartShearCouplingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7621,
        )

        return self.__parent__._cast(_7621.PartToPartShearCouplingLoadCase)

    @property
    def planetary_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7623.PlanetaryGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7623,
        )

        return self.__parent__._cast(_7623.PlanetaryGearSetLoadCase)

    @property
    def planet_carrier_load_case(self: "CastSelf") -> "_7625.PlanetCarrierLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7625,
        )

        return self.__parent__._cast(_7625.PlanetCarrierLoadCase)

    @property
    def point_load_load_case(self: "CastSelf") -> "_7628.PointLoadLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7628,
        )

        return self.__parent__._cast(_7628.PointLoadLoadCase)

    @property
    def power_load_load_case(self: "CastSelf") -> "_7629.PowerLoadLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7629,
        )

        return self.__parent__._cast(_7629.PowerLoadLoadCase)

    @property
    def pulley_load_case(self: "CastSelf") -> "_7630.PulleyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7630,
        )

        return self.__parent__._cast(_7630.PulleyLoadCase)

    @property
    def ring_pins_load_case(self: "CastSelf") -> "_7633.RingPinsLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7633,
        )

        return self.__parent__._cast(_7633.RingPinsLoadCase)

    @property
    def rolling_ring_assembly_load_case(
        self: "CastSelf",
    ) -> "_7635.RollingRingAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7635,
        )

        return self.__parent__._cast(_7635.RollingRingAssemblyLoadCase)

    @property
    def rolling_ring_load_case(self: "CastSelf") -> "_7637.RollingRingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7637,
        )

        return self.__parent__._cast(_7637.RollingRingLoadCase)

    @property
    def root_assembly_load_case(self: "CastSelf") -> "_7638.RootAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7638,
        )

        return self.__parent__._cast(_7638.RootAssemblyLoadCase)

    @property
    def shaft_hub_connection_load_case(
        self: "CastSelf",
    ) -> "_7639.ShaftHubConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7639,
        )

        return self.__parent__._cast(_7639.ShaftHubConnectionLoadCase)

    @property
    def shaft_load_case(self: "CastSelf") -> "_7640.ShaftLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7640,
        )

        return self.__parent__._cast(_7640.ShaftLoadCase)

    @property
    def specialised_assembly_load_case(
        self: "CastSelf",
    ) -> "_7642.SpecialisedAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7642,
        )

        return self.__parent__._cast(_7642.SpecialisedAssemblyLoadCase)

    @property
    def spiral_bevel_gear_load_case(
        self: "CastSelf",
    ) -> "_7643.SpiralBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7643,
        )

        return self.__parent__._cast(_7643.SpiralBevelGearLoadCase)

    @property
    def spiral_bevel_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7645.SpiralBevelGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7645,
        )

        return self.__parent__._cast(_7645.SpiralBevelGearSetLoadCase)

    @property
    def spring_damper_half_load_case(
        self: "CastSelf",
    ) -> "_7647.SpringDamperHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7647,
        )

        return self.__parent__._cast(_7647.SpringDamperHalfLoadCase)

    @property
    def spring_damper_load_case(self: "CastSelf") -> "_7648.SpringDamperLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7648,
        )

        return self.__parent__._cast(_7648.SpringDamperLoadCase)

    @property
    def straight_bevel_diff_gear_load_case(
        self: "CastSelf",
    ) -> "_7649.StraightBevelDiffGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7649,
        )

        return self.__parent__._cast(_7649.StraightBevelDiffGearLoadCase)

    @property
    def straight_bevel_diff_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7651.StraightBevelDiffGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7651,
        )

        return self.__parent__._cast(_7651.StraightBevelDiffGearSetLoadCase)

    @property
    def straight_bevel_gear_load_case(
        self: "CastSelf",
    ) -> "_7652.StraightBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7652,
        )

        return self.__parent__._cast(_7652.StraightBevelGearLoadCase)

    @property
    def straight_bevel_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7654.StraightBevelGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7654,
        )

        return self.__parent__._cast(_7654.StraightBevelGearSetLoadCase)

    @property
    def straight_bevel_planet_gear_load_case(
        self: "CastSelf",
    ) -> "_7655.StraightBevelPlanetGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7655,
        )

        return self.__parent__._cast(_7655.StraightBevelPlanetGearLoadCase)

    @property
    def straight_bevel_sun_gear_load_case(
        self: "CastSelf",
    ) -> "_7656.StraightBevelSunGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7656,
        )

        return self.__parent__._cast(_7656.StraightBevelSunGearLoadCase)

    @property
    def synchroniser_half_load_case(
        self: "CastSelf",
    ) -> "_7657.SynchroniserHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7657,
        )

        return self.__parent__._cast(_7657.SynchroniserHalfLoadCase)

    @property
    def synchroniser_load_case(self: "CastSelf") -> "_7658.SynchroniserLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7658,
        )

        return self.__parent__._cast(_7658.SynchroniserLoadCase)

    @property
    def synchroniser_part_load_case(
        self: "CastSelf",
    ) -> "_7659.SynchroniserPartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7659,
        )

        return self.__parent__._cast(_7659.SynchroniserPartLoadCase)

    @property
    def synchroniser_sleeve_load_case(
        self: "CastSelf",
    ) -> "_7660.SynchroniserSleeveLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7660,
        )

        return self.__parent__._cast(_7660.SynchroniserSleeveLoadCase)

    @property
    def torque_converter_load_case(self: "CastSelf") -> "_7664.TorqueConverterLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7664,
        )

        return self.__parent__._cast(_7664.TorqueConverterLoadCase)

    @property
    def torque_converter_pump_load_case(
        self: "CastSelf",
    ) -> "_7665.TorqueConverterPumpLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7665,
        )

        return self.__parent__._cast(_7665.TorqueConverterPumpLoadCase)

    @property
    def torque_converter_turbine_load_case(
        self: "CastSelf",
    ) -> "_7666.TorqueConverterTurbineLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7666,
        )

        return self.__parent__._cast(_7666.TorqueConverterTurbineLoadCase)

    @property
    def unbalanced_mass_load_case(self: "CastSelf") -> "_7671.UnbalancedMassLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7671,
        )

        return self.__parent__._cast(_7671.UnbalancedMassLoadCase)

    @property
    def virtual_component_load_case(
        self: "CastSelf",
    ) -> "_7672.VirtualComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7672,
        )

        return self.__parent__._cast(_7672.VirtualComponentLoadCase)

    @property
    def worm_gear_load_case(self: "CastSelf") -> "_7673.WormGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7673,
        )

        return self.__parent__._cast(_7673.WormGearLoadCase)

    @property
    def worm_gear_set_load_case(self: "CastSelf") -> "_7675.WormGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7675,
        )

        return self.__parent__._cast(_7675.WormGearSetLoadCase)

    @property
    def zerol_bevel_gear_load_case(self: "CastSelf") -> "_7676.ZerolBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7676,
        )

        return self.__parent__._cast(_7676.ZerolBevelGearLoadCase)

    @property
    def zerol_bevel_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7678.ZerolBevelGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7678,
        )

        return self.__parent__._cast(_7678.ZerolBevelGearSetLoadCase)

    @property
    def part_load_case(self: "CastSelf") -> "PartLoadCase":
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
class PartLoadCase(_2732.PartAnalysis):
    """PartLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def excitation_data_is_up_to_date(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ExcitationDataIsUpToDate")

        if temp is None:
            return False

        return temp

    @property
    def harmonic_excitation_type(
        self: "Self",
    ) -> "enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType":
        """EnumWithSelectedValue[mastapy.system_model.analyses_and_results.static_loads.HarmonicExcitationType]"""
        temp = pythonnet_property_get(self.wrapped, "HarmonicExcitationType")

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value)

    @harmonic_excitation_type.setter
    @enforce_parameter_types
    def harmonic_excitation_type(
        self: "Self", value: "_7585.HarmonicExcitationType"
    ) -> None:
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_HarmonicExcitationType.implicit_type()
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        pythonnet_property_set(self.wrapped, "HarmonicExcitationType", value)

    @property
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_StaticLoadCase":
        """ListWithSelectedItem[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]"""
        temp = pythonnet_property_get(
            self.wrapped,
            "LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp",
        )

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_StaticLoadCase",
        )(temp)

    @load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up.setter
    @enforce_parameter_types
    def load_case_for_harmonic_excitation_type_advanced_system_deflection_current_load_case_set_up(
        self: "Self", value: "_7493.StaticLoadCase"
    ) -> None:
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        pythonnet_property_set(
            self.wrapped,
            "LoadCaseForHarmonicExcitationTypeAdvancedSystemDeflectionCurrentLoadCaseSetUp",
            value,
        )

    @property
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(
        self: "Self",
    ) -> "bool":
        """bool"""
        temp = pythonnet_property_get(
            self.wrapped,
            "UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp",
        )

        if temp is None:
            return False

        return temp

    @use_this_load_case_for_advanced_system_deflection_current_load_case_set_up.setter
    @enforce_parameter_types
    def use_this_load_case_for_advanced_system_deflection_current_load_case_set_up(
        self: "Self", value: "bool"
    ) -> None:
        pythonnet_property_set(
            self.wrapped,
            "UseThisLoadCaseForAdvancedSystemDeflectionCurrentLoadCaseSetUp",
            bool(value) if value is not None else False,
        )

    @property
    def component_design(self: "Self") -> "_2537.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_load_case(self: "Self") -> "_7493.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "StaticLoadCase")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case(self: "Self") -> "_7662.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "TimeSeriesLoadCase")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def clear_user_specified_excitation_data_for_this_load_case(self: "Self") -> None:
        """Method does not return."""
        pythonnet_method_call(
            self.wrapped, "ClearUserSpecifiedExcitationDataForThisLoadCase"
        )

    def get_harmonic_load_data_for_import(self: "Self") -> "_1438.HarmonicLoadDataBase":
        """mastapy.electric_machines.harmonic_load_data.HarmonicLoadDataBase"""
        method_result = pythonnet_method_call(
            self.wrapped, "GetHarmonicLoadDataForImport"
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_PartLoadCase":
        """Cast to another type.

        Returns:
            _Cast_PartLoadCase
        """
        return _Cast_PartLoadCase(self)
