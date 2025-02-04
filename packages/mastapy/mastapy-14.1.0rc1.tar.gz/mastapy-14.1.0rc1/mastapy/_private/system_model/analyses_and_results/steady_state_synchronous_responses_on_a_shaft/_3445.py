"""SynchroniserPartSteadyStateSynchronousResponseOnAShaft"""

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
    _3366,
)

_SYNCHRONISER_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3353,
        _3407,
        _3409,
        _3444,
        _3446,
    )
    from mastapy._private.system_model.part_model.couplings import _2685

    Self = TypeVar(
        "Self", bound="SynchroniserPartSteadyStateSynchronousResponseOnAShaft"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="SynchroniserPartSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft",
    )


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartSteadyStateSynchronousResponseOnAShaft",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft:
    """Special nested class for casting SynchroniserPartSteadyStateSynchronousResponseOnAShaft to subclasses."""

    __parent__: "SynchroniserPartSteadyStateSynchronousResponseOnAShaft"

    @property
    def coupling_half_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3366.CouplingHalfSteadyStateSynchronousResponseOnAShaft":
        return self.__parent__._cast(
            _3366.CouplingHalfSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def mountable_component_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3407.MountableComponentSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3407,
        )

        return self.__parent__._cast(
            _3407.MountableComponentSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def component_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3353.ComponentSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3353,
        )

        return self.__parent__._cast(
            _3353.ComponentSteadyStateSynchronousResponseOnAShaft
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
    def synchroniser_half_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3444.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3444,
        )

        return self.__parent__._cast(
            _3444.SynchroniserHalfSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "_3446.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
            _3446,
        )

        return self.__parent__._cast(
            _3446.SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft
        )

    @property
    def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
        self: "CastSelf",
    ) -> "SynchroniserPartSteadyStateSynchronousResponseOnAShaft":
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
class SynchroniserPartSteadyStateSynchronousResponseOnAShaft(
    _3366.CouplingHalfSteadyStateSynchronousResponseOnAShaft
):
    """SynchroniserPartSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _SYNCHRONISER_PART_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2685.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft":
        """Cast to another type.

        Returns:
            _Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft
        """
        return _Cast_SynchroniserPartSteadyStateSynchronousResponseOnAShaft(self)
