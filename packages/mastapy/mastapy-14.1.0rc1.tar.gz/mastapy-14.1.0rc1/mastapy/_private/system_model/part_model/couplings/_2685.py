"""SynchroniserPart"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.part_model.couplings import _2658

_SYNCHRONISER_PART = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SynchroniserPart"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.part_model import _2511, _2533, _2537
    from mastapy._private.system_model.part_model.couplings import _2684, _2686

    Self = TypeVar("Self", bound="SynchroniserPart")
    CastSelf = TypeVar("CastSelf", bound="SynchroniserPart._Cast_SynchroniserPart")


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPart",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SynchroniserPart:
    """Special nested class for casting SynchroniserPart to subclasses."""

    __parent__: "SynchroniserPart"

    @property
    def coupling_half(self: "CastSelf") -> "_2658.CouplingHalf":
        return self.__parent__._cast(_2658.CouplingHalf)

    @property
    def mountable_component(self: "CastSelf") -> "_2533.MountableComponent":
        from mastapy._private.system_model.part_model import _2533

        return self.__parent__._cast(_2533.MountableComponent)

    @property
    def component(self: "CastSelf") -> "_2511.Component":
        from mastapy._private.system_model.part_model import _2511

        return self.__parent__._cast(_2511.Component)

    @property
    def part(self: "CastSelf") -> "_2537.Part":
        from mastapy._private.system_model.part_model import _2537

        return self.__parent__._cast(_2537.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2269.DesignEntity":
        from mastapy._private.system_model import _2269

        return self.__parent__._cast(_2269.DesignEntity)

    @property
    def synchroniser_half(self: "CastSelf") -> "_2684.SynchroniserHalf":
        from mastapy._private.system_model.part_model.couplings import _2684

        return self.__parent__._cast(_2684.SynchroniserHalf)

    @property
    def synchroniser_sleeve(self: "CastSelf") -> "_2686.SynchroniserSleeve":
        from mastapy._private.system_model.part_model.couplings import _2686

        return self.__parent__._cast(_2686.SynchroniserSleeve)

    @property
    def synchroniser_part(self: "CastSelf") -> "SynchroniserPart":
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
class SynchroniserPart(_2658.CouplingHalf):
    """SynchroniserPart

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SYNCHRONISER_PART

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_SynchroniserPart":
        """Cast to another type.

        Returns:
            _Cast_SynchroniserPart
        """
        return _Cast_SynchroniserPart(self)
