"""InnerShaftSocketBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.connections_and_sockets import _2360

_INNER_SHAFT_SOCKET_BASE = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "InnerShaftSocketBase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets import (
        _2342,
        _2345,
        _2362,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal import (
        _2399,
        _2402,
    )

    Self = TypeVar("Self", bound="InnerShaftSocketBase")
    CastSelf = TypeVar(
        "CastSelf", bound="InnerShaftSocketBase._Cast_InnerShaftSocketBase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("InnerShaftSocketBase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_InnerShaftSocketBase:
    """Special nested class for casting InnerShaftSocketBase to subclasses."""

    __parent__: "InnerShaftSocketBase"

    @property
    def shaft_socket(self: "CastSelf") -> "_2360.ShaftSocket":
        return self.__parent__._cast(_2360.ShaftSocket)

    @property
    def cylindrical_socket(self: "CastSelf") -> "_2342.CylindricalSocket":
        from mastapy._private.system_model.connections_and_sockets import _2342

        return self.__parent__._cast(_2342.CylindricalSocket)

    @property
    def socket(self: "CastSelf") -> "_2362.Socket":
        from mastapy._private.system_model.connections_and_sockets import _2362

        return self.__parent__._cast(_2362.Socket)

    @property
    def inner_shaft_socket(self: "CastSelf") -> "_2345.InnerShaftSocket":
        from mastapy._private.system_model.connections_and_sockets import _2345

        return self.__parent__._cast(_2345.InnerShaftSocket)

    @property
    def cycloidal_disc_axial_left_socket(
        self: "CastSelf",
    ) -> "_2399.CycloidalDiscAxialLeftSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2399,
        )

        return self.__parent__._cast(_2399.CycloidalDiscAxialLeftSocket)

    @property
    def cycloidal_disc_inner_socket(
        self: "CastSelf",
    ) -> "_2402.CycloidalDiscInnerSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2402,
        )

        return self.__parent__._cast(_2402.CycloidalDiscInnerSocket)

    @property
    def inner_shaft_socket_base(self: "CastSelf") -> "InnerShaftSocketBase":
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
class InnerShaftSocketBase(_2360.ShaftSocket):
    """InnerShaftSocketBase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _INNER_SHAFT_SOCKET_BASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_InnerShaftSocketBase":
        """Cast to another type.

        Returns:
            _Cast_InnerShaftSocketBase
        """
        return _Cast_InnerShaftSocketBase(self)
