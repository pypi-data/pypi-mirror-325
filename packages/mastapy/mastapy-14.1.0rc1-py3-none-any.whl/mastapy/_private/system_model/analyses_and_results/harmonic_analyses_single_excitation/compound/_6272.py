"""AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6300,
)

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6139,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6279,
        _6282,
        _6283,
        _6284,
        _6293,
        _6326,
        _6330,
        _6347,
        _6349,
        _6369,
        _6375,
        _6378,
        _6381,
        _6382,
        _6396,
    )

    Self = TypeVar(
        "Self", bound="AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation._Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation:
    """Special nested class for casting AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

    __parent__: "AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation"

    @property
    def conical_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6300.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
        return self.__parent__._cast(
            _6300.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6326.GearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6326,
        )

        return self.__parent__._cast(
            _6326.GearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def mountable_component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6347.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6347,
        )

        return self.__parent__._cast(
            _6347.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def component_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6293.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6293,
        )

        return self.__parent__._cast(
            _6293.ComponentCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6349.PartCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6349,
        )

        return self.__parent__._cast(
            _6349.PartCompoundHarmonicAnalysisOfSingleExcitation
        )

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
    def bevel_differential_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6279.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6279,
        )

        return self.__parent__._cast(
            _6279.BevelDifferentialGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_planet_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6282.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6282,
        )

        return self.__parent__._cast(
            _6282.BevelDifferentialPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_sun_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6283.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6283,
        )

        return self.__parent__._cast(
            _6283.BevelDifferentialSunGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6284.BevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6284,
        )

        return self.__parent__._cast(
            _6284.BevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def hypoid_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6330.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6330,
        )

        return self.__parent__._cast(
            _6330.HypoidGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spiral_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6369.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6369,
        )

        return self.__parent__._cast(
            _6369.SpiralBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_diff_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6375.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6375,
        )

        return self.__parent__._cast(
            _6375.StraightBevelDiffGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6378.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6378,
        )

        return self.__parent__._cast(
            _6378.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_planet_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6381.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6381,
        )

        return self.__parent__._cast(
            _6381.StraightBevelPlanetGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_sun_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6382.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6382,
        )

        return self.__parent__._cast(
            _6382.StraightBevelSunGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def zerol_bevel_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6396.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6396,
        )

        return self.__parent__._cast(
            _6396.ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def agma_gleason_conical_gear_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
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
class AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation(
    _6300.ConicalGearCompoundHarmonicAnalysisOfSingleExcitation
):
    """AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_6139.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6139.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation":
        """Cast to another type.

        Returns:
            _Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation
        """
        return _Cast_AGMAGleasonConicalGearCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
