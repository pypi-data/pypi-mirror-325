"""MountableComponentPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.power_flows import _4152

_MOUNTABLE_COMPONENT_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "MountableComponentPowerFlow",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import (
        _4132,
        _4135,
        _4139,
        _4141,
        _4142,
        _4144,
        _4149,
        _4154,
        _4157,
        _4160,
        _4163,
        _4165,
        _4169,
        _4176,
        _4178,
        _4182,
        _4189,
        _4193,
        _4197,
        _4200,
        _4203,
        _4205,
        _4206,
        _4210,
        _4211,
        _4213,
        _4217,
        _4218,
        _4221,
        _4222,
        _4223,
        _4227,
        _4229,
        _4234,
        _4237,
        _4240,
        _4243,
        _4245,
        _4246,
        _4247,
        _4248,
        _4250,
        _4254,
        _4255,
        _4256,
        _4257,
        _4259,
        _4262,
    )
    from mastapy._private.system_model.part_model import _2533

    Self = TypeVar("Self", bound="MountableComponentPowerFlow")
    CastSelf = TypeVar(
        "CastSelf",
        bound="MountableComponentPowerFlow._Cast_MountableComponentPowerFlow",
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MountableComponentPowerFlow:
    """Special nested class for casting MountableComponentPowerFlow to subclasses."""

    __parent__: "MountableComponentPowerFlow"

    @property
    def component_power_flow(self: "CastSelf") -> "_4152.ComponentPowerFlow":
        return self.__parent__._cast(_4152.ComponentPowerFlow)

    @property
    def part_power_flow(self: "CastSelf") -> "_4211.PartPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4211

        return self.__parent__._cast(_4211.PartPowerFlow)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7709.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7709,
        )

        return self.__parent__._cast(_7709.PartStaticLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7706.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7706,
        )

        return self.__parent__._cast(_7706.PartAnalysisCase)

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
    def agma_gleason_conical_gear_power_flow(
        self: "CastSelf",
    ) -> "_4132.AGMAGleasonConicalGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4132

        return self.__parent__._cast(_4132.AGMAGleasonConicalGearPowerFlow)

    @property
    def bearing_power_flow(self: "CastSelf") -> "_4135.BearingPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4135

        return self.__parent__._cast(_4135.BearingPowerFlow)

    @property
    def bevel_differential_gear_power_flow(
        self: "CastSelf",
    ) -> "_4139.BevelDifferentialGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4139

        return self.__parent__._cast(_4139.BevelDifferentialGearPowerFlow)

    @property
    def bevel_differential_planet_gear_power_flow(
        self: "CastSelf",
    ) -> "_4141.BevelDifferentialPlanetGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4141

        return self.__parent__._cast(_4141.BevelDifferentialPlanetGearPowerFlow)

    @property
    def bevel_differential_sun_gear_power_flow(
        self: "CastSelf",
    ) -> "_4142.BevelDifferentialSunGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4142

        return self.__parent__._cast(_4142.BevelDifferentialSunGearPowerFlow)

    @property
    def bevel_gear_power_flow(self: "CastSelf") -> "_4144.BevelGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4144

        return self.__parent__._cast(_4144.BevelGearPowerFlow)

    @property
    def clutch_half_power_flow(self: "CastSelf") -> "_4149.ClutchHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4149

        return self.__parent__._cast(_4149.ClutchHalfPowerFlow)

    @property
    def concept_coupling_half_power_flow(
        self: "CastSelf",
    ) -> "_4154.ConceptCouplingHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4154

        return self.__parent__._cast(_4154.ConceptCouplingHalfPowerFlow)

    @property
    def concept_gear_power_flow(self: "CastSelf") -> "_4157.ConceptGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4157

        return self.__parent__._cast(_4157.ConceptGearPowerFlow)

    @property
    def conical_gear_power_flow(self: "CastSelf") -> "_4160.ConicalGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4160

        return self.__parent__._cast(_4160.ConicalGearPowerFlow)

    @property
    def connector_power_flow(self: "CastSelf") -> "_4163.ConnectorPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4163

        return self.__parent__._cast(_4163.ConnectorPowerFlow)

    @property
    def coupling_half_power_flow(self: "CastSelf") -> "_4165.CouplingHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4165

        return self.__parent__._cast(_4165.CouplingHalfPowerFlow)

    @property
    def cvt_pulley_power_flow(self: "CastSelf") -> "_4169.CVTPulleyPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4169

        return self.__parent__._cast(_4169.CVTPulleyPowerFlow)

    @property
    def cylindrical_gear_power_flow(
        self: "CastSelf",
    ) -> "_4176.CylindricalGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4176

        return self.__parent__._cast(_4176.CylindricalGearPowerFlow)

    @property
    def cylindrical_planet_gear_power_flow(
        self: "CastSelf",
    ) -> "_4178.CylindricalPlanetGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4178

        return self.__parent__._cast(_4178.CylindricalPlanetGearPowerFlow)

    @property
    def face_gear_power_flow(self: "CastSelf") -> "_4182.FaceGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4182

        return self.__parent__._cast(_4182.FaceGearPowerFlow)

    @property
    def gear_power_flow(self: "CastSelf") -> "_4189.GearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4189

        return self.__parent__._cast(_4189.GearPowerFlow)

    @property
    def hypoid_gear_power_flow(self: "CastSelf") -> "_4193.HypoidGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4193

        return self.__parent__._cast(_4193.HypoidGearPowerFlow)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_power_flow(
        self: "CastSelf",
    ) -> "_4197.KlingelnbergCycloPalloidConicalGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4197

        return self.__parent__._cast(_4197.KlingelnbergCycloPalloidConicalGearPowerFlow)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_power_flow(
        self: "CastSelf",
    ) -> "_4200.KlingelnbergCycloPalloidHypoidGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4200

        return self.__parent__._cast(_4200.KlingelnbergCycloPalloidHypoidGearPowerFlow)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_power_flow(
        self: "CastSelf",
    ) -> "_4203.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4203

        return self.__parent__._cast(
            _4203.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
        )

    @property
    def mass_disc_power_flow(self: "CastSelf") -> "_4205.MassDiscPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4205

        return self.__parent__._cast(_4205.MassDiscPowerFlow)

    @property
    def measurement_component_power_flow(
        self: "CastSelf",
    ) -> "_4206.MeasurementComponentPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4206

        return self.__parent__._cast(_4206.MeasurementComponentPowerFlow)

    @property
    def oil_seal_power_flow(self: "CastSelf") -> "_4210.OilSealPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4210

        return self.__parent__._cast(_4210.OilSealPowerFlow)

    @property
    def part_to_part_shear_coupling_half_power_flow(
        self: "CastSelf",
    ) -> "_4213.PartToPartShearCouplingHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4213

        return self.__parent__._cast(_4213.PartToPartShearCouplingHalfPowerFlow)

    @property
    def planet_carrier_power_flow(self: "CastSelf") -> "_4217.PlanetCarrierPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4217

        return self.__parent__._cast(_4217.PlanetCarrierPowerFlow)

    @property
    def point_load_power_flow(self: "CastSelf") -> "_4218.PointLoadPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4218

        return self.__parent__._cast(_4218.PointLoadPowerFlow)

    @property
    def power_load_power_flow(self: "CastSelf") -> "_4221.PowerLoadPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4221

        return self.__parent__._cast(_4221.PowerLoadPowerFlow)

    @property
    def pulley_power_flow(self: "CastSelf") -> "_4222.PulleyPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4222

        return self.__parent__._cast(_4222.PulleyPowerFlow)

    @property
    def ring_pins_power_flow(self: "CastSelf") -> "_4223.RingPinsPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4223

        return self.__parent__._cast(_4223.RingPinsPowerFlow)

    @property
    def rolling_ring_power_flow(self: "CastSelf") -> "_4227.RollingRingPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4227

        return self.__parent__._cast(_4227.RollingRingPowerFlow)

    @property
    def shaft_hub_connection_power_flow(
        self: "CastSelf",
    ) -> "_4229.ShaftHubConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4229

        return self.__parent__._cast(_4229.ShaftHubConnectionPowerFlow)

    @property
    def spiral_bevel_gear_power_flow(
        self: "CastSelf",
    ) -> "_4234.SpiralBevelGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4234

        return self.__parent__._cast(_4234.SpiralBevelGearPowerFlow)

    @property
    def spring_damper_half_power_flow(
        self: "CastSelf",
    ) -> "_4237.SpringDamperHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4237

        return self.__parent__._cast(_4237.SpringDamperHalfPowerFlow)

    @property
    def straight_bevel_diff_gear_power_flow(
        self: "CastSelf",
    ) -> "_4240.StraightBevelDiffGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4240

        return self.__parent__._cast(_4240.StraightBevelDiffGearPowerFlow)

    @property
    def straight_bevel_gear_power_flow(
        self: "CastSelf",
    ) -> "_4243.StraightBevelGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4243

        return self.__parent__._cast(_4243.StraightBevelGearPowerFlow)

    @property
    def straight_bevel_planet_gear_power_flow(
        self: "CastSelf",
    ) -> "_4245.StraightBevelPlanetGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4245

        return self.__parent__._cast(_4245.StraightBevelPlanetGearPowerFlow)

    @property
    def straight_bevel_sun_gear_power_flow(
        self: "CastSelf",
    ) -> "_4246.StraightBevelSunGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4246

        return self.__parent__._cast(_4246.StraightBevelSunGearPowerFlow)

    @property
    def synchroniser_half_power_flow(
        self: "CastSelf",
    ) -> "_4247.SynchroniserHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4247

        return self.__parent__._cast(_4247.SynchroniserHalfPowerFlow)

    @property
    def synchroniser_part_power_flow(
        self: "CastSelf",
    ) -> "_4248.SynchroniserPartPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4248

        return self.__parent__._cast(_4248.SynchroniserPartPowerFlow)

    @property
    def synchroniser_sleeve_power_flow(
        self: "CastSelf",
    ) -> "_4250.SynchroniserSleevePowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4250

        return self.__parent__._cast(_4250.SynchroniserSleevePowerFlow)

    @property
    def torque_converter_pump_power_flow(
        self: "CastSelf",
    ) -> "_4254.TorqueConverterPumpPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4254

        return self.__parent__._cast(_4254.TorqueConverterPumpPowerFlow)

    @property
    def torque_converter_turbine_power_flow(
        self: "CastSelf",
    ) -> "_4255.TorqueConverterTurbinePowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4255

        return self.__parent__._cast(_4255.TorqueConverterTurbinePowerFlow)

    @property
    def unbalanced_mass_power_flow(self: "CastSelf") -> "_4256.UnbalancedMassPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4256

        return self.__parent__._cast(_4256.UnbalancedMassPowerFlow)

    @property
    def virtual_component_power_flow(
        self: "CastSelf",
    ) -> "_4257.VirtualComponentPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4257

        return self.__parent__._cast(_4257.VirtualComponentPowerFlow)

    @property
    def worm_gear_power_flow(self: "CastSelf") -> "_4259.WormGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4259

        return self.__parent__._cast(_4259.WormGearPowerFlow)

    @property
    def zerol_bevel_gear_power_flow(
        self: "CastSelf",
    ) -> "_4262.ZerolBevelGearPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4262

        return self.__parent__._cast(_4262.ZerolBevelGearPowerFlow)

    @property
    def mountable_component_power_flow(
        self: "CastSelf",
    ) -> "MountableComponentPowerFlow":
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
class MountableComponentPowerFlow(_4152.ComponentPowerFlow):
    """MountableComponentPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MOUNTABLE_COMPONENT_POWER_FLOW

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
    def cast_to(self: "Self") -> "_Cast_MountableComponentPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_MountableComponentPowerFlow
        """
        return _Cast_MountableComponentPowerFlow(self)
