"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.bearings.bearing_designs.rolling._2200 import (
        AngularContactBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2201 import (
        AngularContactThrustBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2202 import (
        AsymmetricSphericalRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2203 import (
        AxialThrustCylindricalRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2204 import (
        AxialThrustNeedleRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2205 import BallBearing
    from mastapy._private.bearings.bearing_designs.rolling._2206 import (
        BallBearingShoulderDefinition,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2207 import (
        BarrelRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2208 import (
        BearingProtection,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2209 import (
        BearingProtectionDetailsModifier,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2210 import (
        BearingProtectionLevel,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2211 import (
        BearingTypeExtraInformation,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2212 import CageBridgeShape
    from mastapy._private.bearings.bearing_designs.rolling._2213 import (
        CrossedRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2214 import (
        CylindricalRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2215 import (
        DeepGrooveBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2216 import DiameterSeries
    from mastapy._private.bearings.bearing_designs.rolling._2217 import (
        FatigueLoadLimitCalculationMethodEnum,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2218 import (
        FourPointContactAngleDefinition,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2219 import (
        FourPointContactBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2220 import (
        GeometricConstants,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2221 import (
        GeometricConstantsForRollingFrictionalMoments,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2222 import (
        GeometricConstantsForSlidingFrictionalMoments,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2223 import HeightSeries
    from mastapy._private.bearings.bearing_designs.rolling._2224 import (
        MultiPointContactBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2225 import (
        NeedleRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2226 import (
        NonBarrelRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2227 import RollerBearing
    from mastapy._private.bearings.bearing_designs.rolling._2228 import RollerEndShape
    from mastapy._private.bearings.bearing_designs.rolling._2229 import RollerRibDetail
    from mastapy._private.bearings.bearing_designs.rolling._2230 import RollingBearing
    from mastapy._private.bearings.bearing_designs.rolling._2231 import (
        RollingBearingElement,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2232 import (
        SelfAligningBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2233 import (
        SKFSealFrictionalMomentConstants,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2234 import SleeveType
    from mastapy._private.bearings.bearing_designs.rolling._2235 import (
        SphericalRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2236 import (
        SphericalRollerThrustBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2237 import (
        TaperRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2238 import (
        ThreePointContactBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2239 import (
        ThrustBallBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2240 import (
        ToroidalRollerBearing,
    )
    from mastapy._private.bearings.bearing_designs.rolling._2241 import WidthSeries
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.bearings.bearing_designs.rolling._2200": [
            "AngularContactBallBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2201": [
            "AngularContactThrustBallBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2202": [
            "AsymmetricSphericalRollerBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2203": [
            "AxialThrustCylindricalRollerBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2204": [
            "AxialThrustNeedleRollerBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2205": ["BallBearing"],
        "_private.bearings.bearing_designs.rolling._2206": [
            "BallBearingShoulderDefinition"
        ],
        "_private.bearings.bearing_designs.rolling._2207": ["BarrelRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2208": ["BearingProtection"],
        "_private.bearings.bearing_designs.rolling._2209": [
            "BearingProtectionDetailsModifier"
        ],
        "_private.bearings.bearing_designs.rolling._2210": ["BearingProtectionLevel"],
        "_private.bearings.bearing_designs.rolling._2211": [
            "BearingTypeExtraInformation"
        ],
        "_private.bearings.bearing_designs.rolling._2212": ["CageBridgeShape"],
        "_private.bearings.bearing_designs.rolling._2213": ["CrossedRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2214": ["CylindricalRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2215": ["DeepGrooveBallBearing"],
        "_private.bearings.bearing_designs.rolling._2216": ["DiameterSeries"],
        "_private.bearings.bearing_designs.rolling._2217": [
            "FatigueLoadLimitCalculationMethodEnum"
        ],
        "_private.bearings.bearing_designs.rolling._2218": [
            "FourPointContactAngleDefinition"
        ],
        "_private.bearings.bearing_designs.rolling._2219": [
            "FourPointContactBallBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2220": ["GeometricConstants"],
        "_private.bearings.bearing_designs.rolling._2221": [
            "GeometricConstantsForRollingFrictionalMoments"
        ],
        "_private.bearings.bearing_designs.rolling._2222": [
            "GeometricConstantsForSlidingFrictionalMoments"
        ],
        "_private.bearings.bearing_designs.rolling._2223": ["HeightSeries"],
        "_private.bearings.bearing_designs.rolling._2224": [
            "MultiPointContactBallBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2225": ["NeedleRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2226": ["NonBarrelRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2227": ["RollerBearing"],
        "_private.bearings.bearing_designs.rolling._2228": ["RollerEndShape"],
        "_private.bearings.bearing_designs.rolling._2229": ["RollerRibDetail"],
        "_private.bearings.bearing_designs.rolling._2230": ["RollingBearing"],
        "_private.bearings.bearing_designs.rolling._2231": ["RollingBearingElement"],
        "_private.bearings.bearing_designs.rolling._2232": ["SelfAligningBallBearing"],
        "_private.bearings.bearing_designs.rolling._2233": [
            "SKFSealFrictionalMomentConstants"
        ],
        "_private.bearings.bearing_designs.rolling._2234": ["SleeveType"],
        "_private.bearings.bearing_designs.rolling._2235": ["SphericalRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2236": [
            "SphericalRollerThrustBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2237": ["TaperRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2238": [
            "ThreePointContactBallBearing"
        ],
        "_private.bearings.bearing_designs.rolling._2239": ["ThrustBallBearing"],
        "_private.bearings.bearing_designs.rolling._2240": ["ToroidalRollerBearing"],
        "_private.bearings.bearing_designs.rolling._2241": ["WidthSeries"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AngularContactBallBearing",
    "AngularContactThrustBallBearing",
    "AsymmetricSphericalRollerBearing",
    "AxialThrustCylindricalRollerBearing",
    "AxialThrustNeedleRollerBearing",
    "BallBearing",
    "BallBearingShoulderDefinition",
    "BarrelRollerBearing",
    "BearingProtection",
    "BearingProtectionDetailsModifier",
    "BearingProtectionLevel",
    "BearingTypeExtraInformation",
    "CageBridgeShape",
    "CrossedRollerBearing",
    "CylindricalRollerBearing",
    "DeepGrooveBallBearing",
    "DiameterSeries",
    "FatigueLoadLimitCalculationMethodEnum",
    "FourPointContactAngleDefinition",
    "FourPointContactBallBearing",
    "GeometricConstants",
    "GeometricConstantsForRollingFrictionalMoments",
    "GeometricConstantsForSlidingFrictionalMoments",
    "HeightSeries",
    "MultiPointContactBallBearing",
    "NeedleRollerBearing",
    "NonBarrelRollerBearing",
    "RollerBearing",
    "RollerEndShape",
    "RollerRibDetail",
    "RollingBearing",
    "RollingBearingElement",
    "SelfAligningBallBearing",
    "SKFSealFrictionalMomentConstants",
    "SleeveType",
    "SphericalRollerBearing",
    "SphericalRollerThrustBearing",
    "TaperRollerBearing",
    "ThreePointContactBallBearing",
    "ThrustBallBearing",
    "ToroidalRollerBearing",
    "WidthSeries",
)
