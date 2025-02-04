"""Part"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from PIL.Image import Image

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.implicit import overridable
from mastapy._private._internal.overridable_constructor import _unpack_overridable
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_method_call,
    pythonnet_property_get,
    pythonnet_property_set,
)
from mastapy._private._internal.type_enforcement import enforce_parameter_types
from mastapy._private.system_model import _2269

_PART = python_net_import("SMT.MastaAPI.SystemModel.PartModel", "Part")

if TYPE_CHECKING:
    from typing import Any, List, Tuple, Type, TypeVar, Union

    from mastapy._private.math_utility import _1577
    from mastapy._private.system_model.connections_and_sockets import _2338
    from mastapy._private.system_model.import_export import _2308
    from mastapy._private.system_model.part_model import (
        _2500,
        _2501,
        _2502,
        _2503,
        _2506,
        _2509,
        _2510,
        _2511,
        _2514,
        _2515,
        _2519,
        _2520,
        _2521,
        _2522,
        _2529,
        _2530,
        _2531,
        _2532,
        _2533,
        _2535,
        _2538,
        _2540,
        _2541,
        _2544,
        _2546,
        _2547,
        _2549,
    )
    from mastapy._private.system_model.part_model.couplings import (
        _2649,
        _2651,
        _2652,
        _2654,
        _2655,
        _2657,
        _2658,
        _2660,
        _2661,
        _2662,
        _2663,
        _2665,
        _2672,
        _2673,
        _2674,
        _2680,
        _2681,
        _2682,
        _2684,
        _2685,
        _2686,
        _2687,
        _2688,
        _2690,
    )
    from mastapy._private.system_model.part_model.cycloidal import _2640, _2641, _2642
    from mastapy._private.system_model.part_model.gears import (
        _2585,
        _2586,
        _2587,
        _2588,
        _2589,
        _2590,
        _2591,
        _2592,
        _2593,
        _2594,
        _2595,
        _2596,
        _2597,
        _2598,
        _2599,
        _2600,
        _2601,
        _2602,
        _2604,
        _2606,
        _2607,
        _2608,
        _2609,
        _2610,
        _2611,
        _2612,
        _2613,
        _2614,
        _2615,
        _2616,
        _2617,
        _2618,
        _2619,
        _2620,
        _2621,
        _2622,
        _2623,
        _2624,
        _2625,
        _2626,
    )
    from mastapy._private.system_model.part_model.shaft_model import _2552

    Self = TypeVar("Self", bound="Part")
    CastSelf = TypeVar("CastSelf", bound="Part._Cast_Part")


__docformat__ = "restructuredtext en"
__all__ = ("Part",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_Part:
    """Special nested class for casting Part to subclasses."""

    __parent__: "Part"

    @property
    def design_entity(self: "CastSelf") -> "_2269.DesignEntity":
        return self.__parent__._cast(_2269.DesignEntity)

    @property
    def assembly(self: "CastSelf") -> "_2500.Assembly":
        return self.__parent__._cast(_2500.Assembly)

    @property
    def abstract_assembly(self: "CastSelf") -> "_2501.AbstractAssembly":
        from mastapy._private.system_model.part_model import _2501

        return self.__parent__._cast(_2501.AbstractAssembly)

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
    def bolted_joint(self: "CastSelf") -> "_2510.BoltedJoint":
        from mastapy._private.system_model.part_model import _2510

        return self.__parent__._cast(_2510.BoltedJoint)

    @property
    def component(self: "CastSelf") -> "_2511.Component":
        from mastapy._private.system_model.part_model import _2511

        return self.__parent__._cast(_2511.Component)

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
    def flexible_pin_assembly(self: "CastSelf") -> "_2521.FlexiblePinAssembly":
        from mastapy._private.system_model.part_model import _2521

        return self.__parent__._cast(_2521.FlexiblePinAssembly)

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
    def microphone_array(self: "CastSelf") -> "_2532.MicrophoneArray":
        from mastapy._private.system_model.part_model import _2532

        return self.__parent__._cast(_2532.MicrophoneArray)

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
    def root_assembly(self: "CastSelf") -> "_2544.RootAssembly":
        from mastapy._private.system_model.part_model import _2544

        return self.__parent__._cast(_2544.RootAssembly)

    @property
    def specialised_assembly(self: "CastSelf") -> "_2546.SpecialisedAssembly":
        from mastapy._private.system_model.part_model import _2546

        return self.__parent__._cast(_2546.SpecialisedAssembly)

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
    def agma_gleason_conical_gear_set(
        self: "CastSelf",
    ) -> "_2586.AGMAGleasonConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2586

        return self.__parent__._cast(_2586.AGMAGleasonConicalGearSet)

    @property
    def bevel_differential_gear(self: "CastSelf") -> "_2587.BevelDifferentialGear":
        from mastapy._private.system_model.part_model.gears import _2587

        return self.__parent__._cast(_2587.BevelDifferentialGear)

    @property
    def bevel_differential_gear_set(
        self: "CastSelf",
    ) -> "_2588.BevelDifferentialGearSet":
        from mastapy._private.system_model.part_model.gears import _2588

        return self.__parent__._cast(_2588.BevelDifferentialGearSet)

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
    def bevel_gear_set(self: "CastSelf") -> "_2592.BevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2592

        return self.__parent__._cast(_2592.BevelGearSet)

    @property
    def concept_gear(self: "CastSelf") -> "_2593.ConceptGear":
        from mastapy._private.system_model.part_model.gears import _2593

        return self.__parent__._cast(_2593.ConceptGear)

    @property
    def concept_gear_set(self: "CastSelf") -> "_2594.ConceptGearSet":
        from mastapy._private.system_model.part_model.gears import _2594

        return self.__parent__._cast(_2594.ConceptGearSet)

    @property
    def conical_gear(self: "CastSelf") -> "_2595.ConicalGear":
        from mastapy._private.system_model.part_model.gears import _2595

        return self.__parent__._cast(_2595.ConicalGear)

    @property
    def conical_gear_set(self: "CastSelf") -> "_2596.ConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2596

        return self.__parent__._cast(_2596.ConicalGearSet)

    @property
    def cylindrical_gear(self: "CastSelf") -> "_2597.CylindricalGear":
        from mastapy._private.system_model.part_model.gears import _2597

        return self.__parent__._cast(_2597.CylindricalGear)

    @property
    def cylindrical_gear_set(self: "CastSelf") -> "_2598.CylindricalGearSet":
        from mastapy._private.system_model.part_model.gears import _2598

        return self.__parent__._cast(_2598.CylindricalGearSet)

    @property
    def cylindrical_planet_gear(self: "CastSelf") -> "_2599.CylindricalPlanetGear":
        from mastapy._private.system_model.part_model.gears import _2599

        return self.__parent__._cast(_2599.CylindricalPlanetGear)

    @property
    def face_gear(self: "CastSelf") -> "_2600.FaceGear":
        from mastapy._private.system_model.part_model.gears import _2600

        return self.__parent__._cast(_2600.FaceGear)

    @property
    def face_gear_set(self: "CastSelf") -> "_2601.FaceGearSet":
        from mastapy._private.system_model.part_model.gears import _2601

        return self.__parent__._cast(_2601.FaceGearSet)

    @property
    def gear(self: "CastSelf") -> "_2602.Gear":
        from mastapy._private.system_model.part_model.gears import _2602

        return self.__parent__._cast(_2602.Gear)

    @property
    def gear_set(self: "CastSelf") -> "_2604.GearSet":
        from mastapy._private.system_model.part_model.gears import _2604

        return self.__parent__._cast(_2604.GearSet)

    @property
    def hypoid_gear(self: "CastSelf") -> "_2606.HypoidGear":
        from mastapy._private.system_model.part_model.gears import _2606

        return self.__parent__._cast(_2606.HypoidGear)

    @property
    def hypoid_gear_set(self: "CastSelf") -> "_2607.HypoidGearSet":
        from mastapy._private.system_model.part_model.gears import _2607

        return self.__parent__._cast(_2607.HypoidGearSet)

    @property
    def klingelnberg_cyclo_palloid_conical_gear(
        self: "CastSelf",
    ) -> "_2608.KlingelnbergCycloPalloidConicalGear":
        from mastapy._private.system_model.part_model.gears import _2608

        return self.__parent__._cast(_2608.KlingelnbergCycloPalloidConicalGear)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set(
        self: "CastSelf",
    ) -> "_2609.KlingelnbergCycloPalloidConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2609

        return self.__parent__._cast(_2609.KlingelnbergCycloPalloidConicalGearSet)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear(
        self: "CastSelf",
    ) -> "_2610.KlingelnbergCycloPalloidHypoidGear":
        from mastapy._private.system_model.part_model.gears import _2610

        return self.__parent__._cast(_2610.KlingelnbergCycloPalloidHypoidGear)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: "CastSelf",
    ) -> "_2611.KlingelnbergCycloPalloidHypoidGearSet":
        from mastapy._private.system_model.part_model.gears import _2611

        return self.__parent__._cast(_2611.KlingelnbergCycloPalloidHypoidGearSet)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear(
        self: "CastSelf",
    ) -> "_2612.KlingelnbergCycloPalloidSpiralBevelGear":
        from mastapy._private.system_model.part_model.gears import _2612

        return self.__parent__._cast(_2612.KlingelnbergCycloPalloidSpiralBevelGear)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
        self: "CastSelf",
    ) -> "_2613.KlingelnbergCycloPalloidSpiralBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2613

        return self.__parent__._cast(_2613.KlingelnbergCycloPalloidSpiralBevelGearSet)

    @property
    def planetary_gear_set(self: "CastSelf") -> "_2614.PlanetaryGearSet":
        from mastapy._private.system_model.part_model.gears import _2614

        return self.__parent__._cast(_2614.PlanetaryGearSet)

    @property
    def spiral_bevel_gear(self: "CastSelf") -> "_2615.SpiralBevelGear":
        from mastapy._private.system_model.part_model.gears import _2615

        return self.__parent__._cast(_2615.SpiralBevelGear)

    @property
    def spiral_bevel_gear_set(self: "CastSelf") -> "_2616.SpiralBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2616

        return self.__parent__._cast(_2616.SpiralBevelGearSet)

    @property
    def straight_bevel_diff_gear(self: "CastSelf") -> "_2617.StraightBevelDiffGear":
        from mastapy._private.system_model.part_model.gears import _2617

        return self.__parent__._cast(_2617.StraightBevelDiffGear)

    @property
    def straight_bevel_diff_gear_set(
        self: "CastSelf",
    ) -> "_2618.StraightBevelDiffGearSet":
        from mastapy._private.system_model.part_model.gears import _2618

        return self.__parent__._cast(_2618.StraightBevelDiffGearSet)

    @property
    def straight_bevel_gear(self: "CastSelf") -> "_2619.StraightBevelGear":
        from mastapy._private.system_model.part_model.gears import _2619

        return self.__parent__._cast(_2619.StraightBevelGear)

    @property
    def straight_bevel_gear_set(self: "CastSelf") -> "_2620.StraightBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2620

        return self.__parent__._cast(_2620.StraightBevelGearSet)

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
    def worm_gear_set(self: "CastSelf") -> "_2624.WormGearSet":
        from mastapy._private.system_model.part_model.gears import _2624

        return self.__parent__._cast(_2624.WormGearSet)

    @property
    def zerol_bevel_gear(self: "CastSelf") -> "_2625.ZerolBevelGear":
        from mastapy._private.system_model.part_model.gears import _2625

        return self.__parent__._cast(_2625.ZerolBevelGear)

    @property
    def zerol_bevel_gear_set(self: "CastSelf") -> "_2626.ZerolBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2626

        return self.__parent__._cast(_2626.ZerolBevelGearSet)

    @property
    def cycloidal_assembly(self: "CastSelf") -> "_2640.CycloidalAssembly":
        from mastapy._private.system_model.part_model.cycloidal import _2640

        return self.__parent__._cast(_2640.CycloidalAssembly)

    @property
    def cycloidal_disc(self: "CastSelf") -> "_2641.CycloidalDisc":
        from mastapy._private.system_model.part_model.cycloidal import _2641

        return self.__parent__._cast(_2641.CycloidalDisc)

    @property
    def ring_pins(self: "CastSelf") -> "_2642.RingPins":
        from mastapy._private.system_model.part_model.cycloidal import _2642

        return self.__parent__._cast(_2642.RingPins)

    @property
    def belt_drive(self: "CastSelf") -> "_2649.BeltDrive":
        from mastapy._private.system_model.part_model.couplings import _2649

        return self.__parent__._cast(_2649.BeltDrive)

    @property
    def clutch(self: "CastSelf") -> "_2651.Clutch":
        from mastapy._private.system_model.part_model.couplings import _2651

        return self.__parent__._cast(_2651.Clutch)

    @property
    def clutch_half(self: "CastSelf") -> "_2652.ClutchHalf":
        from mastapy._private.system_model.part_model.couplings import _2652

        return self.__parent__._cast(_2652.ClutchHalf)

    @property
    def concept_coupling(self: "CastSelf") -> "_2654.ConceptCoupling":
        from mastapy._private.system_model.part_model.couplings import _2654

        return self.__parent__._cast(_2654.ConceptCoupling)

    @property
    def concept_coupling_half(self: "CastSelf") -> "_2655.ConceptCouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2655

        return self.__parent__._cast(_2655.ConceptCouplingHalf)

    @property
    def coupling(self: "CastSelf") -> "_2657.Coupling":
        from mastapy._private.system_model.part_model.couplings import _2657

        return self.__parent__._cast(_2657.Coupling)

    @property
    def coupling_half(self: "CastSelf") -> "_2658.CouplingHalf":
        from mastapy._private.system_model.part_model.couplings import _2658

        return self.__parent__._cast(_2658.CouplingHalf)

    @property
    def cvt(self: "CastSelf") -> "_2660.CVT":
        from mastapy._private.system_model.part_model.couplings import _2660

        return self.__parent__._cast(_2660.CVT)

    @property
    def cvt_pulley(self: "CastSelf") -> "_2661.CVTPulley":
        from mastapy._private.system_model.part_model.couplings import _2661

        return self.__parent__._cast(_2661.CVTPulley)

    @property
    def part_to_part_shear_coupling(
        self: "CastSelf",
    ) -> "_2662.PartToPartShearCoupling":
        from mastapy._private.system_model.part_model.couplings import _2662

        return self.__parent__._cast(_2662.PartToPartShearCoupling)

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
    def rolling_ring_assembly(self: "CastSelf") -> "_2673.RollingRingAssembly":
        from mastapy._private.system_model.part_model.couplings import _2673

        return self.__parent__._cast(_2673.RollingRingAssembly)

    @property
    def shaft_hub_connection(self: "CastSelf") -> "_2674.ShaftHubConnection":
        from mastapy._private.system_model.part_model.couplings import _2674

        return self.__parent__._cast(_2674.ShaftHubConnection)

    @property
    def spring_damper(self: "CastSelf") -> "_2680.SpringDamper":
        from mastapy._private.system_model.part_model.couplings import _2680

        return self.__parent__._cast(_2680.SpringDamper)

    @property
    def spring_damper_half(self: "CastSelf") -> "_2681.SpringDamperHalf":
        from mastapy._private.system_model.part_model.couplings import _2681

        return self.__parent__._cast(_2681.SpringDamperHalf)

    @property
    def synchroniser(self: "CastSelf") -> "_2682.Synchroniser":
        from mastapy._private.system_model.part_model.couplings import _2682

        return self.__parent__._cast(_2682.Synchroniser)

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
    def torque_converter(self: "CastSelf") -> "_2687.TorqueConverter":
        from mastapy._private.system_model.part_model.couplings import _2687

        return self.__parent__._cast(_2687.TorqueConverter)

    @property
    def torque_converter_pump(self: "CastSelf") -> "_2688.TorqueConverterPump":
        from mastapy._private.system_model.part_model.couplings import _2688

        return self.__parent__._cast(_2688.TorqueConverterPump)

    @property
    def torque_converter_turbine(self: "CastSelf") -> "_2690.TorqueConverterTurbine":
        from mastapy._private.system_model.part_model.couplings import _2690

        return self.__parent__._cast(_2690.TorqueConverterTurbine)

    @property
    def part(self: "CastSelf") -> "Part":
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
class Part(_2269.DesignEntity):
    """Part

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def two_d_drawing(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "TwoDDrawing")

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def two_d_drawing_full_model(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "TwoDDrawingFullModel")

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_isometric_view(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ThreeDIsometricView")

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view(self: "Self") -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ThreeDView")

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_into_the_screen(
        self: "Self",
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "ThreeDViewOrientatedInXyPlaneWithZAxisPointingIntoTheScreen"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xy_plane_with_z_axis_pointing_out_of_the_screen(
        self: "Self",
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "ThreeDViewOrientatedInXyPlaneWithZAxisPointingOutOfTheScreen"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_into_the_screen(
        self: "Self",
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "ThreeDViewOrientatedInXzPlaneWithYAxisPointingIntoTheScreen"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_xz_plane_with_y_axis_pointing_out_of_the_screen(
        self: "Self",
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "ThreeDViewOrientatedInXzPlaneWithYAxisPointingOutOfTheScreen"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_into_the_screen(
        self: "Self",
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "ThreeDViewOrientatedInYzPlaneWithXAxisPointingIntoTheScreen"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def three_d_view_orientated_in_yz_plane_with_x_axis_pointing_out_of_the_screen(
        self: "Self",
    ) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "ThreeDViewOrientatedInYzPlaneWithXAxisPointingOutOfTheScreen"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def drawing_number(self: "Self") -> "str":
        """str"""
        temp = pythonnet_property_get(self.wrapped, "DrawingNumber")

        if temp is None:
            return ""

        return temp

    @drawing_number.setter
    @enforce_parameter_types
    def drawing_number(self: "Self", value: "str") -> None:
        pythonnet_property_set(
            self.wrapped, "DrawingNumber", str(value) if value is not None else ""
        )

    @property
    def editable_name(self: "Self") -> "str":
        """str"""
        temp = pythonnet_property_get(self.wrapped, "EditableName")

        if temp is None:
            return ""

        return temp

    @editable_name.setter
    @enforce_parameter_types
    def editable_name(self: "Self", value: "str") -> None:
        pythonnet_property_set(
            self.wrapped, "EditableName", str(value) if value is not None else ""
        )

    @property
    def full_name_without_root_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "FullNameWithoutRootName")

        if temp is None:
            return ""

        return temp

    @property
    def mass(self: "Self") -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = pythonnet_property_get(self.wrapped, "Mass")

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._private._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mass.setter
    @enforce_parameter_types
    def mass(self: "Self", value: "Union[float, Tuple[float, bool]]") -> None:
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        pythonnet_property_set(self.wrapped, "Mass", value)

    @property
    def unique_name(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "UniqueName")

        if temp is None:
            return ""

        return temp

    @property
    def mass_properties_from_design(self: "Self") -> "_1577.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "MassPropertiesFromDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_from_design_including_planetary_duplicates(
        self: "Self",
    ) -> "_1577.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "MassPropertiesFromDesignIncludingPlanetaryDuplicates"
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connections(self: "Self") -> "List[_2338.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Connections")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def local_connections(self: "Self") -> "List[_2338.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "LocalConnections")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def connections_to(self: "Self", part: "Part") -> "List[_2338.Connection]":
        """List[mastapy.system_model.connections_and_sockets.Connection]

        Args:
            part (mastapy.system_model.part_model.Part)
        """
        return conversion.pn_to_mp_objects_in_list(
            pythonnet_method_call(
                self.wrapped, "ConnectionsTo", part.wrapped if part else None
            )
        )

    @enforce_parameter_types
    def copy_to(self: "Self", container: "_2500.Assembly") -> "Part":
        """mastapy.system_model.part_model.Part

        Args:
            container (mastapy.system_model.part_model.Assembly)
        """
        method_result = pythonnet_method_call(
            self.wrapped, "CopyTo", container.wrapped if container else None
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def create_geometry_export_options(self: "Self") -> "_2308.GeometryExportOptions":
        """mastapy.system_model.import_export.GeometryExportOptions"""
        method_result = pythonnet_method_call(
            self.wrapped, "CreateGeometryExportOptions"
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    def delete_connections(self: "Self") -> None:
        """Method does not return."""
        pythonnet_method_call(self.wrapped, "DeleteConnections")

    @property
    def cast_to(self: "Self") -> "_Cast_Part":
        """Cast to another type.

        Returns:
            _Cast_Part
        """
        return _Cast_Part(self)
