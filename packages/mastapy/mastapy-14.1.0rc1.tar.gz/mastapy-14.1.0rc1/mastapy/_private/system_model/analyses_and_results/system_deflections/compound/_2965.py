"""CouplingCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
    _3030,
)

_COUPLING_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CouplingCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2806,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2928,
        _2949,
        _2954,
        _3010,
        _3011,
        _3034,
        _3049,
    )

    Self = TypeVar("Self", bound="CouplingCompoundSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingCompoundSystemDeflection._Cast_CouplingCompoundSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingCompoundSystemDeflection:
    """Special nested class for casting CouplingCompoundSystemDeflection to subclasses."""

    __parent__: "CouplingCompoundSystemDeflection"

    @property
    def specialised_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3030.SpecialisedAssemblyCompoundSystemDeflection":
        return self.__parent__._cast(_3030.SpecialisedAssemblyCompoundSystemDeflection)

    @property
    def abstract_assembly_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2928.AbstractAssemblyCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2928,
        )

        return self.__parent__._cast(_2928.AbstractAssemblyCompoundSystemDeflection)

    @property
    def part_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3010.PartCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3010,
        )

        return self.__parent__._cast(_3010.PartCompoundSystemDeflection)

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
    def clutch_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2949.ClutchCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2949,
        )

        return self.__parent__._cast(_2949.ClutchCompoundSystemDeflection)

    @property
    def concept_coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2954.ConceptCouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2954,
        )

        return self.__parent__._cast(_2954.ConceptCouplingCompoundSystemDeflection)

    @property
    def part_to_part_shear_coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3011.PartToPartShearCouplingCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3011,
        )

        return self.__parent__._cast(
            _3011.PartToPartShearCouplingCompoundSystemDeflection
        )

    @property
    def spring_damper_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3034.SpringDamperCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3034,
        )

        return self.__parent__._cast(_3034.SpringDamperCompoundSystemDeflection)

    @property
    def torque_converter_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3049.TorqueConverterCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3049,
        )

        return self.__parent__._cast(_3049.TorqueConverterCompoundSystemDeflection)

    @property
    def coupling_compound_system_deflection(
        self: "CastSelf",
    ) -> "CouplingCompoundSystemDeflection":
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
class CouplingCompoundSystemDeflection(
    _3030.SpecialisedAssemblyCompoundSystemDeflection
):
    """CouplingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_COMPOUND_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_analysis_cases(self: "Self") -> "List[_2806.CouplingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_2806.CouplingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_CouplingCompoundSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_CouplingCompoundSystemDeflection
        """
        return _Cast_CouplingCompoundSystemDeflection(self)
