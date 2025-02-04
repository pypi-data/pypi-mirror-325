"""HypoidGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.static_loads import _7503

_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "HypoidGearSetLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7494,
        _7536,
        _7583,
        _7593,
        _7594,
        _7618,
        _7642,
    )
    from mastapy._private.system_model.part_model.gears import _2607

    Self = TypeVar("Self", bound="HypoidGearSetLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="HypoidGearSetLoadCase._Cast_HypoidGearSetLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_HypoidGearSetLoadCase:
    """Special nested class for casting HypoidGearSetLoadCase to subclasses."""

    __parent__: "HypoidGearSetLoadCase"

    @property
    def agma_gleason_conical_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7503.AGMAGleasonConicalGearSetLoadCase":
        return self.__parent__._cast(_7503.AGMAGleasonConicalGearSetLoadCase)

    @property
    def conical_gear_set_load_case(self: "CastSelf") -> "_7536.ConicalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7536,
        )

        return self.__parent__._cast(_7536.ConicalGearSetLoadCase)

    @property
    def gear_set_load_case(self: "CastSelf") -> "_7583.GearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7583,
        )

        return self.__parent__._cast(_7583.GearSetLoadCase)

    @property
    def specialised_assembly_load_case(
        self: "CastSelf",
    ) -> "_7642.SpecialisedAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7642,
        )

        return self.__parent__._cast(_7642.SpecialisedAssemblyLoadCase)

    @property
    def abstract_assembly_load_case(
        self: "CastSelf",
    ) -> "_7494.AbstractAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7494,
        )

        return self.__parent__._cast(_7494.AbstractAssemblyLoadCase)

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
    def hypoid_gear_set_load_case(self: "CastSelf") -> "HypoidGearSetLoadCase":
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
class HypoidGearSetLoadCase(_7503.AGMAGleasonConicalGearSetLoadCase):
    """HypoidGearSetLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _HYPOID_GEAR_SET_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2607.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def agma_gleason_conical_gears_load_case(
        self: "Self",
    ) -> "List[_7593.HypoidGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AGMAGleasonConicalGearsLoadCase")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gears_load_case(self: "Self") -> "List[_7593.HypoidGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "HypoidGearsLoadCase")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_load_case(
        self: "Self",
    ) -> "List[_7594.HypoidGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AGMAGleasonConicalMeshesLoadCase")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_load_case(self: "Self") -> "List[_7594.HypoidGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "HypoidMeshesLoadCase")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_HypoidGearSetLoadCase":
        """Cast to another type.

        Returns:
            _Cast_HypoidGearSetLoadCase
        """
        return _Cast_HypoidGearSetLoadCase(self)
