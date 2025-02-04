"""CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6159,
)

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6138,
        _6170,
        _6236,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal import _2401

    Self = TypeVar(
        "Self",
        bound="CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation._Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation:
    """Special nested class for casting CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

    __parent__: (
        "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation"
    )

    @property
    def coaxial_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6159.CoaxialConnectionHarmonicAnalysisOfSingleExcitation":
        return self.__parent__._cast(
            _6159.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6236.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6236,
        )

        return self.__parent__._cast(
            _6236.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def abstract_shaft_to_mountable_component_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6138.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6138,
        )

        return self.__parent__._cast(
            _6138.AbstractShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6170.ConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6170,
        )

        return self.__parent__._cast(_6170.ConnectionHarmonicAnalysisOfSingleExcitation)

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
    def cycloidal_disc_central_bearing_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation":
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
class CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation(
    _6159.CoaxialConnectionHarmonicAnalysisOfSingleExcitation
):
    """CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
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
    ) -> "_2401.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

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
    ) -> (
        "_Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation"
    ):
        """Cast to another type.

        Returns:
            _Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation
        """
        return _Cast_CycloidalDiscCentralBearingConnectionHarmonicAnalysisOfSingleExcitation(
            self
        )
