"""AbstractShaftOrHousingModalAnalysisAtAStiffness"""

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
    _4989,
)

_ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "AbstractShaftOrHousingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4965,
        _5009,
        _5021,
        _5047,
        _5064,
    )
    from mastapy._private.system_model.part_model import _2503

    Self = TypeVar("Self", bound="AbstractShaftOrHousingModalAnalysisAtAStiffness")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingModalAnalysisAtAStiffness",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness:
    """Special nested class for casting AbstractShaftOrHousingModalAnalysisAtAStiffness to subclasses."""

    __parent__: "AbstractShaftOrHousingModalAnalysisAtAStiffness"

    @property
    def component_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4989.ComponentModalAnalysisAtAStiffness":
        return self.__parent__._cast(_4989.ComponentModalAnalysisAtAStiffness)

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
    def abstract_shaft_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4965.AbstractShaftModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4965,
        )

        return self.__parent__._cast(_4965.AbstractShaftModalAnalysisAtAStiffness)

    @property
    def cycloidal_disc_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5009.CycloidalDiscModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5009,
        )

        return self.__parent__._cast(_5009.CycloidalDiscModalAnalysisAtAStiffness)

    @property
    def fe_part_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5021.FEPartModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5021,
        )

        return self.__parent__._cast(_5021.FEPartModalAnalysisAtAStiffness)

    @property
    def shaft_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5064.ShaftModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5064,
        )

        return self.__parent__._cast(_5064.ShaftModalAnalysisAtAStiffness)

    @property
    def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "AbstractShaftOrHousingModalAnalysisAtAStiffness":
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
class AbstractShaftOrHousingModalAnalysisAtAStiffness(
    _4989.ComponentModalAnalysisAtAStiffness
):
    """AbstractShaftOrHousingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS_AT_A_STIFFNESS

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
    ) -> "_Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness
        """
        return _Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness(self)
