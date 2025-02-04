"""TorqueConverterConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.static_loads import _7539

_TORQUE_CONVERTER_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterConnectionLoadCase",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7537,
        _7599,
    )
    from mastapy._private.system_model.connections_and_sockets.couplings import _2418

    Self = TypeVar("Self", bound="TorqueConverterConnectionLoadCase")
    CastSelf = TypeVar(
        "CastSelf",
        bound="TorqueConverterConnectionLoadCase._Cast_TorqueConverterConnectionLoadCase",
    )


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_TorqueConverterConnectionLoadCase:
    """Special nested class for casting TorqueConverterConnectionLoadCase to subclasses."""

    __parent__: "TorqueConverterConnectionLoadCase"

    @property
    def coupling_connection_load_case(
        self: "CastSelf",
    ) -> "_7539.CouplingConnectionLoadCase":
        return self.__parent__._cast(_7539.CouplingConnectionLoadCase)

    @property
    def inter_mountable_component_connection_load_case(
        self: "CastSelf",
    ) -> "_7599.InterMountableComponentConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7599,
        )

        return self.__parent__._cast(_7599.InterMountableComponentConnectionLoadCase)

    @property
    def connection_load_case(self: "CastSelf") -> "_7537.ConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7537,
        )

        return self.__parent__._cast(_7537.ConnectionLoadCase)

    @property
    def connection_analysis(self: "CastSelf") -> "_2724.ConnectionAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2724

        return self.__parent__._cast(_2724.ConnectionAnalysis)

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
    def torque_converter_connection_load_case(
        self: "CastSelf",
    ) -> "TorqueConverterConnectionLoadCase":
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
class TorqueConverterConnectionLoadCase(_7539.CouplingConnectionLoadCase):
    """TorqueConverterConnectionLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _TORQUE_CONVERTER_CONNECTION_LOAD_CASE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2418.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_TorqueConverterConnectionLoadCase":
        """Cast to another type.

        Returns:
            _Cast_TorqueConverterConnectionLoadCase
        """
        return _Cast_TorqueConverterConnectionLoadCase(self)
