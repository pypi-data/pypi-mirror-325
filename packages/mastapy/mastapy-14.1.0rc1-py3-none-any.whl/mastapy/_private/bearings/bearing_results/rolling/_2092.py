"""LoadedNonBarrelRollerElement"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.bearings.bearing_results.rolling import _2093

_LOADED_NON_BARREL_ROLLER_ELEMENT = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedNonBarrelRollerElement"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.bearings.bearing_results.rolling import (
        _2058,
        _2061,
        _2073,
        _2079,
        _2085,
        _2112,
    )

    Self = TypeVar("Self", bound="LoadedNonBarrelRollerElement")
    CastSelf = TypeVar(
        "CastSelf",
        bound="LoadedNonBarrelRollerElement._Cast_LoadedNonBarrelRollerElement",
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonBarrelRollerElement",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_LoadedNonBarrelRollerElement:
    """Special nested class for casting LoadedNonBarrelRollerElement to subclasses."""

    __parent__: "LoadedNonBarrelRollerElement"

    @property
    def loaded_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2093.LoadedRollerBearingElement":
        return self.__parent__._cast(_2093.LoadedRollerBearingElement)

    @property
    def loaded_element(self: "CastSelf") -> "_2079.LoadedElement":
        from mastapy._private.bearings.bearing_results.rolling import _2079

        return self.__parent__._cast(_2079.LoadedElement)

    @property
    def loaded_axial_thrust_cylindrical_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2058.LoadedAxialThrustCylindricalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2058

        return self.__parent__._cast(
            _2058.LoadedAxialThrustCylindricalRollerBearingElement
        )

    @property
    def loaded_axial_thrust_needle_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2061.LoadedAxialThrustNeedleRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2061

        return self.__parent__._cast(_2061.LoadedAxialThrustNeedleRollerBearingElement)

    @property
    def loaded_cylindrical_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2073.LoadedCylindricalRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2073

        return self.__parent__._cast(_2073.LoadedCylindricalRollerBearingElement)

    @property
    def loaded_needle_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2085.LoadedNeedleRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2085

        return self.__parent__._cast(_2085.LoadedNeedleRollerBearingElement)

    @property
    def loaded_taper_roller_bearing_element(
        self: "CastSelf",
    ) -> "_2112.LoadedTaperRollerBearingElement":
        from mastapy._private.bearings.bearing_results.rolling import _2112

        return self.__parent__._cast(_2112.LoadedTaperRollerBearingElement)

    @property
    def loaded_non_barrel_roller_element(
        self: "CastSelf",
    ) -> "LoadedNonBarrelRollerElement":
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
class LoadedNonBarrelRollerElement(_2093.LoadedRollerBearingElement):
    """LoadedNonBarrelRollerElement

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _LOADED_NON_BARREL_ROLLER_ELEMENT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def minimum_smt_rib_stress_safety_factor(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "MinimumSMTRibStressSafetyFactor")

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: "Self") -> "_Cast_LoadedNonBarrelRollerElement":
        """Cast to another type.

        Returns:
            _Cast_LoadedNonBarrelRollerElement
        """
        return _Cast_LoadedNonBarrelRollerElement(self)
