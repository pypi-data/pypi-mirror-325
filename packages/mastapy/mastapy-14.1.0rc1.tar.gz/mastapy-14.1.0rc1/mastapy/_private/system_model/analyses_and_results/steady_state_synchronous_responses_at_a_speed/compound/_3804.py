"""PartCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7707

_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "PartCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7704
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3672,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3723,
        _3724,
        _3725,
        _3727,
        _3729,
        _3730,
        _3731,
        _3733,
        _3734,
        _3736,
        _3737,
        _3738,
        _3739,
        _3741,
        _3742,
        _3743,
        _3744,
        _3746,
        _3748,
        _3749,
        _3751,
        _3752,
        _3754,
        _3755,
        _3757,
        _3759,
        _3760,
        _3762,
        _3764,
        _3765,
        _3766,
        _3768,
        _3770,
        _3772,
        _3773,
        _3774,
        _3775,
        _3776,
        _3778,
        _3779,
        _3780,
        _3781,
        _3783,
        _3784,
        _3785,
        _3787,
        _3789,
        _3791,
        _3792,
        _3794,
        _3795,
        _3797,
        _3798,
        _3799,
        _3800,
        _3801,
        _3802,
        _3803,
        _3805,
        _3807,
        _3809,
        _3810,
        _3811,
        _3812,
        _3813,
        _3814,
        _3816,
        _3817,
        _3819,
        _3820,
        _3821,
        _3823,
        _3824,
        _3826,
        _3827,
        _3829,
        _3830,
        _3832,
        _3833,
        _3835,
        _3836,
        _3837,
        _3838,
        _3839,
        _3840,
        _3841,
        _3842,
        _3844,
        _3845,
        _3846,
        _3847,
        _3848,
        _3850,
        _3851,
        _3853,
    )

    Self = TypeVar("Self", bound="PartCompoundSteadyStateSynchronousResponseAtASpeed")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PartCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartCompoundSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartCompoundSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting PartCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: "PartCompoundSteadyStateSynchronousResponseAtASpeed"

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7707.PartCompoundAnalysis":
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
    def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3723.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3723,
        )

        return self.__parent__._cast(
            _3723.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def abstract_shaft_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3724.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3724,
        )

        return self.__parent__._cast(
            _3724.AbstractShaftCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def abstract_shaft_or_housing_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3725.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3725,
        )

        return self.__parent__._cast(
            _3725.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3727.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3727,
        )

        return self.__parent__._cast(
            _3727.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_3729.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3729,
        )

        return self.__parent__._cast(
            _3729.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3730.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3730,
        )

        return self.__parent__._cast(
            _3730.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bearing_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3731.BearingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3731,
        )

        return self.__parent__._cast(
            _3731.BearingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def belt_drive_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3733.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3733,
        )

        return self.__parent__._cast(
            _3733.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3734.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3734,
        )

        return self.__parent__._cast(
            _3734.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3736.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3736,
        )

        return self.__parent__._cast(
            _3736.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3737.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3737,
        )

        return self.__parent__._cast(
            _3737.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3738.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3738,
        )

        return self.__parent__._cast(
            _3738.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3739.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3739,
        )

        return self.__parent__._cast(
            _3739.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3741.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3741,
        )

        return self.__parent__._cast(
            _3741.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bolt_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3742.BoltCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3742,
        )

        return self.__parent__._cast(
            _3742.BoltCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def bolted_joint_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3743.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3743,
        )

        return self.__parent__._cast(
            _3743.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def clutch_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3744.ClutchCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3744,
        )

        return self.__parent__._cast(
            _3744.ClutchCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3746.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3746,
        )

        return self.__parent__._cast(
            _3746.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3748.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3748,
        )

        return self.__parent__._cast(
            _3748.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3749.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3749,
        )

        return self.__parent__._cast(
            _3749.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3751.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3751,
        )

        return self.__parent__._cast(
            _3751.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3752.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3752,
        )

        return self.__parent__._cast(
            _3752.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3754.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3754,
        )

        return self.__parent__._cast(
            _3754.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3755.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3755,
        )

        return self.__parent__._cast(
            _3755.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3757.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3757,
        )

        return self.__parent__._cast(
            _3757.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def connector_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3759.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3759,
        )

        return self.__parent__._cast(
            _3759.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def coupling_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3760.CouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3760,
        )

        return self.__parent__._cast(
            _3760.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3762.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3762,
        )

        return self.__parent__._cast(
            _3762.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cvt_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3764.CVTCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3764,
        )

        return self.__parent__._cast(
            _3764.CVTCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3765.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3765,
        )

        return self.__parent__._cast(
            _3765.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3766.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3766,
        )

        return self.__parent__._cast(
            _3766.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cycloidal_disc_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3768.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3768,
        )

        return self.__parent__._cast(
            _3768.CycloidalDiscCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3770.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3770,
        )

        return self.__parent__._cast(
            _3770.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3772.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3772,
        )

        return self.__parent__._cast(
            _3772.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3773.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3773,
        )

        return self.__parent__._cast(
            _3773.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def datum_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3774.DatumCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3774,
        )

        return self.__parent__._cast(
            _3774.DatumCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def external_cad_model_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3775.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3775,
        )

        return self.__parent__._cast(
            _3775.ExternalCADModelCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def face_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3776.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3776,
        )

        return self.__parent__._cast(
            _3776.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3778.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3778,
        )

        return self.__parent__._cast(
            _3778.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def fe_part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3779.FEPartCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3779,
        )

        return self.__parent__._cast(
            _3779.FEPartCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def flexible_pin_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3780.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3780,
        )

        return self.__parent__._cast(
            _3780.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3781.GearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3781,
        )

        return self.__parent__._cast(
            _3781.GearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3783.GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3783,
        )

        return self.__parent__._cast(
            _3783.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def guide_dxf_model_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3784.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3784,
        )

        return self.__parent__._cast(
            _3784.GuideDxfModelCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3785.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3785,
        )

        return self.__parent__._cast(
            _3785.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3787.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3787,
        )

        return self.__parent__._cast(
            _3787.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3789.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3789,
        )

        return self.__parent__._cast(
            _3789.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3791.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3791,
        )

        return self.__parent__._cast(
            _3791.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3792.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3792,
        )

        return self.__parent__._cast(
            _3792.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3794.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3794,
        )

        return self.__parent__._cast(
            _3794.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3795.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3795,
        )

        return self.__parent__._cast(
            _3795.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3797.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3797,
        )

        return self.__parent__._cast(
            _3797.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def mass_disc_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3798.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3798,
        )

        return self.__parent__._cast(
            _3798.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def measurement_component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3799.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3799,
        )

        return self.__parent__._cast(
            _3799.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def microphone_array_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3800.MicrophoneArrayCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3800,
        )

        return self.__parent__._cast(
            _3800.MicrophoneArrayCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def microphone_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3801.MicrophoneCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3801,
        )

        return self.__parent__._cast(
            _3801.MicrophoneCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3802.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3802,
        )

        return self.__parent__._cast(
            _3802.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3803.OilSealCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3803,
        )

        return self.__parent__._cast(
            _3803.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3805.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3805,
        )

        return self.__parent__._cast(
            _3805.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3807.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3807,
        )

        return self.__parent__._cast(
            _3807.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3809.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3809,
        )

        return self.__parent__._cast(
            _3809.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3810.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3810,
        )

        return self.__parent__._cast(
            _3810.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def point_load_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3811.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3811,
        )

        return self.__parent__._cast(
            _3811.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def power_load_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3812.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3812,
        )

        return self.__parent__._cast(
            _3812.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def pulley_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3813.PulleyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3813,
        )

        return self.__parent__._cast(
            _3813.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def ring_pins_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3814.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3814,
        )

        return self.__parent__._cast(
            _3814.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3816.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3816,
        )

        return self.__parent__._cast(
            _3816.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3817.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3817,
        )

        return self.__parent__._cast(
            _3817.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def root_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3819.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3819,
        )

        return self.__parent__._cast(
            _3819.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3820.ShaftCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3820,
        )

        return self.__parent__._cast(
            _3820.ShaftCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3821.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3821,
        )

        return self.__parent__._cast(
            _3821.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3823.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3823,
        )

        return self.__parent__._cast(
            _3823.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3824.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3824,
        )

        return self.__parent__._cast(
            _3824.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3826.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3826,
        )

        return self.__parent__._cast(
            _3826.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spring_damper_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3827.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3827,
        )

        return self.__parent__._cast(
            _3827.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3829.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3829,
        )

        return self.__parent__._cast(
            _3829.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3830.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3830,
        )

        return self.__parent__._cast(
            _3830.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3832.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3832,
        )

        return self.__parent__._cast(
            _3832.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3833.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3833,
        )

        return self.__parent__._cast(
            _3833.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3835.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3835,
        )

        return self.__parent__._cast(
            _3835.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3836.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3836,
        )

        return self.__parent__._cast(
            _3836.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3837.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3837,
        )

        return self.__parent__._cast(
            _3837.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3838.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3838,
        )

        return self.__parent__._cast(
            _3838.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3839.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3839,
        )

        return self.__parent__._cast(
            _3839.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3840.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3840,
        )

        return self.__parent__._cast(
            _3840.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3841.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3841,
        )

        return self.__parent__._cast(
            _3841.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3842.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3842,
        )

        return self.__parent__._cast(
            _3842.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3844.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3844,
        )

        return self.__parent__._cast(
            _3844.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3845.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3845,
        )

        return self.__parent__._cast(
            _3845.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3846.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3846,
        )

        return self.__parent__._cast(
            _3846.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3847.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3847,
        )

        return self.__parent__._cast(
            _3847.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def worm_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3848.WormGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3848,
        )

        return self.__parent__._cast(
            _3848.WormGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3850.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3850,
        )

        return self.__parent__._cast(
            _3850.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3851.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3851,
        )

        return self.__parent__._cast(
            _3851.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3853.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3853,
        )

        return self.__parent__._cast(
            _3853.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
        )

    @property
    def part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "PartCompoundSteadyStateSynchronousResponseAtASpeed":
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
class PartCompoundSteadyStateSynchronousResponseAtASpeed(_7707.PartCompoundAnalysis):
    """PartCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_3672.PartSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PartSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_3672.PartSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PartSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_PartCompoundSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_PartCompoundSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_PartCompoundSteadyStateSynchronousResponseAtASpeed(self)
