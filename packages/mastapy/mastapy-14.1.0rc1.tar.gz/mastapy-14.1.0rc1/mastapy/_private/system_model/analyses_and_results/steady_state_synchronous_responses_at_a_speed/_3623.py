"""ConicalGearMeshSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3649,
)

_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3595,
        _3602,
        _3607,
        _3626,
        _3653,
        _3656,
        _3657,
        _3660,
        _3663,
        _3692,
        _3699,
        _3702,
        _3720,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import _2373

    Self = TypeVar(
        "Self", bound="ConicalGearMeshSteadyStateSynchronousResponseAtASpeed"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_ConicalGearMeshSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearMeshSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting ConicalGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: "ConicalGearMeshSteadyStateSynchronousResponseAtASpeed"

    @property
    def gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3649.GearMeshSteadyStateSynchronousResponseAtASpeed":
        return self.__parent__._cast(
            _3649.GearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3656.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3656,
        )

        return self.__parent__._cast(
            _3656.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3626.ConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3626,
        )

        return self.__parent__._cast(
            _3626.ConnectionSteadyStateSynchronousResponseAtASpeed
        )

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
    def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3595.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3595,
        )

        return self.__parent__._cast(
            _3595.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3602.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3602,
        )

        return self.__parent__._cast(
            _3602.BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3607.BevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3607,
        )

        return self.__parent__._cast(
            _3607.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3653.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3653,
        )

        return self.__parent__._cast(
            _3653.HypoidGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3657.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3657,
        )

        return self.__parent__._cast(
            _3657.KlingelnbergCycloPalloidConicalGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3660.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3660,
        )

        return self.__parent__._cast(
            _3660.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3663.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3663,
        )

        return self.__parent__._cast(
            _3663.KlingelnbergCycloPalloidSpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3692.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3692,
        )

        return self.__parent__._cast(
            _3692.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3699.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3699,
        )

        return self.__parent__._cast(
            _3699.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3702.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3702,
        )

        return self.__parent__._cast(
            _3702.StraightBevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def zerol_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3720.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3720,
        )

        return self.__parent__._cast(
            _3720.ZerolBevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
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
class ConicalGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3649.GearMeshSteadyStateSynchronousResponseAtASpeed
):
    """ConicalGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2373.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: "Self",
    ) -> "List[ConicalGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Planetaries")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_ConicalGearMeshSteadyStateSynchronousResponseAtASpeed(self)
