"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.bearings.roller_bearing_profiles._1991 import ProfileDataToUse
    from mastapy._private.bearings.roller_bearing_profiles._1992 import ProfileSet
    from mastapy._private.bearings.roller_bearing_profiles._1993 import ProfileToFit
    from mastapy._private.bearings.roller_bearing_profiles._1994 import (
        RollerBearingConicalProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1995 import (
        RollerBearingCrownedProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1996 import (
        RollerBearingDinLundbergProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1997 import (
        RollerBearingFlatProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1998 import (
        RollerBearingJohnsGoharProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._1999 import (
        RollerBearingLundbergProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._2000 import (
        RollerBearingProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._2001 import (
        RollerBearingTangentialCrownedProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._2002 import (
        RollerBearingUserSpecifiedProfile,
    )
    from mastapy._private.bearings.roller_bearing_profiles._2003 import (
        RollerRaceProfilePoint,
    )
    from mastapy._private.bearings.roller_bearing_profiles._2004 import (
        UserSpecifiedProfilePoint,
    )
    from mastapy._private.bearings.roller_bearing_profiles._2005 import (
        UserSpecifiedRollerRaceProfilePoint,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.bearings.roller_bearing_profiles._1991": ["ProfileDataToUse"],
        "_private.bearings.roller_bearing_profiles._1992": ["ProfileSet"],
        "_private.bearings.roller_bearing_profiles._1993": ["ProfileToFit"],
        "_private.bearings.roller_bearing_profiles._1994": [
            "RollerBearingConicalProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1995": [
            "RollerBearingCrownedProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1996": [
            "RollerBearingDinLundbergProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1997": ["RollerBearingFlatProfile"],
        "_private.bearings.roller_bearing_profiles._1998": [
            "RollerBearingJohnsGoharProfile"
        ],
        "_private.bearings.roller_bearing_profiles._1999": [
            "RollerBearingLundbergProfile"
        ],
        "_private.bearings.roller_bearing_profiles._2000": ["RollerBearingProfile"],
        "_private.bearings.roller_bearing_profiles._2001": [
            "RollerBearingTangentialCrownedProfile"
        ],
        "_private.bearings.roller_bearing_profiles._2002": [
            "RollerBearingUserSpecifiedProfile"
        ],
        "_private.bearings.roller_bearing_profiles._2003": ["RollerRaceProfilePoint"],
        "_private.bearings.roller_bearing_profiles._2004": [
            "UserSpecifiedProfilePoint"
        ],
        "_private.bearings.roller_bearing_profiles._2005": [
            "UserSpecifiedRollerRaceProfilePoint"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "ProfileDataToUse",
    "ProfileSet",
    "ProfileToFit",
    "RollerBearingConicalProfile",
    "RollerBearingCrownedProfile",
    "RollerBearingDinLundbergProfile",
    "RollerBearingFlatProfile",
    "RollerBearingJohnsGoharProfile",
    "RollerBearingLundbergProfile",
    "RollerBearingProfile",
    "RollerBearingTangentialCrownedProfile",
    "RollerBearingUserSpecifiedProfile",
    "RollerRaceProfilePoint",
    "UserSpecifiedProfilePoint",
    "UserSpecifiedRollerRaceProfilePoint",
)
