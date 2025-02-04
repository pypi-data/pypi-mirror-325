"""MultiNodeFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.fe.links import _2485

_MULTI_NODE_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "MultiNodeFELink"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.fe.links import (
        _2486,
        _2488,
        _2489,
        _2490,
        _2491,
        _2493,
        _2494,
        _2495,
        _2496,
        _2497,
        _2498,
    )

    Self = TypeVar("Self", bound="MultiNodeFELink")
    CastSelf = TypeVar("CastSelf", bound="MultiNodeFELink._Cast_MultiNodeFELink")


__docformat__ = "restructuredtext en"
__all__ = ("MultiNodeFELink",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MultiNodeFELink:
    """Special nested class for casting MultiNodeFELink to subclasses."""

    __parent__: "MultiNodeFELink"

    @property
    def fe_link(self: "CastSelf") -> "_2485.FELink":
        return self.__parent__._cast(_2485.FELink)

    @property
    def electric_machine_stator_fe_link(
        self: "CastSelf",
    ) -> "_2486.ElectricMachineStatorFELink":
        from mastapy._private.system_model.fe.links import _2486

        return self.__parent__._cast(_2486.ElectricMachineStatorFELink)

    @property
    def gear_mesh_fe_link(self: "CastSelf") -> "_2488.GearMeshFELink":
        from mastapy._private.system_model.fe.links import _2488

        return self.__parent__._cast(_2488.GearMeshFELink)

    @property
    def gear_with_duplicated_meshes_fe_link(
        self: "CastSelf",
    ) -> "_2489.GearWithDuplicatedMeshesFELink":
        from mastapy._private.system_model.fe.links import _2489

        return self.__parent__._cast(_2489.GearWithDuplicatedMeshesFELink)

    @property
    def multi_angle_connection_fe_link(
        self: "CastSelf",
    ) -> "_2490.MultiAngleConnectionFELink":
        from mastapy._private.system_model.fe.links import _2490

        return self.__parent__._cast(_2490.MultiAngleConnectionFELink)

    @property
    def multi_node_connector_fe_link(
        self: "CastSelf",
    ) -> "_2491.MultiNodeConnectorFELink":
        from mastapy._private.system_model.fe.links import _2491

        return self.__parent__._cast(_2491.MultiNodeConnectorFELink)

    @property
    def planetary_connector_multi_node_fe_link(
        self: "CastSelf",
    ) -> "_2493.PlanetaryConnectorMultiNodeFELink":
        from mastapy._private.system_model.fe.links import _2493

        return self.__parent__._cast(_2493.PlanetaryConnectorMultiNodeFELink)

    @property
    def planet_based_fe_link(self: "CastSelf") -> "_2494.PlanetBasedFELink":
        from mastapy._private.system_model.fe.links import _2494

        return self.__parent__._cast(_2494.PlanetBasedFELink)

    @property
    def planet_carrier_fe_link(self: "CastSelf") -> "_2495.PlanetCarrierFELink":
        from mastapy._private.system_model.fe.links import _2495

        return self.__parent__._cast(_2495.PlanetCarrierFELink)

    @property
    def point_load_fe_link(self: "CastSelf") -> "_2496.PointLoadFELink":
        from mastapy._private.system_model.fe.links import _2496

        return self.__parent__._cast(_2496.PointLoadFELink)

    @property
    def rolling_ring_connection_fe_link(
        self: "CastSelf",
    ) -> "_2497.RollingRingConnectionFELink":
        from mastapy._private.system_model.fe.links import _2497

        return self.__parent__._cast(_2497.RollingRingConnectionFELink)

    @property
    def shaft_hub_connection_fe_link(
        self: "CastSelf",
    ) -> "_2498.ShaftHubConnectionFELink":
        from mastapy._private.system_model.fe.links import _2498

        return self.__parent__._cast(_2498.ShaftHubConnectionFELink)

    @property
    def multi_node_fe_link(self: "CastSelf") -> "MultiNodeFELink":
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
class MultiNodeFELink(_2485.FELink):
    """MultiNodeFELink

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MULTI_NODE_FE_LINK

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_MultiNodeFELink":
        """Cast to another type.

        Returns:
            _Cast_MultiNodeFELink
        """
        return _Cast_MultiNodeFELink(self)
