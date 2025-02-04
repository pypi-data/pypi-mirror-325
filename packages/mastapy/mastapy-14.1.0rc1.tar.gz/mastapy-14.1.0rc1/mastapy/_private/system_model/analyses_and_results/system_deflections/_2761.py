"""AbstractShaftOrHousingSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.system_deflections import _2790

_ABSTRACT_SHAFT_OR_HOUSING_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AbstractShaftOrHousingSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7708,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import _4128
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2762,
        _2813,
        _2832,
        _2862,
        _2881,
    )
    from mastapy._private.system_model.part_model import _2503

    Self = TypeVar("Self", bound="AbstractShaftOrHousingSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftOrHousingSystemDeflection:
    """Special nested class for casting AbstractShaftOrHousingSystemDeflection to subclasses."""

    __parent__: "AbstractShaftOrHousingSystemDeflection"

    @property
    def component_system_deflection(
        self: "CastSelf",
    ) -> "_2790.ComponentSystemDeflection":
        return self.__parent__._cast(_2790.ComponentSystemDeflection)

    @property
    def part_system_deflection(self: "CastSelf") -> "_2862.PartSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2862,
        )

        return self.__parent__._cast(_2862.PartSystemDeflection)

    @property
    def part_fe_analysis(self: "CastSelf") -> "_7708.PartFEAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7708,
        )

        return self.__parent__._cast(_7708.PartFEAnalysis)

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
    def abstract_shaft_system_deflection(
        self: "CastSelf",
    ) -> "_2762.AbstractShaftSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2762,
        )

        return self.__parent__._cast(_2762.AbstractShaftSystemDeflection)

    @property
    def cycloidal_disc_system_deflection(
        self: "CastSelf",
    ) -> "_2813.CycloidalDiscSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2813,
        )

        return self.__parent__._cast(_2813.CycloidalDiscSystemDeflection)

    @property
    def fe_part_system_deflection(self: "CastSelf") -> "_2832.FEPartSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2832,
        )

        return self.__parent__._cast(_2832.FEPartSystemDeflection)

    @property
    def shaft_system_deflection(self: "CastSelf") -> "_2881.ShaftSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2881,
        )

        return self.__parent__._cast(_2881.ShaftSystemDeflection)

    @property
    def abstract_shaft_or_housing_system_deflection(
        self: "CastSelf",
    ) -> "AbstractShaftOrHousingSystemDeflection":
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
class AbstractShaftOrHousingSystemDeflection(_2790.ComponentSystemDeflection):
    """AbstractShaftOrHousingSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_SHAFT_OR_HOUSING_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def mass_including_connected_components(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "MassIncludingConnectedComponents")

        if temp is None:
            return 0.0

        return temp

    @property
    def polar_inertia_including_connected_components(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "PolarInertiaIncludingConnectedComponents"
        )

        if temp is None:
            return 0.0

        return temp

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
    def power_flow_results(self: "Self") -> "_4128.AbstractShaftOrHousingPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AbstractShaftOrHousingPowerFlow

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "PowerFlowResults")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractShaftOrHousingSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftOrHousingSystemDeflection
        """
        return _Cast_AbstractShaftOrHousingSystemDeflection(self)
