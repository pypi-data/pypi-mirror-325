"""BevelGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.part_model.gears import _2585

_BEVEL_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear")

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.bevel import _1228
    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.part_model import _2511, _2533, _2537
    from mastapy._private.system_model.part_model.gears import (
        _2587,
        _2589,
        _2590,
        _2595,
        _2602,
        _2615,
        _2617,
        _2619,
        _2621,
        _2622,
        _2625,
    )

    Self = TypeVar("Self", bound="BevelGear")
    CastSelf = TypeVar("CastSelf", bound="BevelGear._Cast_BevelGear")


__docformat__ = "restructuredtext en"
__all__ = ("BevelGear",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelGear:
    """Special nested class for casting BevelGear to subclasses."""

    __parent__: "BevelGear"

    @property
    def agma_gleason_conical_gear(self: "CastSelf") -> "_2585.AGMAGleasonConicalGear":
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
    def bevel_differential_gear(self: "CastSelf") -> "_2587.BevelDifferentialGear":
        from mastapy._private.system_model.part_model.gears import _2587

        return self.__parent__._cast(_2587.BevelDifferentialGear)

    @property
    def bevel_differential_planet_gear(
        self: "CastSelf",
    ) -> "_2589.BevelDifferentialPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2589

        return self.__parent__._cast(_2589.BevelDifferentialPlanetGear)

    @property
    def bevel_differential_sun_gear(
        self: "CastSelf",
    ) -> "_2590.BevelDifferentialSunGear":
        from mastapy._private.system_model.part_model.gears import _2590

        return self.__parent__._cast(_2590.BevelDifferentialSunGear)

    @property
    def spiral_bevel_gear(self: "CastSelf") -> "_2615.SpiralBevelGear":
        from mastapy._private.system_model.part_model.gears import _2615

        return self.__parent__._cast(_2615.SpiralBevelGear)

    @property
    def straight_bevel_diff_gear(self: "CastSelf") -> "_2617.StraightBevelDiffGear":
        from mastapy._private.system_model.part_model.gears import _2617

        return self.__parent__._cast(_2617.StraightBevelDiffGear)

    @property
    def straight_bevel_gear(self: "CastSelf") -> "_2619.StraightBevelGear":
        from mastapy._private.system_model.part_model.gears import _2619

        return self.__parent__._cast(_2619.StraightBevelGear)

    @property
    def straight_bevel_planet_gear(self: "CastSelf") -> "_2621.StraightBevelPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2621

        return self.__parent__._cast(_2621.StraightBevelPlanetGear)

    @property
    def straight_bevel_sun_gear(self: "CastSelf") -> "_2622.StraightBevelSunGear":
        from mastapy._private.system_model.part_model.gears import _2622

        return self.__parent__._cast(_2622.StraightBevelSunGear)

    @property
    def zerol_bevel_gear(self: "CastSelf") -> "_2625.ZerolBevelGear":
        from mastapy._private.system_model.part_model.gears import _2625

        return self.__parent__._cast(_2625.ZerolBevelGear)

    @property
    def bevel_gear(self: "CastSelf") -> "BevelGear":
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
class BevelGear(_2585.AGMAGleasonConicalGear):
    """BevelGear

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEVEL_GEAR

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def conical_gear_design(self: "Self") -> "_1228.BevelGearDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearDesign

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConicalGearDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_design(self: "Self") -> "_1228.BevelGearDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearDesign

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "BevelGearDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_BevelGear":
        """Cast to another type.

        Returns:
            _Cast_BevelGear
        """
        return _Cast_BevelGear(self)
