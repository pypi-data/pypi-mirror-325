"""AbstractShaftCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3199,
)

_ABSTRACT_SHAFT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AbstractShaftCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3064,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3222,
        _3242,
        _3278,
        _3294,
    )

    Self = TypeVar("Self", bound="AbstractShaftCompoundSteadyStateSynchronousResponse")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftCompoundSteadyStateSynchronousResponse._Cast_AbstractShaftCompoundSteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundSteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftCompoundSteadyStateSynchronousResponse:
    """Special nested class for casting AbstractShaftCompoundSteadyStateSynchronousResponse to subclasses."""

    __parent__: "AbstractShaftCompoundSteadyStateSynchronousResponse"

    @property
    def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3199.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse":
        return self.__parent__._cast(
            _3199.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
        )

    @property
    def component_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3222.ComponentCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3222,
        )

        return self.__parent__._cast(
            _3222.ComponentCompoundSteadyStateSynchronousResponse
        )

    @property
    def part_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3278.PartCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3278,
        )

        return self.__parent__._cast(_3278.PartCompoundSteadyStateSynchronousResponse)

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
    def cycloidal_disc_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3242.CycloidalDiscCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3242,
        )

        return self.__parent__._cast(
            _3242.CycloidalDiscCompoundSteadyStateSynchronousResponse
        )

    @property
    def shaft_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3294.ShaftCompoundSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
            _3294,
        )

        return self.__parent__._cast(_3294.ShaftCompoundSteadyStateSynchronousResponse)

    @property
    def abstract_shaft_compound_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "AbstractShaftCompoundSteadyStateSynchronousResponse":
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
class AbstractShaftCompoundSteadyStateSynchronousResponse(
    _3199.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
):
    """AbstractShaftCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_SHAFT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_3064.AbstractShaftSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractShaftSteadyStateSynchronousResponse]

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
    ) -> "List[_3064.AbstractShaftSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractShaftSteadyStateSynchronousResponse]

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
    ) -> "_Cast_AbstractShaftCompoundSteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftCompoundSteadyStateSynchronousResponse
        """
        return _Cast_AbstractShaftCompoundSteadyStateSynchronousResponse(self)
