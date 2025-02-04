"""SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6268,
)

_SPECIALISED_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6237,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6274,
        _6278,
        _6281,
        _6286,
        _6288,
        _6289,
        _6294,
        _6299,
        _6302,
        _6305,
        _6309,
        _6311,
        _6317,
        _6323,
        _6325,
        _6328,
        _6332,
        _6336,
        _6339,
        _6342,
        _6345,
        _6349,
        _6350,
        _6354,
        _6361,
        _6371,
        _6372,
        _6377,
        _6380,
        _6383,
        _6387,
        _6395,
        _6398,
    )

    Self = TypeVar(
        "Self", bound="SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation._Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation:
    """Special nested class for casting SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

    __parent__: "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation"

    @property
    def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6268.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        return self.__parent__._cast(
            _6268.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6349.PartCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6349,
        )

        return self.__parent__._cast(
            _6349.PartCompoundHarmonicAnalysisOfSingleExcitation
        )

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
    def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6274.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6274,
        )

        return self.__parent__._cast(
            _6274.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def belt_drive_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6278.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6278,
        )

        return self.__parent__._cast(
            _6278.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6281.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6281,
        )

        return self.__parent__._cast(
            _6281.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6286.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6286,
        )

        return self.__parent__._cast(
            _6286.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bolted_joint_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6288.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6288,
        )

        return self.__parent__._cast(
            _6288.BoltedJointCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def clutch_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6289.ClutchCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6289,
        )

        return self.__parent__._cast(
            _6289.ClutchCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_coupling_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6294.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6294,
        )

        return self.__parent__._cast(
            _6294.ConceptCouplingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6299.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6299,
        )

        return self.__parent__._cast(
            _6299.ConceptGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6302.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6302,
        )

        return self.__parent__._cast(
            _6302.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def coupling_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6305.CouplingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6305,
        )

        return self.__parent__._cast(
            _6305.CouplingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cvt_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6309.CVTCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6309,
        )

        return self.__parent__._cast(
            _6309.CVTCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cycloidal_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6311.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6311,
        )

        return self.__parent__._cast(
            _6311.CycloidalAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cylindrical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6317.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6317,
        )

        return self.__parent__._cast(
            _6317.CylindricalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def face_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6323.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6323,
        )

        return self.__parent__._cast(
            _6323.FaceGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def flexible_pin_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6325.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6325,
        )

        return self.__parent__._cast(
            _6325.FlexiblePinAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6328.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6328,
        )

        return self.__parent__._cast(
            _6328.GearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6332.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6332,
        )

        return self.__parent__._cast(
            _6332.HypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6336.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6336,
        )

        return self.__parent__._cast(
            _6336.KlingelnbergCycloPalloidConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6339.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6339,
        )

        return self.__parent__._cast(
            _6339.KlingelnbergCycloPalloidHypoidGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6342.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6342,
        )

        return self.__parent__._cast(
            _6342.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def microphone_array_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6345.MicrophoneArrayCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6345,
        )

        return self.__parent__._cast(
            _6345.MicrophoneArrayCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_to_part_shear_coupling_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6350.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6350,
        )

        return self.__parent__._cast(
            _6350.PartToPartShearCouplingCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def planetary_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6354.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6354,
        )

        return self.__parent__._cast(
            _6354.PlanetaryGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def rolling_ring_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6361.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6361,
        )

        return self.__parent__._cast(
            _6361.RollingRingAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6371.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6371,
        )

        return self.__parent__._cast(
            _6371.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spring_damper_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6372.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6372,
        )

        return self.__parent__._cast(
            _6372.SpringDamperCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6377.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6377,
        )

        return self.__parent__._cast(
            _6377.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6380.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6380,
        )

        return self.__parent__._cast(
            _6380.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def synchroniser_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6383.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6383,
        )

        return self.__parent__._cast(
            _6383.SynchroniserCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def torque_converter_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6387.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6387,
        )

        return self.__parent__._cast(
            _6387.TorqueConverterCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def worm_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6395.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6395,
        )

        return self.__parent__._cast(
            _6395.WormGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6398.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
            _6398,
        )

        return self.__parent__._cast(
            _6398.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
        )

    @property
    def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
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
class SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation(
    _6268.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
):
    """SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _SPECIALISED_ASSEMBLY_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_6237.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6237.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
        """Cast to another type.

        Returns:
            _Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
        """
        return _Cast_SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation(self)
