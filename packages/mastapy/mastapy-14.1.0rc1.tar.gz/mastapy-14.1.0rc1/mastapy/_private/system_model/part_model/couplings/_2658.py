"""CouplingHalf"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.system_model.part_model import _2533

_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
)

if TYPE_CHECKING:
    from typing import Any, Tuple, Type, TypeVar, Union

    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.part_model import _2511, _2537
    from mastapy._private.system_model.part_model.couplings import (
        _2652,
        _2655,
        _2661,
        _2663,
        _2665,
        _2672,
        _2681,
        _2684,
        _2685,
        _2686,
        _2688,
        _2690,
    )

    Self = TypeVar("Self", bound="CouplingHalf")
    CastSelf = TypeVar("CastSelf", bound="CouplingHalf._Cast_CouplingHalf")


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalf",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalf:
    """Special nested class for casting CouplingHalf to subclasses."""

    __parent__: "CouplingHalf"

    @property
    def mountable_component(self: "CastSelf") -> "_2533.MountableComponent":
        return self.__parent__._cast(_2533.MountableComponent)

    @property
    def component(self: "CastSelf") -> "_2511.Component":
        from mastapy._private.system_model.part_model import _2511

        return self.__parent__._cast(_2511.Component)

    @property
    def part(self: "CastSelf") -> "_2537.Part":
        from mastapy._private.system_model.part_model import _2537

        return self.__parent__._cast(_2537.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2269.DesignEntity":
        from mastapy._private.system_model import _2269

        return self.__parent__._cast(_2269.DesignEntity)

    @property
    def clutch_half(self: "CastSelf") -> "_2652.ClutchHalf":
        from mastapy._private.system_model.part_model.couplings import _2652

        return self.__parent__._cast(_2652.ClutchHalf)

    @property
    def concept_coupling_half(self: "CastSelf") -> "_2655.ConceptCouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2655

        return self.__parent__._cast(_2655.ConceptCouplingHalf)

    @property
    def cvt_pulley(self: "CastSelf") -> "_2661.CVTPulley":
        from mastapy._private.system_model.part_model.couplings import _2661

        return self.__parent__._cast(_2661.CVTPulley)

    @property
    def part_to_part_shear_coupling_half(
        self: "CastSelf",
    ) -> "_2663.PartToPartShearCouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2663

        return self.__parent__._cast(_2663.PartToPartShearCouplingHalf)

    @property
    def pulley(self: "CastSelf") -> "_2665.Pulley":
        from mastapy._private.system_model.part_model.couplings import _2665

        return self.__parent__._cast(_2665.Pulley)

    @property
    def rolling_ring(self: "CastSelf") -> "_2672.RollingRing":
        from mastapy._private.system_model.part_model.couplings import _2672

        return self.__parent__._cast(_2672.RollingRing)

    @property
    def spring_damper_half(self: "CastSelf") -> "_2681.SpringDamperHalf":
        from mastapy._private.system_model.part_model.couplings import _2681

        return self.__parent__._cast(_2681.SpringDamperHalf)

    @property
    def synchroniser_half(self: "CastSelf") -> "_2684.SynchroniserHalf":
        from mastapy._private.system_model.part_model.couplings import _2684

        return self.__parent__._cast(_2684.SynchroniserHalf)

    @property
    def synchroniser_part(self: "CastSelf") -> "_2685.SynchroniserPart":
        from mastapy._private.system_model.part_model.couplings import _2685

        return self.__parent__._cast(_2685.SynchroniserPart)

    @property
    def synchroniser_sleeve(self: "CastSelf") -> "_2686.SynchroniserSleeve":
        from mastapy._private.system_model.part_model.couplings import _2686

        return self.__parent__._cast(_2686.SynchroniserSleeve)

    @property
    def torque_converter_pump(self: "CastSelf") -> "_2688.TorqueConverterPump":
        from mastapy._private.system_model.part_model.couplings import _2688

        return self.__parent__._cast(_2688.TorqueConverterPump)

    @property
    def torque_converter_turbine(self: "CastSelf") -> "_2690.TorqueConverterTurbine":
        from mastapy._private.system_model.part_model.couplings import _2690

        return self.__parent__._cast(_2690.TorqueConverterTurbine)

    @property
    def coupling_half(self: "CastSelf") -> "CouplingHalf":
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
class CouplingHalf(_2533.MountableComponent):
    """CouplingHalf

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_HALF

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def bore(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = pythonnet_property_get(self.wrapped, "Bore")

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bore.setter
    @enforce_parameter_types
    def bore(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        pythonnet_property_set(self.wrapped, "Bore", value)

    @property
    def diameter(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = pythonnet_property_get(self.wrapped, "Diameter")

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        pythonnet_property_set(self.wrapped, "Diameter", value)

    @property
    def width(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "Width")

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped, "Width", float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: "Self") -> "_Cast_CouplingHalf":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalf
        """
        return _Cast_CouplingHalf(self)
