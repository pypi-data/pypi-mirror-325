"""BevelDifferentialPlanetGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.static_loads import _7510

_BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialPlanetGearLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7501,
        _7515,
        _7525,
        _7532,
        _7578,
        _7614,
        _7618,
    )
    from mastapy._private.system_model.part_model.gears import _2589

    Self = TypeVar("Self", bound="BevelDifferentialPlanetGearLoadCase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="BevelDifferentialPlanetGearLoadCase._Cast_BevelDifferentialPlanetGearLoadCase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelDifferentialPlanetGearLoadCase:
    """Special nested class for casting BevelDifferentialPlanetGearLoadCase to subclasses."""

    __parent__: "BevelDifferentialPlanetGearLoadCase"

    @property
    def bevel_differential_gear_load_case(
        self: "CastSelf",
    ) -> "_7510.BevelDifferentialGearLoadCase":
        return self.__parent__._cast(_7510.BevelDifferentialGearLoadCase)

    @property
    def bevel_gear_load_case(self: "CastSelf") -> "_7515.BevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7515,
        )

        return self.__parent__._cast(_7515.BevelGearLoadCase)

    @property
    def agma_gleason_conical_gear_load_case(
        self: "CastSelf",
    ) -> "_7501.AGMAGleasonConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7501,
        )

        return self.__parent__._cast(_7501.AGMAGleasonConicalGearLoadCase)

    @property
    def conical_gear_load_case(self: "CastSelf") -> "_7532.ConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7532,
        )

        return self.__parent__._cast(_7532.ConicalGearLoadCase)

    @property
    def gear_load_case(self: "CastSelf") -> "_7578.GearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7578,
        )

        return self.__parent__._cast(_7578.GearLoadCase)

    @property
    def mountable_component_load_case(
        self: "CastSelf",
    ) -> "_7614.MountableComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7614,
        )

        return self.__parent__._cast(_7614.MountableComponentLoadCase)

    @property
    def component_load_case(self: "CastSelf") -> "_7525.ComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7525,
        )

        return self.__parent__._cast(_7525.ComponentLoadCase)

    @property
    def part_load_case(self: "CastSelf") -> "_7618.PartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7618,
        )

        return self.__parent__._cast(_7618.PartLoadCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2732.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2732

        return self.__parent__._cast(_2732.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2728.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2728

        return self.__parent__._cast(_2728.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2726.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2726

        return self.__parent__._cast(_2726.DesignEntityAnalysis)

    @property
    def bevel_differential_planet_gear_load_case(
        self: "CastSelf",
    ) -> "BevelDifferentialPlanetGearLoadCase":
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
class BevelDifferentialPlanetGearLoadCase(_7510.BevelDifferentialGearLoadCase):
    """BevelDifferentialPlanetGearLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEVEL_DIFFERENTIAL_PLANET_GEAR_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2589.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_BevelDifferentialPlanetGearLoadCase":
        """Cast to another type.

        Returns:
            _Cast_BevelDifferentialPlanetGearLoadCase
        """
        return _Cast_BevelDifferentialPlanetGearLoadCase(self)
