"""AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5530

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7703,
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
        _5519,
        _5539,
        _5541,
        _5589,
        _5605,
    )
    from mastapy._private.system_model.connections_and_sockets import _2331

    Self = TypeVar(
        "Self",
        bound="AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis:
    """Special nested class for casting AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"

    @property
    def connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5530.ConnectionMultibodyDynamicsAnalysis":
        return self.__parent__._cast(_5530.ConnectionMultibodyDynamicsAnalysis)

    @property
    def connection_time_series_load_analysis_case(
        self: "CastSelf",
    ) -> "_7703.ConnectionTimeSeriesLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7703,
        )

        return self.__parent__._cast(_7703.ConnectionTimeSeriesLoadAnalysisCase)

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
    def coaxial_connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5519.CoaxialConnectionMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5519,
        )

        return self.__parent__._cast(_5519.CoaxialConnectionMultibodyDynamicsAnalysis)

    @property
    def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5539.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5539,
        )

        return self.__parent__._cast(
            _5539.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5541.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5541,
        )

        return self.__parent__._cast(
            _5541.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
        )

    @property
    def planetary_connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5589.PlanetaryConnectionMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5589,
        )

        return self.__parent__._cast(_5589.PlanetaryConnectionMultibodyDynamicsAnalysis)

    @property
    def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5605.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses import (
            _5605,
        )

        return self.__parent__._cast(
            _5605.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
        )

    @property
    def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
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
class AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis(
    _5530.ConnectionMultibodyDynamicsAnalysis
):
    """AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(
        self: "Self",
    ) -> "_2331.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
        """
        return (
            _Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis(
                self
            )
        )
