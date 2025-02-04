"""LoadedDetailedBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.bearings.bearing_results import _2022

_LOADED_DETAILED_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedDetailedBearingResults"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings import _1939
    from mastapy._private.bearings.bearing_results import _2014
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
    )
    from mastapy._private.materials import _286

    Self = TypeVar("Self", bound="LoadedDetailedBearingResults")
    CastSelf = TypeVar(
        "CastSelf",
        bound="LoadedDetailedBearingResults._Cast_LoadedDetailedBearingResults",
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedDetailedBearingResults",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedDetailedBearingResults:
    """Special nested class for casting LoadedDetailedBearingResults to subclasses."""

    __parent__: "LoadedDetailedBearingResults"

    @property
    def loaded_non_linear_bearing_results(
        self: "CastSelf",
    ) -> "_2022.LoadedNonLinearBearingResults":
        return self.__parent__._cast(_2022.LoadedNonLinearBearingResults)

    @property
    def loaded_bearing_results(self: "CastSelf") -> "_2014.LoadedBearingResults":
        from mastapy._private.bearings.bearing_results import _2014

        return self.__parent__._cast(_2014.LoadedBearingResults)

    @property
    def bearing_load_case_results_lightweight(
        self: "CastSelf",
    ) -> "_1939.BearingLoadCaseResultsLightweight":
        from mastapy._private.bearings import _1939

        return self.__parent__._cast(_1939.BearingLoadCaseResultsLightweight)

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
    def loaded_detailed_bearing_results(
        self: "CastSelf",
    ) -> "LoadedDetailedBearingResults":
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
class LoadedDetailedBearingResults(_2022.LoadedNonLinearBearingResults):
    """LoadedDetailedBearingResults

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_DETAILED_BEARING_RESULTS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def lubricant_flow_rate(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "LubricantFlowRate")

        if temp is None:
            return 0.0

        return temp

    @lubricant_flow_rate.setter
    @enforce_parameter_types
    def lubricant_flow_rate(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "LubricantFlowRate",
            float(value) if value is not None else 0.0,
        )

    @property
    def oil_sump_temperature(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "OilSumpTemperature")

        if temp is None:
            return 0.0

        return temp

    @oil_sump_temperature.setter
    @enforce_parameter_types
    def oil_sump_temperature(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "OilSumpTemperature",
            float(value) if value is not None else 0.0,
        )

    @property
    def operating_air_temperature(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "OperatingAirTemperature")

        if temp is None:
            return 0.0

        return temp

    @operating_air_temperature.setter
    @enforce_parameter_types
    def operating_air_temperature(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "OperatingAirTemperature",
            float(value) if value is not None else 0.0,
        )

    @property
    def temperature_when_assembled(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "TemperatureWhenAssembled")

        if temp is None:
            return 0.0

        return temp

    @temperature_when_assembled.setter
    @enforce_parameter_types
    def temperature_when_assembled(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "TemperatureWhenAssembled",
            float(value) if value is not None else 0.0,
        )

    @property
    def lubrication(self: "Self") -> "_286.LubricationDetail":
        """mastapy.materials.LubricationDetail

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Lubrication")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedDetailedBearingResults":
        """Cast to another type.

        Returns:
            _Cast_LoadedDetailedBearingResults
        """
        return _Cast_LoadedDetailedBearingResults(self)
