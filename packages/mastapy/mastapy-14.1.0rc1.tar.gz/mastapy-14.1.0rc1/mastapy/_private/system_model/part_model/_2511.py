"""Component"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_method_call,
    pythonnet_method_call_overload,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private._math.vector_3d import Vector3D
from mastapy._private.system_model.part_model import _2537

_COMPONENT = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Component")
_SOCKET = python_net_import("SMT.MastaAPI.SystemModel.ConnectionsAndSockets", "Socket")

if TYPE_CHECKING:
    from typing import Any, List, Tuple, Type, TypeVar, Union

    from mastapy._private.math_utility import _1558, _1559
    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.connections_and_sockets import (
        _2336,
        _2338,
        _2357,
        _2362,
    )
    from mastapy._private.system_model.part_model import (
        _2502,
        _2503,
        _2506,
        _2509,
        _2512,
        _2514,
        _2515,
        _2519,
        _2520,
        _2522,
        _2529,
        _2530,
        _2531,
        _2533,
        _2535,
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
    from mastapy._private.system_model.part_model.cycloidal import _2641, _2642
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
    from mastapy._private.system_model.part_model.shaft_model import _2552

    Self = TypeVar("Self", bound="Component")
    CastSelf = TypeVar("CastSelf", bound="Component._Cast_Component")


__docformat__ = "restructuredtext en"
__all__ = ("Component",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Component:
    """Special nested class for casting Component to subclasses."""

    __parent__: "Component"

    @property
    def part(self: "CastSelf") -> "_2537.Part":
        return self.__parent__._cast(_2537.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2269.DesignEntity":
        from mastapy._private.system_model import _2269

        return self.__parent__._cast(_2269.DesignEntity)

    @property
    def abstract_shaft(self: "CastSelf") -> "_2502.AbstractShaft":
        from mastapy._private.system_model.part_model import _2502

        return self.__parent__._cast(_2502.AbstractShaft)

    @property
    def abstract_shaft_or_housing(self: "CastSelf") -> "_2503.AbstractShaftOrHousing":
        from mastapy._private.system_model.part_model import _2503

        return self.__parent__._cast(_2503.AbstractShaftOrHousing)

    @property
    def bearing(self: "CastSelf") -> "_2506.Bearing":
        from mastapy._private.system_model.part_model import _2506

        return self.__parent__._cast(_2506.Bearing)

    @property
    def bolt(self: "CastSelf") -> "_2509.Bolt":
        from mastapy._private.system_model.part_model import _2509

        return self.__parent__._cast(_2509.Bolt)

    @property
    def connector(self: "CastSelf") -> "_2514.Connector":
        from mastapy._private.system_model.part_model import _2514

        return self.__parent__._cast(_2514.Connector)

    @property
    def datum(self: "CastSelf") -> "_2515.Datum":
        from mastapy._private.system_model.part_model import _2515

        return self.__parent__._cast(_2515.Datum)

    @property
    def external_cad_model(self: "CastSelf") -> "_2519.ExternalCADModel":
        from mastapy._private.system_model.part_model import _2519

        return self.__parent__._cast(_2519.ExternalCADModel)

    @property
    def fe_part(self: "CastSelf") -> "_2520.FEPart":
        from mastapy._private.system_model.part_model import _2520

        return self.__parent__._cast(_2520.FEPart)

    @property
    def guide_dxf_model(self: "CastSelf") -> "_2522.GuideDxfModel":
        from mastapy._private.system_model.part_model import _2522

        return self.__parent__._cast(_2522.GuideDxfModel)

    @property
    def mass_disc(self: "CastSelf") -> "_2529.MassDisc":
        from mastapy._private.system_model.part_model import _2529

        return self.__parent__._cast(_2529.MassDisc)

    @property
    def measurement_component(self: "CastSelf") -> "_2530.MeasurementComponent":
        from mastapy._private.system_model.part_model import _2530

        return self.__parent__._cast(_2530.MeasurementComponent)

    @property
    def microphone(self: "CastSelf") -> "_2531.Microphone":
        from mastapy._private.system_model.part_model import _2531

        return self.__parent__._cast(_2531.Microphone)

    @property
    def mountable_component(self: "CastSelf") -> "_2533.MountableComponent":
        from mastapy._private.system_model.part_model import _2533

        return self.__parent__._cast(_2533.MountableComponent)

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
    def shaft(self: "CastSelf") -> "_2552.Shaft":
        from mastapy._private.system_model.part_model.shaft_model import _2552

        return self.__parent__._cast(_2552.Shaft)

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
    def cycloidal_disc(self: "CastSelf") -> "_2641.CycloidalDisc":
        from mastapy._private.system_model.part_model.cycloidal import _2641

        return self.__parent__._cast(_2641.CycloidalDisc)

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
    def component(self: "CastSelf") -> "Component":
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
class Component(_2537.Part):
    """Component

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPONENT

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
    def length(self: "Self") -> "float":
        """float"""
        temp = pythonnet_property_get(self.wrapped, "Length")

        if temp is None:
            return 0.0

        return temp

    @length.setter
    @enforce_parameter_types
    def length(self: "Self", value: "float") -> None:
        pythonnet_property_set(
            self.wrapped, "Length", float(value) if value is not None else 0.0
        )

    @property
    def polar_inertia(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = pythonnet_property_get(self.wrapped, "PolarInertia")

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @polar_inertia.setter
    @enforce_parameter_types
    def polar_inertia(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        pythonnet_property_set(self.wrapped, "PolarInertia", value)

    @property
    def polar_inertia_for_synchroniser_sizing_only(
        self: "Self",
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = pythonnet_property_get(
            self.wrapped, "PolarInertiaForSynchroniserSizingOnly"
        )

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @polar_inertia_for_synchroniser_sizing_only.setter
    @enforce_parameter_types
    def polar_inertia_for_synchroniser_sizing_only(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        pythonnet_property_set(
            self.wrapped, "PolarInertiaForSynchroniserSizingOnly", value
        )

    @property
    def reason_mass_properties_are_unknown(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ReasonMassPropertiesAreUnknown")

        if temp is None:
            return ""

        return temp

    @property
    def reason_mass_properties_are_zero(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ReasonMassPropertiesAreZero")

        if temp is None:
            return ""

        return temp

    @property
    def translation(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Translation")

        if temp is None:
            return ""

        return temp

    @property
    def transverse_inertia(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = pythonnet_property_get(self.wrapped, "TransverseInertia")

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @transverse_inertia.setter
    @enforce_parameter_types
    def transverse_inertia(
        self: "Self", value: "Union[float, Tuple[float, bool]]"
    ) -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        pythonnet_property_set(self.wrapped, "TransverseInertia", value)

    @property
    def x_axis(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "XAxis")

        if temp is None:
            return ""

        return temp

    @property
    def y_axis(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "YAxis")

        if temp is None:
            return ""

        return temp

    @property
    def z_axis(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ZAxis")

        if temp is None:
            return ""

        return temp

    @property
    def coordinate_system_euler_angles(self: "Self") -> "Vector3D":
        """Vector3D"""
        temp = pythonnet_property_get(self.wrapped, "CoordinateSystemEulerAngles")

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @coordinate_system_euler_angles.setter
    @enforce_parameter_types
    def coordinate_system_euler_angles(self: "Self", value: "Vector3D") -> None:
        value = conversion.mp_to_pn_vector3d(value)
        pythonnet_property_set(self.wrapped, "CoordinateSystemEulerAngles", value)

    @property
    def local_coordinate_system(self: "Self") -> "_1558.CoordinateSystem3D":
        """mastapy.math_utility.CoordinateSystem3D

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "LocalCoordinateSystem")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def position(self: "Self") -> "Vector3D":
        """Vector3D"""
        temp = pythonnet_property_get(self.wrapped, "Position")

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @position.setter
    @enforce_parameter_types
    def position(self: "Self", value: "Vector3D") -> None:
        value = conversion.mp_to_pn_vector3d(value)
        pythonnet_property_set(self.wrapped, "Position", value)

    @property
    def component_connections(self: "Self") -> "List[_2336.ComponentConnection]":
        """List[mastapy.system_model.connections_and_sockets.ComponentConnection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentConnections")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def available_socket_offsets(self: "Self") -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AvailableSocketOffsets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @property
    def centre_offset(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CentreOffset")

        if temp is None:
            return 0.0

        return temp

    @property
    def translation_vector(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "TranslationVector")

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def x_axis_vector(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "XAxisVector")

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def y_axis_vector(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "YAxisVector")

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def z_axis_vector(self: "Self") -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ZAxisVector")

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def can_connect_to(self: "Self", component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = pythonnet_method_call(
            self.wrapped, "CanConnectTo", component.wrapped if component else None
        )
        return method_result

    @enforce_parameter_types
    def can_delete_connection(self: "Self", connection: "_2338.Connection") -> "bool":
        """bool

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = pythonnet_method_call(
            self.wrapped,
            "CanDeleteConnection",
            connection.wrapped if connection else None,
        )
        return method_result

    @enforce_parameter_types
    def connect_to(
        self: "Self", component: "Component"
    ) -> "_2512.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped,
            "ConnectTo",
            [_COMPONENT],
            component.wrapped if component else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def connect_to_socket(
        self: "Self", socket: "_2362.Socket"
    ) -> "_2512.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        method_result = pythonnet_method_call_overload(
            self.wrapped, "ConnectTo", [_SOCKET], socket.wrapped if socket else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_coordinate_system_editor(self: "Self") -> "_1559.CoordinateSystemEditor":
        """mastapy.math_utility.CoordinateSystemEditor"""
        method_result = pythonnet_method_call(
            self.wrapped, "CreateCoordinateSystemEditor"
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def diameter_at_middle_of_connection(
        self: "Self", connection: "_2338.Connection"
    ) -> "float":
        """float

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = pythonnet_method_call(
            self.wrapped,
            "DiameterAtMiddleOfConnection",
            connection.wrapped if connection else None,
        )
        return method_result

    @enforce_parameter_types
    def diameter_of_socket_for(self: "Self", connection: "_2338.Connection") -> "float":
        """float

        Args:
            connection (mastapy.system_model.connections_and_sockets.Connection)
        """
        method_result = pythonnet_method_call(
            self.wrapped,
            "DiameterOfSocketFor",
            connection.wrapped if connection else None,
        )
        return method_result

    @enforce_parameter_types
    def is_coaxially_connected_to(self: "Self", component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = pythonnet_method_call(
            self.wrapped,
            "IsCoaxiallyConnectedTo",
            component.wrapped if component else None,
        )
        return method_result

    @enforce_parameter_types
    def is_directly_connected_to(self: "Self", component: "Component") -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = pythonnet_method_call(
            self.wrapped,
            "IsDirectlyConnectedTo",
            component.wrapped if component else None,
        )
        return method_result

    @enforce_parameter_types
    def is_directly_or_indirectly_connected_to(
        self: "Self", component: "Component"
    ) -> "bool":
        """bool

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        method_result = pythonnet_method_call(
            self.wrapped,
            "IsDirectlyOrIndirectlyConnectedTo",
            component.wrapped if component else None,
        )
        return method_result

    @enforce_parameter_types
    def move_all_concentric_parts_radially(
        self: "Self", delta_x: "float", delta_y: "float"
    ) -> "bool":
        """bool

        Args:
            delta_x (float)
            delta_y (float)
        """
        delta_x = float(delta_x)
        delta_y = float(delta_y)
        method_result = pythonnet_method_call(
            self.wrapped,
            "MoveAllConcentricPartsRadially",
            delta_x if delta_x else 0.0,
            delta_y if delta_y else 0.0,
        )
        return method_result

    @enforce_parameter_types
    def move_along_axis(self: "Self", delta: "float") -> None:
        """Method does not return.

        Args:
            delta (float)
        """
        delta = float(delta)
        pythonnet_method_call(self.wrapped, "MoveAlongAxis", delta if delta else 0.0)

    @enforce_parameter_types
    def move_with_concentric_parts_to_new_origin(
        self: "Self", target_origin: "Vector3D"
    ) -> "bool":
        """bool

        Args:
            target_origin (Vector3D)
        """
        target_origin = conversion.mp_to_pn_vector3d(target_origin)
        method_result = pythonnet_method_call(
            self.wrapped, "MoveWithConcentricPartsToNewOrigin", target_origin
        )
        return method_result

    @enforce_parameter_types
    def possible_sockets_to_connect_with_component(
        self: "Self", component: "Component"
    ) -> "List[_2362.Socket]":
        """List[mastapy.system_model.connections_and_sockets.Socket]

        Args:
            component (mastapy.system_model.part_model.Component)
        """
        return conversion.pn_to_mp_objects_in_list(
            pythonnet_method_call_overload(
                self.wrapped,
                "PossibleSocketsToConnectWith",
                [_COMPONENT],
                component.wrapped if component else None,
            )
        )

    @enforce_parameter_types
    def possible_sockets_to_connect_with(
        self: "Self", socket: "_2362.Socket"
    ) -> "List[_2362.Socket]":
        """List[mastapy.system_model.connections_and_sockets.Socket]

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)
        """
        return conversion.pn_to_mp_objects_in_list(
            pythonnet_method_call_overload(
                self.wrapped,
                "PossibleSocketsToConnectWith",
                [_SOCKET],
                socket.wrapped if socket else None,
            )
        )

    @enforce_parameter_types
    def set_position_and_axis_of_component_and_connected_components(
        self: "Self", origin: "Vector3D", z_axis: "Vector3D"
    ) -> "_2357.RealignmentResult":
        """mastapy.system_model.connections_and_sockets.RealignmentResult

        Args:
            origin (Vector3D)
            z_axis (Vector3D)
        """
        origin = conversion.mp_to_pn_vector3d(origin)
        z_axis = conversion.mp_to_pn_vector3d(z_axis)
        method_result = pythonnet_method_call(
            self.wrapped,
            "SetPositionAndAxisOfComponentAndConnectedComponents",
            origin,
            z_axis,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_position_and_rotation_of_component_and_connected_components(
        self: "Self", new_coordinate_system: "_1558.CoordinateSystem3D"
    ) -> "_2357.RealignmentResult":
        """mastapy.system_model.connections_and_sockets.RealignmentResult

        Args:
            new_coordinate_system (mastapy.math_utility.CoordinateSystem3D)
        """
        method_result = pythonnet_method_call(
            self.wrapped,
            "SetPositionAndRotationOfComponentAndConnectedComponents",
            new_coordinate_system.wrapped if new_coordinate_system else None,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def set_position_of_component_and_connected_components(
        self: "Self", position: "Vector3D"
    ) -> "_2357.RealignmentResult":
        """mastapy.system_model.connections_and_sockets.RealignmentResult

        Args:
            position (Vector3D)
        """
        position = conversion.mp_to_pn_vector3d(position)
        method_result = pythonnet_method_call(
            self.wrapped, "SetPositionOfComponentAndConnectedComponents", position
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def socket_named(self: "Self", socket_name: "str") -> "_2362.Socket":
        """mastapy.system_model.connections_and_sockets.Socket

        Args:
            socket_name (str)
        """
        socket_name = str(socket_name)
        method_result = pythonnet_method_call(
            self.wrapped, "SocketNamed", socket_name if socket_name else ""
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def try_connect_to(
        self: "Self", component: "Component", hint_offset: "float" = float("nan")
    ) -> "_2512.ComponentsConnectedResult":
        """mastapy.system_model.part_model.ComponentsConnectedResult

        Args:
            component (mastapy.system_model.part_model.Component)
            hint_offset (float, optional)
        """
        hint_offset = float(hint_offset)
        method_result = pythonnet_method_call(
            self.wrapped,
            "TryConnectTo",
            component.wrapped if component else None,
            hint_offset if hint_offset else 0.0,
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_Component":
        """Cast to another type.

        Returns:
            _Cast_Component
        """
        return _Cast_Component(self)
