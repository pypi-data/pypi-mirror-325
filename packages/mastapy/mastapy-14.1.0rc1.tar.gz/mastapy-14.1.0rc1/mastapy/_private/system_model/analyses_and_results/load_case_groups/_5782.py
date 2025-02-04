"""AbstractStaticLoadCaseGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

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
from mastapy._private.system_model.analyses_and_results.load_case_groups import _5781
from mastapy._private.system_model.analyses_and_results.static_loads import (
    _7507,
    _7549,
    _7551,
    _7553,
    _7575,
    _7578,
    _7580,
    _7583,
    _7628,
    _7629,
)
from mastapy._private.system_model.connections_and_sockets.gears import _2375, _2379
from mastapy._private.system_model.part_model import _2506, _2520, _2540, _2541
from mastapy._private.system_model.part_model.gears import _2597, _2598, _2602, _2604

_ABSTRACT_STATIC_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "AbstractStaticLoadCaseGroup",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import (
        _2722,
        _2733,
        _2735,
        _2736,
        _2743,
        _2746,
        _2751,
        _2752,
        _2753,
        _2756,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups import (
        _5780,
        _5785,
        _5786,
        _5789,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import (
        _5795,
        _5798,
        _5799,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7493,
        _7505,
    )

    Self = TypeVar("Self", bound="AbstractStaticLoadCaseGroup")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractStaticLoadCaseGroup._Cast_AbstractStaticLoadCaseGroup",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractStaticLoadCaseGroup",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractStaticLoadCaseGroup:
    """Special nested class for casting AbstractStaticLoadCaseGroup to subclasses."""

    __parent__: "AbstractStaticLoadCaseGroup"

    @property
    def abstract_load_case_group(self: "CastSelf") -> "_5781.AbstractLoadCaseGroup":
        return self.__parent__._cast(_5781.AbstractLoadCaseGroup)

    @property
    def abstract_design_state_load_case_group(
        self: "CastSelf",
    ) -> "_5780.AbstractDesignStateLoadCaseGroup":
        return self.__parent__._cast(_5780.AbstractDesignStateLoadCaseGroup)

    @property
    def design_state(self: "CastSelf") -> "_5785.DesignState":
        from mastapy._private.system_model.analyses_and_results.load_case_groups import (
            _5785,
        )

        return self.__parent__._cast(_5785.DesignState)

    @property
    def duty_cycle(self: "CastSelf") -> "_5786.DutyCycle":
        from mastapy._private.system_model.analyses_and_results.load_case_groups import (
            _5786,
        )

        return self.__parent__._cast(_5786.DutyCycle)

    @property
    def sub_group_in_single_design_state(
        self: "CastSelf",
    ) -> "_5789.SubGroupInSingleDesignState":
        from mastapy._private.system_model.analyses_and_results.load_case_groups import (
            _5789,
        )

        return self.__parent__._cast(_5789.SubGroupInSingleDesignState)

    @property
    def abstract_static_load_case_group(
        self: "CastSelf",
    ) -> "AbstractStaticLoadCaseGroup":
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
class AbstractStaticLoadCaseGroup(_5781.AbstractLoadCaseGroup):
    """AbstractStaticLoadCaseGroup

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_STATIC_LOAD_CASE_GROUP

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def max_number_of_load_cases_to_display(self: "Self") -> "int":
        """int"""
        temp = pythonnet_property_get(self.wrapped, "MaxNumberOfLoadCasesToDisplay")

        if temp is None:
            return 0

        return temp

    @max_number_of_load_cases_to_display.setter
    @enforce_parameter_types
    def max_number_of_load_cases_to_display(self: "Self", value: "int") -> None:
        pythonnet_property_set(
            self.wrapped,
            "MaxNumberOfLoadCasesToDisplay",
            int(value) if value is not None else 0,
        )

    @property
    def bearings(
        self: "Self",
    ) -> (
        "List[_5795.ComponentStaticLoadCaseGroup[_2506.Bearing, _7507.BearingLoadCase]]"
    ):
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy.system_model.part_model.Bearing, mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase]]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Bearings")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_sets(
        self: "Self",
    ) -> "List[_5798.GearSetStaticLoadCaseGroup[_2598.CylindricalGearSet, _2597.CylindricalGear, _7549.CylindricalGearLoadCase, _2375.CylindricalGearMesh, _7551.CylindricalGearMeshLoadCase, _7553.CylindricalGearSetLoadCase]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.GearSetStaticLoadCaseGroup[mastapy.system_model.part_model.gears.CylindricalGearSet, mastapy.system_model.part_model.gears.CylindricalGear, mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase, mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh, mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase, mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase]]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CylindricalGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def design_states(self: "Self") -> "List[_5780.AbstractDesignStateLoadCaseGroup]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.AbstractDesignStateLoadCaseGroup]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "DesignStates")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def fe_parts(
        self: "Self",
    ) -> "List[_5795.ComponentStaticLoadCaseGroup[_2520.FEPart, _7575.FEPartLoadCase]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy.system_model.part_model.FEPart, mastapy.system_model.analyses_and_results.static_loads.FEPartLoadCase]]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "FEParts")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_sets(
        self: "Self",
    ) -> "List[_5798.GearSetStaticLoadCaseGroup[_2604.GearSet, _2602.Gear, _7578.GearLoadCase, _2379.GearMesh, _7580.GearMeshLoadCase, _7583.GearSetLoadCase]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.GearSetStaticLoadCaseGroup[mastapy.system_model.part_model.gears.GearSet, mastapy.system_model.part_model.gears.Gear, mastapy.system_model.analyses_and_results.static_loads.GearLoadCase, mastapy.system_model.connections_and_sockets.gears.GearMesh, mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase, mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase]]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "GearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def parts_with_excitations(self: "Self") -> "List[_5799.PartStaticLoadCaseGroup]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.PartStaticLoadCaseGroup]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "PartsWithExcitations")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def point_loads(
        self: "Self",
    ) -> "List[_5795.ComponentStaticLoadCaseGroup[_2540.PointLoad, _7628.PointLoadLoadCase]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy.system_model.part_model.PointLoad, mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase]]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "PointLoads")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_loads(
        self: "Self",
    ) -> "List[_5795.ComponentStaticLoadCaseGroup[_2541.PowerLoad, _7629.PowerLoadLoadCase]]":
        """List[mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups.ComponentStaticLoadCaseGroup[mastapy.system_model.part_model.PowerLoad, mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase]]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "PowerLoads")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def static_loads(self: "Self") -> "List[_7493.StaticLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "StaticLoads")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def static_loads_limited_by_max_number_of_load_cases_to_display(
        self: "Self",
    ) -> "List[_7493.StaticLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "StaticLoadsLimitedByMaxNumberOfLoadCasesToDisplay"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def compound_system_deflection(self: "Self") -> "_2756.CompoundSystemDeflection":
        """mastapy.system_model.analyses_and_results.CompoundSystemDeflection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CompoundSystemDeflection")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_power_flow(self: "Self") -> "_2751.CompoundPowerFlow":
        """mastapy.system_model.analyses_and_results.CompoundPowerFlow

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CompoundPowerFlow")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_advanced_system_deflection(
        self: "Self",
    ) -> "_2733.CompoundAdvancedSystemDeflection":
        """mastapy.system_model.analyses_and_results.CompoundAdvancedSystemDeflection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CompoundAdvancedSystemDeflection")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_harmonic_analysis(self: "Self") -> "_2743.CompoundHarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundHarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CompoundHarmonicAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_steady_state_synchronous_response(
        self: "Self",
    ) -> "_2753.CompoundSteadyStateSynchronousResponse":
        """mastapy.system_model.analyses_and_results.CompoundSteadyStateSynchronousResponse

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "CompoundSteadyStateSynchronousResponse"
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_modal_analysis(self: "Self") -> "_2746.CompoundModalAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundModalAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CompoundModalAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_critical_speed_analysis(
        self: "Self",
    ) -> "_2736.CompoundCriticalSpeedAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundCriticalSpeedAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CompoundCriticalSpeedAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_stability_analysis(self: "Self") -> "_2752.CompoundStabilityAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundStabilityAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CompoundStabilityAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def compound_advanced_time_stepping_analysis_for_modulation(
        self: "Self",
    ) -> "_2735.CompoundAdvancedTimeSteppingAnalysisForModulation":
        """mastapy.system_model.analyses_and_results.CompoundAdvancedTimeSteppingAnalysisForModulation

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "CompoundAdvancedTimeSteppingAnalysisForModulation"
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def clear_user_specified_excitation_data_for_all_load_cases(self: "Self") -> None:
        """Method does not return."""
        pythonnet_method_call(
            self.wrapped, "ClearUserSpecifiedExcitationDataForAllLoadCases"
        )

    def run_power_flow(self: "Self") -> None:
        """Method does not return."""
        pythonnet_method_call(self.wrapped, "RunPowerFlow")

    def set_face_widths_for_specified_safety_factors_from_power_flow(
        self: "Self",
    ) -> None:
        """Method does not return."""
        pythonnet_method_call(
            self.wrapped, "SetFaceWidthsForSpecifiedSafetyFactorsFromPowerFlow"
        )

    @enforce_parameter_types
    def analysis_of(
        self: "Self", analysis_type: "_7505.AnalysisType"
    ) -> "_2722.CompoundAnalysis":
        """mastapy.system_model.analyses_and_results.CompoundAnalysis

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)
        """
        analysis_type = conversion.mp_to_pn_enum(
            analysis_type,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.AnalysisType",
        )
        method_result = pythonnet_method_call(self.wrapped, "AnalysisOf", analysis_type)
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractStaticLoadCaseGroup":
        """Cast to another type.

        Returns:
            _Cast_AbstractStaticLoadCaseGroup
        """
        return _Cast_AbstractStaticLoadCaseGroup(self)
