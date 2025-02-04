"""AbstractAssemblyMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5585

_ABSTRACT_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AbstractAssemblyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7710,
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
        _5497,
        _5499,
        _5504,
        _5507,
        _5512,
        _5513,
        _5517,
        _5523,
        _5526,
        _5529,
        _5534,
        _5536,
        _5538,
        _5544,
        _5550,
        _5552,
        _5556,
        _5560,
        _5568,
        _5571,
        _5574,
        _5580,
        _5588,
        _5590,
        _5597,
        _5600,
        _5607,
        _5610,
        _5614,
        _5617,
        _5620,
        _5624,
        _5629,
        _5638,
        _5641,
    )
    from mastapy._private.system_model.part_model import _2501

    Self = TypeVar("Self", bound="AbstractAssemblyMultibodyDynamicsAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractAssemblyMultibodyDynamicsAnalysis._Cast_AbstractAssemblyMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyMultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractAssemblyMultibodyDynamicsAnalysis:
    """Special nested class for casting AbstractAssemblyMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "AbstractAssemblyMultibodyDynamicsAnalysis"

    @property
    def part_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5585.PartMultibodyDynamicsAnalysis":
        return self.__parent__._cast(_5585.PartMultibodyDynamicsAnalysis)

    @property
    def part_time_series_load_analysis_case(
        self: "CastSelf",
    ) -> "_7710.PartTimeSeriesLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7710,
        )

        return self.__parent__._cast(_7710.PartTimeSeriesLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7706.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7706,
        )

        return self.__parent__._cast(_7706.PartAnalysisCase)

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
    def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5497.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5497,
        )

        return self.__parent__._cast(
            _5497.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
        )

    @property
    def assembly_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5499.AssemblyMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5499,
        )

        return self.__parent__._cast(_5499.AssemblyMultibodyDynamicsAnalysis)

    @property
    def belt_drive_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5504.BeltDriveMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5504,
        )

        return self.__parent__._cast(_5504.BeltDriveMultibodyDynamicsAnalysis)

    @property
    def bevel_differential_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5507.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5507,
        )

        return self.__parent__._cast(
            _5507.BevelDifferentialGearSetMultibodyDynamicsAnalysis
        )

    @property
    def bevel_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5512.BevelGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5512,
        )

        return self.__parent__._cast(_5512.BevelGearSetMultibodyDynamicsAnalysis)

    @property
    def bolted_joint_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5513.BoltedJointMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5513,
        )

        return self.__parent__._cast(_5513.BoltedJointMultibodyDynamicsAnalysis)

    @property
    def clutch_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5517.ClutchMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5517,
        )

        return self.__parent__._cast(_5517.ClutchMultibodyDynamicsAnalysis)

    @property
    def concept_coupling_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5523.ConceptCouplingMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5523,
        )

        return self.__parent__._cast(_5523.ConceptCouplingMultibodyDynamicsAnalysis)

    @property
    def concept_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5526.ConceptGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5526,
        )

        return self.__parent__._cast(_5526.ConceptGearSetMultibodyDynamicsAnalysis)

    @property
    def conical_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5529.ConicalGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5529,
        )

        return self.__parent__._cast(_5529.ConicalGearSetMultibodyDynamicsAnalysis)

    @property
    def coupling_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5534.CouplingMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5534,
        )

        return self.__parent__._cast(_5534.CouplingMultibodyDynamicsAnalysis)

    @property
    def cvt_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5536.CVTMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5536,
        )

        return self.__parent__._cast(_5536.CVTMultibodyDynamicsAnalysis)

    @property
    def cycloidal_assembly_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5538.CycloidalAssemblyMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5538,
        )

        return self.__parent__._cast(_5538.CycloidalAssemblyMultibodyDynamicsAnalysis)

    @property
    def cylindrical_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5544.CylindricalGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5544,
        )

        return self.__parent__._cast(_5544.CylindricalGearSetMultibodyDynamicsAnalysis)

    @property
    def face_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5550.FaceGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5550,
        )

        return self.__parent__._cast(_5550.FaceGearSetMultibodyDynamicsAnalysis)

    @property
    def flexible_pin_assembly_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5552.FlexiblePinAssemblyMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5552,
        )

        return self.__parent__._cast(_5552.FlexiblePinAssemblyMultibodyDynamicsAnalysis)

    @property
    def gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5556.GearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5556,
        )

        return self.__parent__._cast(_5556.GearSetMultibodyDynamicsAnalysis)

    @property
    def hypoid_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5560.HypoidGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5560,
        )

        return self.__parent__._cast(_5560.HypoidGearSetMultibodyDynamicsAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5568.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5568,
        )

        return self.__parent__._cast(
            _5568.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5571.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5571,
        )

        return self.__parent__._cast(
            _5571.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5574.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5574,
        )

        return self.__parent__._cast(
            _5574.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
        )

    @property
    def microphone_array_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5580.MicrophoneArrayMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5580,
        )

        return self.__parent__._cast(_5580.MicrophoneArrayMultibodyDynamicsAnalysis)

    @property
    def part_to_part_shear_coupling_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5588.PartToPartShearCouplingMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5588,
        )

        return self.__parent__._cast(
            _5588.PartToPartShearCouplingMultibodyDynamicsAnalysis
        )

    @property
    def planetary_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5590.PlanetaryGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5590,
        )

        return self.__parent__._cast(_5590.PlanetaryGearSetMultibodyDynamicsAnalysis)

    @property
    def rolling_ring_assembly_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5597.RollingRingAssemblyMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5597,
        )

        return self.__parent__._cast(_5597.RollingRingAssemblyMultibodyDynamicsAnalysis)

    @property
    def root_assembly_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5600.RootAssemblyMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5600,
        )

        return self.__parent__._cast(_5600.RootAssemblyMultibodyDynamicsAnalysis)

    @property
    def specialised_assembly_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5607.SpecialisedAssemblyMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5607,
        )

        return self.__parent__._cast(_5607.SpecialisedAssemblyMultibodyDynamicsAnalysis)

    @property
    def spiral_bevel_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5610.SpiralBevelGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5610,
        )

        return self.__parent__._cast(_5610.SpiralBevelGearSetMultibodyDynamicsAnalysis)

    @property
    def spring_damper_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5614.SpringDamperMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5614,
        )

        return self.__parent__._cast(_5614.SpringDamperMultibodyDynamicsAnalysis)

    @property
    def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5617.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5617,
        )

        return self.__parent__._cast(
            _5617.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5620.StraightBevelGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5620,
        )

        return self.__parent__._cast(
            _5620.StraightBevelGearSetMultibodyDynamicsAnalysis
        )

    @property
    def synchroniser_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5624.SynchroniserMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5624,
        )

        return self.__parent__._cast(_5624.SynchroniserMultibodyDynamicsAnalysis)

    @property
    def torque_converter_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5629.TorqueConverterMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5629,
        )

        return self.__parent__._cast(_5629.TorqueConverterMultibodyDynamicsAnalysis)

    @property
    def worm_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5638.WormGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5638,
        )

        return self.__parent__._cast(_5638.WormGearSetMultibodyDynamicsAnalysis)

    @property
    def zerol_bevel_gear_set_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5641.ZerolBevelGearSetMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5641,
        )

        return self.__parent__._cast(_5641.ZerolBevelGearSetMultibodyDynamicsAnalysis)

    @property
    def abstract_assembly_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "AbstractAssemblyMultibodyDynamicsAnalysis":
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
class AbstractAssemblyMultibodyDynamicsAnalysis(_5585.PartMultibodyDynamicsAnalysis):
    """AbstractAssemblyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_ASSEMBLY_MULTIBODY_DYNAMICS_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2501.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: "Self") -> "_2501.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractAssemblyMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AbstractAssemblyMultibodyDynamicsAnalysis
        """
        return _Cast_AbstractAssemblyMultibodyDynamicsAnalysis(self)
