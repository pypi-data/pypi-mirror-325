"""CylindricalPlanetGearCompoundAdvancedSystemDeflection"""

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
    _7396,
)

_CYLINDRICAL_PLANET_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CylindricalPlanetGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7266,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7374,
        _7407,
        _7428,
        _7430,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )

    Self = TypeVar(
        "Self", bound="CylindricalPlanetGearCompoundAdvancedSystemDeflection"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="CylindricalPlanetGearCompoundAdvancedSystemDeflection._Cast_CylindricalPlanetGearCompoundAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CylindricalPlanetGearCompoundAdvancedSystemDeflection:
    """Special nested class for casting CylindricalPlanetGearCompoundAdvancedSystemDeflection to subclasses."""

    __parent__: "CylindricalPlanetGearCompoundAdvancedSystemDeflection"

    @property
    def cylindrical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7396.CylindricalGearCompoundAdvancedSystemDeflection":
        return self.__parent__._cast(
            _7396.CylindricalGearCompoundAdvancedSystemDeflection
        )

    @property
    def gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7407.GearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7407,
        )

        return self.__parent__._cast(_7407.GearCompoundAdvancedSystemDeflection)

    @property
    def mountable_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7428.MountableComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7428,
        )

        return self.__parent__._cast(
            _7428.MountableComponentCompoundAdvancedSystemDeflection
        )

    @property
    def component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7374.ComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7374,
        )

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
    def cylindrical_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "CylindricalPlanetGearCompoundAdvancedSystemDeflection":
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
class CylindricalPlanetGearCompoundAdvancedSystemDeflection(
    _7396.CylindricalGearCompoundAdvancedSystemDeflection
):
    """CylindricalPlanetGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _CYLINDRICAL_PLANET_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_7266.CylindricalPlanetGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalPlanetGearAdvancedSystemDeflection]

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
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_7266.CylindricalPlanetGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalPlanetGearAdvancedSystemDeflection]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_CylindricalPlanetGearCompoundAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_CylindricalPlanetGearCompoundAdvancedSystemDeflection
        """
        return _Cast_CylindricalPlanetGearCompoundAdvancedSystemDeflection(self)
