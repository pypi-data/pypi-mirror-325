"""CylindricalSocket"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.connections_and_sockets import _2362

_CYLINDRICAL_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "CylindricalSocket"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.connections_and_sockets import (
        _2332,
        _2333,
        _2340,
        _2345,
        _2346,
        _2348,
        _2349,
        _2350,
        _2351,
        _2352,
        _2354,
        _2355,
        _2356,
        _2359,
        _2360,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings import (
        _2409,
        _2411,
        _2413,
        _2415,
        _2417,
        _2419,
        _2420,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal import (
        _2399,
        _2400,
        _2402,
        _2403,
        _2405,
        _2406,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import _2376

    Self = TypeVar("Self", bound="CylindricalSocket")
    CastSelf = TypeVar("CastSelf", bound="CylindricalSocket._Cast_CylindricalSocket")


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalSocket",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalSocket:
    """Special nested class for casting CylindricalSocket to subclasses."""

    __parent__: "CylindricalSocket"

    @property
    def socket(self: "CastSelf") -> "_2362.Socket":
        return self.__parent__._cast(_2362.Socket)

    @property
    def bearing_inner_socket(self: "CastSelf") -> "_2332.BearingInnerSocket":
        from mastapy._private.system_model.connections_and_sockets import _2332

        return self.__parent__._cast(_2332.BearingInnerSocket)

    @property
    def bearing_outer_socket(self: "CastSelf") -> "_2333.BearingOuterSocket":
        from mastapy._private.system_model.connections_and_sockets import _2333

        return self.__parent__._cast(_2333.BearingOuterSocket)

    @property
    def cvt_pulley_socket(self: "CastSelf") -> "_2340.CVTPulleySocket":
        from mastapy._private.system_model.connections_and_sockets import _2340

        return self.__parent__._cast(_2340.CVTPulleySocket)

    @property
    def inner_shaft_socket(self: "CastSelf") -> "_2345.InnerShaftSocket":
        from mastapy._private.system_model.connections_and_sockets import _2345

        return self.__parent__._cast(_2345.InnerShaftSocket)

    @property
    def inner_shaft_socket_base(self: "CastSelf") -> "_2346.InnerShaftSocketBase":
        from mastapy._private.system_model.connections_and_sockets import _2346

        return self.__parent__._cast(_2346.InnerShaftSocketBase)

    @property
    def mountable_component_inner_socket(
        self: "CastSelf",
    ) -> "_2348.MountableComponentInnerSocket":
        from mastapy._private.system_model.connections_and_sockets import _2348

        return self.__parent__._cast(_2348.MountableComponentInnerSocket)

    @property
    def mountable_component_outer_socket(
        self: "CastSelf",
    ) -> "_2349.MountableComponentOuterSocket":
        from mastapy._private.system_model.connections_and_sockets import _2349

        return self.__parent__._cast(_2349.MountableComponentOuterSocket)

    @property
    def mountable_component_socket(
        self: "CastSelf",
    ) -> "_2350.MountableComponentSocket":
        from mastapy._private.system_model.connections_and_sockets import _2350

        return self.__parent__._cast(_2350.MountableComponentSocket)

    @property
    def outer_shaft_socket(self: "CastSelf") -> "_2351.OuterShaftSocket":
        from mastapy._private.system_model.connections_and_sockets import _2351

        return self.__parent__._cast(_2351.OuterShaftSocket)

    @property
    def outer_shaft_socket_base(self: "CastSelf") -> "_2352.OuterShaftSocketBase":
        from mastapy._private.system_model.connections_and_sockets import _2352

        return self.__parent__._cast(_2352.OuterShaftSocketBase)

    @property
    def planetary_socket(self: "CastSelf") -> "_2354.PlanetarySocket":
        from mastapy._private.system_model.connections_and_sockets import _2354

        return self.__parent__._cast(_2354.PlanetarySocket)

    @property
    def planetary_socket_base(self: "CastSelf") -> "_2355.PlanetarySocketBase":
        from mastapy._private.system_model.connections_and_sockets import _2355

        return self.__parent__._cast(_2355.PlanetarySocketBase)

    @property
    def pulley_socket(self: "CastSelf") -> "_2356.PulleySocket":
        from mastapy._private.system_model.connections_and_sockets import _2356

        return self.__parent__._cast(_2356.PulleySocket)

    @property
    def rolling_ring_socket(self: "CastSelf") -> "_2359.RollingRingSocket":
        from mastapy._private.system_model.connections_and_sockets import _2359

        return self.__parent__._cast(_2359.RollingRingSocket)

    @property
    def shaft_socket(self: "CastSelf") -> "_2360.ShaftSocket":
        from mastapy._private.system_model.connections_and_sockets import _2360

        return self.__parent__._cast(_2360.ShaftSocket)

    @property
    def cylindrical_gear_teeth_socket(
        self: "CastSelf",
    ) -> "_2376.CylindricalGearTeethSocket":
        from mastapy._private.system_model.connections_and_sockets.gears import _2376

        return self.__parent__._cast(_2376.CylindricalGearTeethSocket)

    @property
    def cycloidal_disc_axial_left_socket(
        self: "CastSelf",
    ) -> "_2399.CycloidalDiscAxialLeftSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2399,
        )

        return self.__parent__._cast(_2399.CycloidalDiscAxialLeftSocket)

    @property
    def cycloidal_disc_axial_right_socket(
        self: "CastSelf",
    ) -> "_2400.CycloidalDiscAxialRightSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2400,
        )

        return self.__parent__._cast(_2400.CycloidalDiscAxialRightSocket)

    @property
    def cycloidal_disc_inner_socket(
        self: "CastSelf",
    ) -> "_2402.CycloidalDiscInnerSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2402,
        )

        return self.__parent__._cast(_2402.CycloidalDiscInnerSocket)

    @property
    def cycloidal_disc_outer_socket(
        self: "CastSelf",
    ) -> "_2403.CycloidalDiscOuterSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2403,
        )

        return self.__parent__._cast(_2403.CycloidalDiscOuterSocket)

    @property
    def cycloidal_disc_planetary_bearing_socket(
        self: "CastSelf",
    ) -> "_2405.CycloidalDiscPlanetaryBearingSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2405,
        )

        return self.__parent__._cast(_2405.CycloidalDiscPlanetaryBearingSocket)

    @property
    def ring_pins_socket(self: "CastSelf") -> "_2406.RingPinsSocket":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2406,
        )

        return self.__parent__._cast(_2406.RingPinsSocket)

    @property
    def clutch_socket(self: "CastSelf") -> "_2409.ClutchSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2409,
        )

        return self.__parent__._cast(_2409.ClutchSocket)

    @property
    def concept_coupling_socket(self: "CastSelf") -> "_2411.ConceptCouplingSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2411,
        )

        return self.__parent__._cast(_2411.ConceptCouplingSocket)

    @property
    def coupling_socket(self: "CastSelf") -> "_2413.CouplingSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2413,
        )

        return self.__parent__._cast(_2413.CouplingSocket)

    @property
    def part_to_part_shear_coupling_socket(
        self: "CastSelf",
    ) -> "_2415.PartToPartShearCouplingSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2415,
        )

        return self.__parent__._cast(_2415.PartToPartShearCouplingSocket)

    @property
    def spring_damper_socket(self: "CastSelf") -> "_2417.SpringDamperSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2417,
        )

        return self.__parent__._cast(_2417.SpringDamperSocket)

    @property
    def torque_converter_pump_socket(
        self: "CastSelf",
    ) -> "_2419.TorqueConverterPumpSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2419,
        )

        return self.__parent__._cast(_2419.TorqueConverterPumpSocket)

    @property
    def torque_converter_turbine_socket(
        self: "CastSelf",
    ) -> "_2420.TorqueConverterTurbineSocket":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2420,
        )

        return self.__parent__._cast(_2420.TorqueConverterTurbineSocket)

    @property
    def cylindrical_socket(self: "CastSelf") -> "CylindricalSocket":
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
class CylindricalSocket(_2362.Socket):
    """CylindricalSocket

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CYLINDRICAL_SOCKET

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_CylindricalSocket":
        """Cast to another type.

        Returns:
            _Cast_CylindricalSocket
        """
        return _Cast_CylindricalSocket(self)
