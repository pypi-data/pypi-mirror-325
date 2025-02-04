"""InterMountableComponentConnectionPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.power_flows import _4162

_INTER_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "InterMountableComponentConnectionPowerFlow",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import (
        _4131,
        _4136,
        _4138,
        _4143,
        _4148,
        _4153,
        _4156,
        _4159,
        _4164,
        _4167,
        _4175,
        _4181,
        _4188,
        _4192,
        _4196,
        _4199,
        _4202,
        _4212,
        _4224,
        _4226,
        _4233,
        _4236,
        _4239,
        _4242,
        _4252,
        _4258,
        _4261,
    )
    from mastapy._private.system_model.connections_and_sockets import _2347

    Self = TypeVar("Self", bound="InterMountableComponentConnectionPowerFlow")
    CastSelf = TypeVar(
        "CastSelf",
        bound="InterMountableComponentConnectionPowerFlow._Cast_InterMountableComponentConnectionPowerFlow",
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_InterMountableComponentConnectionPowerFlow:
    """Special nested class for casting InterMountableComponentConnectionPowerFlow to subclasses."""

    __parent__: "InterMountableComponentConnectionPowerFlow"

    @property
    def connection_power_flow(self: "CastSelf") -> "_4162.ConnectionPowerFlow":
        return self.__parent__._cast(_4162.ConnectionPowerFlow)

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
    def agma_gleason_conical_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4131.AGMAGleasonConicalGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4131

        return self.__parent__._cast(_4131.AGMAGleasonConicalGearMeshPowerFlow)

    @property
    def belt_connection_power_flow(self: "CastSelf") -> "_4136.BeltConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4136

        return self.__parent__._cast(_4136.BeltConnectionPowerFlow)

    @property
    def bevel_differential_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4138.BevelDifferentialGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4138

        return self.__parent__._cast(_4138.BevelDifferentialGearMeshPowerFlow)

    @property
    def bevel_gear_mesh_power_flow(self: "CastSelf") -> "_4143.BevelGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4143

        return self.__parent__._cast(_4143.BevelGearMeshPowerFlow)

    @property
    def clutch_connection_power_flow(
        self: "CastSelf",
    ) -> "_4148.ClutchConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4148

        return self.__parent__._cast(_4148.ClutchConnectionPowerFlow)

    @property
    def concept_coupling_connection_power_flow(
        self: "CastSelf",
    ) -> "_4153.ConceptCouplingConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4153

        return self.__parent__._cast(_4153.ConceptCouplingConnectionPowerFlow)

    @property
    def concept_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4156.ConceptGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4156

        return self.__parent__._cast(_4156.ConceptGearMeshPowerFlow)

    @property
    def conical_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4159.ConicalGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4159

        return self.__parent__._cast(_4159.ConicalGearMeshPowerFlow)

    @property
    def coupling_connection_power_flow(
        self: "CastSelf",
    ) -> "_4164.CouplingConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4164

        return self.__parent__._cast(_4164.CouplingConnectionPowerFlow)

    @property
    def cvt_belt_connection_power_flow(
        self: "CastSelf",
    ) -> "_4167.CVTBeltConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4167

        return self.__parent__._cast(_4167.CVTBeltConnectionPowerFlow)

    @property
    def cylindrical_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4175.CylindricalGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4175

        return self.__parent__._cast(_4175.CylindricalGearMeshPowerFlow)

    @property
    def face_gear_mesh_power_flow(self: "CastSelf") -> "_4181.FaceGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4181

        return self.__parent__._cast(_4181.FaceGearMeshPowerFlow)

    @property
    def gear_mesh_power_flow(self: "CastSelf") -> "_4188.GearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4188

        return self.__parent__._cast(_4188.GearMeshPowerFlow)

    @property
    def hypoid_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4192.HypoidGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4192

        return self.__parent__._cast(_4192.HypoidGearMeshPowerFlow)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4196.KlingelnbergCycloPalloidConicalGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4196

        return self.__parent__._cast(
            _4196.KlingelnbergCycloPalloidConicalGearMeshPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4199.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4199

        return self.__parent__._cast(
            _4199.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4202.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4202

        return self.__parent__._cast(
            _4202.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow
        )

    @property
    def part_to_part_shear_coupling_connection_power_flow(
        self: "CastSelf",
    ) -> "_4212.PartToPartShearCouplingConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4212

        return self.__parent__._cast(_4212.PartToPartShearCouplingConnectionPowerFlow)

    @property
    def ring_pins_to_disc_connection_power_flow(
        self: "CastSelf",
    ) -> "_4224.RingPinsToDiscConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4224

        return self.__parent__._cast(_4224.RingPinsToDiscConnectionPowerFlow)

    @property
    def rolling_ring_connection_power_flow(
        self: "CastSelf",
    ) -> "_4226.RollingRingConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4226

        return self.__parent__._cast(_4226.RollingRingConnectionPowerFlow)

    @property
    def spiral_bevel_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4233.SpiralBevelGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4233

        return self.__parent__._cast(_4233.SpiralBevelGearMeshPowerFlow)

    @property
    def spring_damper_connection_power_flow(
        self: "CastSelf",
    ) -> "_4236.SpringDamperConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4236

        return self.__parent__._cast(_4236.SpringDamperConnectionPowerFlow)

    @property
    def straight_bevel_diff_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4239.StraightBevelDiffGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4239

        return self.__parent__._cast(_4239.StraightBevelDiffGearMeshPowerFlow)

    @property
    def straight_bevel_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4242.StraightBevelGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4242

        return self.__parent__._cast(_4242.StraightBevelGearMeshPowerFlow)

    @property
    def torque_converter_connection_power_flow(
        self: "CastSelf",
    ) -> "_4252.TorqueConverterConnectionPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4252

        return self.__parent__._cast(_4252.TorqueConverterConnectionPowerFlow)

    @property
    def worm_gear_mesh_power_flow(self: "CastSelf") -> "_4258.WormGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4258

        return self.__parent__._cast(_4258.WormGearMeshPowerFlow)

    @property
    def zerol_bevel_gear_mesh_power_flow(
        self: "CastSelf",
    ) -> "_4261.ZerolBevelGearMeshPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows import _4261

        return self.__parent__._cast(_4261.ZerolBevelGearMeshPowerFlow)

    @property
    def inter_mountable_component_connection_power_flow(
        self: "CastSelf",
    ) -> "InterMountableComponentConnectionPowerFlow":
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
class InterMountableComponentConnectionPowerFlow(_4162.ConnectionPowerFlow):
    """InterMountableComponentConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _INTER_MOUNTABLE_COMPONENT_CONNECTION_POWER_FLOW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2347.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_InterMountableComponentConnectionPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_InterMountableComponentConnectionPowerFlow
        """
        return _Cast_InterMountableComponentConnectionPowerFlow(self)
