"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.math_utility.measured_data_scaling._1628 import (
        DataScalingOptions,
    )
    from mastapy._private.math_utility.measured_data_scaling._1629 import (
        DataScalingReferenceValues,
    )
    from mastapy._private.math_utility.measured_data_scaling._1630 import (
        DataScalingReferenceValuesBase,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.math_utility.measured_data_scaling._1628": ["DataScalingOptions"],
        "_private.math_utility.measured_data_scaling._1629": [
            "DataScalingReferenceValues"
        ],
        "_private.math_utility.measured_data_scaling._1630": [
            "DataScalingReferenceValuesBase"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "DataScalingOptions",
    "DataScalingReferenceValues",
    "DataScalingReferenceValuesBase",
)
