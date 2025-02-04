"""CustomReportDefinitionItem"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.utility.report import _1833

_CUSTOM_REPORT_DEFINITION_ITEM = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportDefinitionItem"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_results import _2012
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4487,
    )
    from mastapy._private.utility.report import (
        _1804,
        _1812,
        _1813,
        _1814,
        _1815,
        _1824,
        _1825,
        _1836,
        _1839,
        _1841,
    )

    Self = TypeVar("Self", bound="CustomReportDefinitionItem")
    CastSelf = TypeVar(
        "CastSelf", bound="CustomReportDefinitionItem._Cast_CustomReportDefinitionItem"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportDefinitionItem",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CustomReportDefinitionItem:
    """Special nested class for casting CustomReportDefinitionItem to subclasses."""

    __parent__: "CustomReportDefinitionItem"

    @property
    def custom_report_nameable_item(
        self: "CastSelf",
    ) -> "_1833.CustomReportNameableItem":
        return self.__parent__._cast(_1833.CustomReportNameableItem)

    @property
    def custom_report_item(self: "CastSelf") -> "_1825.CustomReportItem":
        from mastapy._private.utility.report import _1825

        return self.__parent__._cast(_1825.CustomReportItem)

    @property
    def ad_hoc_custom_table(self: "CastSelf") -> "_1804.AdHocCustomTable":
        from mastapy._private.utility.report import _1804

        return self.__parent__._cast(_1804.AdHocCustomTable)

    @property
    def custom_chart(self: "CastSelf") -> "_1812.CustomChart":
        from mastapy._private.utility.report import _1812

        return self.__parent__._cast(_1812.CustomChart)

    @property
    def custom_drawing(self: "CastSelf") -> "_1813.CustomDrawing":
        from mastapy._private.utility.report import _1813

        return self.__parent__._cast(_1813.CustomDrawing)

    @property
    def custom_graphic(self: "CastSelf") -> "_1814.CustomGraphic":
        from mastapy._private.utility.report import _1814

        return self.__parent__._cast(_1814.CustomGraphic)

    @property
    def custom_image(self: "CastSelf") -> "_1815.CustomImage":
        from mastapy._private.utility.report import _1815

        return self.__parent__._cast(_1815.CustomImage)

    @property
    def custom_report_html_item(self: "CastSelf") -> "_1824.CustomReportHtmlItem":
        from mastapy._private.utility.report import _1824

        return self.__parent__._cast(_1824.CustomReportHtmlItem)

    @property
    def custom_report_status_item(self: "CastSelf") -> "_1836.CustomReportStatusItem":
        from mastapy._private.utility.report import _1836

        return self.__parent__._cast(_1836.CustomReportStatusItem)

    @property
    def custom_report_text(self: "CastSelf") -> "_1839.CustomReportText":
        from mastapy._private.utility.report import _1839

        return self.__parent__._cast(_1839.CustomReportText)

    @property
    def custom_sub_report(self: "CastSelf") -> "_1841.CustomSubReport":
        from mastapy._private.utility.report import _1841

        return self.__parent__._cast(_1841.CustomSubReport)

    @property
    def loaded_bearing_chart_reporter(
        self: "CastSelf",
    ) -> "_2012.LoadedBearingChartReporter":
        from mastapy._private.bearings.bearing_results import _2012

        return self.__parent__._cast(_2012.LoadedBearingChartReporter)

    @property
    def parametric_study_histogram(
        self: "CastSelf",
    ) -> "_4487.ParametricStudyHistogram":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4487,
        )

        return self.__parent__._cast(_4487.ParametricStudyHistogram)

    @property
    def custom_report_definition_item(self: "CastSelf") -> "CustomReportDefinitionItem":
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
class CustomReportDefinitionItem(_1833.CustomReportNameableItem):
    """CustomReportDefinitionItem

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CUSTOM_REPORT_DEFINITION_ITEM

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CustomReportDefinitionItem":
        """Cast to another type.

        Returns:
            _Cast_CustomReportDefinitionItem
        """
        return _Cast_CustomReportDefinitionItem(self)
