"""SpecialisedAssemblyCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
    _2928,
)

_SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "SpecialisedAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2883,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2934,
        _2938,
        _2941,
        _2946,
        _2948,
        _2949,
        _2954,
        _2959,
        _2962,
        _2965,
        _2969,
        _2971,
        _2977,
        _2984,
        _2986,
        _2989,
        _2993,
        _2997,
        _3000,
        _3003,
        _3006,
        _3010,
        _3011,
        _3015,
        _3022,
        _3033,
        _3034,
        _3039,
        _3042,
        _3045,
        _3049,
        _3057,
        _3060,
    )

    Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpecialisedAssemblyCompoundSystemDeflection._Cast_SpecialisedAssemblyCompoundSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpecialisedAssemblyCompoundSystemDeflection:
    """Special nested class for casting SpecialisedAssemblyCompoundSystemDeflection to subclasses."""

    __parent__: "SpecialisedAssemblyCompoundSystemDeflection"

    @property
    def abstract_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2928.AbstractAssemblyCompoundSystemDeflection":
        return self.__parent__._cast(_2928.AbstractAssemblyCompoundSystemDeflection)

    @property
    def part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3010.PartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3010,
        )

        return self.__parent__._cast(_3010.PartCompoundSystemDeflection)

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7707.PartCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7707,
        )

        return self.__parent__._cast(_7707.PartCompoundAnalysis)

    @property
    def design_entity_compound_analysis(
        self: "CastSelf",
    ) -> "_7704.DesignEntityCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7704,
        )

        return self.__parent__._cast(_7704.DesignEntityCompoundAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2726.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2726

        return self.__parent__._cast(_2726.DesignEntityAnalysis)

    @property
    def agma_gleason_conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2934.AGMAGleasonConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2934,
        )

        return self.__parent__._cast(
            _2934.AGMAGleasonConicalGearSetCompoundSystemDeflection
        )

    @property
    def belt_drive_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2938.BeltDriveCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2938,
        )

        return self.__parent__._cast(_2938.BeltDriveCompoundSystemDeflection)

    @property
    def bevel_differential_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2941.BevelDifferentialGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2941,
        )

        return self.__parent__._cast(
            _2941.BevelDifferentialGearSetCompoundSystemDeflection
        )

    @property
    def bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2946.BevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2946,
        )

        return self.__parent__._cast(_2946.BevelGearSetCompoundSystemDeflection)

    @property
    def bolted_joint_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2948.BoltedJointCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2948,
        )

        return self.__parent__._cast(_2948.BoltedJointCompoundSystemDeflection)

    @property
    def clutch_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2949.ClutchCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2949,
        )

        return self.__parent__._cast(_2949.ClutchCompoundSystemDeflection)

    @property
    def concept_coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2954.ConceptCouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2954,
        )

        return self.__parent__._cast(_2954.ConceptCouplingCompoundSystemDeflection)

    @property
    def concept_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2959.ConceptGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2959,
        )

        return self.__parent__._cast(_2959.ConceptGearSetCompoundSystemDeflection)

    @property
    def conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2962.ConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2962,
        )

        return self.__parent__._cast(_2962.ConicalGearSetCompoundSystemDeflection)

    @property
    def coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2965.CouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2965,
        )

        return self.__parent__._cast(_2965.CouplingCompoundSystemDeflection)

    @property
    def cvt_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2969.CVTCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2969,
        )

        return self.__parent__._cast(_2969.CVTCompoundSystemDeflection)

    @property
    def cycloidal_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2971.CycloidalAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2971,
        )

        return self.__parent__._cast(_2971.CycloidalAssemblyCompoundSystemDeflection)

    @property
    def cylindrical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2977.CylindricalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2977,
        )

        return self.__parent__._cast(_2977.CylindricalGearSetCompoundSystemDeflection)

    @property
    def face_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2984.FaceGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2984,
        )

        return self.__parent__._cast(_2984.FaceGearSetCompoundSystemDeflection)

    @property
    def flexible_pin_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2986.FlexiblePinAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2986,
        )

        return self.__parent__._cast(_2986.FlexiblePinAssemblyCompoundSystemDeflection)

    @property
    def gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2989.GearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2989,
        )

        return self.__parent__._cast(_2989.GearSetCompoundSystemDeflection)

    @property
    def hypoid_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2993.HypoidGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2993,
        )

        return self.__parent__._cast(_2993.HypoidGearSetCompoundSystemDeflection)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2997.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2997,
        )

        return self.__parent__._cast(
            _2997.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3000.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3000,
        )

        return self.__parent__._cast(
            _3000.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3003.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3003,
        )

        return self.__parent__._cast(
            _3003.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
        )

    @property
    def microphone_array_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3006.MicrophoneArrayCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3006,
        )

        return self.__parent__._cast(_3006.MicrophoneArrayCompoundSystemDeflection)

    @property
    def part_to_part_shear_coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3011.PartToPartShearCouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3011,
        )

        return self.__parent__._cast(
            _3011.PartToPartShearCouplingCompoundSystemDeflection
        )

    @property
    def planetary_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3015.PlanetaryGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3015,
        )

        return self.__parent__._cast(_3015.PlanetaryGearSetCompoundSystemDeflection)

    @property
    def rolling_ring_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3022.RollingRingAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3022,
        )

        return self.__parent__._cast(_3022.RollingRingAssemblyCompoundSystemDeflection)

    @property
    def spiral_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3033.SpiralBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3033,
        )

        return self.__parent__._cast(_3033.SpiralBevelGearSetCompoundSystemDeflection)

    @property
    def spring_damper_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3034.SpringDamperCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3034,
        )

        return self.__parent__._cast(_3034.SpringDamperCompoundSystemDeflection)

    @property
    def straight_bevel_diff_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3039.StraightBevelDiffGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3039,
        )

        return self.__parent__._cast(
            _3039.StraightBevelDiffGearSetCompoundSystemDeflection
        )

    @property
    def straight_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3042.StraightBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3042,
        )

        return self.__parent__._cast(_3042.StraightBevelGearSetCompoundSystemDeflection)

    @property
    def synchroniser_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3045.SynchroniserCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3045,
        )

        return self.__parent__._cast(_3045.SynchroniserCompoundSystemDeflection)

    @property
    def torque_converter_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3049.TorqueConverterCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3049,
        )

        return self.__parent__._cast(_3049.TorqueConverterCompoundSystemDeflection)

    @property
    def worm_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3057.WormGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3057,
        )

        return self.__parent__._cast(_3057.WormGearSetCompoundSystemDeflection)

    @property
    def zerol_bevel_gear_set_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3060.ZerolBevelGearSetCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3060,
        )

        return self.__parent__._cast(_3060.ZerolBevelGearSetCompoundSystemDeflection)

    @property
    def specialised_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "SpecialisedAssemblyCompoundSystemDeflection":
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
class SpecialisedAssemblyCompoundSystemDeflection(
    _2928.AbstractAssemblyCompoundSystemDeflection
):
    """SpecialisedAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPECIALISED_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_2883.SpecialisedAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_2883.SpecialisedAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SpecialisedAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_SpecialisedAssemblyCompoundSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_SpecialisedAssemblyCompoundSystemDeflection
        """
        return _Cast_SpecialisedAssemblyCompoundSystemDeflection(self)
