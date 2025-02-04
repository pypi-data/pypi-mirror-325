"""ColumnInputOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private import _0
from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.implicit import list_with_selected_item
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_method_call,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.sentinels import ListWithSelectedItem_None
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.utility.file_access_helpers import _1881
from mastapy._private.utility.units_and_measurements import _1671

_COLUMN_INPUT_OPTIONS = python_net_import(
    "SMT.MastaAPI.UtilityGUI", "ColumnInputOptions"
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
        _7680,
        _7681,
        _7683,
        _7684,
        _7685,
        _7686,
        _7688,
        _7689,
        _7690,
        _7691,
        _7693,
        _7694,
    )
    from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
        _2627,
        _2628,
        _2629,
        _2632,
    )

    Self = TypeVar("Self", bound="ColumnInputOptions")
    CastSelf = TypeVar("CastSelf", bound="ColumnInputOptions._Cast_ColumnInputOptions")


__docformat__ = "restructuredtext en"
__all__ = ("ColumnInputOptions",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ColumnInputOptions:
    """Special nested class for casting ColumnInputOptions to subclasses."""

    __parent__: "ColumnInputOptions"

    @property
    def boost_pressure_input_options(
        self: "CastSelf",
    ) -> "_2627.BoostPressureInputOptions":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2627,
        )

        return self.__parent__._cast(_2627.BoostPressureInputOptions)

    @property
    def input_power_input_options(self: "CastSelf") -> "_2628.InputPowerInputOptions":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2628,
        )

        return self.__parent__._cast(_2628.InputPowerInputOptions)

    @property
    def pressure_ratio_input_options(
        self: "CastSelf",
    ) -> "_2629.PressureRatioInputOptions":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2629,
        )

        return self.__parent__._cast(_2629.PressureRatioInputOptions)

    @property
    def rotor_speed_input_options(self: "CastSelf") -> "_2632.RotorSpeedInputOptions":
        from mastapy._private.system_model.part_model.gears.supercharger_rotor_set import (
            _2632,
        )

        return self.__parent__._cast(_2632.RotorSpeedInputOptions)

    @property
    def boost_pressure_load_case_input_options(
        self: "CastSelf",
    ) -> "_7680.BoostPressureLoadCaseInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7680,
        )

        return self.__parent__._cast(_7680.BoostPressureLoadCaseInputOptions)

    @property
    def design_state_options(self: "CastSelf") -> "_7681.DesignStateOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7681,
        )

        return self.__parent__._cast(_7681.DesignStateOptions)

    @property
    def force_input_options(self: "CastSelf") -> "_7683.ForceInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7683,
        )

        return self.__parent__._cast(_7683.ForceInputOptions)

    @property
    def gear_ratio_input_options(self: "CastSelf") -> "_7684.GearRatioInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7684,
        )

        return self.__parent__._cast(_7684.GearRatioInputOptions)

    @property
    def load_case_name_options(self: "CastSelf") -> "_7685.LoadCaseNameOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7685,
        )

        return self.__parent__._cast(_7685.LoadCaseNameOptions)

    @property
    def moment_input_options(self: "CastSelf") -> "_7686.MomentInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7686,
        )

        return self.__parent__._cast(_7686.MomentInputOptions)

    @property
    def point_load_input_options(self: "CastSelf") -> "_7688.PointLoadInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7688,
        )

        return self.__parent__._cast(_7688.PointLoadInputOptions)

    @property
    def power_load_input_options(self: "CastSelf") -> "_7689.PowerLoadInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7689,
        )

        return self.__parent__._cast(_7689.PowerLoadInputOptions)

    @property
    def ramp_or_steady_state_input_options(
        self: "CastSelf",
    ) -> "_7690.RampOrSteadyStateInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7690,
        )

        return self.__parent__._cast(_7690.RampOrSteadyStateInputOptions)

    @property
    def speed_input_options(self: "CastSelf") -> "_7691.SpeedInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7691,
        )

        return self.__parent__._cast(_7691.SpeedInputOptions)

    @property
    def time_step_input_options(self: "CastSelf") -> "_7693.TimeStepInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7693,
        )

        return self.__parent__._cast(_7693.TimeStepInputOptions)

    @property
    def torque_input_options(self: "CastSelf") -> "_7694.TorqueInputOptions":
        from mastapy._private.system_model.analyses_and_results.static_loads.duty_cycle_definition import (
            _7694,
        )

        return self.__parent__._cast(_7694.TorqueInputOptions)

    @property
    def column_input_options(self: "CastSelf") -> "ColumnInputOptions":
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
class ColumnInputOptions(_0.APIBase):
    """ColumnInputOptions

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COLUMN_INPUT_OPTIONS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def column(
        self: "Self",
    ) -> "list_with_selected_item.ListWithSelectedItem_ColumnTitle":
        """ListWithSelectedItem[mastapy.utility.file_access_helpers.ColumnTitle]"""
        temp = pythonnet_property_get(self.wrapped, "Column")

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_ColumnTitle",
        )(temp)

    @column.setter
    @enforce_parameter_types
    def column(self: "Self", value: "_1881.ColumnTitle") -> None:
        wrapper_type = (
            list_with_selected_item.ListWithSelectedItem_ColumnTitle.wrapper_type()
        )
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_ColumnTitle.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        pythonnet_property_set(self.wrapped, "Column", value)

    @property
    def unit(self: "Self") -> "list_with_selected_item.ListWithSelectedItem_Unit":
        """ListWithSelectedItem[mastapy.utility.units_and_measurements.Unit]"""
        temp = pythonnet_property_get(self.wrapped, "Unit")

        if temp is None:
            return None

        selected_value = temp.SelectedValue

        if selected_value is None:
            return ListWithSelectedItem_None(temp)

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_Unit",
        )(temp)

    @unit.setter
    @enforce_parameter_types
    def unit(self: "Self", value: "_1671.Unit") -> None:
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.wrapper_type()
        enclosed_type = (
            list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        )
        value = wrapper_type[enclosed_type](
            value.wrapped if value is not None else None
        )
        pythonnet_property_set(self.wrapped, "Unit", value)

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
    def cast_to(self: "Self") -> "_Cast_ColumnInputOptions":
        """Cast to another type.

        Returns:
            _Cast_ColumnInputOptions
        """
        return _Cast_ColumnInputOptions(self)
