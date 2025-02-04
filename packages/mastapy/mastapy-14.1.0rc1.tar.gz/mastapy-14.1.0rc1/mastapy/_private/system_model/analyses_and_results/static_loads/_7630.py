"""PulleyLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.static_loads import _7540

_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PulleyLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7525,
        _7544,
        _7614,
        _7618,
    )
    from mastapy._private.system_model.part_model.couplings import _2665

    Self = TypeVar("Self", bound="PulleyLoadCase")
    CastSelf = TypeVar("CastSelf", bound="PulleyLoadCase._Cast_PulleyLoadCase")


__docformat__ = "restructuredtext en"
__all__ = ("PulleyLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PulleyLoadCase:
    """Special nested class for casting PulleyLoadCase to subclasses."""

    __parent__: "PulleyLoadCase"

    @property
    def coupling_half_load_case(self: "CastSelf") -> "_7540.CouplingHalfLoadCase":
        return self.__parent__._cast(_7540.CouplingHalfLoadCase)

    @property
    def mountable_component_load_case(
        self: "CastSelf",
    ) -> "_7614.MountableComponentLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7614,
        )

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
    def cvt_pulley_load_case(self: "CastSelf") -> "_7544.CVTPulleyLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7544,
        )

        return self.__parent__._cast(_7544.CVTPulleyLoadCase)

    @property
    def pulley_load_case(self: "CastSelf") -> "PulleyLoadCase":
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
class PulleyLoadCase(_7540.CouplingHalfLoadCase):
    """PulleyLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PULLEY_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2665.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_PulleyLoadCase":
        """Cast to another type.

        Returns:
            _Cast_PulleyLoadCase
        """
        return _Cast_PulleyLoadCase(self)
