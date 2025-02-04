"""ZerolBevelGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.connections_and_sockets.gears import _2369

_ZEROL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ZerolBevelGearMesh"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.gears.gear_designs.zerol_bevel import _985
    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.connections_and_sockets import _2338, _2347
    from mastapy._private.system_model.connections_and_sockets.gears import (
        _2365,
        _2373,
        _2379,
    )

    Self = TypeVar("Self", bound="ZerolBevelGearMesh")
    CastSelf = TypeVar("CastSelf", bound="ZerolBevelGearMesh._Cast_ZerolBevelGearMesh")


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMesh",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ZerolBevelGearMesh:
    """Special nested class for casting ZerolBevelGearMesh to subclasses."""

    __parent__: "ZerolBevelGearMesh"

    @property
    def bevel_gear_mesh(self: "CastSelf") -> "_2369.BevelGearMesh":
        return self.__parent__._cast(_2369.BevelGearMesh)

    @property
    def agma_gleason_conical_gear_mesh(
        self: "CastSelf",
    ) -> "_2365.AGMAGleasonConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2365

        return self.__parent__._cast(_2365.AGMAGleasonConicalGearMesh)

    @property
    def conical_gear_mesh(self: "CastSelf") -> "_2373.ConicalGearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2373

        return self.__parent__._cast(_2373.ConicalGearMesh)

    @property
    def gear_mesh(self: "CastSelf") -> "_2379.GearMesh":
        from mastapy._private.system_model.connections_and_sockets.gears import _2379

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
    def zerol_bevel_gear_mesh(self: "CastSelf") -> "ZerolBevelGearMesh":
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
class ZerolBevelGearMesh(_2369.BevelGearMesh):
    """ZerolBevelGearMesh

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ZEROL_BEVEL_GEAR_MESH

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bevel_gear_mesh_design(self: "Self") -> "_985.ZerolBevelGearMeshDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "BevelGearMeshDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gear_mesh_design(self: "Self") -> "_985.ZerolBevelGearMeshDesign":
        """mastapy.gears.gear_designs.zerol_bevel.ZerolBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ZerolBevelGearMeshDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ZerolBevelGearMesh":
        """Cast to another type.

        Returns:
            _Cast_ZerolBevelGearMesh
        """
        return _Cast_ZerolBevelGearMesh(self)
