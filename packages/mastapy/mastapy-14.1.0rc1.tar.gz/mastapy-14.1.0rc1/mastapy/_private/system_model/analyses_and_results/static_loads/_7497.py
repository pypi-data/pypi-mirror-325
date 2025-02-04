"""AbstractShaftToMountableComponentConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.static_loads import _7537

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftToMountableComponentConnectionLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7524,
        _7546,
        _7548,
        _7622,
        _7641,
    )
    from mastapy._private.system_model.connections_and_sockets import _2331

    Self = TypeVar("Self", bound="AbstractShaftToMountableComponentConnectionLoadCase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftToMountableComponentConnectionLoadCase:
    """Special nested class for casting AbstractShaftToMountableComponentConnectionLoadCase to subclasses."""

    __parent__: "AbstractShaftToMountableComponentConnectionLoadCase"

    @property
    def connection_load_case(self: "CastSelf") -> "_7537.ConnectionLoadCase":
        return self.__parent__._cast(_7537.ConnectionLoadCase)

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
    def coaxial_connection_load_case(
        self: "CastSelf",
    ) -> "_7524.CoaxialConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7524,
        )

        return self.__parent__._cast(_7524.CoaxialConnectionLoadCase)

    @property
    def cycloidal_disc_central_bearing_connection_load_case(
        self: "CastSelf",
    ) -> "_7546.CycloidalDiscCentralBearingConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7546,
        )

        return self.__parent__._cast(
            _7546.CycloidalDiscCentralBearingConnectionLoadCase
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_load_case(
        self: "CastSelf",
    ) -> "_7548.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7548,
        )

        return self.__parent__._cast(
            _7548.CycloidalDiscPlanetaryBearingConnectionLoadCase
        )

    @property
    def planetary_connection_load_case(
        self: "CastSelf",
    ) -> "_7622.PlanetaryConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7622,
        )

        return self.__parent__._cast(_7622.PlanetaryConnectionLoadCase)

    @property
    def shaft_to_mountable_component_connection_load_case(
        self: "CastSelf",
    ) -> "_7641.ShaftToMountableComponentConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7641,
        )

        return self.__parent__._cast(_7641.ShaftToMountableComponentConnectionLoadCase)

    @property
    def abstract_shaft_to_mountable_component_connection_load_case(
        self: "CastSelf",
    ) -> "AbstractShaftToMountableComponentConnectionLoadCase":
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
class AbstractShaftToMountableComponentConnectionLoadCase(_7537.ConnectionLoadCase):
    """AbstractShaftToMountableComponentConnectionLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(
        self: "Self",
    ) -> "_2331.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

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
    ) -> "_Cast_AbstractShaftToMountableComponentConnectionLoadCase":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftToMountableComponentConnectionLoadCase
        """
        return _Cast_AbstractShaftToMountableComponentConnectionLoadCase(self)
