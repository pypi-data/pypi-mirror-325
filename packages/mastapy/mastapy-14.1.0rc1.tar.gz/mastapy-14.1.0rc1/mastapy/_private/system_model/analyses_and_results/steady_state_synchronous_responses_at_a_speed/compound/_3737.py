"""BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3734,
)

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3605,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3727,
        _3739,
        _3748,
        _3755,
        _3781,
        _3802,
        _3804,
    )

    Self = TypeVar(
        "Self",
        bound="BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed:
    """Special nested class for casting BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

    __parent__: (
        "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
    )

    @property
    def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3734.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed":
        return self.__parent__._cast(
            _3734.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
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
    def part_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "_3804.PartCompoundSteadyStateSynchronousResponseAtASpeed":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
            _3804,
        )

        return self.__parent__._cast(
            _3804.PartCompoundSteadyStateSynchronousResponseAtASpeed
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
    def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
        self: "CastSelf",
    ) -> "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
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
class BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed(
    _3734.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
):
    """BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> (
        "List[_3605.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed]

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
    def component_analysis_cases(
        self: "Self",
    ) -> (
        "List[_3605.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
        """
        return _Cast_BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
