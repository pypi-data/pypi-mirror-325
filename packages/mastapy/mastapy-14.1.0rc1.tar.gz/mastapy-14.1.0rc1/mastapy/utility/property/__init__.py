"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.utility.property._1900 import DeletableCollectionMember
    from mastapy._private.utility.property._1901 import DutyCyclePropertySummary
    from mastapy._private.utility.property._1902 import DutyCyclePropertySummaryForce
    from mastapy._private.utility.property._1903 import (
        DutyCyclePropertySummaryPercentage,
    )
    from mastapy._private.utility.property._1904 import (
        DutyCyclePropertySummarySmallAngle,
    )
    from mastapy._private.utility.property._1905 import DutyCyclePropertySummaryStress
    from mastapy._private.utility.property._1906 import (
        DutyCyclePropertySummaryVeryShortLength,
    )
    from mastapy._private.utility.property._1907 import EnumWithBoolean
    from mastapy._private.utility.property._1908 import (
        NamedRangeWithOverridableMinAndMax,
    )
    from mastapy._private.utility.property._1909 import TypedObjectsWithOption
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.utility.property._1900": ["DeletableCollectionMember"],
        "_private.utility.property._1901": ["DutyCyclePropertySummary"],
        "_private.utility.property._1902": ["DutyCyclePropertySummaryForce"],
        "_private.utility.property._1903": ["DutyCyclePropertySummaryPercentage"],
        "_private.utility.property._1904": ["DutyCyclePropertySummarySmallAngle"],
        "_private.utility.property._1905": ["DutyCyclePropertySummaryStress"],
        "_private.utility.property._1906": ["DutyCyclePropertySummaryVeryShortLength"],
        "_private.utility.property._1907": ["EnumWithBoolean"],
        "_private.utility.property._1908": ["NamedRangeWithOverridableMinAndMax"],
        "_private.utility.property._1909": ["TypedObjectsWithOption"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "DeletableCollectionMember",
    "DutyCyclePropertySummary",
    "DutyCyclePropertySummaryForce",
    "DutyCyclePropertySummaryPercentage",
    "DutyCyclePropertySummarySmallAngle",
    "DutyCyclePropertySummaryStress",
    "DutyCyclePropertySummaryVeryShortLength",
    "EnumWithBoolean",
    "NamedRangeWithOverridableMinAndMax",
    "TypedObjectsWithOption",
)
