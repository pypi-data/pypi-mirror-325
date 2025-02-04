"""LoadedRollerBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.bearings.bearing_results.rolling import _2098

_LOADED_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollerBearingResults"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings import _1939
    from mastapy._private.bearings.bearing_results import _2014, _2019, _2022
    from mastapy._private.bearings.bearing_results.rolling import (
        _2054,
        _2059,
        _2062,
        _2070,
        _2074,
        _2086,
        _2089,
        _2105,
        _2108,
        _2113,
        _2122,
    )

    Self = TypeVar("Self", bound="LoadedRollerBearingResults")
    CastSelf = TypeVar(
        "CastSelf", bound="LoadedRollerBearingResults._Cast_LoadedRollerBearingResults"
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollerBearingResults",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedRollerBearingResults:
    """Special nested class for casting LoadedRollerBearingResults to subclasses."""

    __parent__: "LoadedRollerBearingResults"

    @property
    def loaded_rolling_bearing_results(
        self: "CastSelf",
    ) -> "_2098.LoadedRollingBearingResults":
        return self.__parent__._cast(_2098.LoadedRollingBearingResults)

    @property
    def loaded_detailed_bearing_results(
        self: "CastSelf",
    ) -> "_2019.LoadedDetailedBearingResults":
        from mastapy._private.bearings.bearing_results import _2019

        return self.__parent__._cast(_2019.LoadedDetailedBearingResults)

    @property
    def loaded_non_linear_bearing_results(
        self: "CastSelf",
    ) -> "_2022.LoadedNonLinearBearingResults":
        from mastapy._private.bearings.bearing_results import _2022

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
    def loaded_toroidal_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2122.LoadedToroidalRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2122

        return self.__parent__._cast(_2122.LoadedToroidalRollerBearingResults)

    @property
    def loaded_roller_bearing_results(self: "CastSelf") -> "LoadedRollerBearingResults":
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
class LoadedRollerBearingResults(_2098.LoadedRollingBearingResults):
    """LoadedRollerBearingResults

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_ROLLER_BEARING_RESULTS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def element_angular_velocity(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ElementAngularVelocity")

        if temp is None:
            return 0.0

        return temp

    @property
    def element_centrifugal_force(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ElementCentrifugalForce")

        if temp is None:
            return 0.0

        return temp

    @property
    def element_surface_velocity(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ElementSurfaceVelocity")

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_width_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "HertzianContactWidthInner")

        if temp is None:
            return 0.0

        return temp

    @property
    def hertzian_contact_width_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "HertzianContactWidthOuter")

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_inner(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "MaximumShearStressInner")

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_shear_stress_outer(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "MaximumShearStressOuter")

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedRollerBearingResults":
        """Cast to another type.

        Returns:
            _Cast_LoadedRollerBearingResults
        """
        return _Cast_LoadedRollerBearingResults(self)
