"""AbstractShaftOrHousingSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3087,
)

_ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AbstractShaftOrHousingSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3064,
        _3108,
        _3119,
        _3144,
        _3161,
    )
    from mastapy._private.system_model.part_model import _2503

    Self = TypeVar("Self", bound="AbstractShaftOrHousingSteadyStateSynchronousResponse")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftOrHousingSteadyStateSynchronousResponse._Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingSteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse:
    """Special nested class for casting AbstractShaftOrHousingSteadyStateSynchronousResponse to subclasses."""

    __parent__: "AbstractShaftOrHousingSteadyStateSynchronousResponse"

    @property
    def component_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3087.ComponentSteadyStateSynchronousResponse":
        return self.__parent__._cast(_3087.ComponentSteadyStateSynchronousResponse)

    @property
    def part_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3144.PartSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3144,
        )

        return self.__parent__._cast(_3144.PartSteadyStateSynchronousResponse)

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
    def abstract_shaft_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3064.AbstractShaftSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3064,
        )

        return self.__parent__._cast(_3064.AbstractShaftSteadyStateSynchronousResponse)

    @property
    def cycloidal_disc_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3108.CycloidalDiscSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3108,
        )

        return self.__parent__._cast(_3108.CycloidalDiscSteadyStateSynchronousResponse)

    @property
    def fe_part_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3119.FEPartSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3119,
        )

        return self.__parent__._cast(_3119.FEPartSteadyStateSynchronousResponse)

    @property
    def shaft_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3161.ShaftSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3161,
        )

        return self.__parent__._cast(_3161.ShaftSteadyStateSynchronousResponse)

    @property
    def abstract_shaft_or_housing_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "AbstractShaftOrHousingSteadyStateSynchronousResponse":
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
class AbstractShaftOrHousingSteadyStateSynchronousResponse(
    _3087.ComponentSteadyStateSynchronousResponse
):
    """AbstractShaftOrHousingSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _ABSTRACT_SHAFT_OR_HOUSING_STEADY_STATE_SYNCHRONOUS_RESPONSE
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2503.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "_Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse
        """
        return _Cast_AbstractShaftOrHousingSteadyStateSynchronousResponse(self)
