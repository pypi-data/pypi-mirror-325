"""SpecialisedAssemblyLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.static_loads import _7494

_SPECIALISED_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpecialisedAssemblyLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7503,
        _7509,
        _7512,
        _7517,
        _7518,
        _7522,
        _7528,
        _7531,
        _7536,
        _7541,
        _7543,
        _7545,
        _7553,
        _7574,
        _7576,
        _7583,
        _7595,
        _7602,
        _7605,
        _7608,
        _7612,
        _7618,
        _7621,
        _7623,
        _7635,
        _7645,
        _7648,
        _7651,
        _7654,
        _7658,
        _7664,
        _7675,
        _7678,
    )
    from mastapy._private.system_model.part_model import _2546

    Self = TypeVar("Self", bound="SpecialisedAssemblyLoadCase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpecialisedAssemblyLoadCase._Cast_SpecialisedAssemblyLoadCase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpecialisedAssemblyLoadCase:
    """Special nested class for casting SpecialisedAssemblyLoadCase to subclasses."""

    __parent__: "SpecialisedAssemblyLoadCase"

    @property
    def abstract_assembly_load_case(
        self: "CastSelf",
    ) -> "_7494.AbstractAssemblyLoadCase":
        return self.__parent__._cast(_7494.AbstractAssemblyLoadCase)

    @property
    def part_load_case(self: "CastSelf") -> "_7618.PartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7618,
        )

        return self.__parent__._cast(_7618.PartLoadCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2732.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2732

        return self.__parent__._cast(_2732.PartAnalysis)

    @property
    def design_entity_single_context_analysis(
        self: "CastSelf",
    ) -> "_2728.DesignEntitySingleContextAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2728

        return self.__parent__._cast(_2728.DesignEntitySingleContextAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2726.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2726

        return self.__parent__._cast(_2726.DesignEntityAnalysis)

    @property
    def agma_gleason_conical_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7503.AGMAGleasonConicalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7503,
        )

        return self.__parent__._cast(_7503.AGMAGleasonConicalGearSetLoadCase)

    @property
    def belt_drive_load_case(self: "CastSelf") -> "_7509.BeltDriveLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7509,
        )

        return self.__parent__._cast(_7509.BeltDriveLoadCase)

    @property
    def bevel_differential_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7512.BevelDifferentialGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7512,
        )

        return self.__parent__._cast(_7512.BevelDifferentialGearSetLoadCase)

    @property
    def bevel_gear_set_load_case(self: "CastSelf") -> "_7517.BevelGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7517,
        )

        return self.__parent__._cast(_7517.BevelGearSetLoadCase)

    @property
    def bolted_joint_load_case(self: "CastSelf") -> "_7518.BoltedJointLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7518,
        )

        return self.__parent__._cast(_7518.BoltedJointLoadCase)

    @property
    def clutch_load_case(self: "CastSelf") -> "_7522.ClutchLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7522,
        )

        return self.__parent__._cast(_7522.ClutchLoadCase)

    @property
    def concept_coupling_load_case(self: "CastSelf") -> "_7528.ConceptCouplingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7528,
        )

        return self.__parent__._cast(_7528.ConceptCouplingLoadCase)

    @property
    def concept_gear_set_load_case(self: "CastSelf") -> "_7531.ConceptGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7531,
        )

        return self.__parent__._cast(_7531.ConceptGearSetLoadCase)

    @property
    def conical_gear_set_load_case(self: "CastSelf") -> "_7536.ConicalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7536,
        )

        return self.__parent__._cast(_7536.ConicalGearSetLoadCase)

    @property
    def coupling_load_case(self: "CastSelf") -> "_7541.CouplingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7541,
        )

        return self.__parent__._cast(_7541.CouplingLoadCase)

    @property
    def cvt_load_case(self: "CastSelf") -> "_7543.CVTLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7543,
        )

        return self.__parent__._cast(_7543.CVTLoadCase)

    @property
    def cycloidal_assembly_load_case(
        self: "CastSelf",
    ) -> "_7545.CycloidalAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7545,
        )

        return self.__parent__._cast(_7545.CycloidalAssemblyLoadCase)

    @property
    def cylindrical_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7553.CylindricalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7553,
        )

        return self.__parent__._cast(_7553.CylindricalGearSetLoadCase)

    @property
    def face_gear_set_load_case(self: "CastSelf") -> "_7574.FaceGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7574,
        )

        return self.__parent__._cast(_7574.FaceGearSetLoadCase)

    @property
    def flexible_pin_assembly_load_case(
        self: "CastSelf",
    ) -> "_7576.FlexiblePinAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7576,
        )

        return self.__parent__._cast(_7576.FlexiblePinAssemblyLoadCase)

    @property
    def gear_set_load_case(self: "CastSelf") -> "_7583.GearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7583,
        )

        return self.__parent__._cast(_7583.GearSetLoadCase)

    @property
    def hypoid_gear_set_load_case(self: "CastSelf") -> "_7595.HypoidGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7595,
        )

        return self.__parent__._cast(_7595.HypoidGearSetLoadCase)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7602.KlingelnbergCycloPalloidConicalGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7602,
        )

        return self.__parent__._cast(
            _7602.KlingelnbergCycloPalloidConicalGearSetLoadCase
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7605.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7605,
        )

        return self.__parent__._cast(
            _7605.KlingelnbergCycloPalloidHypoidGearSetLoadCase
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7608.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7608,
        )

        return self.__parent__._cast(
            _7608.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
        )

    @property
    def microphone_array_load_case(self: "CastSelf") -> "_7612.MicrophoneArrayLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7612,
        )

        return self.__parent__._cast(_7612.MicrophoneArrayLoadCase)

    @property
    def part_to_part_shear_coupling_load_case(
        self: "CastSelf",
    ) -> "_7621.PartToPartShearCouplingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7621,
        )

        return self.__parent__._cast(_7621.PartToPartShearCouplingLoadCase)

    @property
    def planetary_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7623.PlanetaryGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7623,
        )

        return self.__parent__._cast(_7623.PlanetaryGearSetLoadCase)

    @property
    def rolling_ring_assembly_load_case(
        self: "CastSelf",
    ) -> "_7635.RollingRingAssemblyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7635,
        )

        return self.__parent__._cast(_7635.RollingRingAssemblyLoadCase)

    @property
    def spiral_bevel_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7645.SpiralBevelGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7645,
        )

        return self.__parent__._cast(_7645.SpiralBevelGearSetLoadCase)

    @property
    def spring_damper_load_case(self: "CastSelf") -> "_7648.SpringDamperLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7648,
        )

        return self.__parent__._cast(_7648.SpringDamperLoadCase)

    @property
    def straight_bevel_diff_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7651.StraightBevelDiffGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7651,
        )

        return self.__parent__._cast(_7651.StraightBevelDiffGearSetLoadCase)

    @property
    def straight_bevel_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7654.StraightBevelGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7654,
        )

        return self.__parent__._cast(_7654.StraightBevelGearSetLoadCase)

    @property
    def synchroniser_load_case(self: "CastSelf") -> "_7658.SynchroniserLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7658,
        )

        return self.__parent__._cast(_7658.SynchroniserLoadCase)

    @property
    def torque_converter_load_case(self: "CastSelf") -> "_7664.TorqueConverterLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7664,
        )

        return self.__parent__._cast(_7664.TorqueConverterLoadCase)

    @property
    def worm_gear_set_load_case(self: "CastSelf") -> "_7675.WormGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7675,
        )

        return self.__parent__._cast(_7675.WormGearSetLoadCase)

    @property
    def zerol_bevel_gear_set_load_case(
        self: "CastSelf",
    ) -> "_7678.ZerolBevelGearSetLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7678,
        )

        return self.__parent__._cast(_7678.ZerolBevelGearSetLoadCase)

    @property
    def specialised_assembly_load_case(
        self: "CastSelf",
    ) -> "SpecialisedAssemblyLoadCase":
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
class SpecialisedAssemblyLoadCase(_7494.AbstractAssemblyLoadCase):
    """SpecialisedAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPECIALISED_ASSEMBLY_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2546.SpecialisedAssembly":
        """mastapy.system_model.part_model.SpecialisedAssembly

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_SpecialisedAssemblyLoadCase":
        """Cast to another type.

        Returns:
            _Cast_SpecialisedAssemblyLoadCase
        """
        return _Cast_SpecialisedAssemblyLoadCase(self)
