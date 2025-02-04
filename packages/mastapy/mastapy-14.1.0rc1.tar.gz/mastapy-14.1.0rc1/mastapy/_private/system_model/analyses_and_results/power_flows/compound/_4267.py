"""AbstractShaftToMountableComponentConnectionCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
    _4299,
)

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
        "AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
    )
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7700,
        _7704,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import _4130
    from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
        _4288,
        _4308,
        _4310,
        _4349,
        _4363,
    )

    Self = TypeVar(
        "Self", bound="AbstractShaftToMountableComponentConnectionCompoundPowerFlow"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftToMountableComponentConnectionCompoundPowerFlow._Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionCompoundPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow:
    """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundPowerFlow to subclasses."""

    __parent__: "AbstractShaftToMountableComponentConnectionCompoundPowerFlow"

    @property
    def connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4299.ConnectionCompoundPowerFlow":
        return self.__parent__._cast(_4299.ConnectionCompoundPowerFlow)

    @property
    def connection_compound_analysis(
        self: "CastSelf",
    ) -> "_7700.ConnectionCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7700,
        )

        return self.__parent__._cast(_7700.ConnectionCompoundAnalysis)

    @property
    def design_entity_compound_analysis(
        self: "CastSelf",
    ) -> "_7704.DesignEntityCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7704,
        )

        return self.__parent__._cast(_7704.DesignEntityCompoundAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2726.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2726

        return self.__parent__._cast(_2726.DesignEntityAnalysis)

    @property
    def coaxial_connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4288.CoaxialConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4288,
        )

        return self.__parent__._cast(_4288.CoaxialConnectionCompoundPowerFlow)

    @property
    def cycloidal_disc_central_bearing_connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4308.CycloidalDiscCentralBearingConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4308,
        )

        return self.__parent__._cast(
            _4308.CycloidalDiscCentralBearingConnectionCompoundPowerFlow
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4310.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4310,
        )

        return self.__parent__._cast(
            _4310.CycloidalDiscPlanetaryBearingConnectionCompoundPowerFlow
        )

    @property
    def planetary_connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4349.PlanetaryConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4349,
        )

        return self.__parent__._cast(_4349.PlanetaryConnectionCompoundPowerFlow)

    @property
    def shaft_to_mountable_component_connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4363.ShaftToMountableComponentConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4363,
        )

        return self.__parent__._cast(
            _4363.ShaftToMountableComponentConnectionCompoundPowerFlow
        )

    @property
    def abstract_shaft_to_mountable_component_connection_compound_power_flow(
        self: "CastSelf",
    ) -> "AbstractShaftToMountableComponentConnectionCompoundPowerFlow":
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
class AbstractShaftToMountableComponentConnectionCompoundPowerFlow(
    _4299.ConnectionCompoundPowerFlow
):
    """AbstractShaftToMountableComponentConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_POWER_FLOW
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_4130.AbstractShaftToMountableComponentConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractShaftToMountableComponentConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_4130.AbstractShaftToMountableComponentConnectionPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AbstractShaftToMountableComponentConnectionPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow
        """
        return _Cast_AbstractShaftToMountableComponentConnectionCompoundPowerFlow(self)
