"""GearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.system_model.analyses_and_results.static_loads import _7614

_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Tuple, Type, TypeVar, Union

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7501,
        _7510,
        _7513,
        _7514,
        _7515,
        _7525,
        _7529,
        _7532,
        _7549,
        _7554,
        _7572,
        _7579,
        _7593,
        _7600,
        _7603,
        _7606,
        _7618,
        _7643,
        _7649,
        _7652,
        _7655,
        _7656,
        _7673,
        _7676,
    )
    from mastapy._private.system_model.part_model.gears import _2602

    Self = TypeVar("Self", bound="GearLoadCase")
    CastSelf = TypeVar("CastSelf", bound="GearLoadCase._Cast_GearLoadCase")


__docformat__ = "restructuredtext en"
__all__ = ("GearLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearLoadCase:
    """Special nested class for casting GearLoadCase to subclasses."""

    __parent__: "GearLoadCase"

    @property
    def mountable_component_load_case(
        self: "CastSelf",
    ) -> "_7614.MountableComponentLoadCase":
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
    def agma_gleason_conical_gear_load_case(
        self: "CastSelf",
    ) -> "_7501.AGMAGleasonConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7501,
        )

        return self.__parent__._cast(_7501.AGMAGleasonConicalGearLoadCase)

    @property
    def bevel_differential_gear_load_case(
        self: "CastSelf",
    ) -> "_7510.BevelDifferentialGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7510,
        )

        return self.__parent__._cast(_7510.BevelDifferentialGearLoadCase)

    @property
    def bevel_differential_planet_gear_load_case(
        self: "CastSelf",
    ) -> "_7513.BevelDifferentialPlanetGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7513,
        )

        return self.__parent__._cast(_7513.BevelDifferentialPlanetGearLoadCase)

    @property
    def bevel_differential_sun_gear_load_case(
        self: "CastSelf",
    ) -> "_7514.BevelDifferentialSunGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7514,
        )

        return self.__parent__._cast(_7514.BevelDifferentialSunGearLoadCase)

    @property
    def bevel_gear_load_case(self: "CastSelf") -> "_7515.BevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7515,
        )

        return self.__parent__._cast(_7515.BevelGearLoadCase)

    @property
    def concept_gear_load_case(self: "CastSelf") -> "_7529.ConceptGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7529,
        )

        return self.__parent__._cast(_7529.ConceptGearLoadCase)

    @property
    def conical_gear_load_case(self: "CastSelf") -> "_7532.ConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7532,
        )

        return self.__parent__._cast(_7532.ConicalGearLoadCase)

    @property
    def cylindrical_gear_load_case(self: "CastSelf") -> "_7549.CylindricalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7549,
        )

        return self.__parent__._cast(_7549.CylindricalGearLoadCase)

    @property
    def cylindrical_planet_gear_load_case(
        self: "CastSelf",
    ) -> "_7554.CylindricalPlanetGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7554,
        )

        return self.__parent__._cast(_7554.CylindricalPlanetGearLoadCase)

    @property
    def face_gear_load_case(self: "CastSelf") -> "_7572.FaceGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7572,
        )

        return self.__parent__._cast(_7572.FaceGearLoadCase)

    @property
    def hypoid_gear_load_case(self: "CastSelf") -> "_7593.HypoidGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7593,
        )

        return self.__parent__._cast(_7593.HypoidGearLoadCase)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_load_case(
        self: "CastSelf",
    ) -> "_7600.KlingelnbergCycloPalloidConicalGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7600,
        )

        return self.__parent__._cast(_7600.KlingelnbergCycloPalloidConicalGearLoadCase)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
        self: "CastSelf",
    ) -> "_7603.KlingelnbergCycloPalloidHypoidGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7603,
        )

        return self.__parent__._cast(_7603.KlingelnbergCycloPalloidHypoidGearLoadCase)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
        self: "CastSelf",
    ) -> "_7606.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7606,
        )

        return self.__parent__._cast(
            _7606.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
        )

    @property
    def spiral_bevel_gear_load_case(
        self: "CastSelf",
    ) -> "_7643.SpiralBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7643,
        )

        return self.__parent__._cast(_7643.SpiralBevelGearLoadCase)

    @property
    def straight_bevel_diff_gear_load_case(
        self: "CastSelf",
    ) -> "_7649.StraightBevelDiffGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7649,
        )

        return self.__parent__._cast(_7649.StraightBevelDiffGearLoadCase)

    @property
    def straight_bevel_gear_load_case(
        self: "CastSelf",
    ) -> "_7652.StraightBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7652,
        )

        return self.__parent__._cast(_7652.StraightBevelGearLoadCase)

    @property
    def straight_bevel_planet_gear_load_case(
        self: "CastSelf",
    ) -> "_7655.StraightBevelPlanetGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7655,
        )

        return self.__parent__._cast(_7655.StraightBevelPlanetGearLoadCase)

    @property
    def straight_bevel_sun_gear_load_case(
        self: "CastSelf",
    ) -> "_7656.StraightBevelSunGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7656,
        )

        return self.__parent__._cast(_7656.StraightBevelSunGearLoadCase)

    @property
    def worm_gear_load_case(self: "CastSelf") -> "_7673.WormGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7673,
        )

        return self.__parent__._cast(_7673.WormGearLoadCase)

    @property
    def zerol_bevel_gear_load_case(self: "CastSelf") -> "_7676.ZerolBevelGearLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7676,
        )

        return self.__parent__._cast(_7676.ZerolBevelGearLoadCase)

    @property
    def gear_load_case(self: "CastSelf") -> "GearLoadCase":
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
class GearLoadCase(_7614.MountableComponentLoadCase):
    """GearLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def gear_temperature(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = pythonnet_property_get(self.wrapped, "GearTemperature")

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @gear_temperature.setter
    @enforce_parameter_types
    def gear_temperature(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        pythonnet_property_set(self.wrapped, "GearTemperature", value)

    @property
    def component_design(self: "Self") -> "_2602.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_manufacture_errors(self: "Self") -> "_7579.GearManufactureError":
        """mastapy.system_model.analyses_and_results.static_loads.GearManufactureError

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "GearManufactureErrors")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_GearLoadCase":
        """Cast to another type.

        Returns:
            _Cast_GearLoadCase
        """
        return _Cast_GearLoadCase(self)
