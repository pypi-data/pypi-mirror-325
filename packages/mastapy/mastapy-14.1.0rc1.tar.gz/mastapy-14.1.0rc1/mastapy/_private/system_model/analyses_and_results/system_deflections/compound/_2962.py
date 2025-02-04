"""ConicalGearSetCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
    _2989,
)

_CONICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ConicalGearSetCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.gears.rating.conical import _560
    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2800,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2928,
        _2934,
        _2941,
        _2946,
        _2993,
        _2997,
        _3000,
        _3003,
        _3010,
        _3030,
        _3033,
        _3039,
        _3042,
        _3060,
    )

    Self = TypeVar("Self", bound="ConicalGearSetCompoundSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearSetCompoundSystemDeflection._Cast_ConicalGearSetCompoundSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearSetCompoundSystemDeflection:
    """Special nested class for casting ConicalGearSetCompoundSystemDeflection to subclasses."""

    __parent__: "ConicalGearSetCompoundSystemDeflection"

    @property
    def gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2989.GearSetCompoundSystemDeflection":
        return self.__parent__._cast(_2989.GearSetCompoundSystemDeflection)

    @property
    def specialised_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3030.SpecialisedAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3030,
        )

        return self.__parent__._cast(_3030.SpecialisedAssemblyCompoundSystemDeflection)

    @property
    def abstract_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2928.AbstractAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2928,
        )

        return self.__parent__._cast(_2928.AbstractAssemblyCompoundSystemDeflection)

    @property
    def part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3010.PartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3010,
        )

        return self.__parent__._cast(_3010.PartCompoundSystemDeflection)

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
    def agma_gleason_conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2934.AGMAGleasonConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2934,
        )

        return self.__parent__._cast(
            _2934.AGMAGleasonConicalGearSetCompoundSystemDeflection
        )

    @property
    def bevel_differential_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2941.BevelDifferentialGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2941,
        )

        return self.__parent__._cast(
            _2941.BevelDifferentialGearSetCompoundSystemDeflection
        )

    @property
    def bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2946.BevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2946,
        )

        return self.__parent__._cast(_2946.BevelGearSetCompoundSystemDeflection)

    @property
    def hypoid_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2993.HypoidGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2993,
        )

        return self.__parent__._cast(_2993.HypoidGearSetCompoundSystemDeflection)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2997.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2997,
        )

        return self.__parent__._cast(
            _2997.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3000.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3000,
        )

        return self.__parent__._cast(
            _3000.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3003.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3003,
        )

        return self.__parent__._cast(
            _3003.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
        )

    @property
    def spiral_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3033.SpiralBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3033,
        )

        return self.__parent__._cast(_3033.SpiralBevelGearSetCompoundSystemDeflection)

    @property
    def straight_bevel_diff_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3039.StraightBevelDiffGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3039,
        )

        return self.__parent__._cast(
            _3039.StraightBevelDiffGearSetCompoundSystemDeflection
        )

    @property
    def straight_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3042.StraightBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3042,
        )

        return self.__parent__._cast(_3042.StraightBevelGearSetCompoundSystemDeflection)

    @property
    def zerol_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3060.ZerolBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3060,
        )

        return self.__parent__._cast(_3060.ZerolBevelGearSetCompoundSystemDeflection)

    @property
    def conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "ConicalGearSetCompoundSystemDeflection":
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
class ConicalGearSetCompoundSystemDeflection(_2989.GearSetCompoundSystemDeflection):
    """ConicalGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def conical_gear_set_duty_cycle_rating(
        self: "Self",
    ) -> "_560.ConicalGearSetDutyCycleRating":
        """mastapy.gears.rating.conical.ConicalGearSetDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConicalGearSetDutyCycleRating")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_2800.ConicalGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection]

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
    ) -> "List[_2800.ConicalGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSetSystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_ConicalGearSetCompoundSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearSetCompoundSystemDeflection
        """
        return _Cast_ConicalGearSetCompoundSystemDeflection(self)
