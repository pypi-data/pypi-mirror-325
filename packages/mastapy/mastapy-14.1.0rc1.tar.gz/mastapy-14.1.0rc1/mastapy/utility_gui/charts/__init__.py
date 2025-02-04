"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.utility_gui.charts._1916 import BubbleChartDefinition
    from mastapy._private.utility_gui.charts._1917 import ConstantLine
    from mastapy._private.utility_gui.charts._1918 import CustomLineChart
    from mastapy._private.utility_gui.charts._1919 import CustomTableAndChart
    from mastapy._private.utility_gui.charts._1920 import LegacyChartMathChartDefinition
    from mastapy._private.utility_gui.charts._1921 import MatrixVisualisationDefinition
    from mastapy._private.utility_gui.charts._1922 import ModeConstantLine
    from mastapy._private.utility_gui.charts._1923 import NDChartDefinition
    from mastapy._private.utility_gui.charts._1924 import (
        ParallelCoordinatesChartDefinition,
    )
    from mastapy._private.utility_gui.charts._1925 import PointsForSurface
    from mastapy._private.utility_gui.charts._1926 import ScatterChartDefinition
    from mastapy._private.utility_gui.charts._1927 import Series2D
    from mastapy._private.utility_gui.charts._1928 import SMTAxis
    from mastapy._private.utility_gui.charts._1929 import ThreeDChartDefinition
    from mastapy._private.utility_gui.charts._1930 import ThreeDVectorChartDefinition
    from mastapy._private.utility_gui.charts._1931 import TwoDChartDefinition
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.utility_gui.charts._1916": ["BubbleChartDefinition"],
        "_private.utility_gui.charts._1917": ["ConstantLine"],
        "_private.utility_gui.charts._1918": ["CustomLineChart"],
        "_private.utility_gui.charts._1919": ["CustomTableAndChart"],
        "_private.utility_gui.charts._1920": ["LegacyChartMathChartDefinition"],
        "_private.utility_gui.charts._1921": ["MatrixVisualisationDefinition"],
        "_private.utility_gui.charts._1922": ["ModeConstantLine"],
        "_private.utility_gui.charts._1923": ["NDChartDefinition"],
        "_private.utility_gui.charts._1924": ["ParallelCoordinatesChartDefinition"],
        "_private.utility_gui.charts._1925": ["PointsForSurface"],
        "_private.utility_gui.charts._1926": ["ScatterChartDefinition"],
        "_private.utility_gui.charts._1927": ["Series2D"],
        "_private.utility_gui.charts._1928": ["SMTAxis"],
        "_private.utility_gui.charts._1929": ["ThreeDChartDefinition"],
        "_private.utility_gui.charts._1930": ["ThreeDVectorChartDefinition"],
        "_private.utility_gui.charts._1931": ["TwoDChartDefinition"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "BubbleChartDefinition",
    "ConstantLine",
    "CustomLineChart",
    "CustomTableAndChart",
    "LegacyChartMathChartDefinition",
    "MatrixVisualisationDefinition",
    "ModeConstantLine",
    "NDChartDefinition",
    "ParallelCoordinatesChartDefinition",
    "PointsForSurface",
    "ScatterChartDefinition",
    "Series2D",
    "SMTAxis",
    "ThreeDChartDefinition",
    "ThreeDVectorChartDefinition",
    "TwoDChartDefinition",
)
