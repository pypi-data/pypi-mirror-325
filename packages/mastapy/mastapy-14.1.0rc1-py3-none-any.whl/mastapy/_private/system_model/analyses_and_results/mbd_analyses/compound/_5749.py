"""SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
    _5649,
)

_SPECIALISED_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5607
    from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
        _5655,
        _5659,
        _5662,
        _5667,
        _5669,
        _5670,
        _5675,
        _5680,
        _5683,
        _5686,
        _5690,
        _5692,
        _5698,
        _5704,
        _5706,
        _5709,
        _5713,
        _5717,
        _5720,
        _5723,
        _5726,
        _5730,
        _5731,
        _5735,
        _5742,
        _5752,
        _5753,
        _5758,
        _5761,
        _5764,
        _5768,
        _5776,
        _5779,
    )

    Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis._Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis:
    """Special nested class for casting SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis"

    @property
    def abstract_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5649.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
        return self.__parent__._cast(
            _5649.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def part_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5730.PartCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5730,
        )

        return self.__parent__._cast(_5730.PartCompoundMultibodyDynamicsAnalysis)

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
    def agma_gleason_conical_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5655.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5655,
        )

        return self.__parent__._cast(
            _5655.AGMAGleasonConicalGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def belt_drive_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5659.BeltDriveCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5659,
        )

        return self.__parent__._cast(_5659.BeltDriveCompoundMultibodyDynamicsAnalysis)

    @property
    def bevel_differential_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5662.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5662,
        )

        return self.__parent__._cast(
            _5662.BevelDifferentialGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5667.BevelGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5667,
        )

        return self.__parent__._cast(
            _5667.BevelGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bolted_joint_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5669.BoltedJointCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5669,
        )

        return self.__parent__._cast(_5669.BoltedJointCompoundMultibodyDynamicsAnalysis)

    @property
    def clutch_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5670.ClutchCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5670,
        )

        return self.__parent__._cast(_5670.ClutchCompoundMultibodyDynamicsAnalysis)

    @property
    def concept_coupling_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5675.ConceptCouplingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5675,
        )

        return self.__parent__._cast(
            _5675.ConceptCouplingCompoundMultibodyDynamicsAnalysis
        )

    @property
    def concept_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5680.ConceptGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5680,
        )

        return self.__parent__._cast(
            _5680.ConceptGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def conical_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5683.ConicalGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5683,
        )

        return self.__parent__._cast(
            _5683.ConicalGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def coupling_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5686.CouplingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5686,
        )

        return self.__parent__._cast(_5686.CouplingCompoundMultibodyDynamicsAnalysis)

    @property
    def cvt_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5690.CVTCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5690,
        )

        return self.__parent__._cast(_5690.CVTCompoundMultibodyDynamicsAnalysis)

    @property
    def cycloidal_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5692.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5692,
        )

        return self.__parent__._cast(
            _5692.CycloidalAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def cylindrical_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5698.CylindricalGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5698,
        )

        return self.__parent__._cast(
            _5698.CylindricalGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def face_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5704.FaceGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5704,
        )

        return self.__parent__._cast(_5704.FaceGearSetCompoundMultibodyDynamicsAnalysis)

    @property
    def flexible_pin_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5706.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5706,
        )

        return self.__parent__._cast(
            _5706.FlexiblePinAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5709.GearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5709,
        )

        return self.__parent__._cast(_5709.GearSetCompoundMultibodyDynamicsAnalysis)

    @property
    def hypoid_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5713.HypoidGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5713,
        )

        return self.__parent__._cast(
            _5713.HypoidGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> (
        "_5717.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis"
    ):
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5717,
        )

        return self.__parent__._cast(
            _5717.KlingelnbergCycloPalloidConicalGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5720.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5720,
        )

        return self.__parent__._cast(
            _5720.KlingelnbergCycloPalloidHypoidGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5723.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5723,
        )

        return self.__parent__._cast(
            _5723.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def microphone_array_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5726.MicrophoneArrayCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5726,
        )

        return self.__parent__._cast(
            _5726.MicrophoneArrayCompoundMultibodyDynamicsAnalysis
        )

    @property
    def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5731.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5731,
        )

        return self.__parent__._cast(
            _5731.PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis
        )

    @property
    def planetary_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5735.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5735,
        )

        return self.__parent__._cast(
            _5735.PlanetaryGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def rolling_ring_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5742.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5742,
        )

        return self.__parent__._cast(
            _5742.RollingRingAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def spiral_bevel_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5752.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5752,
        )

        return self.__parent__._cast(
            _5752.SpiralBevelGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def spring_damper_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5753.SpringDamperCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5753,
        )

        return self.__parent__._cast(
            _5753.SpringDamperCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_diff_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5758.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5758,
        )

        return self.__parent__._cast(
            _5758.StraightBevelDiffGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5761.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5761,
        )

        return self.__parent__._cast(
            _5761.StraightBevelGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def synchroniser_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5764.SynchroniserCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5764,
        )

        return self.__parent__._cast(
            _5764.SynchroniserCompoundMultibodyDynamicsAnalysis
        )

    @property
    def torque_converter_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5768.TorqueConverterCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5768,
        )

        return self.__parent__._cast(
            _5768.TorqueConverterCompoundMultibodyDynamicsAnalysis
        )

    @property
    def worm_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5776.WormGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5776,
        )

        return self.__parent__._cast(_5776.WormGearSetCompoundMultibodyDynamicsAnalysis)

    @property
    def zerol_bevel_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5779.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5779,
        )

        return self.__parent__._cast(
            _5779.ZerolBevelGearSetCompoundMultibodyDynamicsAnalysis
        )

    @property
    def specialised_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
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
class SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis(
    _5649.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
):
    """SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPECIALISED_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_5607.SpecialisedAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpecialisedAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "List[_5607.SpecialisedAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SpecialisedAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "_Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
        """
        return _Cast_SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis(self)
