"""CouplingHalfHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.harmonic_analyses import _5911

_COUPLING_HALF_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CouplingHalfHarmonicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5823,
        _5827,
        _5829,
        _5844,
        _5913,
        _5915,
        _5923,
        _5929,
        _5941,
        _5952,
        _5954,
        _5955,
        _5958,
        _5959,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2805,
    )
    from mastapy._private.system_model.part_model.couplings import _2658

    Self = TypeVar("Self", bound="CouplingHalfHarmonicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfHarmonicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalfHarmonicAnalysis:
    """Special nested class for casting CouplingHalfHarmonicAnalysis to subclasses."""

    __parent__: "CouplingHalfHarmonicAnalysis"

    @property
    def mountable_component_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5911.MountableComponentHarmonicAnalysis":
        return self.__parent__._cast(_5911.MountableComponentHarmonicAnalysis)

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
    def clutch_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5823.ClutchHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5823,
        )

        return self.__parent__._cast(_5823.ClutchHalfHarmonicAnalysis)

    @property
    def concept_coupling_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5829.ConceptCouplingHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5829,
        )

        return self.__parent__._cast(_5829.ConceptCouplingHalfHarmonicAnalysis)

    @property
    def cvt_pulley_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5844.CVTPulleyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5844,
        )

        return self.__parent__._cast(_5844.CVTPulleyHarmonicAnalysis)

    @property
    def part_to_part_shear_coupling_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5915.PartToPartShearCouplingHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5915,
        )

        return self.__parent__._cast(_5915.PartToPartShearCouplingHalfHarmonicAnalysis)

    @property
    def pulley_harmonic_analysis(self: "CastSelf") -> "_5923.PulleyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5923,
        )

        return self.__parent__._cast(_5923.PulleyHarmonicAnalysis)

    @property
    def rolling_ring_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5929.RollingRingHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5929,
        )

        return self.__parent__._cast(_5929.RollingRingHarmonicAnalysis)

    @property
    def spring_damper_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5941.SpringDamperHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5941,
        )

        return self.__parent__._cast(_5941.SpringDamperHalfHarmonicAnalysis)

    @property
    def synchroniser_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5952.SynchroniserHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5952,
        )

        return self.__parent__._cast(_5952.SynchroniserHalfHarmonicAnalysis)

    @property
    def synchroniser_part_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5954.SynchroniserPartHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5954,
        )

        return self.__parent__._cast(_5954.SynchroniserPartHarmonicAnalysis)

    @property
    def synchroniser_sleeve_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5955.SynchroniserSleeveHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5955,
        )

        return self.__parent__._cast(_5955.SynchroniserSleeveHarmonicAnalysis)

    @property
    def torque_converter_pump_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5958.TorqueConverterPumpHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5958,
        )

        return self.__parent__._cast(_5958.TorqueConverterPumpHarmonicAnalysis)

    @property
    def torque_converter_turbine_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5959.TorqueConverterTurbineHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5959,
        )

        return self.__parent__._cast(_5959.TorqueConverterTurbineHarmonicAnalysis)

    @property
    def coupling_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "CouplingHalfHarmonicAnalysis":
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
class CouplingHalfHarmonicAnalysis(_5911.MountableComponentHarmonicAnalysis):
    """CouplingHalfHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_HALF_HARMONIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2658.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: "Self") -> "_2805.CouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SystemDeflectionResults")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_CouplingHalfHarmonicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalfHarmonicAnalysis
        """
        return _Cast_CouplingHalfHarmonicAnalysis(self)
