"""DetailedBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.bearings.bearing_designs import _2199

_DETAILED_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "DetailedBearing"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_designs import _2195
    from mastapy._private.bearings.bearing_designs.fluid_film import (
        _2253,
        _2255,
        _2257,
        _2259,
        _2260,
        _2261,
    )
    from mastapy._private.bearings.bearing_designs.rolling import (
        _2200,
        _2201,
        _2202,
        _2203,
        _2204,
        _2205,
        _2207,
        _2213,
        _2214,
        _2215,
        _2219,
        _2224,
        _2225,
        _2226,
        _2227,
        _2230,
        _2232,
        _2235,
        _2236,
        _2237,
        _2238,
        _2239,
        _2240,
    )

    Self = TypeVar("Self", bound="DetailedBearing")
    CastSelf = TypeVar("CastSelf", bound="DetailedBearing._Cast_DetailedBearing")


__docformat__ = "restructuredtext en"
__all__ = ("DetailedBearing",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_DetailedBearing:
    """Special nested class for casting DetailedBearing to subclasses."""

    __parent__: "DetailedBearing"

    @property
    def non_linear_bearing(self: "CastSelf") -> "_2199.NonLinearBearing":
        return self.__parent__._cast(_2199.NonLinearBearing)

    @property
    def bearing_design(self: "CastSelf") -> "_2195.BearingDesign":
        from mastapy._private.bearings.bearing_designs import _2195

        return self.__parent__._cast(_2195.BearingDesign)

    @property
    def angular_contact_ball_bearing(
        self: "CastSelf",
    ) -> "_2200.AngularContactBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2200

        return self.__parent__._cast(_2200.AngularContactBallBearing)

    @property
    def angular_contact_thrust_ball_bearing(
        self: "CastSelf",
    ) -> "_2201.AngularContactThrustBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2201

        return self.__parent__._cast(_2201.AngularContactThrustBallBearing)

    @property
    def asymmetric_spherical_roller_bearing(
        self: "CastSelf",
    ) -> "_2202.AsymmetricSphericalRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2202

        return self.__parent__._cast(_2202.AsymmetricSphericalRollerBearing)

    @property
    def axial_thrust_cylindrical_roller_bearing(
        self: "CastSelf",
    ) -> "_2203.AxialThrustCylindricalRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2203

        return self.__parent__._cast(_2203.AxialThrustCylindricalRollerBearing)

    @property
    def axial_thrust_needle_roller_bearing(
        self: "CastSelf",
    ) -> "_2204.AxialThrustNeedleRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2204

        return self.__parent__._cast(_2204.AxialThrustNeedleRollerBearing)

    @property
    def ball_bearing(self: "CastSelf") -> "_2205.BallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2205

        return self.__parent__._cast(_2205.BallBearing)

    @property
    def barrel_roller_bearing(self: "CastSelf") -> "_2207.BarrelRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2207

        return self.__parent__._cast(_2207.BarrelRollerBearing)

    @property
    def crossed_roller_bearing(self: "CastSelf") -> "_2213.CrossedRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2213

        return self.__parent__._cast(_2213.CrossedRollerBearing)

    @property
    def cylindrical_roller_bearing(
        self: "CastSelf",
    ) -> "_2214.CylindricalRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2214

        return self.__parent__._cast(_2214.CylindricalRollerBearing)

    @property
    def deep_groove_ball_bearing(self: "CastSelf") -> "_2215.DeepGrooveBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2215

        return self.__parent__._cast(_2215.DeepGrooveBallBearing)

    @property
    def four_point_contact_ball_bearing(
        self: "CastSelf",
    ) -> "_2219.FourPointContactBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2219

        return self.__parent__._cast(_2219.FourPointContactBallBearing)

    @property
    def multi_point_contact_ball_bearing(
        self: "CastSelf",
    ) -> "_2224.MultiPointContactBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2224

        return self.__parent__._cast(_2224.MultiPointContactBallBearing)

    @property
    def needle_roller_bearing(self: "CastSelf") -> "_2225.NeedleRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2225

        return self.__parent__._cast(_2225.NeedleRollerBearing)

    @property
    def non_barrel_roller_bearing(self: "CastSelf") -> "_2226.NonBarrelRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2226

        return self.__parent__._cast(_2226.NonBarrelRollerBearing)

    @property
    def roller_bearing(self: "CastSelf") -> "_2227.RollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2227

        return self.__parent__._cast(_2227.RollerBearing)

    @property
    def rolling_bearing(self: "CastSelf") -> "_2230.RollingBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2230

        return self.__parent__._cast(_2230.RollingBearing)

    @property
    def self_aligning_ball_bearing(self: "CastSelf") -> "_2232.SelfAligningBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2232

        return self.__parent__._cast(_2232.SelfAligningBallBearing)

    @property
    def spherical_roller_bearing(self: "CastSelf") -> "_2235.SphericalRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2235

        return self.__parent__._cast(_2235.SphericalRollerBearing)

    @property
    def spherical_roller_thrust_bearing(
        self: "CastSelf",
    ) -> "_2236.SphericalRollerThrustBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2236

        return self.__parent__._cast(_2236.SphericalRollerThrustBearing)

    @property
    def taper_roller_bearing(self: "CastSelf") -> "_2237.TaperRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2237

        return self.__parent__._cast(_2237.TaperRollerBearing)

    @property
    def three_point_contact_ball_bearing(
        self: "CastSelf",
    ) -> "_2238.ThreePointContactBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2238

        return self.__parent__._cast(_2238.ThreePointContactBallBearing)

    @property
    def thrust_ball_bearing(self: "CastSelf") -> "_2239.ThrustBallBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2239

        return self.__parent__._cast(_2239.ThrustBallBearing)

    @property
    def toroidal_roller_bearing(self: "CastSelf") -> "_2240.ToroidalRollerBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2240

        return self.__parent__._cast(_2240.ToroidalRollerBearing)

    @property
    def pad_fluid_film_bearing(self: "CastSelf") -> "_2253.PadFluidFilmBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2253

        return self.__parent__._cast(_2253.PadFluidFilmBearing)

    @property
    def plain_grease_filled_journal_bearing(
        self: "CastSelf",
    ) -> "_2255.PlainGreaseFilledJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2255

        return self.__parent__._cast(_2255.PlainGreaseFilledJournalBearing)

    @property
    def plain_journal_bearing(self: "CastSelf") -> "_2257.PlainJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2257

        return self.__parent__._cast(_2257.PlainJournalBearing)

    @property
    def plain_oil_fed_journal_bearing(
        self: "CastSelf",
    ) -> "_2259.PlainOilFedJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2259

        return self.__parent__._cast(_2259.PlainOilFedJournalBearing)

    @property
    def tilting_pad_journal_bearing(
        self: "CastSelf",
    ) -> "_2260.TiltingPadJournalBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2260

        return self.__parent__._cast(_2260.TiltingPadJournalBearing)

    @property
    def tilting_pad_thrust_bearing(self: "CastSelf") -> "_2261.TiltingPadThrustBearing":
        from mastapy._private.bearings.bearing_designs.fluid_film import _2261

        return self.__parent__._cast(_2261.TiltingPadThrustBearing)

    @property
    def detailed_bearing(self: "CastSelf") -> "DetailedBearing":
        return self.__parent__

    def __getattr__(self: "CastSelf", name: str) -> "Any":
        try:
            return self.__getattribute__(name)
        except AttributeError:
            class_name = utility.camel(name)
            raise CastException(
                f'Detected an invalid cast. Cannot cast to type "{class_name}"'
            ) from None


@extended_dataclass(frozen=True, slots=True, weakref_slot=True, eq=False)
class DetailedBearing(_2199.NonLinearBearing):
    """DetailedBearing

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _DETAILED_BEARING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_DetailedBearing":
        """Cast to another type.

        Returns:
            _Cast_DetailedBearing
        """
        return _Cast_DetailedBearing(self)
