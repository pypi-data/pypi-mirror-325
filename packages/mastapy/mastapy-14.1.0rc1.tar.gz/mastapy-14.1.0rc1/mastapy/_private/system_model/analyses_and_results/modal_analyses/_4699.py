"""CoaxialConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.modal_analyses import _4786

_COAXIAL_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CoaxialConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses import (
        _4678,
        _4710,
        _4720,
    )
    from mastapy._private.system_model.analyses_and_results.static_loads import _7524
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2789,
    )
    from mastapy._private.system_model.connections_and_sockets import _2335

    Self = TypeVar("Self", bound="CoaxialConnectionModalAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="CoaxialConnectionModalAnalysis._Cast_CoaxialConnectionModalAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionModalAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CoaxialConnectionModalAnalysis:
    """Special nested class for casting CoaxialConnectionModalAnalysis to subclasses."""

    __parent__: "CoaxialConnectionModalAnalysis"

    @property
    def shaft_to_mountable_component_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4786.ShaftToMountableComponentConnectionModalAnalysis":
        return self.__parent__._cast(
            _4786.ShaftToMountableComponentConnectionModalAnalysis
        )

    @property
    def abstract_shaft_to_mountable_component_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4678.AbstractShaftToMountableComponentConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4678,
        )

        return self.__parent__._cast(
            _4678.AbstractShaftToMountableComponentConnectionModalAnalysis
        )

    @property
    def connection_modal_analysis(self: "CastSelf") -> "_4710.ConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4710,
        )

        return self.__parent__._cast(_4710.ConnectionModalAnalysis)

    @property
    def connection_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7702.ConnectionStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7702,
        )

        return self.__parent__._cast(_7702.ConnectionStaticLoadAnalysisCase)

    @property
    def connection_analysis_case(self: "CastSelf") -> "_7699.ConnectionAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7699,
        )

        return self.__parent__._cast(_7699.ConnectionAnalysisCase)

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
    def cycloidal_disc_central_bearing_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4720.CycloidalDiscCentralBearingConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4720,
        )

        return self.__parent__._cast(
            _4720.CycloidalDiscCentralBearingConnectionModalAnalysis
        )

    @property
    def coaxial_connection_modal_analysis(
        self: "CastSelf",
    ) -> "CoaxialConnectionModalAnalysis":
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
class CoaxialConnectionModalAnalysis(
    _4786.ShaftToMountableComponentConnectionModalAnalysis
):
    """CoaxialConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COAXIAL_CONNECTION_MODAL_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2335.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: "Self") -> "_7524.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionLoadCase")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: "Self",
    ) -> "_2789.CoaxialConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SystemDeflectionResults")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_CoaxialConnectionModalAnalysis":
        """Cast to another type.

        Returns:
            _Cast_CoaxialConnectionModalAnalysis
        """
        return _Cast_CoaxialConnectionModalAnalysis(self)
