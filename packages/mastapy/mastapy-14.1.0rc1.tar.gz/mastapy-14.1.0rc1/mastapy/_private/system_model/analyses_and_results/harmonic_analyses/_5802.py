"""AbstractShaftHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.harmonic_analyses import _5803

_ABSTRACT_SHAFT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AbstractShaftHarmonicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5827,
        _5847,
        _5913,
        _5931,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2762,
    )
    from mastapy._private.system_model.part_model import _2502

    Self = TypeVar("Self", bound="AbstractShaftHarmonicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftHarmonicAnalysis._Cast_AbstractShaftHarmonicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftHarmonicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftHarmonicAnalysis:
    """Special nested class for casting AbstractShaftHarmonicAnalysis to subclasses."""

    __parent__: "AbstractShaftHarmonicAnalysis"

    @property
    def abstract_shaft_or_housing_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5803.AbstractShaftOrHousingHarmonicAnalysis":
        return self.__parent__._cast(_5803.AbstractShaftOrHousingHarmonicAnalysis)

    @property
    def component_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5827.ComponentHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5827,
        )

        return self.__parent__._cast(_5827.ComponentHarmonicAnalysis)

    @property
    def part_harmonic_analysis(self: "CastSelf") -> "_5913.PartHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5913,
        )

        return self.__parent__._cast(_5913.PartHarmonicAnalysis)

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
    def cycloidal_disc_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5847.CycloidalDiscHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5847,
        )

        return self.__parent__._cast(_5847.CycloidalDiscHarmonicAnalysis)

    @property
    def shaft_harmonic_analysis(self: "CastSelf") -> "_5931.ShaftHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5931,
        )

        return self.__parent__._cast(_5931.ShaftHarmonicAnalysis)

    @property
    def abstract_shaft_harmonic_analysis(
        self: "CastSelf",
    ) -> "AbstractShaftHarmonicAnalysis":
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
class AbstractShaftHarmonicAnalysis(_5803.AbstractShaftOrHousingHarmonicAnalysis):
    """AbstractShaftHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_SHAFT_HARMONIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2502.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: "Self",
    ) -> "_2762.AbstractShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SystemDeflectionResults")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractShaftHarmonicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftHarmonicAnalysis
        """
        return _Cast_AbstractShaftHarmonicAnalysis(self)
