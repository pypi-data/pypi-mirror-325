"""StraightBevelGearSetCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
    _6559,
)

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "StraightBevelGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
        _6522,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6541,
        _6547,
        _6575,
        _6601,
        _6622,
        _6641,
        _6651,
        _6652,
    )
    from mastapy._private.system_model.part_model.gears import _2620

    Self = TypeVar("Self", bound="StraightBevelGearSetCompoundDynamicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelGearSetCompoundDynamicAnalysis._Cast_StraightBevelGearSetCompoundDynamicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetCompoundDynamicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelGearSetCompoundDynamicAnalysis:
    """Special nested class for casting StraightBevelGearSetCompoundDynamicAnalysis to subclasses."""

    __parent__: "StraightBevelGearSetCompoundDynamicAnalysis"

    @property
    def bevel_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6559.BevelGearSetCompoundDynamicAnalysis":
        return self.__parent__._cast(_6559.BevelGearSetCompoundDynamicAnalysis)

    @property
    def agma_gleason_conical_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6547.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6547,
        )

        return self.__parent__._cast(
            _6547.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
        )

    @property
    def conical_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6575.ConicalGearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6575,
        )

        return self.__parent__._cast(_6575.ConicalGearSetCompoundDynamicAnalysis)

    @property
    def gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6601.GearSetCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6601,
        )

        return self.__parent__._cast(_6601.GearSetCompoundDynamicAnalysis)

    @property
    def specialised_assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6641.SpecialisedAssemblyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6641,
        )

        return self.__parent__._cast(_6641.SpecialisedAssemblyCompoundDynamicAnalysis)

    @property
    def abstract_assembly_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6541.AbstractAssemblyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6541,
        )

        return self.__parent__._cast(_6541.AbstractAssemblyCompoundDynamicAnalysis)

    @property
    def part_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6622.PartCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6622,
        )

        return self.__parent__._cast(_6622.PartCompoundDynamicAnalysis)

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7707.PartCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7707,
        )

        return self.__parent__._cast(_7707.PartCompoundAnalysis)

    @property
    def design_entity_compound_analysis(
        self: "CastSelf",
    ) -> "_7704.DesignEntityCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7704,
        )

        return self.__parent__._cast(_7704.DesignEntityCompoundAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2726.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2726

        return self.__parent__._cast(_2726.DesignEntityAnalysis)

    @property
    def straight_bevel_gear_set_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "StraightBevelGearSetCompoundDynamicAnalysis":
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
class StraightBevelGearSetCompoundDynamicAnalysis(
    _6559.BevelGearSetCompoundDynamicAnalysis
):
    """StraightBevelGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2620.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: "Self") -> "_2620.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6522.StraightBevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearSetDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gears_compound_dynamic_analysis(
        self: "Self",
    ) -> "List[_6651.StraightBevelGearCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelGearCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "StraightBevelGearsCompoundDynamicAnalysis"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_compound_dynamic_analysis(
        self: "Self",
    ) -> "List[_6652.StraightBevelGearMeshCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.StraightBevelGearMeshCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "StraightBevelMeshesCompoundDynamicAnalysis"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_6522.StraightBevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.StraightBevelGearSetDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_StraightBevelGearSetCompoundDynamicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelGearSetCompoundDynamicAnalysis
        """
        return _Cast_StraightBevelGearSetCompoundDynamicAnalysis(self)
