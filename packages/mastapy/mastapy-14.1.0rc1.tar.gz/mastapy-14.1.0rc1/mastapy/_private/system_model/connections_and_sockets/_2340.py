"""CVTPulleySocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.connections_and_sockets import _2356

_CVT_PULLEY_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CVTPulleySocket"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets import _2342, _2362

    Self = TypeVar("Self", bound="CVTPulleySocket")
    CastSelf = TypeVar("CastSelf", bound="CVTPulleySocket._Cast_CVTPulleySocket")


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleySocket",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CVTPulleySocket:
    """Special nested class for casting CVTPulleySocket to subclasses."""

    __parent__: "CVTPulleySocket"

    @property
    def pulley_socket(self: "CastSelf") -> "_2356.PulleySocket":
        return self.__parent__._cast(_2356.PulleySocket)

    @property
    def cylindrical_socket(self: "CastSelf") -> "_2342.CylindricalSocket":
        from mastapy._private.system_model.connections_and_sockets import _2342

        return self.__parent__._cast(_2342.CylindricalSocket)

    @property
    def socket(self: "CastSelf") -> "_2362.Socket":
        from mastapy._private.system_model.connections_and_sockets import _2362

        return self.__parent__._cast(_2362.Socket)

    @property
    def cvt_pulley_socket(self: "CastSelf") -> "CVTPulleySocket":
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
class CVTPulleySocket(_2356.PulleySocket):
    """CVTPulleySocket

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CVT_PULLEY_SOCKET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CVTPulleySocket":
        """Cast to another type.

        Returns:
            _Cast_CVTPulleySocket
        """
        return _Cast_CVTPulleySocket(self)
