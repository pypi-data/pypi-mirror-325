"""ConicalGearCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5418,
)

_CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ConicalGearCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5261,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5364,
        _5371,
        _5374,
        _5375,
        _5376,
        _5385,
        _5422,
        _5426,
        _5429,
        _5432,
        _5439,
        _5441,
        _5461,
        _5467,
        _5470,
        _5473,
        _5474,
        _5488,
    )

    Self = TypeVar("Self", bound="ConicalGearCompoundModalAnalysisAtASpeed")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearCompoundModalAnalysisAtASpeed._Cast_ConicalGearCompoundModalAnalysisAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundModalAnalysisAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearCompoundModalAnalysisAtASpeed:
    """Special nested class for casting ConicalGearCompoundModalAnalysisAtASpeed to subclasses."""

    __parent__: "ConicalGearCompoundModalAnalysisAtASpeed"

    @property
    def gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5418.GearCompoundModalAnalysisAtASpeed":
        return self.__parent__._cast(_5418.GearCompoundModalAnalysisAtASpeed)

    @property
    def mountable_component_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5439.MountableComponentCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5439,
        )

        return self.__parent__._cast(
            _5439.MountableComponentCompoundModalAnalysisAtASpeed
        )

    @property
    def component_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5385.ComponentCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5385,
        )

        return self.__parent__._cast(_5385.ComponentCompoundModalAnalysisAtASpeed)

    @property
    def part_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5441.PartCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5441,
        )

        return self.__parent__._cast(_5441.PartCompoundModalAnalysisAtASpeed)

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
    def agma_gleason_conical_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5364.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5364,
        )

        return self.__parent__._cast(
            _5364.AGMAGleasonConicalGearCompoundModalAnalysisAtASpeed
        )

    @property
    def bevel_differential_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5371.BevelDifferentialGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5371,
        )

        return self.__parent__._cast(
            _5371.BevelDifferentialGearCompoundModalAnalysisAtASpeed
        )

    @property
    def bevel_differential_planet_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5374.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5374,
        )

        return self.__parent__._cast(
            _5374.BevelDifferentialPlanetGearCompoundModalAnalysisAtASpeed
        )

    @property
    def bevel_differential_sun_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5375.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5375,
        )

        return self.__parent__._cast(
            _5375.BevelDifferentialSunGearCompoundModalAnalysisAtASpeed
        )

    @property
    def bevel_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5376.BevelGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5376,
        )

        return self.__parent__._cast(_5376.BevelGearCompoundModalAnalysisAtASpeed)

    @property
    def hypoid_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5422.HypoidGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5422,
        )

        return self.__parent__._cast(_5422.HypoidGearCompoundModalAnalysisAtASpeed)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5426.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5426,
        )

        return self.__parent__._cast(
            _5426.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5429.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5429,
        )

        return self.__parent__._cast(
            _5429.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5432.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5432,
        )

        return self.__parent__._cast(
            _5432.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtASpeed
        )

    @property
    def spiral_bevel_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5461.SpiralBevelGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5461,
        )

        return self.__parent__._cast(_5461.SpiralBevelGearCompoundModalAnalysisAtASpeed)

    @property
    def straight_bevel_diff_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5467.StraightBevelDiffGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5467,
        )

        return self.__parent__._cast(
            _5467.StraightBevelDiffGearCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5470.StraightBevelGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5470,
        )

        return self.__parent__._cast(
            _5470.StraightBevelGearCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_planet_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5473.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5473,
        )

        return self.__parent__._cast(
            _5473.StraightBevelPlanetGearCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_sun_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5474.StraightBevelSunGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5474,
        )

        return self.__parent__._cast(
            _5474.StraightBevelSunGearCompoundModalAnalysisAtASpeed
        )

    @property
    def zerol_bevel_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5488.ZerolBevelGearCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5488,
        )

        return self.__parent__._cast(_5488.ZerolBevelGearCompoundModalAnalysisAtASpeed)

    @property
    def conical_gear_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "ConicalGearCompoundModalAnalysisAtASpeed":
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
class ConicalGearCompoundModalAnalysisAtASpeed(_5418.GearCompoundModalAnalysisAtASpeed):
    """ConicalGearCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def planetaries(self: "Self") -> "List[ConicalGearCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.ConicalGearCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Planetaries")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_5261.ConicalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConicalGearModalAnalysisAtASpeed]

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
    ) -> "List[_5261.ConicalGearModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ConicalGearModalAnalysisAtASpeed]

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
    def cast_to(self: "Self") -> "_Cast_ConicalGearCompoundModalAnalysisAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearCompoundModalAnalysisAtASpeed
        """
        return _Cast_ConicalGearCompoundModalAnalysisAtASpeed(self)
