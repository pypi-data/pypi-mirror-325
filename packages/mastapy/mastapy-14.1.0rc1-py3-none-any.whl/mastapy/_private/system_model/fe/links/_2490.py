"""MultiAngleConnectionFELink"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.fe.links import _2492

_MULTI_ANGLE_CONNECTION_FE_LINK = python_net_import(
    "SMT.MastaAPI.SystemModel.FE.Links", "MultiAngleConnectionFELink"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.fe.links import _2485, _2488, _2497

    Self = TypeVar("Self", bound="MultiAngleConnectionFELink")
    CastSelf = TypeVar(
        "CastSelf", bound="MultiAngleConnectionFELink._Cast_MultiAngleConnectionFELink"
    )


__docformat__ = "restructuredtext en"
__all__ = ("MultiAngleConnectionFELink",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MultiAngleConnectionFELink:
    """Special nested class for casting MultiAngleConnectionFELink to subclasses."""

    __parent__: "MultiAngleConnectionFELink"

    @property
    def multi_node_fe_link(self: "CastSelf") -> "_2492.MultiNodeFELink":
        return self.__parent__._cast(_2492.MultiNodeFELink)

    @property
    def fe_link(self: "CastSelf") -> "_2485.FELink":
        from mastapy._private.system_model.fe.links import _2485

        return self.__parent__._cast(_2485.FELink)

    @property
    def gear_mesh_fe_link(self: "CastSelf") -> "_2488.GearMeshFELink":
        from mastapy._private.system_model.fe.links import _2488

        return self.__parent__._cast(_2488.GearMeshFELink)

    @property
    def rolling_ring_connection_fe_link(
        self: "CastSelf",
    ) -> "_2497.RollingRingConnectionFELink":
        from mastapy._private.system_model.fe.links import _2497

        return self.__parent__._cast(_2497.RollingRingConnectionFELink)

    @property
    def multi_angle_connection_fe_link(
        self: "CastSelf",
    ) -> "MultiAngleConnectionFELink":
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
class MultiAngleConnectionFELink(_2492.MultiNodeFELink):
    """MultiAngleConnectionFELink

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MULTI_ANGLE_CONNECTION_FE_LINK

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_MultiAngleConnectionFELink":
        """Cast to another type.

        Returns:
            _Cast_MultiAngleConnectionFELink
        """
        return _Cast_MultiAngleConnectionFELink(self)
