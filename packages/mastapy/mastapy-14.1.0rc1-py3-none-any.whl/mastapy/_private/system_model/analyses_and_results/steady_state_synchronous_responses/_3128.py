"""InterMountableComponentConnectionSteadyStateSynchronousResponse"""

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
    _3097,
)

_INTER_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "InterMountableComponentConnectionSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3066,
        _3071,
        _3073,
        _3078,
        _3083,
        _3088,
        _3091,
        _3094,
        _3099,
        _3102,
        _3109,
        _3116,
        _3121,
        _3125,
        _3129,
        _3132,
        _3135,
        _3145,
        _3155,
        _3157,
        _3164,
        _3167,
        _3173,
        _3176,
        _3185,
        _3191,
        _3194,
    )
    from mastapy._private.system_model.connections_and_sockets import _2347

    Self = TypeVar(
        "Self", bound="InterMountableComponentConnectionSteadyStateSynchronousResponse"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="InterMountableComponentConnectionSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionSteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse:
    """Special nested class for casting InterMountableComponentConnectionSteadyStateSynchronousResponse to subclasses."""

    __parent__: "InterMountableComponentConnectionSteadyStateSynchronousResponse"

    @property
    def connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3097.ConnectionSteadyStateSynchronousResponse":
        return self.__parent__._cast(_3097.ConnectionSteadyStateSynchronousResponse)

    @property
    def connection_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7702.ConnectionStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7702,
        )

        return self.__parent__._cast(_7702.ConnectionStaticLoadAnalysisCase)

    @property
    def connection_analysis_case(self: "CastSelf") -> "_7699.ConnectionAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7699,
        )

        return self.__parent__._cast(_7699.ConnectionAnalysisCase)

    @property
    def connection_analysis(self: "CastSelf") -> "_2724.ConnectionAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2724

        return self.__parent__._cast(_2724.ConnectionAnalysis)

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
    def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3066.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3066,
        )

        return self.__parent__._cast(
            _3066.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
        )

    @property
    def belt_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3071.BeltConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3071,
        )

        return self.__parent__._cast(_3071.BeltConnectionSteadyStateSynchronousResponse)

    @property
    def bevel_differential_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3073.BevelDifferentialGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3073,
        )

        return self.__parent__._cast(
            _3073.BevelDifferentialGearMeshSteadyStateSynchronousResponse
        )

    @property
    def bevel_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3078.BevelGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3078,
        )

        return self.__parent__._cast(_3078.BevelGearMeshSteadyStateSynchronousResponse)

    @property
    def clutch_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3083.ClutchConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3083,
        )

        return self.__parent__._cast(
            _3083.ClutchConnectionSteadyStateSynchronousResponse
        )

    @property
    def concept_coupling_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3088.ConceptCouplingConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3088,
        )

        return self.__parent__._cast(
            _3088.ConceptCouplingConnectionSteadyStateSynchronousResponse
        )

    @property
    def concept_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3091.ConceptGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3091,
        )

        return self.__parent__._cast(
            _3091.ConceptGearMeshSteadyStateSynchronousResponse
        )

    @property
    def conical_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3094.ConicalGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3094,
        )

        return self.__parent__._cast(
            _3094.ConicalGearMeshSteadyStateSynchronousResponse
        )

    @property
    def coupling_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3099.CouplingConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3099,
        )

        return self.__parent__._cast(
            _3099.CouplingConnectionSteadyStateSynchronousResponse
        )

    @property
    def cvt_belt_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3102.CVTBeltConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3102,
        )

        return self.__parent__._cast(
            _3102.CVTBeltConnectionSteadyStateSynchronousResponse
        )

    @property
    def cylindrical_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3109.CylindricalGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3109,
        )

        return self.__parent__._cast(
            _3109.CylindricalGearMeshSteadyStateSynchronousResponse
        )

    @property
    def face_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3116.FaceGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3116,
        )

        return self.__parent__._cast(_3116.FaceGearMeshSteadyStateSynchronousResponse)

    @property
    def gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3121.GearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3121,
        )

        return self.__parent__._cast(_3121.GearMeshSteadyStateSynchronousResponse)

    @property
    def hypoid_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3125.HypoidGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3125,
        )

        return self.__parent__._cast(_3125.HypoidGearMeshSteadyStateSynchronousResponse)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3129.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3129,
        )

        return self.__parent__._cast(
            _3129.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3132.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3132,
        )

        return self.__parent__._cast(
            _3132.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3135.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3135,
        )

        return self.__parent__._cast(
            _3135.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponse
        )

    @property
    def part_to_part_shear_coupling_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3145.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3145,
        )

        return self.__parent__._cast(
            _3145.PartToPartShearCouplingConnectionSteadyStateSynchronousResponse
        )

    @property
    def ring_pins_to_disc_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3155.RingPinsToDiscConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3155,
        )

        return self.__parent__._cast(
            _3155.RingPinsToDiscConnectionSteadyStateSynchronousResponse
        )

    @property
    def rolling_ring_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3157.RollingRingConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3157,
        )

        return self.__parent__._cast(
            _3157.RollingRingConnectionSteadyStateSynchronousResponse
        )

    @property
    def spiral_bevel_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3164.SpiralBevelGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3164,
        )

        return self.__parent__._cast(
            _3164.SpiralBevelGearMeshSteadyStateSynchronousResponse
        )

    @property
    def spring_damper_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3167.SpringDamperConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3167,
        )

        return self.__parent__._cast(
            _3167.SpringDamperConnectionSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_diff_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3173.StraightBevelDiffGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3173,
        )

        return self.__parent__._cast(
            _3173.StraightBevelDiffGearMeshSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3176.StraightBevelGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3176,
        )

        return self.__parent__._cast(
            _3176.StraightBevelGearMeshSteadyStateSynchronousResponse
        )

    @property
    def torque_converter_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3185.TorqueConverterConnectionSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3185,
        )

        return self.__parent__._cast(
            _3185.TorqueConverterConnectionSteadyStateSynchronousResponse
        )

    @property
    def worm_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3191.WormGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3191,
        )

        return self.__parent__._cast(_3191.WormGearMeshSteadyStateSynchronousResponse)

    @property
    def zerol_bevel_gear_mesh_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3194.ZerolBevelGearMeshSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3194,
        )

        return self.__parent__._cast(
            _3194.ZerolBevelGearMeshSteadyStateSynchronousResponse
        )

    @property
    def inter_mountable_component_connection_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "InterMountableComponentConnectionSteadyStateSynchronousResponse":
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
class InterMountableComponentConnectionSteadyStateSynchronousResponse(
    _3097.ConnectionSteadyStateSynchronousResponse
):
    """InterMountableComponentConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _INTER_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2347.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse
        """
        return _Cast_InterMountableComponentConnectionSteadyStateSynchronousResponse(
            self
        )
