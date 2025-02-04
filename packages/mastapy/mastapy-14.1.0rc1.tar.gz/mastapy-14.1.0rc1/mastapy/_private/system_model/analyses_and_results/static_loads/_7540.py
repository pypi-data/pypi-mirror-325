"""CouplingHalfLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.static_loads import _7614

_COUPLING_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingHalfLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7521,
        _7525,
        _7527,
        _7544,
        _7618,
        _7620,
        _7630,
        _7637,
        _7647,
        _7657,
        _7659,
        _7660,
        _7665,
        _7666,
    )
    from mastapy._private.system_model.part_model.couplings import _2658

    Self = TypeVar("Self", bound="CouplingHalfLoadCase")
    CastSelf = TypeVar(
        "CastSelf", bound="CouplingHalfLoadCase._Cast_CouplingHalfLoadCase"
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CouplingHalfLoadCase:
    """Special nested class for casting CouplingHalfLoadCase to subclasses."""

    __parent__: "CouplingHalfLoadCase"

    @property
    def mountable_component_load_case(
        self: "CastSelf",
    ) -> "_7614.MountableComponentLoadCase":
        return self.__parent__._cast(_7614.MountableComponentLoadCase)

    @property
    def component_load_case(self: "CastSelf") -> "_7525.ComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7525,
        )

        return self.__parent__._cast(_7525.ComponentLoadCase)

    @property
    def part_load_case(self: "CastSelf") -> "_7618.PartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7618,
        )

        return self.__parent__._cast(_7618.PartLoadCase)

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
    def clutch_half_load_case(self: "CastSelf") -> "_7521.ClutchHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7521,
        )

        return self.__parent__._cast(_7521.ClutchHalfLoadCase)

    @property
    def concept_coupling_half_load_case(
        self: "CastSelf",
    ) -> "_7527.ConceptCouplingHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7527,
        )

        return self.__parent__._cast(_7527.ConceptCouplingHalfLoadCase)

    @property
    def cvt_pulley_load_case(self: "CastSelf") -> "_7544.CVTPulleyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7544,
        )

        return self.__parent__._cast(_7544.CVTPulleyLoadCase)

    @property
    def part_to_part_shear_coupling_half_load_case(
        self: "CastSelf",
    ) -> "_7620.PartToPartShearCouplingHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7620,
        )

        return self.__parent__._cast(_7620.PartToPartShearCouplingHalfLoadCase)

    @property
    def pulley_load_case(self: "CastSelf") -> "_7630.PulleyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7630,
        )

        return self.__parent__._cast(_7630.PulleyLoadCase)

    @property
    def rolling_ring_load_case(self: "CastSelf") -> "_7637.RollingRingLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7637,
        )

        return self.__parent__._cast(_7637.RollingRingLoadCase)

    @property
    def spring_damper_half_load_case(
        self: "CastSelf",
    ) -> "_7647.SpringDamperHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7647,
        )

        return self.__parent__._cast(_7647.SpringDamperHalfLoadCase)

    @property
    def synchroniser_half_load_case(
        self: "CastSelf",
    ) -> "_7657.SynchroniserHalfLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7657,
        )

        return self.__parent__._cast(_7657.SynchroniserHalfLoadCase)

    @property
    def synchroniser_part_load_case(
        self: "CastSelf",
    ) -> "_7659.SynchroniserPartLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7659,
        )

        return self.__parent__._cast(_7659.SynchroniserPartLoadCase)

    @property
    def synchroniser_sleeve_load_case(
        self: "CastSelf",
    ) -> "_7660.SynchroniserSleeveLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7660,
        )

        return self.__parent__._cast(_7660.SynchroniserSleeveLoadCase)

    @property
    def torque_converter_pump_load_case(
        self: "CastSelf",
    ) -> "_7665.TorqueConverterPumpLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7665,
        )

        return self.__parent__._cast(_7665.TorqueConverterPumpLoadCase)

    @property
    def torque_converter_turbine_load_case(
        self: "CastSelf",
    ) -> "_7666.TorqueConverterTurbineLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7666,
        )

        return self.__parent__._cast(_7666.TorqueConverterTurbineLoadCase)

    @property
    def coupling_half_load_case(self: "CastSelf") -> "CouplingHalfLoadCase":
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
class CouplingHalfLoadCase(_7614.MountableComponentLoadCase):
    """CouplingHalfLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COUPLING_HALF_LOAD_CASE

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
    def cast_to(self: "Self") -> "_Cast_CouplingHalfLoadCase":
        """Cast to another type.

        Returns:
            _Cast_CouplingHalfLoadCase
        """
        return _Cast_CouplingHalfLoadCase(self)
