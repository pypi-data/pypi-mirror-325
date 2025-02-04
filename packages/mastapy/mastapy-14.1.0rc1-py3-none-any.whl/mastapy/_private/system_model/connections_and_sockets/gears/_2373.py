"""ConicalGearMesh"""

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
from mastapy._private.system_model.connections_and_sockets.gears import _2379

_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearMesh"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.connections_and_sockets import _2338, _2347
    from mastapy._private.system_model.connections_and_sockets.gears import (
        _2365,
        _2367,
        _2369,
        _2381,
        _2384,
        _2385,
        _2386,
        _2389,
        _2391,
        _2393,
        _2397,
    )

    Self = TypeVar("Self", bound="ConicalGearMesh")
    CastSelf = TypeVar("CastSelf", bound="ConicalGearMesh._Cast_ConicalGearMesh")


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMesh",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearMesh:
    """Special nested class for casting ConicalGearMesh to subclasses."""

    __parent__: "ConicalGearMesh"

    @property
    def gear_mesh(self: "CastSelf") -> "_2379.GearMesh":
        return self.__parent__._cast(_2379.GearMesh)

    @property
    def inter_mountable_component_connection(
        self: "CastSelf",
    ) -> "_2347.InterMountableComponentConnection":
        from mastapy._private.system_model.connections_and_sockets import _2347

        return self.__parent__._cast(_2347.InterMountableComponentConnection)

    @property
    def connection(self: "CastSelf") -> "_2338.Connection":
        from mastapy._private.system_model.connections_and_sockets import _2338

        return self.__parent__._cast(_2338.Connection)

    @property
    def design_entity(self: "CastSelf") -> "_2269.DesignEntity":
        from mastapy._private.system_model import _2269

        return self.__parent__._cast(_2269.DesignEntity)

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
    def zerol_bevel_gear_mesh(self: "CastSelf") -> "_2397.ZerolBevelGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2397

        return self.__parent__._cast(_2397.ZerolBevelGearMesh)

    @property
    def conical_gear_mesh(self: "CastSelf") -> "ConicalGearMesh":
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
class ConicalGearMesh(_2379.GearMesh):
    """ConicalGearMesh

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_MESH

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def crowning(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "Crowning")

        if temp is None:
            return 0.0

        return temp

    @crowning.setter
    @enforce_parameter_types
    def crowning(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped, "Crowning", float(value) if value is not None else 0.0
        )

    @property
    def pinion_drop_angle(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "PinionDropAngle")

        if temp is None:
            return 0.0

        return temp

    @pinion_drop_angle.setter
    @enforce_parameter_types
    def pinion_drop_angle(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped, "PinionDropAngle", float(value) if value is not None else 0.0
        )

    @property
    def wheel_drop_angle(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "WheelDropAngle")

        if temp is None:
            return 0.0

        return temp

    @wheel_drop_angle.setter
    @enforce_parameter_types
    def wheel_drop_angle(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped, "WheelDropAngle", float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalGearMesh":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearMesh
        """
        return _Cast_ConicalGearMesh(self)
