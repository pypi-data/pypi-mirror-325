"""CycloidalDiscCentralBearingConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.connections_and_sockets import _2335

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscCentralBearingConnection",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.connections_and_sockets import (
        _2331,
        _2338,
        _2361,
    )

    Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CycloidalDiscCentralBearingConnection._Cast_CycloidalDiscCentralBearingConnection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CycloidalDiscCentralBearingConnection:
    """Special nested class for casting CycloidalDiscCentralBearingConnection to subclasses."""

    __parent__: "CycloidalDiscCentralBearingConnection"

    @property
    def coaxial_connection(self: "CastSelf") -> "_2335.CoaxialConnection":
        return self.__parent__._cast(_2335.CoaxialConnection)

    @property
    def shaft_to_mountable_component_connection(
        self: "CastSelf",
    ) -> "_2361.ShaftToMountableComponentConnection":
        from mastapy._private.system_model.connections_and_sockets import _2361

        return self.__parent__._cast(_2361.ShaftToMountableComponentConnection)

    @property
    def abstract_shaft_to_mountable_component_connection(
        self: "CastSelf",
    ) -> "_2331.AbstractShaftToMountableComponentConnection":
        from mastapy._private.system_model.connections_and_sockets import _2331

        return self.__parent__._cast(_2331.AbstractShaftToMountableComponentConnection)

    @property
    def connection(self: "CastSelf") -> "_2338.Connection":
        from mastapy._private.system_model.connections_and_sockets import _2338

        return self.__parent__._cast(_2338.Connection)

    @property
    def design_entity(self: "CastSelf") -> "_2269.DesignEntity":
        from mastapy._private.system_model import _2269

        return self.__parent__._cast(_2269.DesignEntity)

    @property
    def cycloidal_disc_central_bearing_connection(
        self: "CastSelf",
    ) -> "CycloidalDiscCentralBearingConnection":
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
class CycloidalDiscCentralBearingConnection(_2335.CoaxialConnection):
    """CycloidalDiscCentralBearingConnection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CycloidalDiscCentralBearingConnection":
        """Cast to another type.

        Returns:
            _Cast_CycloidalDiscCentralBearingConnection
        """
        return _Cast_CycloidalDiscCentralBearingConnection(self)
