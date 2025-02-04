"""ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"""

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
    _3594,
)

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3615,
        _3626,
        _3635,
        _3676,
    )
    from mastapy._private.system_model.connections_and_sockets import _2361

    Self = TypeVar(
        "Self",
        bound="ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed._Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: (
        "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed"
    )

    @property
    def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3594.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
        return self.__parent__._cast(
            _3594.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
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
    def coaxial_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3615.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3615,
        )

        return self.__parent__._cast(
            _3615.CoaxialConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_disc_central_bearing_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3635.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3635,
        )

        return self.__parent__._cast(
            _3635.CycloidalDiscCentralBearingConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def planetary_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3676.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3676,
        )

        return self.__parent__._cast(
            _3676.PlanetaryConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_to_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
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
class ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed(
    _3594.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
):
    """ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2361.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

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
    ) -> "_Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_ShaftToMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed(
            self
        )
