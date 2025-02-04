"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5780 import (
        AbstractDesignStateLoadCaseGroup,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5781 import (
        AbstractLoadCaseGroup,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5782 import (
        AbstractStaticLoadCaseGroup,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5783 import (
        ClutchEngagementStatus,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5784 import (
        ConceptSynchroGearEngagementStatus,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5785 import (
        DesignState,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5786 import (
        DutyCycle,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5787 import (
        GenericClutchEngagementStatus,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5788 import (
        LoadCaseGroupHistograms,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5789 import (
        SubGroupInSingleDesignState,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5790 import (
        SystemOptimisationGearSet,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5791 import (
        SystemOptimiserGearSetOptimisation,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5792 import (
        SystemOptimiserTargets,
    )
    from mastapy._private.system_model.analyses_and_results.load_case_groups._5793 import (
        TimeSeriesLoadCaseGroup,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.analyses_and_results.load_case_groups._5780": [
            "AbstractDesignStateLoadCaseGroup"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5781": [
            "AbstractLoadCaseGroup"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5782": [
            "AbstractStaticLoadCaseGroup"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5783": [
            "ClutchEngagementStatus"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5784": [
            "ConceptSynchroGearEngagementStatus"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5785": [
            "DesignState"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5786": [
            "DutyCycle"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5787": [
            "GenericClutchEngagementStatus"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5788": [
            "LoadCaseGroupHistograms"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5789": [
            "SubGroupInSingleDesignState"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5790": [
            "SystemOptimisationGearSet"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5791": [
            "SystemOptimiserGearSetOptimisation"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5792": [
            "SystemOptimiserTargets"
        ],
        "_private.system_model.analyses_and_results.load_case_groups._5793": [
            "TimeSeriesLoadCaseGroup"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AbstractDesignStateLoadCaseGroup",
    "AbstractLoadCaseGroup",
    "AbstractStaticLoadCaseGroup",
    "ClutchEngagementStatus",
    "ConceptSynchroGearEngagementStatus",
    "DesignState",
    "DutyCycle",
    "GenericClutchEngagementStatus",
    "LoadCaseGroupHistograms",
    "SubGroupInSingleDesignState",
    "SystemOptimisationGearSet",
    "SystemOptimiserGearSetOptimisation",
    "SystemOptimiserTargets",
    "TimeSeriesLoadCaseGroup",
)
