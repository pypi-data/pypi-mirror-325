"""AGMAGleasonConicalGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.part_model.gears import _2596

_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.part_model import _2501, _2537, _2546
    from mastapy._private.system_model.part_model.gears import (
        _2588,
        _2592,
        _2604,
        _2607,
        _2616,
        _2618,
        _2620,
        _2626,
    )

    Self = TypeVar("Self", bound="AGMAGleasonConicalGearSet")
    CastSelf = TypeVar(
        "CastSelf", bound="AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSet",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AGMAGleasonConicalGearSet:
    """Special nested class for casting AGMAGleasonConicalGearSet to subclasses."""

    __parent__: "AGMAGleasonConicalGearSet"

    @property
    def conical_gear_set(self: "CastSelf") -> "_2596.ConicalGearSet":
        return self.__parent__._cast(_2596.ConicalGearSet)

    @property
    def gear_set(self: "CastSelf") -> "_2604.GearSet":
        from mastapy._private.system_model.part_model.gears import _2604

        return self.__parent__._cast(_2604.GearSet)

    @property
    def specialised_assembly(self: "CastSelf") -> "_2546.SpecialisedAssembly":
        from mastapy._private.system_model.part_model import _2546

        return self.__parent__._cast(_2546.SpecialisedAssembly)

    @property
    def abstract_assembly(self: "CastSelf") -> "_2501.AbstractAssembly":
        from mastapy._private.system_model.part_model import _2501

        return self.__parent__._cast(_2501.AbstractAssembly)

    @property
    def part(self: "CastSelf") -> "_2537.Part":
        from mastapy._private.system_model.part_model import _2537

        return self.__parent__._cast(_2537.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2269.DesignEntity":
        from mastapy._private.system_model import _2269

        return self.__parent__._cast(_2269.DesignEntity)

    @property
    def bevel_differential_gear_set(
        self: "CastSelf",
    ) -> "_2588.BevelDifferentialGearSet":
        from mastapy._private.system_model.part_model.gears import _2588

        return self.__parent__._cast(_2588.BevelDifferentialGearSet)

    @property
    def bevel_gear_set(self: "CastSelf") -> "_2592.BevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2592

        return self.__parent__._cast(_2592.BevelGearSet)

    @property
    def hypoid_gear_set(self: "CastSelf") -> "_2607.HypoidGearSet":
        from mastapy._private.system_model.part_model.gears import _2607

        return self.__parent__._cast(_2607.HypoidGearSet)

    @property
    def spiral_bevel_gear_set(self: "CastSelf") -> "_2616.SpiralBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2616

        return self.__parent__._cast(_2616.SpiralBevelGearSet)

    @property
    def straight_bevel_diff_gear_set(
        self: "CastSelf",
    ) -> "_2618.StraightBevelDiffGearSet":
        from mastapy._private.system_model.part_model.gears import _2618

        return self.__parent__._cast(_2618.StraightBevelDiffGearSet)

    @property
    def straight_bevel_gear_set(self: "CastSelf") -> "_2620.StraightBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2620

        return self.__parent__._cast(_2620.StraightBevelGearSet)

    @property
    def zerol_bevel_gear_set(self: "CastSelf") -> "_2626.ZerolBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2626

        return self.__parent__._cast(_2626.ZerolBevelGearSet)

    @property
    def agma_gleason_conical_gear_set(self: "CastSelf") -> "AGMAGleasonConicalGearSet":
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
class AGMAGleasonConicalGearSet(_2596.ConicalGearSet):
    """AGMAGleasonConicalGearSet

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _AGMA_GLEASON_CONICAL_GEAR_SET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_AGMAGleasonConicalGearSet":
        """Cast to another type.

        Returns:
            _Cast_AGMAGleasonConicalGearSet
        """
        return _Cast_AGMAGleasonConicalGearSet(self)
