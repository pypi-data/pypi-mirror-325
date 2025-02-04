"""LoadedBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.bearings import _1939

_LOADED_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedBearingResults"
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.bearings.bearing_designs import _2195
    from mastapy._private.bearings.bearing_results import (
        _2016,
        _2017,
        _2018,
        _2019,
        _2020,
        _2022,
        _2025,
    )
    from mastapy._private.bearings.bearing_results.fluid_film import (
        _2184,
        _2185,
        _2186,
        _2187,
        _2189,
        _2192,
        _2193,
    )
    from mastapy._private.bearings.bearing_results.rolling import (
        _2048,
        _2051,
        _2054,
        _2059,
        _2062,
        _2067,
        _2070,
        _2074,
        _2077,
        _2082,
        _2086,
        _2089,
        _2094,
        _2098,
        _2101,
        _2105,
        _2108,
        _2113,
        _2116,
        _2119,
        _2122,
        _2133,
    )
    from mastapy._private.math_utility.measured_vectors import _1623

    Self = TypeVar("Self", bound="LoadedBearingResults")
    CastSelf = TypeVar(
        "CastSelf", bound="LoadedBearingResults._Cast_LoadedBearingResults"
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedBearingResults",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedBearingResults:
    """Special nested class for casting LoadedBearingResults to subclasses."""

    __parent__: "LoadedBearingResults"

    @property
    def bearing_load_case_results_lightweight(
        self: "CastSelf",
    ) -> "_1939.BearingLoadCaseResultsLightweight":
        return self.__parent__._cast(_1939.BearingLoadCaseResultsLightweight)

    @property
    def loaded_concept_axial_clearance_bearing_results(
        self: "CastSelf",
    ) -> "_2016.LoadedConceptAxialClearanceBearingResults":
        from mastapy._private.bearings.bearing_results import _2016

        return self.__parent__._cast(_2016.LoadedConceptAxialClearanceBearingResults)

    @property
    def loaded_concept_clearance_bearing_results(
        self: "CastSelf",
    ) -> "_2017.LoadedConceptClearanceBearingResults":
        from mastapy._private.bearings.bearing_results import _2017

        return self.__parent__._cast(_2017.LoadedConceptClearanceBearingResults)

    @property
    def loaded_concept_radial_clearance_bearing_results(
        self: "CastSelf",
    ) -> "_2018.LoadedConceptRadialClearanceBearingResults":
        from mastapy._private.bearings.bearing_results import _2018

        return self.__parent__._cast(_2018.LoadedConceptRadialClearanceBearingResults)

    @property
    def loaded_detailed_bearing_results(
        self: "CastSelf",
    ) -> "_2019.LoadedDetailedBearingResults":
        from mastapy._private.bearings.bearing_results import _2019

        return self.__parent__._cast(_2019.LoadedDetailedBearingResults)

    @property
    def loaded_linear_bearing_results(
        self: "CastSelf",
    ) -> "_2020.LoadedLinearBearingResults":
        from mastapy._private.bearings.bearing_results import _2020

        return self.__parent__._cast(_2020.LoadedLinearBearingResults)

    @property
    def loaded_non_linear_bearing_results(
        self: "CastSelf",
    ) -> "_2022.LoadedNonLinearBearingResults":
        from mastapy._private.bearings.bearing_results import _2022

        return self.__parent__._cast(_2022.LoadedNonLinearBearingResults)

    @property
    def loaded_angular_contact_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2048.LoadedAngularContactBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2048

        return self.__parent__._cast(_2048.LoadedAngularContactBallBearingResults)

    @property
    def loaded_angular_contact_thrust_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2051.LoadedAngularContactThrustBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2051

        return self.__parent__._cast(_2051.LoadedAngularContactThrustBallBearingResults)

    @property
    def loaded_asymmetric_spherical_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2054.LoadedAsymmetricSphericalRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2054

        return self.__parent__._cast(
            _2054.LoadedAsymmetricSphericalRollerBearingResults
        )

    @property
    def loaded_axial_thrust_cylindrical_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2059.LoadedAxialThrustCylindricalRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2059

        return self.__parent__._cast(
            _2059.LoadedAxialThrustCylindricalRollerBearingResults
        )

    @property
    def loaded_axial_thrust_needle_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2062.LoadedAxialThrustNeedleRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2062

        return self.__parent__._cast(_2062.LoadedAxialThrustNeedleRollerBearingResults)

    @property
    def loaded_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2067.LoadedBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2067

        return self.__parent__._cast(_2067.LoadedBallBearingResults)

    @property
    def loaded_crossed_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2070.LoadedCrossedRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2070

        return self.__parent__._cast(_2070.LoadedCrossedRollerBearingResults)

    @property
    def loaded_cylindrical_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2074.LoadedCylindricalRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2074

        return self.__parent__._cast(_2074.LoadedCylindricalRollerBearingResults)

    @property
    def loaded_deep_groove_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2077.LoadedDeepGrooveBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2077

        return self.__parent__._cast(_2077.LoadedDeepGrooveBallBearingResults)

    @property
    def loaded_four_point_contact_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2082.LoadedFourPointContactBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2082

        return self.__parent__._cast(_2082.LoadedFourPointContactBallBearingResults)

    @property
    def loaded_needle_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2086.LoadedNeedleRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2086

        return self.__parent__._cast(_2086.LoadedNeedleRollerBearingResults)

    @property
    def loaded_non_barrel_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2089.LoadedNonBarrelRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2089

        return self.__parent__._cast(_2089.LoadedNonBarrelRollerBearingResults)

    @property
    def loaded_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2094.LoadedRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2094

        return self.__parent__._cast(_2094.LoadedRollerBearingResults)

    @property
    def loaded_rolling_bearing_results(
        self: "CastSelf",
    ) -> "_2098.LoadedRollingBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2098

        return self.__parent__._cast(_2098.LoadedRollingBearingResults)

    @property
    def loaded_self_aligning_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2101.LoadedSelfAligningBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2101

        return self.__parent__._cast(_2101.LoadedSelfAligningBallBearingResults)

    @property
    def loaded_spherical_roller_radial_bearing_results(
        self: "CastSelf",
    ) -> "_2105.LoadedSphericalRollerRadialBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2105

        return self.__parent__._cast(_2105.LoadedSphericalRollerRadialBearingResults)

    @property
    def loaded_spherical_roller_thrust_bearing_results(
        self: "CastSelf",
    ) -> "_2108.LoadedSphericalRollerThrustBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2108

        return self.__parent__._cast(_2108.LoadedSphericalRollerThrustBearingResults)

    @property
    def loaded_taper_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2113.LoadedTaperRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2113

        return self.__parent__._cast(_2113.LoadedTaperRollerBearingResults)

    @property
    def loaded_three_point_contact_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2116.LoadedThreePointContactBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2116

        return self.__parent__._cast(_2116.LoadedThreePointContactBallBearingResults)

    @property
    def loaded_thrust_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2119.LoadedThrustBallBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2119

        return self.__parent__._cast(_2119.LoadedThrustBallBearingResults)

    @property
    def loaded_toroidal_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2122.LoadedToroidalRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2122

        return self.__parent__._cast(_2122.LoadedToroidalRollerBearingResults)

    @property
    def loaded_fluid_film_bearing_results(
        self: "CastSelf",
    ) -> "_2184.LoadedFluidFilmBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2184

        return self.__parent__._cast(_2184.LoadedFluidFilmBearingResults)

    @property
    def loaded_grease_filled_journal_bearing_results(
        self: "CastSelf",
    ) -> "_2185.LoadedGreaseFilledJournalBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2185

        return self.__parent__._cast(_2185.LoadedGreaseFilledJournalBearingResults)

    @property
    def loaded_pad_fluid_film_bearing_results(
        self: "CastSelf",
    ) -> "_2186.LoadedPadFluidFilmBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2186

        return self.__parent__._cast(_2186.LoadedPadFluidFilmBearingResults)

    @property
    def loaded_plain_journal_bearing_results(
        self: "CastSelf",
    ) -> "_2187.LoadedPlainJournalBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2187

        return self.__parent__._cast(_2187.LoadedPlainJournalBearingResults)

    @property
    def loaded_plain_oil_fed_journal_bearing(
        self: "CastSelf",
    ) -> "_2189.LoadedPlainOilFedJournalBearing":
        from mastapy._private.bearings.bearing_results.fluid_film import _2189

        return self.__parent__._cast(_2189.LoadedPlainOilFedJournalBearing)

    @property
    def loaded_tilting_pad_journal_bearing_results(
        self: "CastSelf",
    ) -> "_2192.LoadedTiltingPadJournalBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2192

        return self.__parent__._cast(_2192.LoadedTiltingPadJournalBearingResults)

    @property
    def loaded_tilting_pad_thrust_bearing_results(
        self: "CastSelf",
    ) -> "_2193.LoadedTiltingPadThrustBearingResults":
        from mastapy._private.bearings.bearing_results.fluid_film import _2193

        return self.__parent__._cast(_2193.LoadedTiltingPadThrustBearingResults)

    @property
    def loaded_bearing_results(self: "CastSelf") -> "LoadedBearingResults":
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
class LoadedBearingResults(_1939.BearingLoadCaseResultsLightweight):
    """LoadedBearingResults

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_BEARING_RESULTS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def angle_of_gravity_from_z_axis(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AngleOfGravityFromZAxis")

        if temp is None:
            return 0.0

        return temp

    @property
    def axial_displacement_preload(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "AxialDisplacementPreload")

        if temp is None:
            return 0.0

        return temp

    @axial_displacement_preload.setter
    @enforce_parameter_types
    def axial_displacement_preload(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "AxialDisplacementPreload",
            float(value) if value is not None else 0.0,
        )

    @property
    def duration(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "Duration")

        if temp is None:
            return 0.0

        return temp

    @duration.setter
    @enforce_parameter_types
    def duration(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped, "Duration", float(value) if value is not None else 0.0
        )

    @property
    def force_results_are_overridden(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ForceResultsAreOverridden")

        if temp is None:
            return False

        return temp

    @property
    def inner_ring_angular_rotation(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "InnerRingAngularRotation")

        if temp is None:
            return 0.0

        return temp

    @inner_ring_angular_rotation.setter
    @enforce_parameter_types
    def inner_ring_angular_rotation(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "InnerRingAngularRotation",
            float(value) if value is not None else 0.0,
        )

    @property
    def inner_ring_angular_velocity(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "InnerRingAngularVelocity")

        if temp is None:
            return 0.0

        return temp

    @inner_ring_angular_velocity.setter
    @enforce_parameter_types
    def inner_ring_angular_velocity(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "InnerRingAngularVelocity",
            float(value) if value is not None else 0.0,
        )

    @property
    def orientation(self: "Self") -> "_2025.Orientations":
        """mastapy.bearings.bearing_results.Orientations"""
        temp = pythonnet_property_get(self.wrapped, "Orientation")

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy._private.bearings.bearing_results._2025", "Orientations"
        )(value)

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: "Self", value: "_2025.Orientations") -> None:
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Bearings.BearingResults.Orientations"
        )
        pythonnet_property_set(self.wrapped, "Orientation", value)

    @property
    def outer_ring_angular_rotation(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "OuterRingAngularRotation")

        if temp is None:
            return 0.0

        return temp

    @outer_ring_angular_rotation.setter
    @enforce_parameter_types
    def outer_ring_angular_rotation(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "OuterRingAngularRotation",
            float(value) if value is not None else 0.0,
        )

    @property
    def outer_ring_angular_velocity(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "OuterRingAngularVelocity")

        if temp is None:
            return 0.0

        return temp

    @outer_ring_angular_velocity.setter
    @enforce_parameter_types
    def outer_ring_angular_velocity(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "OuterRingAngularVelocity",
            float(value) if value is not None else 0.0,
        )

    @property
    def relative_angular_velocity(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "RelativeAngularVelocity")

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_axial_displacement(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "RelativeAxialDisplacement")

        if temp is None:
            return 0.0

        return temp

    @property
    def relative_radial_displacement(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "RelativeRadialDisplacement")

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_relative_angular_velocity(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SignedRelativeAngularVelocity")

        if temp is None:
            return 0.0

        return temp

    @property
    def specified_axial_internal_clearance(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "SpecifiedAxialInternalClearance")

        if temp is None:
            return 0.0

        return temp

    @specified_axial_internal_clearance.setter
    @enforce_parameter_types
    def specified_axial_internal_clearance(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "SpecifiedAxialInternalClearance",
            float(value) if value is not None else 0.0,
        )

    @property
    def specified_radial_internal_clearance(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "SpecifiedRadialInternalClearance")

        if temp is None:
            return 0.0

        return temp

    @specified_radial_internal_clearance.setter
    @enforce_parameter_types
    def specified_radial_internal_clearance(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "SpecifiedRadialInternalClearance",
            float(value) if value is not None else 0.0,
        )

    @property
    def bearing(self: "Self") -> "_2195.BearingDesign":
        """mastapy.bearings.bearing_designs.BearingDesign

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Bearing")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def force_on_inner_race(
        self: "Self",
    ) -> "_1623.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ForceOnInnerRace")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ring_results(self: "Self") -> "List[_2133.RingForceAndDisplacement]":
        """List[mastapy.bearings.bearing_results.rolling.RingForceAndDisplacement]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "RingResults")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedBearingResults":
        """Cast to another type.

        Returns:
            _Cast_LoadedBearingResults
        """
        return _Cast_LoadedBearingResults(self)
