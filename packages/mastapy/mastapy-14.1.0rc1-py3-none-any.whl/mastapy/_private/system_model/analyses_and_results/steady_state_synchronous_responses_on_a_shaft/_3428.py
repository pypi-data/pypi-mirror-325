"""SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3328,
)

_SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3333,
        _3338,
        _3340,
        _3345,
        _3347,
        _3351,
        _3356,
        _3358,
        _3361,
        _3367,
        _3370,
        _3371,
        _3376,
        _3382,
        _3385,
        _3387,
        _3391,
        _3395,
        _3398,
        _3401,
        _3405,
        _3409,
        _3412,
        _3414,
        _3421,
        _3430,
        _3434,
        _3437,
        _3440,
        _3447,
        _3450,
        _3455,
        _3458,
    )
    from mastapy._private.system_model.part_model import _2546

    Self = TypeVar(
        "Self", bound="SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft:
    """Special nested class for casting SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft to subclasses."""

    __parent__: "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft"

    @property
    def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3328.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
        return self.__parent__._cast(
            _3328.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
        )

    @property
    def part_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3409.PartSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3409,
        )

        return self.__parent__._cast(_3409.PartSteadyStateSynchronousResponseOnAShaft)

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
    def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3333.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3333,
        )

        return self.__parent__._cast(
            _3333.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def belt_drive_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3338.BeltDriveSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3338,
        )

        return self.__parent__._cast(
            _3338.BeltDriveSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_differential_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3340.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3340,
        )

        return self.__parent__._cast(
            _3340.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3345.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3345,
        )

        return self.__parent__._cast(
            _3345.BevelGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def bolted_joint_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3347.BoltedJointSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3347,
        )

        return self.__parent__._cast(
            _3347.BoltedJointSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def clutch_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3351.ClutchSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3351,
        )

        return self.__parent__._cast(_3351.ClutchSteadyStateSynchronousResponseOnAShaft)

    @property
    def concept_coupling_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3356.ConceptCouplingSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3356,
        )

        return self.__parent__._cast(
            _3356.ConceptCouplingSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def concept_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3358.ConceptGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3358,
        )

        return self.__parent__._cast(
            _3358.ConceptGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3361.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3361,
        )

        return self.__parent__._cast(
            _3361.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def coupling_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3367.CouplingSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3367,
        )

        return self.__parent__._cast(
            _3367.CouplingSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cvt_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3370.CVTSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3370,
        )

        return self.__parent__._cast(_3370.CVTSteadyStateSynchronousResponseOnAShaft)

    @property
    def cycloidal_assembly_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3371.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3371,
        )

        return self.__parent__._cast(
            _3371.CycloidalAssemblySteadyStateSynchronousResponseOnAShaft
        )

    @property
    def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3376.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3376,
        )

        return self.__parent__._cast(
            _3376.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def face_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3382.FaceGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3382,
        )

        return self.__parent__._cast(
            _3382.FaceGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def flexible_pin_assembly_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3385.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3385,
        )

        return self.__parent__._cast(
            _3385.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft
        )

    @property
    def gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3387.GearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3387,
        )

        return self.__parent__._cast(
            _3387.GearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3391.HypoidGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3391,
        )

        return self.__parent__._cast(
            _3391.HypoidGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3395.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3395,
        )

        return self.__parent__._cast(
            _3395.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3398.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3398,
        )

        return self.__parent__._cast(
            _3398.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3401.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3401,
        )

        return self.__parent__._cast(
            _3401.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def microphone_array_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3405.MicrophoneArraySteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3405,
        )

        return self.__parent__._cast(
            _3405.MicrophoneArraySteadyStateSynchronousResponseOnAShaft
        )

    @property
    def part_to_part_shear_coupling_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3412.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3412,
        )

        return self.__parent__._cast(
            _3412.PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3414.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3414,
        )

        return self.__parent__._cast(
            _3414.PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def rolling_ring_assembly_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3421.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3421,
        )

        return self.__parent__._cast(
            _3421.RollingRingAssemblySteadyStateSynchronousResponseOnAShaft
        )

    @property
    def spiral_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3430.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3430,
        )

        return self.__parent__._cast(
            _3430.SpiralBevelGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def spring_damper_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3434.SpringDamperSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3434,
        )

        return self.__parent__._cast(
            _3434.SpringDamperSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_diff_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3437.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3437,
        )

        return self.__parent__._cast(
            _3437.StraightBevelDiffGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def straight_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3440.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3440,
        )

        return self.__parent__._cast(
            _3440.StraightBevelGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3447.SynchroniserSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3447,
        )

        return self.__parent__._cast(
            _3447.SynchroniserSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def torque_converter_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3450.TorqueConverterSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3450,
        )

        return self.__parent__._cast(
            _3450.TorqueConverterSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def worm_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3455.WormGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3455,
        )

        return self.__parent__._cast(
            _3455.WormGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3458.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3458,
        )

        return self.__parent__._cast(
            _3458.ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
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
class SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft(
    _3328.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
):
    """SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _SPECIALISED_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    )

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
        """Cast to another type.

        Returns:
            _Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
        """
        return _Cast_SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft(self)
