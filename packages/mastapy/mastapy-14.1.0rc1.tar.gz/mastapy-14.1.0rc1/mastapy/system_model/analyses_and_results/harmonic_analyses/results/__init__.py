"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.results._5969 import (
        ConnectedComponentType,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.results._5970 import (
        ExcitationSourceSelection,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.results._5971 import (
        ExcitationSourceSelectionBase,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.results._5972 import (
        ExcitationSourceSelectionGroup,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.results._5973 import (
        HarmonicSelection,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.results._5974 import (
        ModalContributionDisplayMethod,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.results._5975 import (
        ModalContributionFilteringMethod,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.results._5976 import (
        ResultLocationSelectionGroup,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.results._5977 import (
        ResultLocationSelectionGroups,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses.results._5978 import (
        ResultNodeSelection,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.analyses_and_results.harmonic_analyses.results._5969": [
            "ConnectedComponentType"
        ],
        "_private.system_model.analyses_and_results.harmonic_analyses.results._5970": [
            "ExcitationSourceSelection"
        ],
        "_private.system_model.analyses_and_results.harmonic_analyses.results._5971": [
            "ExcitationSourceSelectionBase"
        ],
        "_private.system_model.analyses_and_results.harmonic_analyses.results._5972": [
            "ExcitationSourceSelectionGroup"
        ],
        "_private.system_model.analyses_and_results.harmonic_analyses.results._5973": [
            "HarmonicSelection"
        ],
        "_private.system_model.analyses_and_results.harmonic_analyses.results._5974": [
            "ModalContributionDisplayMethod"
        ],
        "_private.system_model.analyses_and_results.harmonic_analyses.results._5975": [
            "ModalContributionFilteringMethod"
        ],
        "_private.system_model.analyses_and_results.harmonic_analyses.results._5976": [
            "ResultLocationSelectionGroup"
        ],
        "_private.system_model.analyses_and_results.harmonic_analyses.results._5977": [
            "ResultLocationSelectionGroups"
        ],
        "_private.system_model.analyses_and_results.harmonic_analyses.results._5978": [
            "ResultNodeSelection"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ConnectedComponentType",
    "ExcitationSourceSelection",
    "ExcitationSourceSelectionBase",
    "ExcitationSourceSelectionGroup",
    "HarmonicSelection",
    "ModalContributionDisplayMethod",
    "ModalContributionFilteringMethod",
    "ResultLocationSelectionGroup",
    "ResultLocationSelectionGroups",
    "ResultNodeSelection",
)
