"""StraightBevelDiffGearCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
    _4849,
)

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "StraightBevelDiffGearCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses import _4795
    from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
        _4837,
        _4858,
        _4865,
        _4891,
        _4912,
        _4914,
        _4946,
        _4947,
    )
    from mastapy._private.system_model.part_model.gears import _2617

    Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundModalAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="StraightBevelDiffGearCompoundModalAnalysis._Cast_StraightBevelDiffGearCompoundModalAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundModalAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_StraightBevelDiffGearCompoundModalAnalysis:
    """Special nested class for casting StraightBevelDiffGearCompoundModalAnalysis to subclasses."""

    __parent__: "StraightBevelDiffGearCompoundModalAnalysis"

    @property
    def bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4849.BevelGearCompoundModalAnalysis":
        return self.__parent__._cast(_4849.BevelGearCompoundModalAnalysis)

    @property
    def agma_gleason_conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4837.AGMAGleasonConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4837,
        )

        return self.__parent__._cast(_4837.AGMAGleasonConicalGearCompoundModalAnalysis)

    @property
    def conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4865.ConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4865,
        )

        return self.__parent__._cast(_4865.ConicalGearCompoundModalAnalysis)

    @property
    def gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4891.GearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4891,
        )

        return self.__parent__._cast(_4891.GearCompoundModalAnalysis)

    @property
    def mountable_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4912.MountableComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4912,
        )

        return self.__parent__._cast(_4912.MountableComponentCompoundModalAnalysis)

    @property
    def component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4858.ComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4858,
        )

        return self.__parent__._cast(_4858.ComponentCompoundModalAnalysis)

    @property
    def part_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4914.PartCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4914,
        )

        return self.__parent__._cast(_4914.PartCompoundModalAnalysis)

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
    def straight_bevel_planet_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4946.StraightBevelPlanetGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4946,
        )

        return self.__parent__._cast(_4946.StraightBevelPlanetGearCompoundModalAnalysis)

    @property
    def straight_bevel_sun_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4947.StraightBevelSunGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4947,
        )

        return self.__parent__._cast(_4947.StraightBevelSunGearCompoundModalAnalysis)

    @property
    def straight_bevel_diff_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "StraightBevelDiffGearCompoundModalAnalysis":
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
class StraightBevelDiffGearCompoundModalAnalysis(_4849.BevelGearCompoundModalAnalysis):
    """StraightBevelDiffGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_MODAL_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2617.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_4795.StraightBevelDiffGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis]

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
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_4795.StraightBevelDiffGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearModalAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_StraightBevelDiffGearCompoundModalAnalysis":
        """Cast to another type.

        Returns:
            _Cast_StraightBevelDiffGearCompoundModalAnalysis
        """
        return _Cast_StraightBevelDiffGearCompoundModalAnalysis(self)
