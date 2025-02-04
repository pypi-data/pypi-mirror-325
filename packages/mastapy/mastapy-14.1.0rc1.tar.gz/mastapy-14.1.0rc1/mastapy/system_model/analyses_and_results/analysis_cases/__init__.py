"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7696 import (
        AnalysisCase,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7697 import (
        AbstractAnalysisOptions,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7698 import (
        CompoundAnalysisCase,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7699 import (
        ConnectionAnalysisCase,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7700 import (
        ConnectionCompoundAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7701 import (
        ConnectionFEAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7702 import (
        ConnectionStaticLoadAnalysisCase,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7703 import (
        ConnectionTimeSeriesLoadAnalysisCase,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7704 import (
        DesignEntityCompoundAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7705 import (
        FEAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7706 import (
        PartAnalysisCase,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7707 import (
        PartCompoundAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7708 import (
        PartFEAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7709 import (
        PartStaticLoadAnalysisCase,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7710 import (
        PartTimeSeriesLoadAnalysisCase,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7711 import (
        StaticLoadAnalysisCase,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases._7712 import (
        TimeSeriesLoadAnalysisCase,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.analyses_and_results.analysis_cases._7696": [
            "AnalysisCase"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7697": [
            "AbstractAnalysisOptions"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7698": [
            "CompoundAnalysisCase"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7699": [
            "ConnectionAnalysisCase"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7700": [
            "ConnectionCompoundAnalysis"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7701": [
            "ConnectionFEAnalysis"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7702": [
            "ConnectionStaticLoadAnalysisCase"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7703": [
            "ConnectionTimeSeriesLoadAnalysisCase"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7704": [
            "DesignEntityCompoundAnalysis"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7705": [
            "FEAnalysis"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7706": [
            "PartAnalysisCase"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7707": [
            "PartCompoundAnalysis"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7708": [
            "PartFEAnalysis"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7709": [
            "PartStaticLoadAnalysisCase"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7710": [
            "PartTimeSeriesLoadAnalysisCase"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7711": [
            "StaticLoadAnalysisCase"
        ],
        "_private.system_model.analyses_and_results.analysis_cases._7712": [
            "TimeSeriesLoadAnalysisCase"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AnalysisCase",
    "AbstractAnalysisOptions",
    "CompoundAnalysisCase",
    "ConnectionAnalysisCase",
    "ConnectionCompoundAnalysis",
    "ConnectionFEAnalysis",
    "ConnectionStaticLoadAnalysisCase",
    "ConnectionTimeSeriesLoadAnalysisCase",
    "DesignEntityCompoundAnalysis",
    "FEAnalysis",
    "PartAnalysisCase",
    "PartCompoundAnalysis",
    "PartFEAnalysis",
    "PartStaticLoadAnalysisCase",
    "PartTimeSeriesLoadAnalysisCase",
    "StaticLoadAnalysisCase",
    "TimeSeriesLoadAnalysisCase",
)
