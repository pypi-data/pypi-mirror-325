"""ConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7702

_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7699
    from mastapy._private.system_model.analyses_and_results.stability_analyses import (
        _3857,
        _3858,
        _3863,
        _3865,
        _3870,
        _3875,
        _3878,
        _3880,
        _3883,
        _3886,
        _3891,
        _3895,
        _3899,
        _3900,
        _3902,
        _3909,
        _3914,
        _3918,
        _3921,
        _3922,
        _3925,
        _3928,
        _3938,
        _3941,
        _3948,
        _3950,
        _3955,
        _3957,
        _3960,
        _3963,
        _3966,
        _3969,
        _3978,
        _3984,
        _3987,
    )
    from mastapy._private.system_model.connections_and_sockets import _2338

    Self = TypeVar("Self", bound="ConnectionStabilityAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionStabilityAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConnectionStabilityAnalysis:
    """Special nested class for casting ConnectionStabilityAnalysis to subclasses."""

    __parent__: "ConnectionStabilityAnalysis"

    @property
    def connection_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7702.ConnectionStaticLoadAnalysisCase":
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
    def abstract_shaft_to_mountable_component_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3857.AbstractShaftToMountableComponentConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3857,
        )

        return self.__parent__._cast(
            _3857.AbstractShaftToMountableComponentConnectionStabilityAnalysis
        )

    @property
    def agma_gleason_conical_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3858.AGMAGleasonConicalGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3858,
        )

        return self.__parent__._cast(_3858.AGMAGleasonConicalGearMeshStabilityAnalysis)

    @property
    def belt_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3863.BeltConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3863,
        )

        return self.__parent__._cast(_3863.BeltConnectionStabilityAnalysis)

    @property
    def bevel_differential_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3865.BevelDifferentialGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3865,
        )

        return self.__parent__._cast(_3865.BevelDifferentialGearMeshStabilityAnalysis)

    @property
    def bevel_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3870.BevelGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3870,
        )

        return self.__parent__._cast(_3870.BevelGearMeshStabilityAnalysis)

    @property
    def clutch_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3875.ClutchConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3875,
        )

        return self.__parent__._cast(_3875.ClutchConnectionStabilityAnalysis)

    @property
    def coaxial_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3878.CoaxialConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3878,
        )

        return self.__parent__._cast(_3878.CoaxialConnectionStabilityAnalysis)

    @property
    def concept_coupling_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3880.ConceptCouplingConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3880,
        )

        return self.__parent__._cast(_3880.ConceptCouplingConnectionStabilityAnalysis)

    @property
    def concept_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3883.ConceptGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3883,
        )

        return self.__parent__._cast(_3883.ConceptGearMeshStabilityAnalysis)

    @property
    def conical_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3886.ConicalGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3886,
        )

        return self.__parent__._cast(_3886.ConicalGearMeshStabilityAnalysis)

    @property
    def coupling_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3891.CouplingConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3891,
        )

        return self.__parent__._cast(_3891.CouplingConnectionStabilityAnalysis)

    @property
    def cvt_belt_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3895.CVTBeltConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3895,
        )

        return self.__parent__._cast(_3895.CVTBeltConnectionStabilityAnalysis)

    @property
    def cycloidal_disc_central_bearing_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3899.CycloidalDiscCentralBearingConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3899,
        )

        return self.__parent__._cast(
            _3899.CycloidalDiscCentralBearingConnectionStabilityAnalysis
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3900.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3900,
        )

        return self.__parent__._cast(
            _3900.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
        )

    @property
    def cylindrical_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3902.CylindricalGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3902,
        )

        return self.__parent__._cast(_3902.CylindricalGearMeshStabilityAnalysis)

    @property
    def face_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3909.FaceGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3909,
        )

        return self.__parent__._cast(_3909.FaceGearMeshStabilityAnalysis)

    @property
    def gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3914.GearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3914,
        )

        return self.__parent__._cast(_3914.GearMeshStabilityAnalysis)

    @property
    def hypoid_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3918.HypoidGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3918,
        )

        return self.__parent__._cast(_3918.HypoidGearMeshStabilityAnalysis)

    @property
    def inter_mountable_component_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3921.InterMountableComponentConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3921,
        )

        return self.__parent__._cast(
            _3921.InterMountableComponentConnectionStabilityAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3922.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3922,
        )

        return self.__parent__._cast(
            _3922.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3925.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3925,
        )

        return self.__parent__._cast(
            _3925.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3928.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3928,
        )

        return self.__parent__._cast(
            _3928.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
        )

    @property
    def part_to_part_shear_coupling_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3938.PartToPartShearCouplingConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3938,
        )

        return self.__parent__._cast(
            _3938.PartToPartShearCouplingConnectionStabilityAnalysis
        )

    @property
    def planetary_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3941.PlanetaryConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3941,
        )

        return self.__parent__._cast(_3941.PlanetaryConnectionStabilityAnalysis)

    @property
    def ring_pins_to_disc_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3948.RingPinsToDiscConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3948,
        )

        return self.__parent__._cast(_3948.RingPinsToDiscConnectionStabilityAnalysis)

    @property
    def rolling_ring_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3950.RollingRingConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3950,
        )

        return self.__parent__._cast(_3950.RollingRingConnectionStabilityAnalysis)

    @property
    def shaft_to_mountable_component_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3955.ShaftToMountableComponentConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3955,
        )

        return self.__parent__._cast(
            _3955.ShaftToMountableComponentConnectionStabilityAnalysis
        )

    @property
    def spiral_bevel_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3957.SpiralBevelGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3957,
        )

        return self.__parent__._cast(_3957.SpiralBevelGearMeshStabilityAnalysis)

    @property
    def spring_damper_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3960.SpringDamperConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3960,
        )

        return self.__parent__._cast(_3960.SpringDamperConnectionStabilityAnalysis)

    @property
    def straight_bevel_diff_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3966.StraightBevelDiffGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3966,
        )

        return self.__parent__._cast(_3966.StraightBevelDiffGearMeshStabilityAnalysis)

    @property
    def straight_bevel_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3969.StraightBevelGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3969,
        )

        return self.__parent__._cast(_3969.StraightBevelGearMeshStabilityAnalysis)

    @property
    def torque_converter_connection_stability_analysis(
        self: "CastSelf",
    ) -> "_3978.TorqueConverterConnectionStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3978,
        )

        return self.__parent__._cast(_3978.TorqueConverterConnectionStabilityAnalysis)

    @property
    def worm_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3984.WormGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3984,
        )

        return self.__parent__._cast(_3984.WormGearMeshStabilityAnalysis)

    @property
    def zerol_bevel_gear_mesh_stability_analysis(
        self: "CastSelf",
    ) -> "_3987.ZerolBevelGearMeshStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses import (
            _3987,
        )

        return self.__parent__._cast(_3987.ZerolBevelGearMeshStabilityAnalysis)

    @property
    def connection_stability_analysis(
        self: "CastSelf",
    ) -> "ConnectionStabilityAnalysis":
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
class ConnectionStabilityAnalysis(_7702.ConnectionStaticLoadAnalysisCase):
    """ConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTION_STABILITY_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2338.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: "Self") -> "_2338.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def stability_analysis(self: "Self") -> "_3963.StabilityAnalysis":
        """mastapy.system_model.analyses_and_results.stability_analyses.StabilityAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "StabilityAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ConnectionStabilityAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ConnectionStabilityAnalysis
        """
        return _Cast_ConnectionStabilityAnalysis(self)
