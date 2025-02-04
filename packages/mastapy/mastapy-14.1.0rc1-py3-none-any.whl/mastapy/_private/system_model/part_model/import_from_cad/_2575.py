"""MountableComponentFromCAD"""

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
from mastapy._private.system_model.part_model.import_from_cad import _2565

_MOUNTABLE_COMPONENT_FROM_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD", "MountableComponentFromCAD"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.part_model.import_from_cad import (
        _2564,
        _2566,
        _2567,
        _2568,
        _2569,
        _2570,
        _2571,
        _2572,
        _2573,
        _2577,
        _2578,
        _2579,
    )

    Self = TypeVar("Self", bound="MountableComponentFromCAD")
    CastSelf = TypeVar(
        "CastSelf", bound="MountableComponentFromCAD._Cast_MountableComponentFromCAD"
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentFromCAD",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MountableComponentFromCAD:
    """Special nested class for casting MountableComponentFromCAD to subclasses."""

    __parent__: "MountableComponentFromCAD"

    @property
    def component_from_cad(self: "CastSelf") -> "_2565.ComponentFromCAD":
        return self.__parent__._cast(_2565.ComponentFromCAD)

    @property
    def component_from_cad_base(self: "CastSelf") -> "_2566.ComponentFromCADBase":
        from mastapy._private.system_model.part_model.import_from_cad import _2566

        return self.__parent__._cast(_2566.ComponentFromCADBase)

    @property
    def clutch_from_cad(self: "CastSelf") -> "_2564.ClutchFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2564

        return self.__parent__._cast(_2564.ClutchFromCAD)

    @property
    def concept_bearing_from_cad(self: "CastSelf") -> "_2567.ConceptBearingFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2567

        return self.__parent__._cast(_2567.ConceptBearingFromCAD)

    @property
    def connector_from_cad(self: "CastSelf") -> "_2568.ConnectorFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2568

        return self.__parent__._cast(_2568.ConnectorFromCAD)

    @property
    def cylindrical_gear_from_cad(self: "CastSelf") -> "_2569.CylindricalGearFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2569

        return self.__parent__._cast(_2569.CylindricalGearFromCAD)

    @property
    def cylindrical_gear_in_planetary_set_from_cad(
        self: "CastSelf",
    ) -> "_2570.CylindricalGearInPlanetarySetFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2570

        return self.__parent__._cast(_2570.CylindricalGearInPlanetarySetFromCAD)

    @property
    def cylindrical_planet_gear_from_cad(
        self: "CastSelf",
    ) -> "_2571.CylindricalPlanetGearFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2571

        return self.__parent__._cast(_2571.CylindricalPlanetGearFromCAD)

    @property
    def cylindrical_ring_gear_from_cad(
        self: "CastSelf",
    ) -> "_2572.CylindricalRingGearFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2572

        return self.__parent__._cast(_2572.CylindricalRingGearFromCAD)

    @property
    def cylindrical_sun_gear_from_cad(
        self: "CastSelf",
    ) -> "_2573.CylindricalSunGearFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2573

        return self.__parent__._cast(_2573.CylindricalSunGearFromCAD)

    @property
    def pulley_from_cad(self: "CastSelf") -> "_2577.PulleyFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2577

        return self.__parent__._cast(_2577.PulleyFromCAD)

    @property
    def rigid_connector_from_cad(self: "CastSelf") -> "_2578.RigidConnectorFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2578

        return self.__parent__._cast(_2578.RigidConnectorFromCAD)

    @property
    def rolling_bearing_from_cad(self: "CastSelf") -> "_2579.RollingBearingFromCAD":
        from mastapy._private.system_model.part_model.import_from_cad import _2579

        return self.__parent__._cast(_2579.RollingBearingFromCAD)

    @property
    def mountable_component_from_cad(self: "CastSelf") -> "MountableComponentFromCAD":
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
class MountableComponentFromCAD(_2565.ComponentFromCAD):
    """MountableComponentFromCAD

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MOUNTABLE_COMPONENT_FROM_CAD

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def offset(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "Offset")

        if temp is None:
            return 0.0

        return temp

    @offset.setter
    @enforce_parameter_types
    def offset(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped, "Offset", float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: "Self") -> "_Cast_MountableComponentFromCAD":
        """Cast to another type.

        Returns:
            _Cast_MountableComponentFromCAD
        """
        return _Cast_MountableComponentFromCAD(self)
