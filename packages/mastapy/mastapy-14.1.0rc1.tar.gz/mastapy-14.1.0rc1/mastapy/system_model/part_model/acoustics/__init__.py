"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.part_model.acoustics._2700 import (
        AcousticAnalysisOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2701 import (
        AcousticAnalysisSetup,
    )
    from mastapy._private.system_model.part_model.acoustics._2702 import (
        AcousticAnalysisSetupCacheReporting,
    )
    from mastapy._private.system_model.part_model.acoustics._2703 import (
        AcousticAnalysisSetupCollection,
    )
    from mastapy._private.system_model.part_model.acoustics._2704 import (
        AcousticEnvelopeType,
    )
    from mastapy._private.system_model.part_model.acoustics._2705 import (
        AcousticInputSurfaceOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2706 import (
        CacheMemoryEstimates,
    )
    from mastapy._private.system_model.part_model.acoustics._2707 import (
        FEPartInputSurfaceOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2708 import (
        FESurfaceSelectionForAcousticEnvelope,
    )
    from mastapy._private.system_model.part_model.acoustics._2709 import HoleInFaceGroup
    from mastapy._private.system_model.part_model.acoustics._2710 import (
        MeshedResultPlane,
    )
    from mastapy._private.system_model.part_model.acoustics._2711 import (
        MeshedResultSphere,
    )
    from mastapy._private.system_model.part_model.acoustics._2712 import (
        MeshedResultSurface,
    )
    from mastapy._private.system_model.part_model.acoustics._2713 import (
        MeshedResultSurfaceBase,
    )
    from mastapy._private.system_model.part_model.acoustics._2714 import (
        MicrophoneArrayDesign,
    )
    from mastapy._private.system_model.part_model.acoustics._2715 import (
        PartSelectionForAcousticEnvelope,
    )
    from mastapy._private.system_model.part_model.acoustics._2716 import (
        ResultPlaneOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2717 import (
        ResultSphereOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2718 import (
        ResultSurfaceCollection,
    )
    from mastapy._private.system_model.part_model.acoustics._2719 import (
        ResultSurfaceOptions,
    )
    from mastapy._private.system_model.part_model.acoustics._2720 import (
        SphericalEnvelopeCentreDefinition,
    )
    from mastapy._private.system_model.part_model.acoustics._2721 import (
        SphericalEnvelopeType,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model.acoustics._2700": ["AcousticAnalysisOptions"],
        "_private.system_model.part_model.acoustics._2701": ["AcousticAnalysisSetup"],
        "_private.system_model.part_model.acoustics._2702": [
            "AcousticAnalysisSetupCacheReporting"
        ],
        "_private.system_model.part_model.acoustics._2703": [
            "AcousticAnalysisSetupCollection"
        ],
        "_private.system_model.part_model.acoustics._2704": ["AcousticEnvelopeType"],
        "_private.system_model.part_model.acoustics._2705": [
            "AcousticInputSurfaceOptions"
        ],
        "_private.system_model.part_model.acoustics._2706": ["CacheMemoryEstimates"],
        "_private.system_model.part_model.acoustics._2707": [
            "FEPartInputSurfaceOptions"
        ],
        "_private.system_model.part_model.acoustics._2708": [
            "FESurfaceSelectionForAcousticEnvelope"
        ],
        "_private.system_model.part_model.acoustics._2709": ["HoleInFaceGroup"],
        "_private.system_model.part_model.acoustics._2710": ["MeshedResultPlane"],
        "_private.system_model.part_model.acoustics._2711": ["MeshedResultSphere"],
        "_private.system_model.part_model.acoustics._2712": ["MeshedResultSurface"],
        "_private.system_model.part_model.acoustics._2713": ["MeshedResultSurfaceBase"],
        "_private.system_model.part_model.acoustics._2714": ["MicrophoneArrayDesign"],
        "_private.system_model.part_model.acoustics._2715": [
            "PartSelectionForAcousticEnvelope"
        ],
        "_private.system_model.part_model.acoustics._2716": ["ResultPlaneOptions"],
        "_private.system_model.part_model.acoustics._2717": ["ResultSphereOptions"],
        "_private.system_model.part_model.acoustics._2718": ["ResultSurfaceCollection"],
        "_private.system_model.part_model.acoustics._2719": ["ResultSurfaceOptions"],
        "_private.system_model.part_model.acoustics._2720": [
            "SphericalEnvelopeCentreDefinition"
        ],
        "_private.system_model.part_model.acoustics._2721": ["SphericalEnvelopeType"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AcousticAnalysisOptions",
    "AcousticAnalysisSetup",
    "AcousticAnalysisSetupCacheReporting",
    "AcousticAnalysisSetupCollection",
    "AcousticEnvelopeType",
    "AcousticInputSurfaceOptions",
    "CacheMemoryEstimates",
    "FEPartInputSurfaceOptions",
    "FESurfaceSelectionForAcousticEnvelope",
    "HoleInFaceGroup",
    "MeshedResultPlane",
    "MeshedResultSphere",
    "MeshedResultSurface",
    "MeshedResultSurfaceBase",
    "MicrophoneArrayDesign",
    "PartSelectionForAcousticEnvelope",
    "ResultPlaneOptions",
    "ResultSphereOptions",
    "ResultSurfaceCollection",
    "ResultSurfaceOptions",
    "SphericalEnvelopeCentreDefinition",
    "SphericalEnvelopeType",
)
