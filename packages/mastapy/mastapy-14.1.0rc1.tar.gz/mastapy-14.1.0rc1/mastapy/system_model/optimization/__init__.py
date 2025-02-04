"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.optimization._2292 import (
        ConicalGearOptimisationStrategy,
    )
    from mastapy._private.system_model.optimization._2293 import (
        ConicalGearOptimizationStep,
    )
    from mastapy._private.system_model.optimization._2294 import (
        ConicalGearOptimizationStrategyDatabase,
    )
    from mastapy._private.system_model.optimization._2295 import (
        CylindricalGearOptimisationStrategy,
    )
    from mastapy._private.system_model.optimization._2296 import (
        CylindricalGearOptimizationStep,
    )
    from mastapy._private.system_model.optimization._2297 import (
        MeasuredAndFactorViewModel,
    )
    from mastapy._private.system_model.optimization._2298 import (
        MicroGeometryOptimisationTarget,
    )
    from mastapy._private.system_model.optimization._2299 import OptimizationStep
    from mastapy._private.system_model.optimization._2300 import OptimizationStrategy
    from mastapy._private.system_model.optimization._2301 import (
        OptimizationStrategyBase,
    )
    from mastapy._private.system_model.optimization._2302 import (
        OptimizationStrategyDatabase,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.optimization._2292": ["ConicalGearOptimisationStrategy"],
        "_private.system_model.optimization._2293": ["ConicalGearOptimizationStep"],
        "_private.system_model.optimization._2294": [
            "ConicalGearOptimizationStrategyDatabase"
        ],
        "_private.system_model.optimization._2295": [
            "CylindricalGearOptimisationStrategy"
        ],
        "_private.system_model.optimization._2296": ["CylindricalGearOptimizationStep"],
        "_private.system_model.optimization._2297": ["MeasuredAndFactorViewModel"],
        "_private.system_model.optimization._2298": ["MicroGeometryOptimisationTarget"],
        "_private.system_model.optimization._2299": ["OptimizationStep"],
        "_private.system_model.optimization._2300": ["OptimizationStrategy"],
        "_private.system_model.optimization._2301": ["OptimizationStrategyBase"],
        "_private.system_model.optimization._2302": ["OptimizationStrategyDatabase"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ConicalGearOptimisationStrategy",
    "ConicalGearOptimizationStep",
    "ConicalGearOptimizationStrategyDatabase",
    "CylindricalGearOptimisationStrategy",
    "CylindricalGearOptimizationStep",
    "MeasuredAndFactorViewModel",
    "MicroGeometryOptimisationTarget",
    "OptimizationStep",
    "OptimizationStrategy",
    "OptimizationStrategyBase",
    "OptimizationStrategyDatabase",
)
