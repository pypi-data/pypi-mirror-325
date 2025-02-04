"""PartSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7709

_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "PartSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7706
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3591,
        _3592,
        _3593,
        _3596,
        _3597,
        _3598,
        _3599,
        _3601,
        _3603,
        _3604,
        _3605,
        _3606,
        _3608,
        _3609,
        _3610,
        _3611,
        _3613,
        _3614,
        _3616,
        _3618,
        _3619,
        _3621,
        _3622,
        _3624,
        _3625,
        _3627,
        _3629,
        _3630,
        _3632,
        _3633,
        _3634,
        _3637,
        _3639,
        _3640,
        _3641,
        _3642,
        _3643,
        _3645,
        _3646,
        _3647,
        _3648,
        _3650,
        _3651,
        _3652,
        _3654,
        _3655,
        _3658,
        _3659,
        _3661,
        _3662,
        _3664,
        _3665,
        _3666,
        _3667,
        _3668,
        _3669,
        _3670,
        _3671,
        _3674,
        _3675,
        _3677,
        _3678,
        _3679,
        _3680,
        _3681,
        _3682,
        _3684,
        _3686,
        _3687,
        _3688,
        _3689,
        _3691,
        _3693,
        _3694,
        _3696,
        _3697,
        _3698,
        _3700,
        _3701,
        _3703,
        _3704,
        _3705,
        _3706,
        _3707,
        _3708,
        _3709,
        _3710,
        _3712,
        _3713,
        _3714,
        _3715,
        _3716,
        _3718,
        _3719,
        _3721,
        _3722,
    )
    from mastapy._private.system_model.part_model import _2537

    Self = TypeVar("Self", bound="PartSteadyStateSynchronousResponseAtASpeed")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PartSteadyStateSynchronousResponseAtASpeed._Cast_PartSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting PartSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: "PartSteadyStateSynchronousResponseAtASpeed"

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7709.PartStaticLoadAnalysisCase":
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
    def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3592.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3592,
        )

        return self.__parent__._cast(
            _3592.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def abstract_shaft_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3593.AbstractShaftSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3593,
        )

        return self.__parent__._cast(
            _3593.AbstractShaftSteadyStateSynchronousResponseAtASpeed
        )

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
    def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3597.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3597,
        )

        return self.__parent__._cast(
            _3597.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def assembly_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3598.AssemblySteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3598,
        )

        return self.__parent__._cast(
            _3598.AssemblySteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bearing_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3599.BearingSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3599,
        )

        return self.__parent__._cast(
            _3599.BearingSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def belt_drive_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3601.BeltDriveSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3601,
        )

        return self.__parent__._cast(
            _3601.BeltDriveSteadyStateSynchronousResponseAtASpeed
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
    def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3604.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3604,
        )

        return self.__parent__._cast(
            _3604.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3605.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3605,
        )

        return self.__parent__._cast(
            _3605.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3606.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3606,
        )

        return self.__parent__._cast(
            _3606.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
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
    def bevel_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3609.BevelGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3609,
        )

        return self.__parent__._cast(
            _3609.BevelGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bolted_joint_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3610.BoltedJointSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3610,
        )

        return self.__parent__._cast(
            _3610.BoltedJointSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bolt_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3611.BoltSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3611,
        )

        return self.__parent__._cast(_3611.BoltSteadyStateSynchronousResponseAtASpeed)

    @property
    def clutch_half_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3613.ClutchHalfSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3613,
        )

        return self.__parent__._cast(
            _3613.ClutchHalfSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def clutch_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3614.ClutchSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3614,
        )

        return self.__parent__._cast(_3614.ClutchSteadyStateSynchronousResponseAtASpeed)

    @property
    def component_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3616.ComponentSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3616,
        )

        return self.__parent__._cast(
            _3616.ComponentSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3618.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3618,
        )

        return self.__parent__._cast(
            _3618.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_coupling_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3619.ConceptCouplingSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3619,
        )

        return self.__parent__._cast(
            _3619.ConceptCouplingSteadyStateSynchronousResponseAtASpeed
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
    def concept_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3622.ConceptGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3622,
        )

        return self.__parent__._cast(
            _3622.ConceptGearSteadyStateSynchronousResponseAtASpeed
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
    def conical_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3625.ConicalGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3625,
        )

        return self.__parent__._cast(
            _3625.ConicalGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def connector_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3627.ConnectorSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3627,
        )

        return self.__parent__._cast(
            _3627.ConnectorSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def coupling_half_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3629.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3629,
        )

        return self.__parent__._cast(
            _3629.CouplingHalfSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def coupling_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3630.CouplingSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3630,
        )

        return self.__parent__._cast(
            _3630.CouplingSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cvt_pulley_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3632.CVTPulleySteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3632,
        )

        return self.__parent__._cast(
            _3632.CVTPulleySteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cvt_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3633.CVTSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3633,
        )

        return self.__parent__._cast(_3633.CVTSteadyStateSynchronousResponseAtASpeed)

    @property
    def cycloidal_assembly_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3634.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3634,
        )

        return self.__parent__._cast(
            _3634.CycloidalAssemblySteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3637.CycloidalDiscSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3637,
        )

        return self.__parent__._cast(
            _3637.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
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
    def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3640.CylindricalGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3640,
        )

        return self.__parent__._cast(
            _3640.CylindricalGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3641.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3641,
        )

        return self.__parent__._cast(
            _3641.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def datum_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3642.DatumSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3642,
        )

        return self.__parent__._cast(_3642.DatumSteadyStateSynchronousResponseAtASpeed)

    @property
    def external_cad_model_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3643.ExternalCADModelSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3643,
        )

        return self.__parent__._cast(
            _3643.ExternalCADModelSteadyStateSynchronousResponseAtASpeed
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
    def face_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3646.FaceGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3646,
        )

        return self.__parent__._cast(
            _3646.FaceGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def fe_part_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3647.FEPartSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3647,
        )

        return self.__parent__._cast(_3647.FEPartSteadyStateSynchronousResponseAtASpeed)

    @property
    def flexible_pin_assembly_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3648.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3648,
        )

        return self.__parent__._cast(
            _3648.FlexiblePinAssemblySteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_set_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3650.GearSetSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3650,
        )

        return self.__parent__._cast(
            _3650.GearSetSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3651.GearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3651,
        )

        return self.__parent__._cast(_3651.GearSteadyStateSynchronousResponseAtASpeed)

    @property
    def guide_dxf_model_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3652.GuideDxfModelSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3652,
        )

        return self.__parent__._cast(
            _3652.GuideDxfModelSteadyStateSynchronousResponseAtASpeed
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
    def hypoid_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3655.HypoidGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3655,
        )

        return self.__parent__._cast(
            _3655.HypoidGearSteadyStateSynchronousResponseAtASpeed
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
    def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3659.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3659,
        )

        return self.__parent__._cast(
            _3659.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
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
    def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3662.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3662,
        )

        return self.__parent__._cast(
            _3662.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
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
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3665.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3665,
        )

        return self.__parent__._cast(
            _3665.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def mass_disc_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3666.MassDiscSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3666,
        )

        return self.__parent__._cast(
            _3666.MassDiscSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def measurement_component_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3667.MeasurementComponentSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3667,
        )

        return self.__parent__._cast(
            _3667.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def microphone_array_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3668.MicrophoneArraySteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3668,
        )

        return self.__parent__._cast(
            _3668.MicrophoneArraySteadyStateSynchronousResponseAtASpeed
        )

    @property
    def microphone_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3669.MicrophoneSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3669,
        )

        return self.__parent__._cast(
            _3669.MicrophoneSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def mountable_component_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3670.MountableComponentSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3670,
        )

        return self.__parent__._cast(
            _3670.MountableComponentSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def oil_seal_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3671.OilSealSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3671,
        )

        return self.__parent__._cast(
            _3671.OilSealSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3674.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3674,
        )

        return self.__parent__._cast(
            _3674.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_to_part_shear_coupling_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3675.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3675,
        )

        return self.__parent__._cast(
            _3675.PartToPartShearCouplingSteadyStateSynchronousResponseAtASpeed
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
    def planet_carrier_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3678.PlanetCarrierSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3678,
        )

        return self.__parent__._cast(
            _3678.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def point_load_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3679.PointLoadSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3679,
        )

        return self.__parent__._cast(
            _3679.PointLoadSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def power_load_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3680.PowerLoadSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3680,
        )

        return self.__parent__._cast(
            _3680.PowerLoadSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def pulley_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3681.PulleySteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3681,
        )

        return self.__parent__._cast(_3681.PulleySteadyStateSynchronousResponseAtASpeed)

    @property
    def ring_pins_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3682.RingPinsSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3682,
        )

        return self.__parent__._cast(
            _3682.RingPinsSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def rolling_ring_assembly_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3684.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3684,
        )

        return self.__parent__._cast(
            _3684.RollingRingAssemblySteadyStateSynchronousResponseAtASpeed
        )

    @property
    def rolling_ring_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3686.RollingRingSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3686,
        )

        return self.__parent__._cast(
            _3686.RollingRingSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def root_assembly_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3687.RootAssemblySteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3687,
        )

        return self.__parent__._cast(
            _3687.RootAssemblySteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3688.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3688,
        )

        return self.__parent__._cast(
            _3688.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3689.ShaftSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3689,
        )

        return self.__parent__._cast(_3689.ShaftSteadyStateSynchronousResponseAtASpeed)

    @property
    def specialised_assembly_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3691.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3691,
        )

        return self.__parent__._cast(
            _3691.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
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
    def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3694.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3694,
        )

        return self.__parent__._cast(
            _3694.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spring_damper_half_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3696.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3696,
        )

        return self.__parent__._cast(
            _3696.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spring_damper_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3697.SpringDamperSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3697,
        )

        return self.__parent__._cast(
            _3697.SpringDamperSteadyStateSynchronousResponseAtASpeed
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
    def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3701.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3701,
        )

        return self.__parent__._cast(
            _3701.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
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
    def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3704.StraightBevelGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3704,
        )

        return self.__parent__._cast(
            _3704.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3705.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3705,
        )

        return self.__parent__._cast(
            _3705.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3706.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3706,
        )

        return self.__parent__._cast(
            _3706.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_half_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3707.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3707,
        )

        return self.__parent__._cast(
            _3707.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_part_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3708.SynchroniserPartSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3708,
        )

        return self.__parent__._cast(
            _3708.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3709.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3709,
        )

        return self.__parent__._cast(
            _3709.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3710.SynchroniserSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3710,
        )

        return self.__parent__._cast(
            _3710.SynchroniserSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3712.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3712,
        )

        return self.__parent__._cast(
            _3712.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3713.TorqueConverterSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3713,
        )

        return self.__parent__._cast(
            _3713.TorqueConverterSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3714.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3714,
        )

        return self.__parent__._cast(
            _3714.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3715.UnbalancedMassSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3715,
        )

        return self.__parent__._cast(
            _3715.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def virtual_component_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3716.VirtualComponentSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3716,
        )

        return self.__parent__._cast(
            _3716.VirtualComponentSteadyStateSynchronousResponseAtASpeed
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
    def worm_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3719.WormGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3719,
        )

        return self.__parent__._cast(
            _3719.WormGearSteadyStateSynchronousResponseAtASpeed
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
    def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3722.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
            _3722,
        )

        return self.__parent__._cast(
            _3722.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "PartSteadyStateSynchronousResponseAtASpeed":
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
class PartSteadyStateSynchronousResponseAtASpeed(_7709.PartStaticLoadAnalysisCase):
    """PartSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2537.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def steady_state_synchronous_response_at_a_speed(
        self: "Self",
    ) -> "_3698.SteadyStateSynchronousResponseAtASpeed":
        """mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.SteadyStateSynchronousResponseAtASpeed

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "SteadyStateSynchronousResponseAtASpeed"
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_PartSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_PartSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_PartSteadyStateSynchronousResponseAtASpeed(self)
