"""CouplingConnectionCompoundAdvancedSystemDeflection"""

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
    _7414,
)

_COUPLING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CouplingConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7253,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7371,
        _7376,
        _7384,
        _7432,
        _7454,
        _7469,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7700,
        _7704,
    )

    Self = TypeVar("Self", bound="CouplingConnectionCompoundAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingConnectionCompoundAdvancedSystemDeflection._Cast_CouplingConnectionCompoundAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCompoundAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingConnectionCompoundAdvancedSystemDeflection:
    """Special nested class for casting CouplingConnectionCompoundAdvancedSystemDeflection to subclasses."""

    __parent__: "CouplingConnectionCompoundAdvancedSystemDeflection"

    @property
    def inter_mountable_component_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7414.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
        return self.__parent__._cast(
            _7414.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7384.ConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7384,
        )

        return self.__parent__._cast(_7384.ConnectionCompoundAdvancedSystemDeflection)

    @property
    def connection_compound_analysis(
        self: "CastSelf",
    ) -> "_7700.ConnectionCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7700,
        )

        return self.__parent__._cast(_7700.ConnectionCompoundAnalysis)

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
    def clutch_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7371.ClutchConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7371,
        )

        return self.__parent__._cast(
            _7371.ClutchConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def concept_coupling_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7376.ConceptCouplingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7376,
        )

        return self.__parent__._cast(
            _7376.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7432.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7432,
        )

        return self.__parent__._cast(
            _7432.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def spring_damper_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7454.SpringDamperConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7454,
        )

        return self.__parent__._cast(
            _7454.SpringDamperConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7469.TorqueConverterConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7469,
        )

        return self.__parent__._cast(
            _7469.TorqueConverterConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def coupling_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "CouplingConnectionCompoundAdvancedSystemDeflection":
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
class CouplingConnectionCompoundAdvancedSystemDeflection(
    _7414.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
):
    """CouplingConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_7253.CouplingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_7253.CouplingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_CouplingConnectionCompoundAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_CouplingConnectionCompoundAdvancedSystemDeflection
        """
        return _Cast_CouplingConnectionCompoundAdvancedSystemDeflection(self)
