"""StraightBevelGearTeethSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.connections_and_sockets.gears import _2370

_STRAIGHT_BEVEL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "StraightBevelGearTeethSocket",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets import _2362
    from mastapy._private.system_model.connections_and_sockets.gears import (
        _2366,
        _2374,
        _2380,
    )

    Self = TypeVar("Self", bound="StraightBevelGearTeethSocket")
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelGearTeethSocket._Cast_StraightBevelGearTeethSocket",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearTeethSocket",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelGearTeethSocket:
    """Special nested class for casting StraightBevelGearTeethSocket to subclasses."""

    __parent__: "StraightBevelGearTeethSocket"

    @property
    def bevel_gear_teeth_socket(self: "CastSelf") -> "_2370.BevelGearTeethSocket":
        return self.__parent__._cast(_2370.BevelGearTeethSocket)

    @property
    def agma_gleason_conical_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2366.AGMAGleasonConicalGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2366

        return self.__parent__._cast(_2366.AGMAGleasonConicalGearTeethSocket)

    @property
    def conical_gear_teeth_socket(self: "CastSelf") -> "_2374.ConicalGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2374

        return self.__parent__._cast(_2374.ConicalGearTeethSocket)

    @property
    def gear_teeth_socket(self: "CastSelf") -> "_2380.GearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2380

        return self.__parent__._cast(_2380.GearTeethSocket)

    @property
    def socket(self: "CastSelf") -> "_2362.Socket":
        from mastapy._private.system_model.connections_and_sockets import _2362

        return self.__parent__._cast(_2362.Socket)

    @property
    def straight_bevel_gear_teeth_socket(
        self: "CastSelf",
    ) -> "StraightBevelGearTeethSocket":
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
class StraightBevelGearTeethSocket(_2370.BevelGearTeethSocket):
    """StraightBevelGearTeethSocket

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STRAIGHT_BEVEL_GEAR_TEETH_SOCKET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_StraightBevelGearTeethSocket":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelGearTeethSocket
        """
        return _Cast_StraightBevelGearTeethSocket(self)
