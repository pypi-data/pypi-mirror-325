"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.analyses_and_results._2722 import (
        CompoundAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2723 import (
        AnalysisCaseVariable,
    )
    from mastapy._private.system_model.analyses_and_results._2724 import (
        ConnectionAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2725 import Context
    from mastapy._private.system_model.analyses_and_results._2726 import (
        DesignEntityAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2727 import (
        DesignEntityGroupAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2728 import (
        DesignEntitySingleContextAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2732 import PartAnalysis
    from mastapy._private.system_model.analyses_and_results._2733 import (
        CompoundAdvancedSystemDeflection,
    )
    from mastapy._private.system_model.analyses_and_results._2734 import (
        CompoundAdvancedSystemDeflectionSubAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2735 import (
        CompoundAdvancedTimeSteppingAnalysisForModulation,
    )
    from mastapy._private.system_model.analyses_and_results._2736 import (
        CompoundCriticalSpeedAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2737 import (
        CompoundDynamicAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2738 import (
        CompoundDynamicModelAtAStiffness,
    )
    from mastapy._private.system_model.analyses_and_results._2739 import (
        CompoundDynamicModelForHarmonicAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2740 import (
        CompoundDynamicModelForModalAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2741 import (
        CompoundDynamicModelForStabilityAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2742 import (
        CompoundDynamicModelForSteadyStateSynchronousResponse,
    )
    from mastapy._private.system_model.analyses_and_results._2743 import (
        CompoundHarmonicAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2744 import (
        CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation,
    )
    from mastapy._private.system_model.analyses_and_results._2745 import (
        CompoundHarmonicAnalysisOfSingleExcitation,
    )
    from mastapy._private.system_model.analyses_and_results._2746 import (
        CompoundModalAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2747 import (
        CompoundModalAnalysisAtASpeed,
    )
    from mastapy._private.system_model.analyses_and_results._2748 import (
        CompoundModalAnalysisAtAStiffness,
    )
    from mastapy._private.system_model.analyses_and_results._2749 import (
        CompoundModalAnalysisForHarmonicAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2750 import (
        CompoundMultibodyDynamicsAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2751 import (
        CompoundPowerFlow,
    )
    from mastapy._private.system_model.analyses_and_results._2752 import (
        CompoundStabilityAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results._2753 import (
        CompoundSteadyStateSynchronousResponse,
    )
    from mastapy._private.system_model.analyses_and_results._2754 import (
        CompoundSteadyStateSynchronousResponseAtASpeed,
    )
    from mastapy._private.system_model.analyses_and_results._2755 import (
        CompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from mastapy._private.system_model.analyses_and_results._2756 import (
        CompoundSystemDeflection,
    )
    from mastapy._private.system_model.analyses_and_results._2757 import (
        CompoundTorsionalSystemDeflection,
    )
    from mastapy._private.system_model.analyses_and_results._2758 import (
        TESetUpForDynamicAnalysisOptions,
    )
    from mastapy._private.system_model.analyses_and_results._2759 import TimeOptions
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.analyses_and_results._2722": ["CompoundAnalysis"],
        "_private.system_model.analyses_and_results._2723": ["AnalysisCaseVariable"],
        "_private.system_model.analyses_and_results._2724": ["ConnectionAnalysis"],
        "_private.system_model.analyses_and_results._2725": ["Context"],
        "_private.system_model.analyses_and_results._2726": ["DesignEntityAnalysis"],
        "_private.system_model.analyses_and_results._2727": [
            "DesignEntityGroupAnalysis"
        ],
        "_private.system_model.analyses_and_results._2728": [
            "DesignEntitySingleContextAnalysis"
        ],
        "_private.system_model.analyses_and_results._2732": ["PartAnalysis"],
        "_private.system_model.analyses_and_results._2733": [
            "CompoundAdvancedSystemDeflection"
        ],
        "_private.system_model.analyses_and_results._2734": [
            "CompoundAdvancedSystemDeflectionSubAnalysis"
        ],
        "_private.system_model.analyses_and_results._2735": [
            "CompoundAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_private.system_model.analyses_and_results._2736": [
            "CompoundCriticalSpeedAnalysis"
        ],
        "_private.system_model.analyses_and_results._2737": ["CompoundDynamicAnalysis"],
        "_private.system_model.analyses_and_results._2738": [
            "CompoundDynamicModelAtAStiffness"
        ],
        "_private.system_model.analyses_and_results._2739": [
            "CompoundDynamicModelForHarmonicAnalysis"
        ],
        "_private.system_model.analyses_and_results._2740": [
            "CompoundDynamicModelForModalAnalysis"
        ],
        "_private.system_model.analyses_and_results._2741": [
            "CompoundDynamicModelForStabilityAnalysis"
        ],
        "_private.system_model.analyses_and_results._2742": [
            "CompoundDynamicModelForSteadyStateSynchronousResponse"
        ],
        "_private.system_model.analyses_and_results._2743": [
            "CompoundHarmonicAnalysis"
        ],
        "_private.system_model.analyses_and_results._2744": [
            "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
        ],
        "_private.system_model.analyses_and_results._2745": [
            "CompoundHarmonicAnalysisOfSingleExcitation"
        ],
        "_private.system_model.analyses_and_results._2746": ["CompoundModalAnalysis"],
        "_private.system_model.analyses_and_results._2747": [
            "CompoundModalAnalysisAtASpeed"
        ],
        "_private.system_model.analyses_and_results._2748": [
            "CompoundModalAnalysisAtAStiffness"
        ],
        "_private.system_model.analyses_and_results._2749": [
            "CompoundModalAnalysisForHarmonicAnalysis"
        ],
        "_private.system_model.analyses_and_results._2750": [
            "CompoundMultibodyDynamicsAnalysis"
        ],
        "_private.system_model.analyses_and_results._2751": ["CompoundPowerFlow"],
        "_private.system_model.analyses_and_results._2752": [
            "CompoundStabilityAnalysis"
        ],
        "_private.system_model.analyses_and_results._2753": [
            "CompoundSteadyStateSynchronousResponse"
        ],
        "_private.system_model.analyses_and_results._2754": [
            "CompoundSteadyStateSynchronousResponseAtASpeed"
        ],
        "_private.system_model.analyses_and_results._2755": [
            "CompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_private.system_model.analyses_and_results._2756": [
            "CompoundSystemDeflection"
        ],
        "_private.system_model.analyses_and_results._2757": [
            "CompoundTorsionalSystemDeflection"
        ],
        "_private.system_model.analyses_and_results._2758": [
            "TESetUpForDynamicAnalysisOptions"
        ],
        "_private.system_model.analyses_and_results._2759": ["TimeOptions"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "CompoundAnalysis",
    "AnalysisCaseVariable",
    "ConnectionAnalysis",
    "Context",
    "DesignEntityAnalysis",
    "DesignEntityGroupAnalysis",
    "DesignEntitySingleContextAnalysis",
    "PartAnalysis",
    "CompoundAdvancedSystemDeflection",
    "CompoundAdvancedSystemDeflectionSubAnalysis",
    "CompoundAdvancedTimeSteppingAnalysisForModulation",
    "CompoundCriticalSpeedAnalysis",
    "CompoundDynamicAnalysis",
    "CompoundDynamicModelAtAStiffness",
    "CompoundDynamicModelForHarmonicAnalysis",
    "CompoundDynamicModelForModalAnalysis",
    "CompoundDynamicModelForStabilityAnalysis",
    "CompoundDynamicModelForSteadyStateSynchronousResponse",
    "CompoundHarmonicAnalysis",
    "CompoundHarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    "CompoundHarmonicAnalysisOfSingleExcitation",
    "CompoundModalAnalysis",
    "CompoundModalAnalysisAtASpeed",
    "CompoundModalAnalysisAtAStiffness",
    "CompoundModalAnalysisForHarmonicAnalysis",
    "CompoundMultibodyDynamicsAnalysis",
    "CompoundPowerFlow",
    "CompoundStabilityAnalysis",
    "CompoundSteadyStateSynchronousResponse",
    "CompoundSteadyStateSynchronousResponseAtASpeed",
    "CompoundSteadyStateSynchronousResponseOnAShaft",
    "CompoundSystemDeflection",
    "CompoundTorsionalSystemDeflection",
    "TESetUpForDynamicAnalysisOptions",
    "TimeOptions",
)
