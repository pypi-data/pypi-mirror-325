"""CouplingHalfCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
    _6620,
)

_COUPLING_HALF_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "CouplingHalfCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
        _6447,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6564,
        _6566,
        _6569,
        _6583,
        _6622,
        _6625,
        _6631,
        _6635,
        _6647,
        _6657,
        _6658,
        _6659,
        _6662,
        _6663,
    )

    Self = TypeVar("Self", bound="CouplingHalfCompoundDynamicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingHalfCompoundDynamicAnalysis._Cast_CouplingHalfCompoundDynamicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundDynamicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalfCompoundDynamicAnalysis:
    """Special nested class for casting CouplingHalfCompoundDynamicAnalysis to subclasses."""

    __parent__: "CouplingHalfCompoundDynamicAnalysis"

    @property
    def mountable_component_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6620.MountableComponentCompoundDynamicAnalysis":
        return self.__parent__._cast(_6620.MountableComponentCompoundDynamicAnalysis)

    @property
    def component_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6566.ComponentCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6566,
        )

        return self.__parent__._cast(_6566.ComponentCompoundDynamicAnalysis)

    @property
    def part_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6622.PartCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6622,
        )

        return self.__parent__._cast(_6622.PartCompoundDynamicAnalysis)

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
    def clutch_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6564.ClutchHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6564,
        )

        return self.__parent__._cast(_6564.ClutchHalfCompoundDynamicAnalysis)

    @property
    def concept_coupling_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6569.ConceptCouplingHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6569,
        )

        return self.__parent__._cast(_6569.ConceptCouplingHalfCompoundDynamicAnalysis)

    @property
    def cvt_pulley_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6583.CVTPulleyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6583,
        )

        return self.__parent__._cast(_6583.CVTPulleyCompoundDynamicAnalysis)

    @property
    def part_to_part_shear_coupling_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6625.PartToPartShearCouplingHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6625,
        )

        return self.__parent__._cast(
            _6625.PartToPartShearCouplingHalfCompoundDynamicAnalysis
        )

    @property
    def pulley_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6631.PulleyCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6631,
        )

        return self.__parent__._cast(_6631.PulleyCompoundDynamicAnalysis)

    @property
    def rolling_ring_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6635.RollingRingCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6635,
        )

        return self.__parent__._cast(_6635.RollingRingCompoundDynamicAnalysis)

    @property
    def spring_damper_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6647.SpringDamperHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6647,
        )

        return self.__parent__._cast(_6647.SpringDamperHalfCompoundDynamicAnalysis)

    @property
    def synchroniser_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6657.SynchroniserHalfCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6657,
        )

        return self.__parent__._cast(_6657.SynchroniserHalfCompoundDynamicAnalysis)

    @property
    def synchroniser_part_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6658.SynchroniserPartCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6658,
        )

        return self.__parent__._cast(_6658.SynchroniserPartCompoundDynamicAnalysis)

    @property
    def synchroniser_sleeve_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6659.SynchroniserSleeveCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6659,
        )

        return self.__parent__._cast(_6659.SynchroniserSleeveCompoundDynamicAnalysis)

    @property
    def torque_converter_pump_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6662.TorqueConverterPumpCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6662,
        )

        return self.__parent__._cast(_6662.TorqueConverterPumpCompoundDynamicAnalysis)

    @property
    def torque_converter_turbine_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6663.TorqueConverterTurbineCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6663,
        )

        return self.__parent__._cast(
            _6663.TorqueConverterTurbineCompoundDynamicAnalysis
        )

    @property
    def coupling_half_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "CouplingHalfCompoundDynamicAnalysis":
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
class CouplingHalfCompoundDynamicAnalysis(
    _6620.MountableComponentCompoundDynamicAnalysis
):
    """CouplingHalfCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_HALF_COMPOUND_DYNAMIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_6447.CouplingHalfDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingHalfDynamicAnalysis]

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
    ) -> "List[_6447.CouplingHalfDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CouplingHalfDynamicAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_CouplingHalfCompoundDynamicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalfCompoundDynamicAnalysis
        """
        return _Cast_CouplingHalfCompoundDynamicAnalysis(self)
