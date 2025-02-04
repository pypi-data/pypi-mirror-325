"""LoadedSelfAligningBallBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.bearings.bearing_results.rolling import _2067

_LOADED_SELF_ALIGNING_BALL_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedSelfAligningBallBearingResults",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings import _1939
    from mastapy._private.bearings.bearing_results import _2014, _2019, _2022
    from mastapy._private.bearings.bearing_results.rolling import _2098

    Self = TypeVar("Self", bound="LoadedSelfAligningBallBearingResults")
    CastSelf = TypeVar(
        "CastSelf",
        bound="LoadedSelfAligningBallBearingResults._Cast_LoadedSelfAligningBallBearingResults",
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedSelfAligningBallBearingResults",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedSelfAligningBallBearingResults:
    """Special nested class for casting LoadedSelfAligningBallBearingResults to subclasses."""

    __parent__: "LoadedSelfAligningBallBearingResults"

    @property
    def loaded_ball_bearing_results(
        self: "CastSelf",
    ) -> "_2067.LoadedBallBearingResults":
        return self.__parent__._cast(_2067.LoadedBallBearingResults)

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
    def loaded_self_aligning_ball_bearing_results(
        self: "CastSelf",
    ) -> "LoadedSelfAligningBallBearingResults":
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
class LoadedSelfAligningBallBearingResults(_2067.LoadedBallBearingResults):
    """LoadedSelfAligningBallBearingResults

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_SELF_ALIGNING_BALL_BEARING_RESULTS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedSelfAligningBallBearingResults":
        """Cast to another type.

        Returns:
            _Cast_LoadedSelfAligningBallBearingResults
        """
        return _Cast_LoadedSelfAligningBallBearingResults(self)
