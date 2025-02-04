"""CycloidalDiscCentralBearingConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.power_flows import _4151

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CycloidalDiscCentralBearingConnectionPowerFlow",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import (
        _4130,
        _4162,
        _4231,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal import _2401

    Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionPowerFlow")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CycloidalDiscCentralBearingConnectionPowerFlow._Cast_CycloidalDiscCentralBearingConnectionPowerFlow",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CycloidalDiscCentralBearingConnectionPowerFlow:
    """Special nested class for casting CycloidalDiscCentralBearingConnectionPowerFlow to subclasses."""

    __parent__: "CycloidalDiscCentralBearingConnectionPowerFlow"

    @property
    def coaxial_connection_power_flow(
        self: "CastSelf",
    ) -> "_4151.CoaxialConnectionPowerFlow":
        return self.__parent__._cast(_4151.CoaxialConnectionPowerFlow)

    @property
    def shaft_to_mountable_component_connection_power_flow(
        self: "CastSelf",
    ) -> "_4231.ShaftToMountableComponentConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4231

        return self.__parent__._cast(_4231.ShaftToMountableComponentConnectionPowerFlow)

    @property
    def abstract_shaft_to_mountable_component_connection_power_flow(
        self: "CastSelf",
    ) -> "_4130.AbstractShaftToMountableComponentConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4130

        return self.__parent__._cast(
            _4130.AbstractShaftToMountableComponentConnectionPowerFlow
        )

    @property
    def connection_power_flow(self: "CastSelf") -> "_4162.ConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4162

        return self.__parent__._cast(_4162.ConnectionPowerFlow)

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
    def cycloidal_disc_central_bearing_connection_power_flow(
        self: "CastSelf",
    ) -> "CycloidalDiscCentralBearingConnectionPowerFlow":
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
class CycloidalDiscCentralBearingConnectionPowerFlow(_4151.CoaxialConnectionPowerFlow):
    """CycloidalDiscCentralBearingConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_POWER_FLOW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(
        self: "Self",
    ) -> "_2401.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_CycloidalDiscCentralBearingConnectionPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_CycloidalDiscCentralBearingConnectionPowerFlow
        """
        return _Cast_CycloidalDiscCentralBearingConnectionPowerFlow(self)
