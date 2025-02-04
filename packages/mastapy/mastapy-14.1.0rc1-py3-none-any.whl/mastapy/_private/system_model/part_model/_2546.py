"""SpecialisedAssembly"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import python_net_import
from mastapy._private.system_model.part_model import _2501

_SPECIALISED_ASSEMBLY = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "SpecialisedAssembly"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model import _2269
    from mastapy._private.system_model.part_model import _2510, _2521, _2532, _2537
    from mastapy._private.system_model.part_model.couplings import (
        _2649,
        _2651,
        _2654,
        _2657,
        _2660,
        _2662,
        _2673,
        _2680,
        _2682,
        _2687,
    )
    from mastapy._private.system_model.part_model.cycloidal import _2640
    from mastapy._private.system_model.part_model.gears import (
        _2586,
        _2588,
        _2592,
        _2594,
        _2596,
        _2598,
        _2601,
        _2604,
        _2607,
        _2609,
        _2611,
        _2613,
        _2614,
        _2616,
        _2618,
        _2620,
        _2624,
        _2626,
    )

    Self = TypeVar("Self", bound="SpecialisedAssembly")
    CastSelf = TypeVar(
        "CastSelf", bound="SpecialisedAssembly._Cast_SpecialisedAssembly"
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssembly",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpecialisedAssembly:
    """Special nested class for casting SpecialisedAssembly to subclasses."""

    __parent__: "SpecialisedAssembly"

    @property
    def abstract_assembly(self: "CastSelf") -> "_2501.AbstractAssembly":
        return self.__parent__._cast(_2501.AbstractAssembly)

    @property
    def part(self: "CastSelf") -> "_2537.Part":
        from mastapy._private.system_model.part_model import _2537

        return self.__parent__._cast(_2537.Part)

    @property
    def design_entity(self: "CastSelf") -> "_2269.DesignEntity":
        from mastapy._private.system_model import _2269

        return self.__parent__._cast(_2269.DesignEntity)

    @property
    def bolted_joint(self: "CastSelf") -> "_2510.BoltedJoint":
        from mastapy._private.system_model.part_model import _2510

        return self.__parent__._cast(_2510.BoltedJoint)

    @property
    def flexible_pin_assembly(self: "CastSelf") -> "_2521.FlexiblePinAssembly":
        from mastapy._private.system_model.part_model import _2521

        return self.__parent__._cast(_2521.FlexiblePinAssembly)

    @property
    def microphone_array(self: "CastSelf") -> "_2532.MicrophoneArray":
        from mastapy._private.system_model.part_model import _2532

        return self.__parent__._cast(_2532.MicrophoneArray)

    @property
    def agma_gleason_conical_gear_set(
        self: "CastSelf",
    ) -> "_2586.AGMAGleasonConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2586

        return self.__parent__._cast(_2586.AGMAGleasonConicalGearSet)

    @property
    def bevel_differential_gear_set(
        self: "CastSelf",
    ) -> "_2588.BevelDifferentialGearSet":
        from mastapy._private.system_model.part_model.gears import _2588

        return self.__parent__._cast(_2588.BevelDifferentialGearSet)

    @property
    def bevel_gear_set(self: "CastSelf") -> "_2592.BevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2592

        return self.__parent__._cast(_2592.BevelGearSet)

    @property
    def concept_gear_set(self: "CastSelf") -> "_2594.ConceptGearSet":
        from mastapy._private.system_model.part_model.gears import _2594

        return self.__parent__._cast(_2594.ConceptGearSet)

    @property
    def conical_gear_set(self: "CastSelf") -> "_2596.ConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2596

        return self.__parent__._cast(_2596.ConicalGearSet)

    @property
    def cylindrical_gear_set(self: "CastSelf") -> "_2598.CylindricalGearSet":
        from mastapy._private.system_model.part_model.gears import _2598

        return self.__parent__._cast(_2598.CylindricalGearSet)

    @property
    def face_gear_set(self: "CastSelf") -> "_2601.FaceGearSet":
        from mastapy._private.system_model.part_model.gears import _2601

        return self.__parent__._cast(_2601.FaceGearSet)

    @property
    def gear_set(self: "CastSelf") -> "_2604.GearSet":
        from mastapy._private.system_model.part_model.gears import _2604

        return self.__parent__._cast(_2604.GearSet)

    @property
    def hypoid_gear_set(self: "CastSelf") -> "_2607.HypoidGearSet":
        from mastapy._private.system_model.part_model.gears import _2607

        return self.__parent__._cast(_2607.HypoidGearSet)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set(
        self: "CastSelf",
    ) -> "_2609.KlingelnbergCycloPalloidConicalGearSet":
        from mastapy._private.system_model.part_model.gears import _2609

        return self.__parent__._cast(_2609.KlingelnbergCycloPalloidConicalGearSet)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set(
        self: "CastSelf",
    ) -> "_2611.KlingelnbergCycloPalloidHypoidGearSet":
        from mastapy._private.system_model.part_model.gears import _2611

        return self.__parent__._cast(_2611.KlingelnbergCycloPalloidHypoidGearSet)

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
    def spiral_bevel_gear_set(self: "CastSelf") -> "_2616.SpiralBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2616

        return self.__parent__._cast(_2616.SpiralBevelGearSet)

    @property
    def straight_bevel_diff_gear_set(
        self: "CastSelf",
    ) -> "_2618.StraightBevelDiffGearSet":
        from mastapy._private.system_model.part_model.gears import _2618

        return self.__parent__._cast(_2618.StraightBevelDiffGearSet)

    @property
    def straight_bevel_gear_set(self: "CastSelf") -> "_2620.StraightBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2620

        return self.__parent__._cast(_2620.StraightBevelGearSet)

    @property
    def worm_gear_set(self: "CastSelf") -> "_2624.WormGearSet":
        from mastapy._private.system_model.part_model.gears import _2624

        return self.__parent__._cast(_2624.WormGearSet)

    @property
    def zerol_bevel_gear_set(self: "CastSelf") -> "_2626.ZerolBevelGearSet":
        from mastapy._private.system_model.part_model.gears import _2626

        return self.__parent__._cast(_2626.ZerolBevelGearSet)

    @property
    def cycloidal_assembly(self: "CastSelf") -> "_2640.CycloidalAssembly":
        from mastapy._private.system_model.part_model.cycloidal import _2640

        return self.__parent__._cast(_2640.CycloidalAssembly)

    @property
    def belt_drive(self: "CastSelf") -> "_2649.BeltDrive":
        from mastapy._private.system_model.part_model.couplings import _2649

        return self.__parent__._cast(_2649.BeltDrive)

    @property
    def clutch(self: "CastSelf") -> "_2651.Clutch":
        from mastapy._private.system_model.part_model.couplings import _2651

        return self.__parent__._cast(_2651.Clutch)

    @property
    def concept_coupling(self: "CastSelf") -> "_2654.ConceptCoupling":
        from mastapy._private.system_model.part_model.couplings import _2654

        return self.__parent__._cast(_2654.ConceptCoupling)

    @property
    def coupling(self: "CastSelf") -> "_2657.Coupling":
        from mastapy._private.system_model.part_model.couplings import _2657

        return self.__parent__._cast(_2657.Coupling)

    @property
    def cvt(self: "CastSelf") -> "_2660.CVT":
        from mastapy._private.system_model.part_model.couplings import _2660

        return self.__parent__._cast(_2660.CVT)

    @property
    def part_to_part_shear_coupling(
        self: "CastSelf",
    ) -> "_2662.PartToPartShearCoupling":
        from mastapy._private.system_model.part_model.couplings import _2662

        return self.__parent__._cast(_2662.PartToPartShearCoupling)

    @property
    def rolling_ring_assembly(self: "CastSelf") -> "_2673.RollingRingAssembly":
        from mastapy._private.system_model.part_model.couplings import _2673

        return self.__parent__._cast(_2673.RollingRingAssembly)

    @property
    def spring_damper(self: "CastSelf") -> "_2680.SpringDamper":
        from mastapy._private.system_model.part_model.couplings import _2680

        return self.__parent__._cast(_2680.SpringDamper)

    @property
    def synchroniser(self: "CastSelf") -> "_2682.Synchroniser":
        from mastapy._private.system_model.part_model.couplings import _2682

        return self.__parent__._cast(_2682.Synchroniser)

    @property
    def torque_converter(self: "CastSelf") -> "_2687.TorqueConverter":
        from mastapy._private.system_model.part_model.couplings import _2687

        return self.__parent__._cast(_2687.TorqueConverter)

    @property
    def specialised_assembly(self: "CastSelf") -> "SpecialisedAssembly":
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
class SpecialisedAssembly(_2501.AbstractAssembly):
    """SpecialisedAssembly

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPECIALISED_ASSEMBLY

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def cast_to(self: "Self") -> "_Cast_SpecialisedAssembly":
        """Cast to another type.

        Returns:
            _Cast_SpecialisedAssembly
        """
        return _Cast_SpecialisedAssembly(self)
