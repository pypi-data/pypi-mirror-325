"""AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7383,
)

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7220,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7349,
        _7362,
        _7367,
        _7409,
        _7413,
        _7430,
        _7449,
        _7452,
        _7458,
        _7461,
        _7479,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )

    Self = TypeVar(
        "Self", bound="AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection:
    """Special nested class for casting AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection to subclasses."""

    __parent__: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"

    @property
    def conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7383.ConicalGearSetCompoundAdvancedSystemDeflection":
        return self.__parent__._cast(
            _7383.ConicalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7409.GearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7409,
        )

        return self.__parent__._cast(_7409.GearSetCompoundAdvancedSystemDeflection)

    @property
    def specialised_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7449.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7449,
        )

        return self.__parent__._cast(
            _7449.SpecialisedAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def abstract_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7349.AbstractAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7349,
        )

        return self.__parent__._cast(
            _7349.AbstractAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7430.PartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7430,
        )

        return self.__parent__._cast(_7430.PartCompoundAdvancedSystemDeflection)

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
    def bevel_differential_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7362.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7362,
        )

        return self.__parent__._cast(
            _7362.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7367.BevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7367,
        )

        return self.__parent__._cast(_7367.BevelGearSetCompoundAdvancedSystemDeflection)

    @property
    def hypoid_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7413.HypoidGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7413,
        )

        return self.__parent__._cast(
            _7413.HypoidGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def spiral_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7452.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7452,
        )

        return self.__parent__._cast(
            _7452.SpiralBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7458.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7458,
        )

        return self.__parent__._cast(
            _7458.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7461.StraightBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7461,
        )

        return self.__parent__._cast(
            _7461.StraightBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def zerol_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7479.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7479,
        )

        return self.__parent__._cast(
            _7479.ZerolBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
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
class AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection(
    _7383.ConicalGearSetCompoundAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_7220.AGMAGleasonConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearSetAdvancedSystemDeflection]

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
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_7220.AGMAGleasonConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearSetAdvancedSystemDeflection]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
        """
        return _Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection(self)
