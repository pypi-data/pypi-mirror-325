"""ConicalGearMeshCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
    _6740,
)

_CONICAL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConicalGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6683,
        _6690,
        _6695,
        _6713,
        _6744,
        _6746,
        _6748,
        _6751,
        _6754,
        _6783,
        _6789,
        _6792,
        _6810,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import _2373

    Self = TypeVar("Self", bound="ConicalGearMeshCriticalSpeedAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearMeshCriticalSpeedAnalysis._Cast_ConicalGearMeshCriticalSpeedAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearMeshCriticalSpeedAnalysis:
    """Special nested class for casting ConicalGearMeshCriticalSpeedAnalysis to subclasses."""

    __parent__: "ConicalGearMeshCriticalSpeedAnalysis"

    @property
    def gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6740.GearMeshCriticalSpeedAnalysis":
        return self.__parent__._cast(_6740.GearMeshCriticalSpeedAnalysis)

    @property
    def inter_mountable_component_connection_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6746.InterMountableComponentConnectionCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6746,
        )

        return self.__parent__._cast(
            _6746.InterMountableComponentConnectionCriticalSpeedAnalysis
        )

    @property
    def connection_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6713.ConnectionCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6713,
        )

        return self.__parent__._cast(_6713.ConnectionCriticalSpeedAnalysis)

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
    def agma_gleason_conical_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6683.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6683,
        )

        return self.__parent__._cast(
            _6683.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
        )

    @property
    def bevel_differential_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6690.BevelDifferentialGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6690,
        )

        return self.__parent__._cast(
            _6690.BevelDifferentialGearMeshCriticalSpeedAnalysis
        )

    @property
    def bevel_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6695.BevelGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6695,
        )

        return self.__parent__._cast(_6695.BevelGearMeshCriticalSpeedAnalysis)

    @property
    def hypoid_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6744.HypoidGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6744,
        )

        return self.__parent__._cast(_6744.HypoidGearMeshCriticalSpeedAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6748.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6748,
        )

        return self.__parent__._cast(
            _6748.KlingelnbergCycloPalloidConicalGearMeshCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6751.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6751,
        )

        return self.__parent__._cast(
            _6751.KlingelnbergCycloPalloidHypoidGearMeshCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6754.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6754,
        )

        return self.__parent__._cast(
            _6754.KlingelnbergCycloPalloidSpiralBevelGearMeshCriticalSpeedAnalysis
        )

    @property
    def spiral_bevel_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6783.SpiralBevelGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6783,
        )

        return self.__parent__._cast(_6783.SpiralBevelGearMeshCriticalSpeedAnalysis)

    @property
    def straight_bevel_diff_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6789.StraightBevelDiffGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6789,
        )

        return self.__parent__._cast(
            _6789.StraightBevelDiffGearMeshCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6792.StraightBevelGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6792,
        )

        return self.__parent__._cast(_6792.StraightBevelGearMeshCriticalSpeedAnalysis)

    @property
    def zerol_bevel_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6810.ZerolBevelGearMeshCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6810,
        )

        return self.__parent__._cast(_6810.ZerolBevelGearMeshCriticalSpeedAnalysis)

    @property
    def conical_gear_mesh_critical_speed_analysis(
        self: "CastSelf",
    ) -> "ConicalGearMeshCriticalSpeedAnalysis":
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
class ConicalGearMeshCriticalSpeedAnalysis(_6740.GearMeshCriticalSpeedAnalysis):
    """ConicalGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2373.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: "Self") -> "List[ConicalGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.ConicalGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Planetaries")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalGearMeshCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearMeshCriticalSpeedAnalysis
        """
        return _Cast_ConicalGearMeshCriticalSpeedAnalysis(self)
