"""ComponentSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3144,
)

_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ComponentSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3063,
        _3064,
        _3068,
        _3070,
        _3075,
        _3076,
        _3077,
        _3080,
        _3082,
        _3084,
        _3089,
        _3093,
        _3096,
        _3098,
        _3100,
        _3103,
        _3108,
        _3111,
        _3112,
        _3113,
        _3115,
        _3118,
        _3119,
        _3123,
        _3124,
        _3127,
        _3131,
        _3134,
        _3137,
        _3138,
        _3139,
        _3141,
        _3142,
        _3143,
        _3146,
        _3150,
        _3151,
        _3152,
        _3153,
        _3154,
        _3158,
        _3160,
        _3161,
        _3166,
        _3168,
        _3175,
        _3178,
        _3179,
        _3180,
        _3181,
        _3182,
        _3183,
        _3186,
        _3188,
        _3189,
        _3190,
        _3193,
        _3196,
    )
    from mastapy._private.system_model.part_model import _2511

    Self = TypeVar("Self", bound="ComponentSteadyStateSynchronousResponse")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ComponentSteadyStateSynchronousResponse._Cast_ComponentSteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentSteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ComponentSteadyStateSynchronousResponse:
    """Special nested class for casting ComponentSteadyStateSynchronousResponse to subclasses."""

    __parent__: "ComponentSteadyStateSynchronousResponse"

    @property
    def part_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3144.PartSteadyStateSynchronousResponse":
        return self.__parent__._cast(_3144.PartSteadyStateSynchronousResponse)

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
    def abstract_shaft_or_housing_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3063.AbstractShaftOrHousingSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3063,
        )

        return self.__parent__._cast(
            _3063.AbstractShaftOrHousingSteadyStateSynchronousResponse
        )

    @property
    def abstract_shaft_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3064.AbstractShaftSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3064,
        )

        return self.__parent__._cast(_3064.AbstractShaftSteadyStateSynchronousResponse)

    @property
    def agma_gleason_conical_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3068.AGMAGleasonConicalGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3068,
        )

        return self.__parent__._cast(
            _3068.AGMAGleasonConicalGearSteadyStateSynchronousResponse
        )

    @property
    def bearing_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3070.BearingSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3070,
        )

        return self.__parent__._cast(_3070.BearingSteadyStateSynchronousResponse)

    @property
    def bevel_differential_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3075.BevelDifferentialGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3075,
        )

        return self.__parent__._cast(
            _3075.BevelDifferentialGearSteadyStateSynchronousResponse
        )

    @property
    def bevel_differential_planet_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3076.BevelDifferentialPlanetGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3076,
        )

        return self.__parent__._cast(
            _3076.BevelDifferentialPlanetGearSteadyStateSynchronousResponse
        )

    @property
    def bevel_differential_sun_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3077.BevelDifferentialSunGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3077,
        )

        return self.__parent__._cast(
            _3077.BevelDifferentialSunGearSteadyStateSynchronousResponse
        )

    @property
    def bevel_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3080.BevelGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3080,
        )

        return self.__parent__._cast(_3080.BevelGearSteadyStateSynchronousResponse)

    @property
    def bolt_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3082.BoltSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3082,
        )

        return self.__parent__._cast(_3082.BoltSteadyStateSynchronousResponse)

    @property
    def clutch_half_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3084.ClutchHalfSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3084,
        )

        return self.__parent__._cast(_3084.ClutchHalfSteadyStateSynchronousResponse)

    @property
    def concept_coupling_half_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3089.ConceptCouplingHalfSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3089,
        )

        return self.__parent__._cast(
            _3089.ConceptCouplingHalfSteadyStateSynchronousResponse
        )

    @property
    def concept_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3093.ConceptGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3093,
        )

        return self.__parent__._cast(_3093.ConceptGearSteadyStateSynchronousResponse)

    @property
    def conical_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3096.ConicalGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3096,
        )

        return self.__parent__._cast(_3096.ConicalGearSteadyStateSynchronousResponse)

    @property
    def connector_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3098.ConnectorSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3098,
        )

        return self.__parent__._cast(_3098.ConnectorSteadyStateSynchronousResponse)

    @property
    def coupling_half_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3100.CouplingHalfSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3100,
        )

        return self.__parent__._cast(_3100.CouplingHalfSteadyStateSynchronousResponse)

    @property
    def cvt_pulley_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3103.CVTPulleySteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3103,
        )

        return self.__parent__._cast(_3103.CVTPulleySteadyStateSynchronousResponse)

    @property
    def cycloidal_disc_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3108.CycloidalDiscSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3108,
        )

        return self.__parent__._cast(_3108.CycloidalDiscSteadyStateSynchronousResponse)

    @property
    def cylindrical_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3111.CylindricalGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3111,
        )

        return self.__parent__._cast(
            _3111.CylindricalGearSteadyStateSynchronousResponse
        )

    @property
    def cylindrical_planet_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3112.CylindricalPlanetGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3112,
        )

        return self.__parent__._cast(
            _3112.CylindricalPlanetGearSteadyStateSynchronousResponse
        )

    @property
    def datum_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3113.DatumSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3113,
        )

        return self.__parent__._cast(_3113.DatumSteadyStateSynchronousResponse)

    @property
    def external_cad_model_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3115.ExternalCADModelSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3115,
        )

        return self.__parent__._cast(
            _3115.ExternalCADModelSteadyStateSynchronousResponse
        )

    @property
    def face_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3118.FaceGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3118,
        )

        return self.__parent__._cast(_3118.FaceGearSteadyStateSynchronousResponse)

    @property
    def fe_part_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3119.FEPartSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3119,
        )

        return self.__parent__._cast(_3119.FEPartSteadyStateSynchronousResponse)

    @property
    def gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3123.GearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3123,
        )

        return self.__parent__._cast(_3123.GearSteadyStateSynchronousResponse)

    @property
    def guide_dxf_model_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3124.GuideDxfModelSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3124,
        )

        return self.__parent__._cast(_3124.GuideDxfModelSteadyStateSynchronousResponse)

    @property
    def hypoid_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3127.HypoidGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3127,
        )

        return self.__parent__._cast(_3127.HypoidGearSteadyStateSynchronousResponse)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3131.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3131,
        )

        return self.__parent__._cast(
            _3131.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3134.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3134,
        )

        return self.__parent__._cast(
            _3134.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3137.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3137,
        )

        return self.__parent__._cast(
            _3137.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse
        )

    @property
    def mass_disc_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3138.MassDiscSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3138,
        )

        return self.__parent__._cast(_3138.MassDiscSteadyStateSynchronousResponse)

    @property
    def measurement_component_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3139.MeasurementComponentSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3139,
        )

        return self.__parent__._cast(
            _3139.MeasurementComponentSteadyStateSynchronousResponse
        )

    @property
    def microphone_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3141.MicrophoneSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3141,
        )

        return self.__parent__._cast(_3141.MicrophoneSteadyStateSynchronousResponse)

    @property
    def mountable_component_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3142.MountableComponentSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3142,
        )

        return self.__parent__._cast(
            _3142.MountableComponentSteadyStateSynchronousResponse
        )

    @property
    def oil_seal_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3143.OilSealSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3143,
        )

        return self.__parent__._cast(_3143.OilSealSteadyStateSynchronousResponse)

    @property
    def part_to_part_shear_coupling_half_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3146.PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3146,
        )

        return self.__parent__._cast(
            _3146.PartToPartShearCouplingHalfSteadyStateSynchronousResponse
        )

    @property
    def planet_carrier_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3150.PlanetCarrierSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3150,
        )

        return self.__parent__._cast(_3150.PlanetCarrierSteadyStateSynchronousResponse)

    @property
    def point_load_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3151.PointLoadSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3151,
        )

        return self.__parent__._cast(_3151.PointLoadSteadyStateSynchronousResponse)

    @property
    def power_load_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3152.PowerLoadSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3152,
        )

        return self.__parent__._cast(_3152.PowerLoadSteadyStateSynchronousResponse)

    @property
    def pulley_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3153.PulleySteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3153,
        )

        return self.__parent__._cast(_3153.PulleySteadyStateSynchronousResponse)

    @property
    def ring_pins_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3154.RingPinsSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3154,
        )

        return self.__parent__._cast(_3154.RingPinsSteadyStateSynchronousResponse)

    @property
    def rolling_ring_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3158.RollingRingSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3158,
        )

        return self.__parent__._cast(_3158.RollingRingSteadyStateSynchronousResponse)

    @property
    def shaft_hub_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3160.ShaftHubConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3160,
        )

        return self.__parent__._cast(
            _3160.ShaftHubConnectionSteadyStateSynchronousResponse
        )

    @property
    def shaft_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3161.ShaftSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3161,
        )

        return self.__parent__._cast(_3161.ShaftSteadyStateSynchronousResponse)

    @property
    def spiral_bevel_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3166.SpiralBevelGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3166,
        )

        return self.__parent__._cast(
            _3166.SpiralBevelGearSteadyStateSynchronousResponse
        )

    @property
    def spring_damper_half_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3168.SpringDamperHalfSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3168,
        )

        return self.__parent__._cast(
            _3168.SpringDamperHalfSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_diff_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3175.StraightBevelDiffGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3175,
        )

        return self.__parent__._cast(
            _3175.StraightBevelDiffGearSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3178.StraightBevelGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3178,
        )

        return self.__parent__._cast(
            _3178.StraightBevelGearSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_planet_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3179.StraightBevelPlanetGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3179,
        )

        return self.__parent__._cast(
            _3179.StraightBevelPlanetGearSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_sun_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3180.StraightBevelSunGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3180,
        )

        return self.__parent__._cast(
            _3180.StraightBevelSunGearSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_half_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3181.SynchroniserHalfSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3181,
        )

        return self.__parent__._cast(
            _3181.SynchroniserHalfSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_part_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3182.SynchroniserPartSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3182,
        )

        return self.__parent__._cast(
            _3182.SynchroniserPartSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_sleeve_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3183.SynchroniserSleeveSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3183,
        )

        return self.__parent__._cast(
            _3183.SynchroniserSleeveSteadyStateSynchronousResponse
        )

    @property
    def torque_converter_pump_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3186.TorqueConverterPumpSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3186,
        )

        return self.__parent__._cast(
            _3186.TorqueConverterPumpSteadyStateSynchronousResponse
        )

    @property
    def torque_converter_turbine_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3188.TorqueConverterTurbineSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3188,
        )

        return self.__parent__._cast(
            _3188.TorqueConverterTurbineSteadyStateSynchronousResponse
        )

    @property
    def unbalanced_mass_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3189.UnbalancedMassSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3189,
        )

        return self.__parent__._cast(_3189.UnbalancedMassSteadyStateSynchronousResponse)

    @property
    def virtual_component_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3190.VirtualComponentSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3190,
        )

        return self.__parent__._cast(
            _3190.VirtualComponentSteadyStateSynchronousResponse
        )

    @property
    def worm_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3193.WormGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3193,
        )

        return self.__parent__._cast(_3193.WormGearSteadyStateSynchronousResponse)

    @property
    def zerol_bevel_gear_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3196.ZerolBevelGearSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3196,
        )

        return self.__parent__._cast(_3196.ZerolBevelGearSteadyStateSynchronousResponse)

    @property
    def component_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "ComponentSteadyStateSynchronousResponse":
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
class ComponentSteadyStateSynchronousResponse(_3144.PartSteadyStateSynchronousResponse):
    """ComponentSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2511.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ComponentSteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_ComponentSteadyStateSynchronousResponse
        """
        return _Cast_ComponentSteadyStateSynchronousResponse(self)
