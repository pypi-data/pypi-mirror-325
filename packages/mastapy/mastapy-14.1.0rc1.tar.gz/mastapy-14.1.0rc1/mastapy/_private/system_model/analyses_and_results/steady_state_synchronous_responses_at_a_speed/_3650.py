"""GearSetSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3691,
)

_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "GearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3591,
        _3596,
        _3603,
        _3608,
        _3621,
        _3624,
        _3639,
        _3645,
        _3649,
        _3651,
        _3654,
        _3658,
        _3661,
        _3664,
        _3672,
        _3677,
        _3693,
        _3700,
        _3703,
        _3718,
        _3721,
    )
    from mastapy._private.system_model.part_model.gears import _2604

    Self = TypeVar("Self", bound="GearSetSteadyStateSynchronousResponseAtASpeed")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearSetSteadyStateSynchronousResponseAtASpeed._Cast_GearSetSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearSetSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearSetSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting GearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: "GearSetSteadyStateSynchronousResponseAtASpeed"

    @property
    def specialised_assembly_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3691.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
        return self.__parent__._cast(
            _3691.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
        )

    @property
    def abstract_assembly_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3591.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3591,
        )

        return self.__parent__._cast(
            _3591.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3672.PartSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3672,
        )

        return self.__parent__._cast(_3672.PartSteadyStateSynchronousResponseAtASpeed)

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
    def agma_gleason_conical_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3596.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3596,
        )

        return self.__parent__._cast(
            _3596.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3603.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3603,
        )

        return self.__parent__._cast(
            _3603.BevelDifferentialGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3608.BevelGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3608,
        )

        return self.__parent__._cast(
            _3608.BevelGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3621.ConceptGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3621,
        )

        return self.__parent__._cast(
            _3621.ConceptGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def conical_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3624.ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3624,
        )

        return self.__parent__._cast(
            _3624.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3639.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3639,
        )

        return self.__parent__._cast(
            _3639.CylindricalGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def face_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3645.FaceGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3645,
        )

        return self.__parent__._cast(
            _3645.FaceGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3654.HypoidGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3654,
        )

        return self.__parent__._cast(
            _3654.HypoidGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3658.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3658,
        )

        return self.__parent__._cast(
            _3658.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3661.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3661,
        )

        return self.__parent__._cast(
            _3661.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3664.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3664,
        )

        return self.__parent__._cast(
            _3664.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def planetary_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3677.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3677,
        )

        return self.__parent__._cast(
            _3677.PlanetaryGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spiral_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3693.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3693,
        )

        return self.__parent__._cast(
            _3693.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_diff_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3700.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3700,
        )

        return self.__parent__._cast(
            _3700.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3703.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3703,
        )

        return self.__parent__._cast(
            _3703.StraightBevelGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def worm_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3718.WormGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3718,
        )

        return self.__parent__._cast(
            _3718.WormGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def zerol_bevel_gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3721.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3721,
        )

        return self.__parent__._cast(
            _3721.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "GearSetSteadyStateSynchronousResponseAtASpeed":
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
class GearSetSteadyStateSynchronousResponseAtASpeed(
    _3691.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
):
    """GearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2604.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_steady_state_synchronous_response_at_a_speed(
        self: "Self",
    ) -> "List[_3651.GearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.GearSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "GearsSteadyStateSynchronousResponseAtASpeed"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_steady_state_synchronous_response_at_a_speed(
        self: "Self",
    ) -> "List[_3649.GearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.GearMeshSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "MeshesSteadyStateSynchronousResponseAtASpeed"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_GearSetSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_GearSetSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_GearSetSteadyStateSynchronousResponseAtASpeed(self)
