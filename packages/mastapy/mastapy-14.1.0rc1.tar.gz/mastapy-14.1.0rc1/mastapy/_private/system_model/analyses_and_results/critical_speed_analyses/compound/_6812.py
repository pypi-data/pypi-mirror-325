"""AbstractAssemblyCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6893,
)

_ABSTRACT_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AbstractAssemblyCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6678,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6818,
        _6819,
        _6822,
        _6825,
        _6830,
        _6832,
        _6833,
        _6838,
        _6843,
        _6846,
        _6849,
        _6853,
        _6855,
        _6861,
        _6867,
        _6869,
        _6872,
        _6876,
        _6880,
        _6883,
        _6886,
        _6889,
        _6894,
        _6898,
        _6905,
        _6908,
        _6912,
        _6915,
        _6916,
        _6921,
        _6924,
        _6927,
        _6931,
        _6939,
        _6942,
    )

    Self = TypeVar("Self", bound="AbstractAssemblyCompoundCriticalSpeedAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractAssemblyCompoundCriticalSpeedAnalysis._Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis:
    """Special nested class for casting AbstractAssemblyCompoundCriticalSpeedAnalysis to subclasses."""

    __parent__: "AbstractAssemblyCompoundCriticalSpeedAnalysis"

    @property
    def part_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6893.PartCompoundCriticalSpeedAnalysis":
        return self.__parent__._cast(_6893.PartCompoundCriticalSpeedAnalysis)

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
    def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6818.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6818,
        )

        return self.__parent__._cast(
            _6818.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6819.AssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6819,
        )

        return self.__parent__._cast(_6819.AssemblyCompoundCriticalSpeedAnalysis)

    @property
    def belt_drive_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6822.BeltDriveCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6822,
        )

        return self.__parent__._cast(_6822.BeltDriveCompoundCriticalSpeedAnalysis)

    @property
    def bevel_differential_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6825.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6825,
        )

        return self.__parent__._cast(
            _6825.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6830.BevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6830,
        )

        return self.__parent__._cast(_6830.BevelGearSetCompoundCriticalSpeedAnalysis)

    @property
    def bolted_joint_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6832.BoltedJointCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6832,
        )

        return self.__parent__._cast(_6832.BoltedJointCompoundCriticalSpeedAnalysis)

    @property
    def clutch_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6833.ClutchCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6833,
        )

        return self.__parent__._cast(_6833.ClutchCompoundCriticalSpeedAnalysis)

    @property
    def concept_coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6838.ConceptCouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6838,
        )

        return self.__parent__._cast(_6838.ConceptCouplingCompoundCriticalSpeedAnalysis)

    @property
    def concept_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6843.ConceptGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6843,
        )

        return self.__parent__._cast(_6843.ConceptGearSetCompoundCriticalSpeedAnalysis)

    @property
    def conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6846.ConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6846,
        )

        return self.__parent__._cast(_6846.ConicalGearSetCompoundCriticalSpeedAnalysis)

    @property
    def coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6849.CouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6849,
        )

        return self.__parent__._cast(_6849.CouplingCompoundCriticalSpeedAnalysis)

    @property
    def cvt_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6853.CVTCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6853,
        )

        return self.__parent__._cast(_6853.CVTCompoundCriticalSpeedAnalysis)

    @property
    def cycloidal_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6855.CycloidalAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6855,
        )

        return self.__parent__._cast(
            _6855.CycloidalAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def cylindrical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6861.CylindricalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6861,
        )

        return self.__parent__._cast(
            _6861.CylindricalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def face_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6867.FaceGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6867,
        )

        return self.__parent__._cast(_6867.FaceGearSetCompoundCriticalSpeedAnalysis)

    @property
    def flexible_pin_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6869.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6869,
        )

        return self.__parent__._cast(
            _6869.FlexiblePinAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6872.GearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6872,
        )

        return self.__parent__._cast(_6872.GearSetCompoundCriticalSpeedAnalysis)

    @property
    def hypoid_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6876.HypoidGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6876,
        )

        return self.__parent__._cast(_6876.HypoidGearSetCompoundCriticalSpeedAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6880.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6880,
        )

        return self.__parent__._cast(
            _6880.KlingelnbergCycloPalloidConicalGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6883.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6883,
        )

        return self.__parent__._cast(
            _6883.KlingelnbergCycloPalloidHypoidGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> (
        "_6886.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis"
    ):
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6886,
        )

        return self.__parent__._cast(
            _6886.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def microphone_array_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6889.MicrophoneArrayCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6889,
        )

        return self.__parent__._cast(_6889.MicrophoneArrayCompoundCriticalSpeedAnalysis)

    @property
    def part_to_part_shear_coupling_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6894.PartToPartShearCouplingCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6894,
        )

        return self.__parent__._cast(
            _6894.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
        )

    @property
    def planetary_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6898.PlanetaryGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6898,
        )

        return self.__parent__._cast(
            _6898.PlanetaryGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def rolling_ring_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6905.RollingRingAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6905,
        )

        return self.__parent__._cast(
            _6905.RollingRingAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def root_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6908.RootAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6908,
        )

        return self.__parent__._cast(_6908.RootAssemblyCompoundCriticalSpeedAnalysis)

    @property
    def specialised_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6912.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6912,
        )

        return self.__parent__._cast(
            _6912.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
        )

    @property
    def spiral_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6915.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6915,
        )

        return self.__parent__._cast(
            _6915.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def spring_damper_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6916.SpringDamperCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6916,
        )

        return self.__parent__._cast(_6916.SpringDamperCompoundCriticalSpeedAnalysis)

    @property
    def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6921.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6921,
        )

        return self.__parent__._cast(
            _6921.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6924.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6924,
        )

        return self.__parent__._cast(
            _6924.StraightBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def synchroniser_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6927.SynchroniserCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6927,
        )

        return self.__parent__._cast(_6927.SynchroniserCompoundCriticalSpeedAnalysis)

    @property
    def torque_converter_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6931.TorqueConverterCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6931,
        )

        return self.__parent__._cast(_6931.TorqueConverterCompoundCriticalSpeedAnalysis)

    @property
    def worm_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6939.WormGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6939,
        )

        return self.__parent__._cast(_6939.WormGearSetCompoundCriticalSpeedAnalysis)

    @property
    def zerol_bevel_gear_set_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6942.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses.compound import (
            _6942,
        )

        return self.__parent__._cast(
            _6942.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
        )

    @property
    def abstract_assembly_compound_critical_speed_analysis(
        self: "CastSelf",
    ) -> "AbstractAssemblyCompoundCriticalSpeedAnalysis":
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
class AbstractAssemblyCompoundCriticalSpeedAnalysis(
    _6893.PartCompoundCriticalSpeedAnalysis
):
    """AbstractAssemblyCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_ASSEMBLY_COMPOUND_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_6678.AbstractAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractAssemblyCriticalSpeedAnalysis]

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
    ) -> "List[_6678.AbstractAssemblyCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractAssemblyCriticalSpeedAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis
        """
        return _Cast_AbstractAssemblyCompoundCriticalSpeedAnalysis(self)
