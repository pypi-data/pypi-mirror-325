"""MountableComponent"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_method_call,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.system_model.part_model import _2511

_MOUNTABLE_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "MountableComponent"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.connections_and_sockets import (
        _2335,
        _2338,
        _2342,
    )
    from mastapy._private.system_model.part_model import (
        _2502,
        _2506,
        _2512,
        _2514,
        _2529,
        _2530,
        _2535,
        _2537,
        _2538,
        _2540,
        _2541,
        _2547,
        _2549,
    )
    from mastapy._private.system_model.part_model.couplings import (
        _2652,
        _2655,
        _2658,
        _2661,
        _2663,
        _2665,
        _2672,
        _2674,
        _2681,
        _2684,
        _2685,
        _2686,
        _2688,
        _2690,
    )
    from mastapy._private.system_model.part_model.cycloidal import _2642
    from mastapy._private.system_model.part_model.gears import (
        _2585,
        _2587,
        _2589,
        _2590,
        _2591,
        _2593,
        _2595,
        _2597,
        _2599,
        _2600,
        _2602,
        _2606,
        _2608,
        _2610,
        _2612,
        _2615,
        _2617,
        _2619,
        _2621,
        _2622,
        _2623,
        _2625,
    )

    Self = TypeVar("Self", bound="MountableComponent")
    CastSelf = TypeVar("CastSelf", bound="MountableComponent._Cast_MountableComponent")


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponent",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MountableComponent:
    """Special nested class for casting MountableComponent to subclasses."""

    __parent__: "MountableComponent"

    @property
    def component(self: "CastSelf") -> "_2511.Component":
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
    def bearing(self: "CastSelf") -> "_2506.Bearing":
        from mastapy._private.system_model.part_model import _2506

        return self.__parent__._cast(_2506.Bearing)

    @property
    def connector(self: "CastSelf") -> "_2514.Connector":
        from mastapy._private.system_model.part_model import _2514

        return self.__parent__._cast(_2514.Connector)

    @property
    def mass_disc(self: "CastSelf") -> "_2529.MassDisc":
        from mastapy._private.system_model.part_model import _2529

        return self.__parent__._cast(_2529.MassDisc)

    @property
    def measurement_component(self: "CastSelf") -> "_2530.MeasurementComponent":
        from mastapy._private.system_model.part_model import _2530

        return self.__parent__._cast(_2530.MeasurementComponent)

    @property
    def oil_seal(self: "CastSelf") -> "_2535.OilSeal":
        from mastapy._private.system_model.part_model import _2535

        return self.__parent__._cast(_2535.OilSeal)

    @property
    def planet_carrier(self: "CastSelf") -> "_2538.PlanetCarrier":
        from mastapy._private.system_model.part_model import _2538

        return self.__parent__._cast(_2538.PlanetCarrier)

    @property
    def point_load(self: "CastSelf") -> "_2540.PointLoad":
        from mastapy._private.system_model.part_model import _2540

        return self.__parent__._cast(_2540.PointLoad)

    @property
    def power_load(self: "CastSelf") -> "_2541.PowerLoad":
        from mastapy._private.system_model.part_model import _2541

        return self.__parent__._cast(_2541.PowerLoad)

    @property
    def unbalanced_mass(self: "CastSelf") -> "_2547.UnbalancedMass":
        from mastapy._private.system_model.part_model import _2547

        return self.__parent__._cast(_2547.UnbalancedMass)

    @property
    def virtual_component(self: "CastSelf") -> "_2549.VirtualComponent":
        from mastapy._private.system_model.part_model import _2549

        return self.__parent__._cast(_2549.VirtualComponent)

    @property
    def agma_gleason_conical_gear(self: "CastSelf") -> "_2585.AGMAGleasonConicalGear":
        from mastapy._private.system_model.part_model.gears import _2585

        return self.__parent__._cast(_2585.AGMAGleasonConicalGear)

    @property
    def bevel_differential_gear(self: "CastSelf") -> "_2587.BevelDifferentialGear":
        from mastapy._private.system_model.part_model.gears import _2587

        return self.__parent__._cast(_2587.BevelDifferentialGear)

    @property
    def bevel_differential_planet_gear(
        self: "CastSelf",
    ) -> "_2589.BevelDifferentialPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2589

        return self.__parent__._cast(_2589.BevelDifferentialPlanetGear)

    @property
    def bevel_differential_sun_gear(
        self: "CastSelf",
    ) -> "_2590.BevelDifferentialSunGear":
        from mastapy._private.system_model.part_model.gears import _2590

        return self.__parent__._cast(_2590.BevelDifferentialSunGear)

    @property
    def bevel_gear(self: "CastSelf") -> "_2591.BevelGear":
        from mastapy._private.system_model.part_model.gears import _2591

        return self.__parent__._cast(_2591.BevelGear)

    @property
    def concept_gear(self: "CastSelf") -> "_2593.ConceptGear":
        from mastapy._private.system_model.part_model.gears import _2593

        return self.__parent__._cast(_2593.ConceptGear)

    @property
    def conical_gear(self: "CastSelf") -> "_2595.ConicalGear":
        from mastapy._private.system_model.part_model.gears import _2595

        return self.__parent__._cast(_2595.ConicalGear)

    @property
    def cylindrical_gear(self: "CastSelf") -> "_2597.CylindricalGear":
        from mastapy._private.system_model.part_model.gears import _2597

        return self.__parent__._cast(_2597.CylindricalGear)

    @property
    def cylindrical_planet_gear(self: "CastSelf") -> "_2599.CylindricalPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2599

        return self.__parent__._cast(_2599.CylindricalPlanetGear)

    @property
    def face_gear(self: "CastSelf") -> "_2600.FaceGear":
        from mastapy._private.system_model.part_model.gears import _2600

        return self.__parent__._cast(_2600.FaceGear)

    @property
    def gear(self: "CastSelf") -> "_2602.Gear":
        from mastapy._private.system_model.part_model.gears import _2602

        return self.__parent__._cast(_2602.Gear)

    @property
    def hypoid_gear(self: "CastSelf") -> "_2606.HypoidGear":
        from mastapy._private.system_model.part_model.gears import _2606

        return self.__parent__._cast(_2606.HypoidGear)

    @property
    def klingelnberg_cyclo_palloid_conical_gear(
        self: "CastSelf",
    ) -> "_2608.KlingelnbergCycloPalloidConicalGear":
        from mastapy._private.system_model.part_model.gears import _2608

        return self.__parent__._cast(_2608.KlingelnbergCycloPalloidConicalGear)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear(
        self: "CastSelf",
    ) -> "_2610.KlingelnbergCycloPalloidHypoidGear":
        from mastapy._private.system_model.part_model.gears import _2610

        return self.__parent__._cast(_2610.KlingelnbergCycloPalloidHypoidGear)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: "CastSelf",
    ) -> "_2612.KlingelnbergCycloPalloidSpiralBevelGear":
        from mastapy._private.system_model.part_model.gears import _2612

        return self.__parent__._cast(_2612.KlingelnbergCycloPalloidSpiralBevelGear)

    @property
    def spiral_bevel_gear(self: "CastSelf") -> "_2615.SpiralBevelGear":
        from mastapy._private.system_model.part_model.gears import _2615

        return self.__parent__._cast(_2615.SpiralBevelGear)

    @property
    def straight_bevel_diff_gear(self: "CastSelf") -> "_2617.StraightBevelDiffGear":
        from mastapy._private.system_model.part_model.gears import _2617

        return self.__parent__._cast(_2617.StraightBevelDiffGear)

    @property
    def straight_bevel_gear(self: "CastSelf") -> "_2619.StraightBevelGear":
        from mastapy._private.system_model.part_model.gears import _2619

        return self.__parent__._cast(_2619.StraightBevelGear)

    @property
    def straight_bevel_planet_gear(self: "CastSelf") -> "_2621.StraightBevelPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2621

        return self.__parent__._cast(_2621.StraightBevelPlanetGear)

    @property
    def straight_bevel_sun_gear(self: "CastSelf") -> "_2622.StraightBevelSunGear":
        from mastapy._private.system_model.part_model.gears import _2622

        return self.__parent__._cast(_2622.StraightBevelSunGear)

    @property
    def worm_gear(self: "CastSelf") -> "_2623.WormGear":
        from mastapy._private.system_model.part_model.gears import _2623

        return self.__parent__._cast(_2623.WormGear)

    @property
    def zerol_bevel_gear(self: "CastSelf") -> "_2625.ZerolBevelGear":
        from mastapy._private.system_model.part_model.gears import _2625

        return self.__parent__._cast(_2625.ZerolBevelGear)

    @property
    def ring_pins(self: "CastSelf") -> "_2642.RingPins":
        from mastapy._private.system_model.part_model.cycloidal import _2642

        return self.__parent__._cast(_2642.RingPins)

    @property
    def clutch_half(self: "CastSelf") -> "_2652.ClutchHalf":
        from mastapy._private.system_model.part_model.couplings import _2652

        return self.__parent__._cast(_2652.ClutchHalf)

    @property
    def concept_coupling_half(self: "CastSelf") -> "_2655.ConceptCouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2655

        return self.__parent__._cast(_2655.ConceptCouplingHalf)

    @property
    def coupling_half(self: "CastSelf") -> "_2658.CouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2658

        return self.__parent__._cast(_2658.CouplingHalf)

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
    def shaft_hub_connection(self: "CastSelf") -> "_2674.ShaftHubConnection":
        from mastapy._private.system_model.part_model.couplings import _2674

        return self.__parent__._cast(_2674.ShaftHubConnection)

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
    def mountable_component(self: "CastSelf") -> "MountableComponent":
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
class MountableComponent(_2511.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MOUNTABLE_COMPONENT

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def rotation_about_axis(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "RotationAboutAxis")

        if temp is None:
            return 0.0

        return temp

    @rotation_about_axis.setter
    @enforce_parameter_types
    def rotation_about_axis(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped,
            "RotationAboutAxis",
            float(value) if value is not None else 0.0,
        )

    @property
    def inner_component(self: "Self") -> "_2502.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "InnerComponent")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_connection(self: "Self") -> "_2338.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "InnerConnection")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def inner_socket(self: "Self") -> "_2342.CylindricalSocket":
        """mastapy.system_model.connections_and_sockets.CylindricalSocket

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "InnerSocket")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def is_mounted(self: "Self") -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "IsMounted")

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def mount_on(
        self: "Self", shaft: "_2502.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2335.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = pythonnet_method_call(
            self.wrapped,
            "MountOn",
            shaft.wrapped if shaft else None,
            offset if offset else 0.0,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_mount_on(
        self: "Self", shaft: "_2502.AbstractShaft", offset: "float" = float("nan")
    ) -> "_2512.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)
        """
        offset = float(offset)
        method_result = pythonnet_method_call(
            self.wrapped,
            "TryMountOn",
            shaft.wrapped if shaft else None,
            offset if offset else 0.0,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_MountableComponent":
        """Cast to another type.

        Returns:
            _Cast_MountableComponent
        """
        return _Cast_MountableComponent(self)
