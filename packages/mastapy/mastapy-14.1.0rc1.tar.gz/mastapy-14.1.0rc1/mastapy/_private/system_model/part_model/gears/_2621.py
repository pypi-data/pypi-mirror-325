"""StraightBevelPlanetGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.part_model.gears import _2617

_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelPlanetGear"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears import _358
    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.part_model import _2511, _2533, _2537
    from mastapy._private.system_model.part_model.gears import (
        _2585,
        _2591,
        _2595,
        _2602,
    )

    Self = TypeVar("Self", bound="StraightBevelPlanetGear")
    CastSelf = TypeVar(
        "CastSelf", bound="StraightBevelPlanetGear._Cast_StraightBevelPlanetGear"
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGear",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelPlanetGear:
    """Special nested class for casting StraightBevelPlanetGear to subclasses."""

    __parent__: "StraightBevelPlanetGear"

    @property
    def straight_bevel_diff_gear(self: "CastSelf") -> "_2617.StraightBevelDiffGear":
        return self.__parent__._cast(_2617.StraightBevelDiffGear)

    @property
    def bevel_gear(self: "CastSelf") -> "_2591.BevelGear":
        from mastapy._private.system_model.part_model.gears import _2591

        return self.__parent__._cast(_2591.BevelGear)

    @property
    def agma_gleason_conical_gear(self: "CastSelf") -> "_2585.AGMAGleasonConicalGear":
        from mastapy._private.system_model.part_model.gears import _2585

        return self.__parent__._cast(_2585.AGMAGleasonConicalGear)

    @property
    def conical_gear(self: "CastSelf") -> "_2595.ConicalGear":
        from mastapy._private.system_model.part_model.gears import _2595

        return self.__parent__._cast(_2595.ConicalGear)

    @property
    def gear(self: "CastSelf") -> "_2602.Gear":
        from mastapy._private.system_model.part_model.gears import _2602

        return self.__parent__._cast(_2602.Gear)

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
    def straight_bevel_planet_gear(self: "CastSelf") -> "StraightBevelPlanetGear":
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
class StraightBevelPlanetGear(_2617.StraightBevelDiffGear):
    """StraightBevelPlanetGear

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STRAIGHT_BEVEL_PLANET_GEAR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def planetary_details(self: "Self") -> "_358.PlanetaryDetail":
        """mastapy.gears.PlanetaryDetail

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "PlanetaryDetails")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_StraightBevelPlanetGear":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelPlanetGear
        """
        return _Cast_StraightBevelPlanetGear(self)
