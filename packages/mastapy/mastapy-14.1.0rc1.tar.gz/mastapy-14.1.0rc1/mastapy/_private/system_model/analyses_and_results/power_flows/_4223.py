"""RingPinsPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.power_flows import _4209

_RING_PINS_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "RingPinsPowerFlow"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import (
        _4152,
        _4211,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads import _7633
    from mastapy._private.system_model.part_model.cycloidal import _2642

    Self = TypeVar("Self", bound="RingPinsPowerFlow")
    CastSelf = TypeVar("CastSelf", bound="RingPinsPowerFlow._Cast_RingPinsPowerFlow")


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_RingPinsPowerFlow:
    """Special nested class for casting RingPinsPowerFlow to subclasses."""

    __parent__: "RingPinsPowerFlow"

    @property
    def mountable_component_power_flow(
        self: "CastSelf",
    ) -> "_4209.MountableComponentPowerFlow":
        return self.__parent__._cast(_4209.MountableComponentPowerFlow)

    @property
    def component_power_flow(self: "CastSelf") -> "_4152.ComponentPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4152

        return self.__parent__._cast(_4152.ComponentPowerFlow)

    @property
    def part_power_flow(self: "CastSelf") -> "_4211.PartPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4211

        return self.__parent__._cast(_4211.PartPowerFlow)

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
    def ring_pins_power_flow(self: "CastSelf") -> "RingPinsPowerFlow":
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
class RingPinsPowerFlow(_4209.MountableComponentPowerFlow):
    """RingPinsPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _RING_PINS_POWER_FLOW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2642.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: "Self") -> "_7633.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentLoadCase")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_RingPinsPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_RingPinsPowerFlow
        """
        return _Cast_RingPinsPowerFlow(self)
