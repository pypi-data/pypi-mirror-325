"""SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3607,
)

_SPIRAL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads import _7644
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3595,
        _3623,
        _3626,
        _3649,
        _3656,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import _2389

    Self = TypeVar(
        "Self", bound="SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"

    @property
    def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3607.BevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        return self.__parent__._cast(
            _3607.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
        )

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
    def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3623.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3623,
        )

        return self.__parent__._cast(
            _3623.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3649.GearMeshSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3649,
        )

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
    def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
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
class SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3607.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
):
    """SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _SPIRAL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2389.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: "Self") -> "_7644.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionLoadCase")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed(self)
