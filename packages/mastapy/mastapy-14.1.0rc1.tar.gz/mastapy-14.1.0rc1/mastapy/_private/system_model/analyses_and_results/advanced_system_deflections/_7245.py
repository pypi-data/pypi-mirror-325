"""ConceptGearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
    _7276,
)

_CONCEPT_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "ConceptGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.gears.rating.concept import _572
    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7211,
        _7243,
        _7244,
        _7298,
        _7317,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads import _7531
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2796,
    )
    from mastapy._private.system_model.part_model.gears import _2594

    Self = TypeVar("Self", bound="ConceptGearSetAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConceptGearSetAdvancedSystemDeflection._Cast_ConceptGearSetAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConceptGearSetAdvancedSystemDeflection:
    """Special nested class for casting ConceptGearSetAdvancedSystemDeflection to subclasses."""

    __parent__: "ConceptGearSetAdvancedSystemDeflection"

    @property
    def gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7276.GearSetAdvancedSystemDeflection":
        return self.__parent__._cast(_7276.GearSetAdvancedSystemDeflection)

    @property
    def specialised_assembly_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7317.SpecialisedAssemblyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7317,
        )

        return self.__parent__._cast(_7317.SpecialisedAssemblyAdvancedSystemDeflection)

    @property
    def abstract_assembly_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7211.AbstractAssemblyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7211,
        )

        return self.__parent__._cast(_7211.AbstractAssemblyAdvancedSystemDeflection)

    @property
    def part_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7298.PartAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7298,
        )

        return self.__parent__._cast(_7298.PartAdvancedSystemDeflection)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7709.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7709,
        )

        return self.__parent__._cast(_7709.PartStaticLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7706.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7706,
        )

        return self.__parent__._cast(_7706.PartAnalysisCase)

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
    def concept_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "ConceptGearSetAdvancedSystemDeflection":
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
class ConceptGearSetAdvancedSystemDeflection(_7276.GearSetAdvancedSystemDeflection):
    """ConceptGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONCEPT_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2594.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: "Self") -> "_7531.ConceptGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyLoadCase")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: "Self") -> "_572.ConceptGearSetRating":
        """mastapy.gears.rating.concept.ConceptGearSetRating

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Rating")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: "Self") -> "_572.ConceptGearSetRating":
        """mastapy.gears.rating.concept.ConceptGearSetRating

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDetailedAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_system_deflection_results(
        self: "Self",
    ) -> "List[_2796.ConceptGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblySystemDeflectionResults")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gears_advanced_system_deflection(
        self: "Self",
    ) -> "List[_7243.ConceptGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "GearsAdvancedSystemDeflection")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_gears_advanced_system_deflection(
        self: "Self",
    ) -> "List[_7243.ConceptGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "ConceptGearsAdvancedSystemDeflection"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_advanced_system_deflection(
        self: "Self",
    ) -> "List[_7244.ConceptGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "MeshesAdvancedSystemDeflection")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_advanced_system_deflection(
        self: "Self",
    ) -> "List[_7244.ConceptGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "ConceptMeshesAdvancedSystemDeflection"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ConceptGearSetAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_ConceptGearSetAdvancedSystemDeflection
        """
        return _Cast_ConceptGearSetAdvancedSystemDeflection(self)
