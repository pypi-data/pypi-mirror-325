"""CycloidalDiscAxialLeftSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.connections_and_sockets import _2346

_CYCLOIDAL_DISC_AXIAL_LEFT_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Cycloidal",
    "CycloidalDiscAxialLeftSocket",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets import (
        _2342,
        _2360,
        _2362,
    )

    Self = TypeVar("Self", bound="CycloidalDiscAxialLeftSocket")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CycloidalDiscAxialLeftSocket._Cast_CycloidalDiscAxialLeftSocket",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscAxialLeftSocket",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CycloidalDiscAxialLeftSocket:
    """Special nested class for casting CycloidalDiscAxialLeftSocket to subclasses."""

    __parent__: "CycloidalDiscAxialLeftSocket"

    @property
    def inner_shaft_socket_base(self: "CastSelf") -> "_2346.InnerShaftSocketBase":
        return self.__parent__._cast(_2346.InnerShaftSocketBase)

    @property
    def shaft_socket(self: "CastSelf") -> "_2360.ShaftSocket":
        from mastapy._private.system_model.connections_and_sockets import _2360

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
    def cycloidal_disc_axial_left_socket(
        self: "CastSelf",
    ) -> "CycloidalDiscAxialLeftSocket":
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
class CycloidalDiscAxialLeftSocket(_2346.InnerShaftSocketBase):
    """CycloidalDiscAxialLeftSocket

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYCLOIDAL_DISC_AXIAL_LEFT_SOCKET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CycloidalDiscAxialLeftSocket":
        """Cast to another type.

        Returns:
            _Cast_CycloidalDiscAxialLeftSocket
        """
        return _Cast_CycloidalDiscAxialLeftSocket(self)
