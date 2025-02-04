"""SpecialisedAssemblyModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4964,
)

_SPECIALISED_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "SpecialisedAssemblyModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4970,
        _4974,
        _4977,
        _4982,
        _4983,
        _4987,
        _4992,
        _4995,
        _4998,
        _5003,
        _5005,
        _5007,
        _5013,
        _5020,
        _5022,
        _5025,
        _5029,
        _5033,
        _5036,
        _5039,
        _5042,
        _5047,
        _5050,
        _5052,
        _5059,
        _5069,
        _5072,
        _5075,
        _5078,
        _5082,
        _5086,
        _5093,
        _5096,
    )
    from mastapy._private.system_model.part_model import _2546

    Self = TypeVar("Self", bound="SpecialisedAssemblyModalAnalysisAtAStiffness")
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpecialisedAssemblyModalAnalysisAtAStiffness._Cast_SpecialisedAssemblyModalAnalysisAtAStiffness",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyModalAnalysisAtAStiffness",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpecialisedAssemblyModalAnalysisAtAStiffness:
    """Special nested class for casting SpecialisedAssemblyModalAnalysisAtAStiffness to subclasses."""

    __parent__: "SpecialisedAssemblyModalAnalysisAtAStiffness"

    @property
    def abstract_assembly_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4964.AbstractAssemblyModalAnalysisAtAStiffness":
        return self.__parent__._cast(_4964.AbstractAssemblyModalAnalysisAtAStiffness)

    @property
    def part_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5047.PartModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5047,
        )

        return self.__parent__._cast(_5047.PartModalAnalysisAtAStiffness)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7709.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7709,
        )

        return self.__parent__._cast(_7709.PartStaticLoadAnalysisCase)

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
    def agma_gleason_conical_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4970.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4970,
        )

        return self.__parent__._cast(
            _4970.AGMAGleasonConicalGearSetModalAnalysisAtAStiffness
        )

    @property
    def belt_drive_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4974.BeltDriveModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4974,
        )

        return self.__parent__._cast(_4974.BeltDriveModalAnalysisAtAStiffness)

    @property
    def bevel_differential_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4977.BevelDifferentialGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4977,
        )

        return self.__parent__._cast(
            _4977.BevelDifferentialGearSetModalAnalysisAtAStiffness
        )

    @property
    def bevel_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4982.BevelGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4982,
        )

        return self.__parent__._cast(_4982.BevelGearSetModalAnalysisAtAStiffness)

    @property
    def bolted_joint_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4983.BoltedJointModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4983,
        )

        return self.__parent__._cast(_4983.BoltedJointModalAnalysisAtAStiffness)

    @property
    def clutch_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4987.ClutchModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4987,
        )

        return self.__parent__._cast(_4987.ClutchModalAnalysisAtAStiffness)

    @property
    def concept_coupling_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4992.ConceptCouplingModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4992,
        )

        return self.__parent__._cast(_4992.ConceptCouplingModalAnalysisAtAStiffness)

    @property
    def concept_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4995.ConceptGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4995,
        )

        return self.__parent__._cast(_4995.ConceptGearSetModalAnalysisAtAStiffness)

    @property
    def conical_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4998.ConicalGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4998,
        )

        return self.__parent__._cast(_4998.ConicalGearSetModalAnalysisAtAStiffness)

    @property
    def coupling_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5003.CouplingModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5003,
        )

        return self.__parent__._cast(_5003.CouplingModalAnalysisAtAStiffness)

    @property
    def cvt_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5005.CVTModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5005,
        )

        return self.__parent__._cast(_5005.CVTModalAnalysisAtAStiffness)

    @property
    def cycloidal_assembly_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5007.CycloidalAssemblyModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5007,
        )

        return self.__parent__._cast(_5007.CycloidalAssemblyModalAnalysisAtAStiffness)

    @property
    def cylindrical_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5013.CylindricalGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5013,
        )

        return self.__parent__._cast(_5013.CylindricalGearSetModalAnalysisAtAStiffness)

    @property
    def face_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5020.FaceGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5020,
        )

        return self.__parent__._cast(_5020.FaceGearSetModalAnalysisAtAStiffness)

    @property
    def flexible_pin_assembly_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5022.FlexiblePinAssemblyModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5022,
        )

        return self.__parent__._cast(_5022.FlexiblePinAssemblyModalAnalysisAtAStiffness)

    @property
    def gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5025.GearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5025,
        )

        return self.__parent__._cast(_5025.GearSetModalAnalysisAtAStiffness)

    @property
    def hypoid_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5029.HypoidGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5029,
        )

        return self.__parent__._cast(_5029.HypoidGearSetModalAnalysisAtAStiffness)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5033.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5033,
        )

        return self.__parent__._cast(
            _5033.KlingelnbergCycloPalloidConicalGearSetModalAnalysisAtAStiffness
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5036.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5036,
        )

        return self.__parent__._cast(
            _5036.KlingelnbergCycloPalloidHypoidGearSetModalAnalysisAtAStiffness
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5039.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5039,
        )

        return self.__parent__._cast(
            _5039.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysisAtAStiffness
        )

    @property
    def microphone_array_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5042.MicrophoneArrayModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5042,
        )

        return self.__parent__._cast(_5042.MicrophoneArrayModalAnalysisAtAStiffness)

    @property
    def part_to_part_shear_coupling_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5050.PartToPartShearCouplingModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5050,
        )

        return self.__parent__._cast(
            _5050.PartToPartShearCouplingModalAnalysisAtAStiffness
        )

    @property
    def planetary_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5052.PlanetaryGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5052,
        )

        return self.__parent__._cast(_5052.PlanetaryGearSetModalAnalysisAtAStiffness)

    @property
    def rolling_ring_assembly_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5059.RollingRingAssemblyModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5059,
        )

        return self.__parent__._cast(_5059.RollingRingAssemblyModalAnalysisAtAStiffness)

    @property
    def spiral_bevel_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5069.SpiralBevelGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5069,
        )

        return self.__parent__._cast(_5069.SpiralBevelGearSetModalAnalysisAtAStiffness)

    @property
    def spring_damper_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5072.SpringDamperModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5072,
        )

        return self.__parent__._cast(_5072.SpringDamperModalAnalysisAtAStiffness)

    @property
    def straight_bevel_diff_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5075.StraightBevelDiffGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5075,
        )

        return self.__parent__._cast(
            _5075.StraightBevelDiffGearSetModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5078.StraightBevelGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5078,
        )

        return self.__parent__._cast(
            _5078.StraightBevelGearSetModalAnalysisAtAStiffness
        )

    @property
    def synchroniser_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5082.SynchroniserModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5082,
        )

        return self.__parent__._cast(_5082.SynchroniserModalAnalysisAtAStiffness)

    @property
    def torque_converter_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5086.TorqueConverterModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5086,
        )

        return self.__parent__._cast(_5086.TorqueConverterModalAnalysisAtAStiffness)

    @property
    def worm_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5093.WormGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5093,
        )

        return self.__parent__._cast(_5093.WormGearSetModalAnalysisAtAStiffness)

    @property
    def zerol_bevel_gear_set_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5096.ZerolBevelGearSetModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5096,
        )

        return self.__parent__._cast(_5096.ZerolBevelGearSetModalAnalysisAtAStiffness)

    @property
    def specialised_assembly_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "SpecialisedAssemblyModalAnalysisAtAStiffness":
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
class SpecialisedAssemblyModalAnalysisAtAStiffness(
    _4964.AbstractAssemblyModalAnalysisAtAStiffness
):
    """SpecialisedAssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _SPECIALISED_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS

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
    def cast_to(self: "Self") -> "_Cast_SpecialisedAssemblyModalAnalysisAtAStiffness":
        """Cast to another type.

        Returns:
            _Cast_SpecialisedAssemblyModalAnalysisAtAStiffness
        """
        return _Cast_SpecialisedAssemblyModalAnalysisAtAStiffness(self)
