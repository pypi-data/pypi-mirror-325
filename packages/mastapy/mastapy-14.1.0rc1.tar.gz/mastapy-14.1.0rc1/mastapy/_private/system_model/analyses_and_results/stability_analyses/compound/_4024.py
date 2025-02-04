"""ConicalGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
    _4050,
)

_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConicalGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.stability_analyses import (
        _3887,
    )
    from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
        _3990,
        _3996,
        _4003,
        _4008,
        _4054,
        _4058,
        _4061,
        _4064,
        _4071,
        _4090,
        _4093,
        _4099,
        _4102,
        _4120,
    )

    Self = TypeVar("Self", bound="ConicalGearSetCompoundStabilityAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundStabilityAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearSetCompoundStabilityAnalysis:
    """Special nested class for casting ConicalGearSetCompoundStabilityAnalysis to subclasses."""

    __parent__: "ConicalGearSetCompoundStabilityAnalysis"

    @property
    def gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4050.GearSetCompoundStabilityAnalysis":
        return self.__parent__._cast(_4050.GearSetCompoundStabilityAnalysis)

    @property
    def specialised_assembly_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4090.SpecialisedAssemblyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4090,
        )

        return self.__parent__._cast(_4090.SpecialisedAssemblyCompoundStabilityAnalysis)

    @property
    def abstract_assembly_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_3990.AbstractAssemblyCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _3990,
        )

        return self.__parent__._cast(_3990.AbstractAssemblyCompoundStabilityAnalysis)

    @property
    def part_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4071.PartCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4071,
        )

        return self.__parent__._cast(_4071.PartCompoundStabilityAnalysis)

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
    def agma_gleason_conical_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_3996.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _3996,
        )

        return self.__parent__._cast(
            _3996.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
        )

    @property
    def bevel_differential_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4003.BevelDifferentialGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4003,
        )

        return self.__parent__._cast(
            _4003.BevelDifferentialGearSetCompoundStabilityAnalysis
        )

    @property
    def bevel_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4008.BevelGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4008,
        )

        return self.__parent__._cast(_4008.BevelGearSetCompoundStabilityAnalysis)

    @property
    def hypoid_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4054.HypoidGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4054,
        )

        return self.__parent__._cast(_4054.HypoidGearSetCompoundStabilityAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4058.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4058,
        )

        return self.__parent__._cast(
            _4058.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4061.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4061,
        )

        return self.__parent__._cast(
            _4061.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4064.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4064,
        )

        return self.__parent__._cast(
            _4064.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
        )

    @property
    def spiral_bevel_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4093.SpiralBevelGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4093,
        )

        return self.__parent__._cast(_4093.SpiralBevelGearSetCompoundStabilityAnalysis)

    @property
    def straight_bevel_diff_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4099.StraightBevelDiffGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4099,
        )

        return self.__parent__._cast(
            _4099.StraightBevelDiffGearSetCompoundStabilityAnalysis
        )

    @property
    def straight_bevel_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4102.StraightBevelGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4102,
        )

        return self.__parent__._cast(
            _4102.StraightBevelGearSetCompoundStabilityAnalysis
        )

    @property
    def zerol_bevel_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4120.ZerolBevelGearSetCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4120,
        )

        return self.__parent__._cast(_4120.ZerolBevelGearSetCompoundStabilityAnalysis)

    @property
    def conical_gear_set_compound_stability_analysis(
        self: "CastSelf",
    ) -> "ConicalGearSetCompoundStabilityAnalysis":
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
class ConicalGearSetCompoundStabilityAnalysis(_4050.GearSetCompoundStabilityAnalysis):
    """ConicalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_3887.ConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearSetStabilityAnalysis]

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
    ) -> "List[_3887.ConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearSetStabilityAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_ConicalGearSetCompoundStabilityAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearSetCompoundStabilityAnalysis
        """
        return _Cast_ConicalGearSetCompoundStabilityAnalysis(self)
