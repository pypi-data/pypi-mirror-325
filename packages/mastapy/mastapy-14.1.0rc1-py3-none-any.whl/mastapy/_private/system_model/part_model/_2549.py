"""VirtualComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.part_model import _2533

_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.part_model import (
        _2511,
        _2529,
        _2530,
        _2537,
        _2540,
        _2541,
        _2547,
    )

    Self = TypeVar("Self", bound="VirtualComponent")
    CastSelf = TypeVar("CastSelf", bound="VirtualComponent._Cast_VirtualComponent")


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponent",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_VirtualComponent:
    """Special nested class for casting VirtualComponent to subclasses."""

    __parent__: "VirtualComponent"

    @property
    def mountable_component(self: "CastSelf") -> "_2533.MountableComponent":
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
    def mass_disc(self: "CastSelf") -> "_2529.MassDisc":
        from mastapy._private.system_model.part_model import _2529

        return self.__parent__._cast(_2529.MassDisc)

    @property
    def measurement_component(self: "CastSelf") -> "_2530.MeasurementComponent":
        from mastapy._private.system_model.part_model import _2530

        return self.__parent__._cast(_2530.MeasurementComponent)

    @property
    def point_load(self: "CastSelf") -> "_2540.PointLoad":
        from mastapy._private.system_model.part_model import _2540

        return self.__parent__._cast(_2540.PointLoad)

    @property
    def power_load(self: "CastSelf") -> "_2541.PowerLoad":
        from mastapy._private.system_model.part_model import _2541

        return self.__parent__._cast(_2541.PowerLoad)

    @property
    def unbalanced_mass(self: "CastSelf") -> "_2547.UnbalancedMass":
        from mastapy._private.system_model.part_model import _2547

        return self.__parent__._cast(_2547.UnbalancedMass)

    @property
    def virtual_component(self: "CastSelf") -> "VirtualComponent":
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
class VirtualComponent(_2533.MountableComponent):
    """VirtualComponent

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _VIRTUAL_COMPONENT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_VirtualComponent":
        """Cast to another type.

        Returns:
            _Cast_VirtualComponent
        """
        return _Cast_VirtualComponent(self)
