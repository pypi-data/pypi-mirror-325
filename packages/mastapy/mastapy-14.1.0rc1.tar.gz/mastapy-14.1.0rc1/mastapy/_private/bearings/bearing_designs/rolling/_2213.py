"""CrossedRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.bearings.bearing_designs.rolling import _2227

_CROSSED_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "CrossedRollerBearing"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_designs import _2195, _2196, _2199
    from mastapy._private.bearings.bearing_designs.rolling import _2230

    Self = TypeVar("Self", bound="CrossedRollerBearing")
    CastSelf = TypeVar(
        "CastSelf", bound="CrossedRollerBearing._Cast_CrossedRollerBearing"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CrossedRollerBearing",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CrossedRollerBearing:
    """Special nested class for casting CrossedRollerBearing to subclasses."""

    __parent__: "CrossedRollerBearing"

    @property
    def roller_bearing(self: "CastSelf") -> "_2227.RollerBearing":
        return self.__parent__._cast(_2227.RollerBearing)

    @property
    def rolling_bearing(self: "CastSelf") -> "_2230.RollingBearing":
        from mastapy._private.bearings.bearing_designs.rolling import _2230

        return self.__parent__._cast(_2230.RollingBearing)

    @property
    def detailed_bearing(self: "CastSelf") -> "_2196.DetailedBearing":
        from mastapy._private.bearings.bearing_designs import _2196

        return self.__parent__._cast(_2196.DetailedBearing)

    @property
    def non_linear_bearing(self: "CastSelf") -> "_2199.NonLinearBearing":
        from mastapy._private.bearings.bearing_designs import _2199

        return self.__parent__._cast(_2199.NonLinearBearing)

    @property
    def bearing_design(self: "CastSelf") -> "_2195.BearingDesign":
        from mastapy._private.bearings.bearing_designs import _2195

        return self.__parent__._cast(_2195.BearingDesign)

    @property
    def crossed_roller_bearing(self: "CastSelf") -> "CrossedRollerBearing":
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
class CrossedRollerBearing(_2227.RollerBearing):
    """CrossedRollerBearing

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CROSSED_ROLLER_BEARING

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CrossedRollerBearing":
        """Cast to another type.

        Returns:
            _Cast_CrossedRollerBearing
        """
        return _Cast_CrossedRollerBearing(self)
