"""MountableComponentLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.static_loads import _7525

_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MountableComponentLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7501,
        _7507,
        _7510,
        _7513,
        _7514,
        _7515,
        _7521,
        _7527,
        _7529,
        _7532,
        _7538,
        _7540,
        _7544,
        _7549,
        _7554,
        _7572,
        _7578,
        _7593,
        _7600,
        _7603,
        _7606,
        _7609,
        _7610,
        _7616,
        _7618,
        _7620,
        _7625,
        _7628,
        _7629,
        _7630,
        _7633,
        _7637,
        _7639,
        _7643,
        _7647,
        _7649,
        _7652,
        _7655,
        _7656,
        _7657,
        _7659,
        _7660,
        _7665,
        _7666,
        _7671,
        _7672,
        _7673,
        _7676,
    )
    from mastapy._private.system_model.part_model import _2533

    Self = TypeVar("Self", bound="MountableComponentLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="MountableComponentLoadCase._Cast_MountableComponentLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MountableComponentLoadCase:
    """Special nested class for casting MountableComponentLoadCase to subclasses."""

    __parent__: "MountableComponentLoadCase"

    @property
    def component_load_case(self: "CastSelf") -> "_7525.ComponentLoadCase":
        return self.__parent__._cast(_7525.ComponentLoadCase)

    @property
    def part_load_case(self: "CastSelf") -> "_7618.PartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7618,
        )

        return self.__parent__._cast(_7618.PartLoadCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2732.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2732

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
    def agma_gleason_conical_gear_load_case(
        self: "CastSelf",
    ) -> "_7501.AGMAGleasonConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7501,
        )

        return self.__parent__._cast(_7501.AGMAGleasonConicalGearLoadCase)

    @property
    def bearing_load_case(self: "CastSelf") -> "_7507.BearingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7507,
        )

        return self.__parent__._cast(_7507.BearingLoadCase)

    @property
    def bevel_differential_gear_load_case(
        self: "CastSelf",
    ) -> "_7510.BevelDifferentialGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7510,
        )

        return self.__parent__._cast(_7510.BevelDifferentialGearLoadCase)

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
    def clutch_half_load_case(self: "CastSelf") -> "_7521.ClutchHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7521,
        )

        return self.__parent__._cast(_7521.ClutchHalfLoadCase)

    @property
    def concept_coupling_half_load_case(
        self: "CastSelf",
    ) -> "_7527.ConceptCouplingHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7527,
        )

        return self.__parent__._cast(_7527.ConceptCouplingHalfLoadCase)

    @property
    def concept_gear_load_case(self: "CastSelf") -> "_7529.ConceptGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7529,
        )

        return self.__parent__._cast(_7529.ConceptGearLoadCase)

    @property
    def conical_gear_load_case(self: "CastSelf") -> "_7532.ConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7532,
        )

        return self.__parent__._cast(_7532.ConicalGearLoadCase)

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
    def cvt_pulley_load_case(self: "CastSelf") -> "_7544.CVTPulleyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7544,
        )

        return self.__parent__._cast(_7544.CVTPulleyLoadCase)

    @property
    def cylindrical_gear_load_case(self: "CastSelf") -> "_7549.CylindricalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7549,
        )

        return self.__parent__._cast(_7549.CylindricalGearLoadCase)

    @property
    def cylindrical_planet_gear_load_case(
        self: "CastSelf",
    ) -> "_7554.CylindricalPlanetGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7554,
        )

        return self.__parent__._cast(_7554.CylindricalPlanetGearLoadCase)

    @property
    def face_gear_load_case(self: "CastSelf") -> "_7572.FaceGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7572,
        )

        return self.__parent__._cast(_7572.FaceGearLoadCase)

    @property
    def gear_load_case(self: "CastSelf") -> "_7578.GearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7578,
        )

        return self.__parent__._cast(_7578.GearLoadCase)

    @property
    def hypoid_gear_load_case(self: "CastSelf") -> "_7593.HypoidGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7593,
        )

        return self.__parent__._cast(_7593.HypoidGearLoadCase)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_load_case(
        self: "CastSelf",
    ) -> "_7600.KlingelnbergCycloPalloidConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7600,
        )

        return self.__parent__._cast(_7600.KlingelnbergCycloPalloidConicalGearLoadCase)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
        self: "CastSelf",
    ) -> "_7603.KlingelnbergCycloPalloidHypoidGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7603,
        )

        return self.__parent__._cast(_7603.KlingelnbergCycloPalloidHypoidGearLoadCase)

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
    def rolling_ring_load_case(self: "CastSelf") -> "_7637.RollingRingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7637,
        )

        return self.__parent__._cast(_7637.RollingRingLoadCase)

    @property
    def shaft_hub_connection_load_case(
        self: "CastSelf",
    ) -> "_7639.ShaftHubConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7639,
        )

        return self.__parent__._cast(_7639.ShaftHubConnectionLoadCase)

    @property
    def spiral_bevel_gear_load_case(
        self: "CastSelf",
    ) -> "_7643.SpiralBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7643,
        )

        return self.__parent__._cast(_7643.SpiralBevelGearLoadCase)

    @property
    def spring_damper_half_load_case(
        self: "CastSelf",
    ) -> "_7647.SpringDamperHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7647,
        )

        return self.__parent__._cast(_7647.SpringDamperHalfLoadCase)

    @property
    def straight_bevel_diff_gear_load_case(
        self: "CastSelf",
    ) -> "_7649.StraightBevelDiffGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7649,
        )

        return self.__parent__._cast(_7649.StraightBevelDiffGearLoadCase)

    @property
    def straight_bevel_gear_load_case(
        self: "CastSelf",
    ) -> "_7652.StraightBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7652,
        )

        return self.__parent__._cast(_7652.StraightBevelGearLoadCase)

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
    def zerol_bevel_gear_load_case(self: "CastSelf") -> "_7676.ZerolBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7676,
        )

        return self.__parent__._cast(_7676.ZerolBevelGearLoadCase)

    @property
    def mountable_component_load_case(self: "CastSelf") -> "MountableComponentLoadCase":
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
class MountableComponentLoadCase(_7525.ComponentLoadCase):
    """MountableComponentLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MOUNTABLE_COMPONENT_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2533.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_MountableComponentLoadCase":
        """Cast to another type.

        Returns:
            _Cast_MountableComponentLoadCase
        """
        return _Cast_MountableComponentLoadCase(self)
