"""CouplingHalfPowerFlow"""

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

_COUPLING_HALF_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "CouplingHalfPowerFlow"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import (
        _4149,
        _4152,
        _4154,
        _4169,
        _4211,
        _4213,
        _4222,
        _4227,
        _4237,
        _4247,
        _4248,
        _4250,
        _4254,
        _4255,
    )
    from mastapy._private.system_model.part_model.couplings import _2658

    Self = TypeVar("Self", bound="CouplingHalfPowerFlow")
    CastSelf = TypeVar(
        "CastSelf", bound="CouplingHalfPowerFlow._Cast_CouplingHalfPowerFlow"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalfPowerFlow:
    """Special nested class for casting CouplingHalfPowerFlow to subclasses."""

    __parent__: "CouplingHalfPowerFlow"

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
    def clutch_half_power_flow(self: "CastSelf") -> "_4149.ClutchHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4149

        return self.__parent__._cast(_4149.ClutchHalfPowerFlow)

    @property
    def concept_coupling_half_power_flow(
        self: "CastSelf",
    ) -> "_4154.ConceptCouplingHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4154

        return self.__parent__._cast(_4154.ConceptCouplingHalfPowerFlow)

    @property
    def cvt_pulley_power_flow(self: "CastSelf") -> "_4169.CVTPulleyPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4169

        return self.__parent__._cast(_4169.CVTPulleyPowerFlow)

    @property
    def part_to_part_shear_coupling_half_power_flow(
        self: "CastSelf",
    ) -> "_4213.PartToPartShearCouplingHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4213

        return self.__parent__._cast(_4213.PartToPartShearCouplingHalfPowerFlow)

    @property
    def pulley_power_flow(self: "CastSelf") -> "_4222.PulleyPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4222

        return self.__parent__._cast(_4222.PulleyPowerFlow)

    @property
    def rolling_ring_power_flow(self: "CastSelf") -> "_4227.RollingRingPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4227

        return self.__parent__._cast(_4227.RollingRingPowerFlow)

    @property
    def spring_damper_half_power_flow(
        self: "CastSelf",
    ) -> "_4237.SpringDamperHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4237

        return self.__parent__._cast(_4237.SpringDamperHalfPowerFlow)

    @property
    def synchroniser_half_power_flow(
        self: "CastSelf",
    ) -> "_4247.SynchroniserHalfPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4247

        return self.__parent__._cast(_4247.SynchroniserHalfPowerFlow)

    @property
    def synchroniser_part_power_flow(
        self: "CastSelf",
    ) -> "_4248.SynchroniserPartPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4248

        return self.__parent__._cast(_4248.SynchroniserPartPowerFlow)

    @property
    def synchroniser_sleeve_power_flow(
        self: "CastSelf",
    ) -> "_4250.SynchroniserSleevePowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4250

        return self.__parent__._cast(_4250.SynchroniserSleevePowerFlow)

    @property
    def torque_converter_pump_power_flow(
        self: "CastSelf",
    ) -> "_4254.TorqueConverterPumpPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4254

        return self.__parent__._cast(_4254.TorqueConverterPumpPowerFlow)

    @property
    def torque_converter_turbine_power_flow(
        self: "CastSelf",
    ) -> "_4255.TorqueConverterTurbinePowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4255

        return self.__parent__._cast(_4255.TorqueConverterTurbinePowerFlow)

    @property
    def coupling_half_power_flow(self: "CastSelf") -> "CouplingHalfPowerFlow":
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
class CouplingHalfPowerFlow(_4209.MountableComponentPowerFlow):
    """CouplingHalfPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_HALF_POWER_FLOW

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
    def cast_to(self: "Self") -> "_Cast_CouplingHalfPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalfPowerFlow
        """
        return _Cast_CouplingHalfPowerFlow(self)
