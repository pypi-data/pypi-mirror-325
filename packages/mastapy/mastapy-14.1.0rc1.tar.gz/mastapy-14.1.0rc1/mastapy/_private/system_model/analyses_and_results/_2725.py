"""Context"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private import _0
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_method_call,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.type_enforcement import enforce_parameter_types

_CONTEXT = python_net_import("SMT.MastaAPI.SystemModel.AnalysesAndResults", "Context")

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model import _2266
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7215,
        _7217,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _6947,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7696,
        _7698,
        _7705,
        _7711,
        _7712,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6718,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
        _6460,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5855,
        _5884,
        _5888,
        _5893,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6197,
        _6215,
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5583
    from mastapy._private.system_model.analyses_and_results.modal_analyses import (
        _4728,
        _4759,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5307,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _5016,
        _5044,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4488,
        _4489,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import _4219
    from mastapy._private.system_model.analyses_and_results.stability_analyses import (
        _3907,
        _3963,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7492,
        _7493,
        _7499,
        _7662,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3114,
        _3170,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3698,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3435,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2902,
        _2909,
    )
    from mastapy._private.utility import _1643

    Self = TypeVar("Self", bound="Context")
    CastSelf = TypeVar("CastSelf", bound="Context._Cast_Context")


__docformat__ = "restructuredtext en"
__all__ = ("Context",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Context:
    """Special nested class for casting Context to subclasses."""

    __parent__: "Context"

    @property
    def system_deflection(self: "CastSelf") -> "_2902.SystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2902,
        )

        return self.__parent__._cast(_2902.SystemDeflection)

    @property
    def torsional_system_deflection(
        self: "CastSelf",
    ) -> "_2909.TorsionalSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2909,
        )

        return self.__parent__._cast(_2909.TorsionalSystemDeflection)

    @property
    def dynamic_model_for_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3114.DynamicModelForSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3114,
        )

        return self.__parent__._cast(
            _3114.DynamicModelForSteadyStateSynchronousResponse
        )

    @property
    def steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3170.SteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3170,
        )

        return self.__parent__._cast(_3170.SteadyStateSynchronousResponse)

    @property
    def steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3435.SteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3435,
        )

        return self.__parent__._cast(_3435.SteadyStateSynchronousResponseOnAShaft)

    @property
    def steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3698.SteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3698,
        )

        return self.__parent__._cast(_3698.SteadyStateSynchronousResponseAtASpeed)

    @property
    def dynamic_model_for_stability_analysis(
        self: "CastSelf",
    ) -> "_3907.DynamicModelForStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3907,
        )

        return self.__parent__._cast(_3907.DynamicModelForStabilityAnalysis)

    @property
    def stability_analysis(self: "CastSelf") -> "_3963.StabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3963,
        )

        return self.__parent__._cast(_3963.StabilityAnalysis)

    @property
    def power_flow(self: "CastSelf") -> "_4219.PowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4219

        return self.__parent__._cast(_4219.PowerFlow)

    @property
    def parametric_study_static_load(
        self: "CastSelf",
    ) -> "_4488.ParametricStudyStaticLoad":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4488,
        )

        return self.__parent__._cast(_4488.ParametricStudyStaticLoad)

    @property
    def parametric_study_tool(self: "CastSelf") -> "_4489.ParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4489,
        )

        return self.__parent__._cast(_4489.ParametricStudyTool)

    @property
    def dynamic_model_for_modal_analysis(
        self: "CastSelf",
    ) -> "_4728.DynamicModelForModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4728,
        )

        return self.__parent__._cast(_4728.DynamicModelForModalAnalysis)

    @property
    def modal_analysis(self: "CastSelf") -> "_4759.ModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4759,
        )

        return self.__parent__._cast(_4759.ModalAnalysis)

    @property
    def dynamic_model_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5016.DynamicModelAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5016,
        )

        return self.__parent__._cast(_5016.DynamicModelAtAStiffness)

    @property
    def modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5044.ModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5044,
        )

        return self.__parent__._cast(_5044.ModalAnalysisAtAStiffness)

    @property
    def modal_analysis_at_a_speed(self: "CastSelf") -> "_5307.ModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5307,
        )

        return self.__parent__._cast(_5307.ModalAnalysisAtASpeed)

    @property
    def multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5583.MultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5583,
        )

        return self.__parent__._cast(_5583.MultibodyDynamicsAnalysis)

    @property
    def dynamic_model_for_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5855.DynamicModelForHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5855,
        )

        return self.__parent__._cast(_5855.DynamicModelForHarmonicAnalysis)

    @property
    def harmonic_analysis(self: "CastSelf") -> "_5884.HarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5884,
        )

        return self.__parent__._cast(_5884.HarmonicAnalysis)

    @property
    def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_5888.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5888,
        )

        return self.__parent__._cast(
            _5888.HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def harmonic_analysis_with_varying_stiffness_static_load_case(
        self: "CastSelf",
    ) -> "_5893.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5893,
        )

        return self.__parent__._cast(
            _5893.HarmonicAnalysisWithVaryingStiffnessStaticLoadCase
        )

    @property
    def harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6197.HarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6197,
        )

        return self.__parent__._cast(_6197.HarmonicAnalysisOfSingleExcitation)

    @property
    def modal_analysis_for_harmonic_analysis(
        self: "CastSelf",
    ) -> "_6215.ModalAnalysisForHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6215,
        )

        return self.__parent__._cast(_6215.ModalAnalysisForHarmonicAnalysis)

    @property
    def dynamic_analysis(self: "CastSelf") -> "_6460.DynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
            _6460,
        )

        return self.__parent__._cast(_6460.DynamicAnalysis)

    @property
    def critical_speed_analysis(self: "CastSelf") -> "_6718.CriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6718,
        )

        return self.__parent__._cast(_6718.CriticalSpeedAnalysis)

    @property
    def advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6947.AdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6947,
        )

        return self.__parent__._cast(_6947.AdvancedTimeSteppingAnalysisForModulation)

    @property
    def advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7215.AdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7215,
        )

        return self.__parent__._cast(_7215.AdvancedSystemDeflection)

    @property
    def advanced_system_deflection_sub_analysis(
        self: "CastSelf",
    ) -> "_7217.AdvancedSystemDeflectionSubAnalysis":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7217,
        )

        return self.__parent__._cast(_7217.AdvancedSystemDeflectionSubAnalysis)

    @property
    def load_case(self: "CastSelf") -> "_7492.LoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7492,
        )

        return self.__parent__._cast(_7492.LoadCase)

    @property
    def static_load_case(self: "CastSelf") -> "_7493.StaticLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7493,
        )

        return self.__parent__._cast(_7493.StaticLoadCase)

    @property
    def advanced_time_stepping_analysis_for_modulation_static_load_case(
        self: "CastSelf",
    ) -> "_7499.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7499,
        )

        return self.__parent__._cast(
            _7499.AdvancedTimeSteppingAnalysisForModulationStaticLoadCase
        )

    @property
    def time_series_load_case(self: "CastSelf") -> "_7662.TimeSeriesLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7662,
        )

        return self.__parent__._cast(_7662.TimeSeriesLoadCase)

    @property
    def analysis_case(self: "CastSelf") -> "_7696.AnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7696,
        )

        return self.__parent__._cast(_7696.AnalysisCase)

    @property
    def compound_analysis_case(self: "CastSelf") -> "_7698.CompoundAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7698,
        )

        return self.__parent__._cast(_7698.CompoundAnalysisCase)

    @property
    def fe_analysis(self: "CastSelf") -> "_7705.FEAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7705,
        )

        return self.__parent__._cast(_7705.FEAnalysis)

    @property
    def static_load_analysis_case(self: "CastSelf") -> "_7711.StaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7711,
        )

        return self.__parent__._cast(_7711.StaticLoadAnalysisCase)

    @property
    def time_series_load_analysis_case(
        self: "CastSelf",
    ) -> "_7712.TimeSeriesLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7712,
        )

        return self.__parent__._cast(_7712.TimeSeriesLoadAnalysisCase)

    @property
    def context(self: "CastSelf") -> "Context":
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
class Context(_0.APIBase):
    """Context

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONTEXT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def comment(self: "Self") -> "str":
        """str"""
        temp = pythonnet_property_get(self.wrapped, "Comment")

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: "Self", value: "str") -> None:
        pythonnet_property_set(
            self.wrapped, "Comment", str(value) if value is not None else ""
        )

    @property
    def name(self: "Self") -> "str":
        """str"""
        temp = pythonnet_property_get(self.wrapped, "Name")

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: "Self", value: "str") -> None:
        pythonnet_property_set(
            self.wrapped, "Name", str(value) if value is not None else ""
        )

    @property
    def save_history_information(self: "Self") -> "_1643.FileHistoryItem":
        """mastapy.utility.FileHistoryItem

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SaveHistoryInformation")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def design_properties(self: "Self") -> "_2266.Design":
        """mastapy.system_model.Design

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "DesignProperties")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: "Self") -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ReportNames")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        pythonnet_method_call(
            self.wrapped, "OutputDefaultReportTo", file_path if file_path else ""
        )

    def get_default_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = pythonnet_method_call(
            self.wrapped, "GetDefaultReportWithEncodedImages"
        )
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        pythonnet_method_call(
            self.wrapped, "OutputActiveReportTo", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_active_report_as_text_to(self: "Self", file_path: "str") -> None:
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        pythonnet_method_call(
            self.wrapped, "OutputActiveReportAsTextTo", file_path if file_path else ""
        )

    def get_active_report_with_encoded_images(self: "Self") -> "str":
        """str"""
        method_result = pythonnet_method_call(
            self.wrapped, "GetActiveReportWithEncodedImages"
        )
        return method_result

    @enforce_parameter_types
    def output_named_report_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        pythonnet_method_call(
            self.wrapped,
            "OutputNamedReportTo",
            report_name if report_name else "",
            file_path if file_path else "",
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        pythonnet_method_call(
            self.wrapped,
            "OutputNamedReportAsMastaReport",
            report_name if report_name else "",
            file_path if file_path else "",
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: "Self", report_name: "str", file_path: "str"
    ) -> None:
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        pythonnet_method_call(
            self.wrapped,
            "OutputNamedReportAsTextTo",
            report_name if report_name else "",
            file_path if file_path else "",
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: "Self", report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = pythonnet_method_call(
            self.wrapped,
            "GetNamedReportWithEncodedImages",
            report_name if report_name else "",
        )
        return method_result

    @property
    def cast_to(self: "Self") -> "_Cast_Context":
        """Cast to another type.

        Returns:
            _Cast_Context
        """
        return _Cast_Context(self)
