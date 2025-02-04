"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7480 import (
        AcousticAnalysisRunType,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7481 import (
        AcousticPreconditionerType,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7482 import (
        AcousticSurfaceSelectionList,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7483 import (
        AcousticSurfaceWithSelection,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7484 import (
        HarmonicAcousticAnalysis,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7485 import (
        InitialGuessOption,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7486 import (
        M2LHfCacheType,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7487 import (
        NearFieldIntegralsCacheType,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7488 import (
        OctreeCreationMethod,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7489 import (
        SingleExcitationDetails,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7490 import (
        SingleHarmonicExcitationAnalysisDetail,
    )
    from mastapy._private.system_model.analyses_and_results.acoustic_analyses._7491 import (
        UnitForceExcitationAnalysisDetail,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.analyses_and_results.acoustic_analyses._7480": [
            "AcousticAnalysisRunType"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7481": [
            "AcousticPreconditionerType"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7482": [
            "AcousticSurfaceSelectionList"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7483": [
            "AcousticSurfaceWithSelection"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7484": [
            "HarmonicAcousticAnalysis"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7485": [
            "InitialGuessOption"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7486": [
            "M2LHfCacheType"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7487": [
            "NearFieldIntegralsCacheType"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7488": [
            "OctreeCreationMethod"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7489": [
            "SingleExcitationDetails"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7490": [
            "SingleHarmonicExcitationAnalysisDetail"
        ],
        "_private.system_model.analyses_and_results.acoustic_analyses._7491": [
            "UnitForceExcitationAnalysisDetail"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AcousticAnalysisRunType",
    "AcousticPreconditionerType",
    "AcousticSurfaceSelectionList",
    "AcousticSurfaceWithSelection",
    "HarmonicAcousticAnalysis",
    "InitialGuessOption",
    "M2LHfCacheType",
    "NearFieldIntegralsCacheType",
    "OctreeCreationMethod",
    "SingleExcitationDetails",
    "SingleHarmonicExcitationAnalysisDetail",
    "UnitForceExcitationAnalysisDetail",
)
