"""LoadedNonBarrelRollerBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.bearings.bearing_results.rolling import _2094

_LOADED_NON_BARREL_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedNonBarrelRollerBearingResults",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings import _1939
    from mastapy._private.bearings.bearing_results import _2014, _2019, _2022
    from mastapy._private.bearings.bearing_results.rolling import (
        _2059,
        _2062,
        _2074,
        _2086,
        _2098,
        _2113,
        _2137,
    )

    Self = TypeVar("Self", bound="LoadedNonBarrelRollerBearingResults")
    CastSelf = TypeVar(
        "CastSelf",
        bound="LoadedNonBarrelRollerBearingResults._Cast_LoadedNonBarrelRollerBearingResults",
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonBarrelRollerBearingResults",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedNonBarrelRollerBearingResults:
    """Special nested class for casting LoadedNonBarrelRollerBearingResults to subclasses."""

    __parent__: "LoadedNonBarrelRollerBearingResults"

    @property
    def loaded_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2094.LoadedRollerBearingResults":
        return self.__parent__._cast(_2094.LoadedRollerBearingResults)

    @property
    def loaded_rolling_bearing_results(
        self: "CastSelf",
    ) -> "_2098.LoadedRollingBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2098

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
    def loaded_taper_roller_bearing_results(
        self: "CastSelf",
    ) -> "_2113.LoadedTaperRollerBearingResults":
        from mastapy._private.bearings.bearing_results.rolling import _2113

        return self.__parent__._cast(_2113.LoadedTaperRollerBearingResults)

    @property
    def loaded_non_barrel_roller_bearing_results(
        self: "CastSelf",
    ) -> "LoadedNonBarrelRollerBearingResults":
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
class LoadedNonBarrelRollerBearingResults(_2094.LoadedRollerBearingResults):
    """LoadedNonBarrelRollerBearingResults

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_NON_BARREL_ROLLER_BEARING_RESULTS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def smt_rib_stress(self: "Self") -> "_2137.SMTRibStressResults":
        """mastapy.bearings.bearing_results.rolling.SMTRibStressResults

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SMTRibStress")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedNonBarrelRollerBearingResults":
        """Cast to another type.

        Returns:
            _Cast_LoadedNonBarrelRollerBearingResults
        """
        return _Cast_LoadedNonBarrelRollerBearingResults(self)
