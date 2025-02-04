"""ConicalGearSetCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6872,
)

_CONICAL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "ConicalGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6712,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6812,
        _6818,
        _6825,
        _6830,
        _6876,
        _6880,
        _6883,
        _6886,
        _6893,
        _6912,
        _6915,
        _6921,
        _6924,
        _6942,
    )

    Self = TypeVar("Self", bound="ConicalGearSetCompoundCriticalSpeedAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearSetCompoundCriticalSpeedAnalysis._Cast_ConicalGearSetCompoundCriticalSpeedAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearSetCompoundCriticalSpeedAnalysis:
    """Special nested class for casting ConicalGearSetCompoundCriticalSpeedAnalysis to subclasses."""

    __parent__: "ConicalGearSetCompoundCriticalSpeedAnalysis"

    @property
    def gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6872.GearSetCompoundCriticalSpeedAnalysis":
        return self.__parent__._cast(_6872.GearSetCompoundCriticalSpeedAnalysis)

    @property
    def specialised_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6912.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6912,
        )

        return self.__parent__._cast(
            _6912.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def abstract_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6812.AbstractAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6812,
        )

        return self.__parent__._cast(
            _6812.AbstractAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6893.PartCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6893,
        )

        return self.__parent__._cast(_6893.PartCompoundCriticalSpeedAnalysis)

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
    def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6818.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6818,
        )

        return self.__parent__._cast(
            _6818.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_differential_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6825.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6825,
        )

        return self.__parent__._cast(
            _6825.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6830.BevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6830,
        )

        return self.__parent__._cast(_6830.BevelGearSetCompoundCriticalSpeedAnalysis)

    @property
    def hypoid_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6876.HypoidGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6876,
        )

        return self.__parent__._cast(_6876.HypoidGearSetCompoundCriticalSpeedAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6880.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6880,
        )

        return self.__parent__._cast(
            _6880.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6883.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6883,
        )

        return self.__parent__._cast(
            _6883.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> (
        "_6886.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
    ):
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6886,
        )

        return self.__parent__._cast(
            _6886.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def spiral_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6915.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6915,
        )

        return self.__parent__._cast(
            _6915.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6921.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6921,
        )

        return self.__parent__._cast(
            _6921.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6924.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6924,
        )

        return self.__parent__._cast(
            _6924.StraightBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def zerol_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6942.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6942,
        )

        return self.__parent__._cast(
            _6942.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "ConicalGearSetCompoundCriticalSpeedAnalysis":
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
class ConicalGearSetCompoundCriticalSpeedAnalysis(
    _6872.GearSetCompoundCriticalSpeedAnalysis
):
    """ConicalGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_6712.ConicalGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearSetCriticalSpeedAnalysis]

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
    ) -> "List[_6712.ConicalGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearSetCriticalSpeedAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_ConicalGearSetCompoundCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearSetCompoundCriticalSpeedAnalysis
        """
        return _Cast_ConicalGearSetCompoundCriticalSpeedAnalysis(self)
