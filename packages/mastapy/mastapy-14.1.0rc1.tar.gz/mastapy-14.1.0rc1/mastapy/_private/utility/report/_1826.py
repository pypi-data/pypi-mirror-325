"""CustomReportItemContainer"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.utility.report import _1825

_CUSTOM_REPORT_ITEM_CONTAINER = python_net_import(
    "SMT.MastaAPI.Utility.Report", "CustomReportItemContainer"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.utility.report import _1816, _1820, _1829, _1837

    Self = TypeVar("Self", bound="CustomReportItemContainer")
    CastSelf = TypeVar(
        "CastSelf", bound="CustomReportItemContainer._Cast_CustomReportItemContainer"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CustomReportItemContainer",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CustomReportItemContainer:
    """Special nested class for casting CustomReportItemContainer to subclasses."""

    __parent__: "CustomReportItemContainer"

    @property
    def custom_report_item(self: "CastSelf") -> "_1825.CustomReportItem":
        return self.__parent__._cast(_1825.CustomReportItem)

    @property
    def custom_report(self: "CastSelf") -> "_1816.CustomReport":
        from mastapy._private.utility.report import _1816

        return self.__parent__._cast(_1816.CustomReport)

    @property
    def custom_report_column(self: "CastSelf") -> "_1820.CustomReportColumn":
        from mastapy._private.utility.report import _1820

        return self.__parent__._cast(_1820.CustomReportColumn)

    @property
    def custom_report_item_container_collection_item(
        self: "CastSelf",
    ) -> "_1829.CustomReportItemContainerCollectionItem":
        from mastapy._private.utility.report import _1829

        return self.__parent__._cast(_1829.CustomReportItemContainerCollectionItem)

    @property
    def custom_report_tab(self: "CastSelf") -> "_1837.CustomReportTab":
        from mastapy._private.utility.report import _1837

        return self.__parent__._cast(_1837.CustomReportTab)

    @property
    def custom_report_item_container(self: "CastSelf") -> "CustomReportItemContainer":
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
class CustomReportItemContainer(_1825.CustomReportItem):
    """CustomReportItemContainer

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CUSTOM_REPORT_ITEM_CONTAINER

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CustomReportItemContainer":
        """Cast to another type.

        Returns:
            _Cast_CustomReportItemContainer
        """
        return _Cast_CustomReportItemContainer(self)
