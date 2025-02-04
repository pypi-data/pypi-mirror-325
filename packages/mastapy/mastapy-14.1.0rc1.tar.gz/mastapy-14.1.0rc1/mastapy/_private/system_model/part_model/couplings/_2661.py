"""CVTPulley"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.implicit import list_with_selected_item
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.system_model.part_model.couplings import _2665, _2674

_CVT_PULLEY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CVTPulley"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.part_model import _2511, _2533, _2537
    from mastapy._private.system_model.part_model.couplings import _2658

    Self = TypeVar("Self", bound="CVTPulley")
    CastSelf = TypeVar("CastSelf", bound="CVTPulley._Cast_CVTPulley")


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulley",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CVTPulley:
    """Special nested class for casting CVTPulley to subclasses."""

    __parent__: "CVTPulley"

    @property
    def pulley(self: "CastSelf") -> "_2665.Pulley":
        return self.__parent__._cast(_2665.Pulley)

    @property
    def coupling_half(self: "CastSelf") -> "_2658.CouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2658

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
    def cvt_pulley(self: "CastSelf") -> "CVTPulley":
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
class CVTPulley(_2665.Pulley):
    """CVTPulley

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CVT_PULLEY

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def is_moving_sheave_on_the_left(self: "Self") -> "bool":
        """bool"""
        temp = pythonnet_property_get(self.wrapped, "IsMovingSheaveOnTheLeft")

        if temp is None:
            return False

        return temp

    @is_moving_sheave_on_the_left.setter
    @enforce_parameter_types
    def is_moving_sheave_on_the_left(self: "Self", value: "bool") -> None:
        pythonnet_property_set(
            self.wrapped,
            "IsMovingSheaveOnTheLeft",
            bool(value) if value is not None else False,
        )

    @property
    def sliding_connection(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_ShaftHubConnection":
        """ListWithSelectedItem[mastapy.system_model.part_model.couplings.ShaftHubConnection]"""
        temp = pythonnet_property_get(self.wrapped, "SlidingConnection")

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ShaftHubConnection",
        )(temp)

    @sliding_connection.setter
    @enforce_parameter_types
    def sliding_connection(self: "Self", value: "_2674.ShaftHubConnection") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ShaftHubConnection.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ShaftHubConnection.implicit_type()
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        pythonnet_property_set(self.wrapped, "SlidingConnection", value)

    @property
    def cast_to(self: "Self") -> "_Cast_CVTPulley":
        """Cast to another type.

        Returns:
            _Cast_CVTPulley
        """
        return _Cast_CVTPulley(self)
