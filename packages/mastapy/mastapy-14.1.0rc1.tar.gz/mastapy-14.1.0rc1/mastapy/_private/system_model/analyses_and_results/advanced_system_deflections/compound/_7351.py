"""AbstractShaftOrHousingCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7374,
)

_ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7213,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7350,
        _7394,
        _7405,
        _7430,
        _7446,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )

    Self = TypeVar(
        "Self", bound="AbstractShaftOrHousingCompoundAdvancedSystemDeflection"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftOrHousingCompoundAdvancedSystemDeflection._Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingCompoundAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection:
    """Special nested class for casting AbstractShaftOrHousingCompoundAdvancedSystemDeflection to subclasses."""

    __parent__: "AbstractShaftOrHousingCompoundAdvancedSystemDeflection"

    @property
    def component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7374.ComponentCompoundAdvancedSystemDeflection":
        return self.__parent__._cast(_7374.ComponentCompoundAdvancedSystemDeflection)

    @property
    def part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7430.PartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7430,
        )

        return self.__parent__._cast(_7430.PartCompoundAdvancedSystemDeflection)

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
    def abstract_shaft_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7350.AbstractShaftCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7350,
        )

        return self.__parent__._cast(
            _7350.AbstractShaftCompoundAdvancedSystemDeflection
        )

    @property
    def cycloidal_disc_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7394.CycloidalDiscCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7394,
        )

        return self.__parent__._cast(
            _7394.CycloidalDiscCompoundAdvancedSystemDeflection
        )

    @property
    def fe_part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7405.FEPartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7405,
        )

        return self.__parent__._cast(_7405.FEPartCompoundAdvancedSystemDeflection)

    @property
    def shaft_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7446.ShaftCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7446,
        )

        return self.__parent__._cast(_7446.ShaftCompoundAdvancedSystemDeflection)

    @property
    def abstract_shaft_or_housing_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
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
class AbstractShaftOrHousingCompoundAdvancedSystemDeflection(
    _7374.ComponentCompoundAdvancedSystemDeflection
):
    """AbstractShaftOrHousingCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _ABSTRACT_SHAFT_OR_HOUSING_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_7213.AbstractShaftOrHousingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AbstractShaftOrHousingAdvancedSystemDeflection]

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
    ) -> "List[_7213.AbstractShaftOrHousingAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AbstractShaftOrHousingAdvancedSystemDeflection]

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
    ) -> "_Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection
        """
        return _Cast_AbstractShaftOrHousingCompoundAdvancedSystemDeflection(self)
