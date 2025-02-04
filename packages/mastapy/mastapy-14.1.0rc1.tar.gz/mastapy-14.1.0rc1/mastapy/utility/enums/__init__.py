"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.utility.enums._1883 import BearingForceArrowOption
    from mastapy._private.utility.enums._1884 import TableAndChartOptions
    from mastapy._private.utility.enums._1885 import ThreeDViewContourOption
    from mastapy._private.utility.enums._1886 import (
        ThreeDViewContourOptionFirstSelection,
    )
    from mastapy._private.utility.enums._1887 import (
        ThreeDViewContourOptionSecondSelection,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.utility.enums._1883": ["BearingForceArrowOption"],
        "_private.utility.enums._1884": ["TableAndChartOptions"],
        "_private.utility.enums._1885": ["ThreeDViewContourOption"],
        "_private.utility.enums._1886": ["ThreeDViewContourOptionFirstSelection"],
        "_private.utility.enums._1887": ["ThreeDViewContourOptionSecondSelection"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BearingForceArrowOption",
    "TableAndChartOptions",
    "ThreeDViewContourOption",
    "ThreeDViewContourOptionFirstSelection",
    "ThreeDViewContourOptionSecondSelection",
)
