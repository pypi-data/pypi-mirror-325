"""CouplingHalfAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
    _7296,
)

_COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CouplingHalfAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7237,
        _7239,
        _7242,
        _7257,
        _7298,
        _7301,
        _7307,
        _7310,
        _7323,
        _7333,
        _7334,
        _7335,
        _7338,
        _7339,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.part_model.couplings import _2658

    Self = TypeVar("Self", bound="CouplingHalfAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CouplingHalfAdvancedSystemDeflection._Cast_CouplingHalfAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalfAdvancedSystemDeflection:
    """Special nested class for casting CouplingHalfAdvancedSystemDeflection to subclasses."""

    __parent__: "CouplingHalfAdvancedSystemDeflection"

    @property
    def mountable_component_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7296.MountableComponentAdvancedSystemDeflection":
        return self.__parent__._cast(_7296.MountableComponentAdvancedSystemDeflection)

    @property
    def component_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7239.ComponentAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7239,
        )

        return self.__parent__._cast(_7239.ComponentAdvancedSystemDeflection)

    @property
    def part_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7298.PartAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7298,
        )

        return self.__parent__._cast(_7298.PartAdvancedSystemDeflection)

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
    def clutch_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7237.ClutchHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7237,
        )

        return self.__parent__._cast(_7237.ClutchHalfAdvancedSystemDeflection)

    @property
    def concept_coupling_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7242.ConceptCouplingHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7242,
        )

        return self.__parent__._cast(_7242.ConceptCouplingHalfAdvancedSystemDeflection)

    @property
    def cvt_pulley_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7257.CVTPulleyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7257,
        )

        return self.__parent__._cast(_7257.CVTPulleyAdvancedSystemDeflection)

    @property
    def part_to_part_shear_coupling_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7301.PartToPartShearCouplingHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7301,
        )

        return self.__parent__._cast(
            _7301.PartToPartShearCouplingHalfAdvancedSystemDeflection
        )

    @property
    def pulley_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7307.PulleyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7307,
        )

        return self.__parent__._cast(_7307.PulleyAdvancedSystemDeflection)

    @property
    def rolling_ring_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7310.RollingRingAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7310,
        )

        return self.__parent__._cast(_7310.RollingRingAdvancedSystemDeflection)

    @property
    def spring_damper_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7323.SpringDamperHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7323,
        )

        return self.__parent__._cast(_7323.SpringDamperHalfAdvancedSystemDeflection)

    @property
    def synchroniser_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7333.SynchroniserHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7333,
        )

        return self.__parent__._cast(_7333.SynchroniserHalfAdvancedSystemDeflection)

    @property
    def synchroniser_part_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7334.SynchroniserPartAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7334,
        )

        return self.__parent__._cast(_7334.SynchroniserPartAdvancedSystemDeflection)

    @property
    def synchroniser_sleeve_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7335.SynchroniserSleeveAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7335,
        )

        return self.__parent__._cast(_7335.SynchroniserSleeveAdvancedSystemDeflection)

    @property
    def torque_converter_pump_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7338.TorqueConverterPumpAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7338,
        )

        return self.__parent__._cast(_7338.TorqueConverterPumpAdvancedSystemDeflection)

    @property
    def torque_converter_turbine_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7339.TorqueConverterTurbineAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7339,
        )

        return self.__parent__._cast(
            _7339.TorqueConverterTurbineAdvancedSystemDeflection
        )

    @property
    def coupling_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "CouplingHalfAdvancedSystemDeflection":
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
class CouplingHalfAdvancedSystemDeflection(
    _7296.MountableComponentAdvancedSystemDeflection
):
    """CouplingHalfAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION

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
    def cast_to(self: "Self") -> "_Cast_CouplingHalfAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalfAdvancedSystemDeflection
        """
        return _Cast_CouplingHalfAdvancedSystemDeflection(self)
