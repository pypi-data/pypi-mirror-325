"""InterMountableComponentConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.system_model.connections_and_sockets import _2338

_INTER_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "InterMountableComponentConnection",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.connections_and_sockets import (
        _2334,
        _2339,
        _2358,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings import (
        _2408,
        _2410,
        _2412,
        _2414,
        _2416,
        _2418,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal import _2407
    from mastapy._private.system_model.connections_and_sockets.gears import (
        _2365,
        _2367,
        _2369,
        _2371,
        _2373,
        _2375,
        _2377,
        _2379,
        _2381,
        _2384,
        _2385,
        _2386,
        _2389,
        _2391,
        _2393,
        _2395,
        _2397,
    )

    Self = TypeVar("Self", bound="InterMountableComponentConnection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="InterMountableComponentConnection._Cast_InterMountableComponentConnection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_InterMountableComponentConnection:
    """Special nested class for casting InterMountableComponentConnection to subclasses."""

    __parent__: "InterMountableComponentConnection"

    @property
    def connection(self: "CastSelf") -> "_2338.Connection":
        return self.__parent__._cast(_2338.Connection)

    @property
    def design_entity(self: "CastSelf") -> "_2269.DesignEntity":
        from mastapy._private.system_model import _2269

        return self.__parent__._cast(_2269.DesignEntity)

    @property
    def belt_connection(self: "CastSelf") -> "_2334.BeltConnection":
        from mastapy._private.system_model.connections_and_sockets import _2334

        return self.__parent__._cast(_2334.BeltConnection)

    @property
    def cvt_belt_connection(self: "CastSelf") -> "_2339.CVTBeltConnection":
        from mastapy._private.system_model.connections_and_sockets import _2339

        return self.__parent__._cast(_2339.CVTBeltConnection)

    @property
    def rolling_ring_connection(self: "CastSelf") -> "_2358.RollingRingConnection":
        from mastapy._private.system_model.connections_and_sockets import _2358

        return self.__parent__._cast(_2358.RollingRingConnection)

    @property
    def agma_gleason_conical_gear_mesh(
        self: "CastSelf",
    ) -> "_2365.AGMAGleasonConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2365

        return self.__parent__._cast(_2365.AGMAGleasonConicalGearMesh)

    @property
    def bevel_differential_gear_mesh(
        self: "CastSelf",
    ) -> "_2367.BevelDifferentialGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2367

        return self.__parent__._cast(_2367.BevelDifferentialGearMesh)

    @property
    def bevel_gear_mesh(self: "CastSelf") -> "_2369.BevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2369

        return self.__parent__._cast(_2369.BevelGearMesh)

    @property
    def concept_gear_mesh(self: "CastSelf") -> "_2371.ConceptGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2371

        return self.__parent__._cast(_2371.ConceptGearMesh)

    @property
    def conical_gear_mesh(self: "CastSelf") -> "_2373.ConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2373

        return self.__parent__._cast(_2373.ConicalGearMesh)

    @property
    def cylindrical_gear_mesh(self: "CastSelf") -> "_2375.CylindricalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2375

        return self.__parent__._cast(_2375.CylindricalGearMesh)

    @property
    def face_gear_mesh(self: "CastSelf") -> "_2377.FaceGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2377

        return self.__parent__._cast(_2377.FaceGearMesh)

    @property
    def gear_mesh(self: "CastSelf") -> "_2379.GearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2379

        return self.__parent__._cast(_2379.GearMesh)

    @property
    def hypoid_gear_mesh(self: "CastSelf") -> "_2381.HypoidGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2381

        return self.__parent__._cast(_2381.HypoidGearMesh)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh(
        self: "CastSelf",
    ) -> "_2384.KlingelnbergCycloPalloidConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2384

        return self.__parent__._cast(_2384.KlingelnbergCycloPalloidConicalGearMesh)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
        self: "CastSelf",
    ) -> "_2385.KlingelnbergCycloPalloidHypoidGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2385

        return self.__parent__._cast(_2385.KlingelnbergCycloPalloidHypoidGearMesh)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
        self: "CastSelf",
    ) -> "_2386.KlingelnbergCycloPalloidSpiralBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2386

        return self.__parent__._cast(_2386.KlingelnbergCycloPalloidSpiralBevelGearMesh)

    @property
    def spiral_bevel_gear_mesh(self: "CastSelf") -> "_2389.SpiralBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2389

        return self.__parent__._cast(_2389.SpiralBevelGearMesh)

    @property
    def straight_bevel_diff_gear_mesh(
        self: "CastSelf",
    ) -> "_2391.StraightBevelDiffGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2391

        return self.__parent__._cast(_2391.StraightBevelDiffGearMesh)

    @property
    def straight_bevel_gear_mesh(self: "CastSelf") -> "_2393.StraightBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2393

        return self.__parent__._cast(_2393.StraightBevelGearMesh)

    @property
    def worm_gear_mesh(self: "CastSelf") -> "_2395.WormGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2395

        return self.__parent__._cast(_2395.WormGearMesh)

    @property
    def zerol_bevel_gear_mesh(self: "CastSelf") -> "_2397.ZerolBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2397

        return self.__parent__._cast(_2397.ZerolBevelGearMesh)

    @property
    def ring_pins_to_disc_connection(
        self: "CastSelf",
    ) -> "_2407.RingPinsToDiscConnection":
        from mastapy._private.system_model.connections_and_sockets.cycloidal import (
            _2407,
        )

        return self.__parent__._cast(_2407.RingPinsToDiscConnection)

    @property
    def clutch_connection(self: "CastSelf") -> "_2408.ClutchConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2408,
        )

        return self.__parent__._cast(_2408.ClutchConnection)

    @property
    def concept_coupling_connection(
        self: "CastSelf",
    ) -> "_2410.ConceptCouplingConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2410,
        )

        return self.__parent__._cast(_2410.ConceptCouplingConnection)

    @property
    def coupling_connection(self: "CastSelf") -> "_2412.CouplingConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2412,
        )

        return self.__parent__._cast(_2412.CouplingConnection)

    @property
    def part_to_part_shear_coupling_connection(
        self: "CastSelf",
    ) -> "_2414.PartToPartShearCouplingConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2414,
        )

        return self.__parent__._cast(_2414.PartToPartShearCouplingConnection)

    @property
    def spring_damper_connection(self: "CastSelf") -> "_2416.SpringDamperConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2416,
        )

        return self.__parent__._cast(_2416.SpringDamperConnection)

    @property
    def torque_converter_connection(
        self: "CastSelf",
    ) -> "_2418.TorqueConverterConnection":
        from mastapy._private.system_model.connections_and_sockets.couplings import (
            _2418,
        )

        return self.__parent__._cast(_2418.TorqueConverterConnection)

    @property
    def inter_mountable_component_connection(
        self: "CastSelf",
    ) -> "InterMountableComponentConnection":
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
class InterMountableComponentConnection(_2338.Connection):
    """InterMountableComponentConnection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _INTER_MOUNTABLE_COMPONENT_CONNECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def additional_modal_damping_ratio(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "AdditionalModalDampingRatio")

        if temp is None:
            return 0.0

        return temp

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "AdditionalModalDampingRatio",
            float(value) if value is not None else 0.0,
        )

    @property
    def cast_to(self: "Self") -> "_Cast_InterMountableComponentConnection":
        """Cast to another type.

        Returns:
            _Cast_InterMountableComponentConnection
        """
        return _Cast_InterMountableComponentConnection(self)
