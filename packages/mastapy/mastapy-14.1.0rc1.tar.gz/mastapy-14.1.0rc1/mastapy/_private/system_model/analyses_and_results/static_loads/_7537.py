"""ConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results import _2724

_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectionLoadCase"
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728
    from mastapy._private.system_model.analyses_and_results.static_loads import (
        _7493,
        _7497,
        _7502,
        _7508,
        _7511,
        _7516,
        _7520,
        _7524,
        _7526,
        _7530,
        _7534,
        _7539,
        _7542,
        _7546,
        _7548,
        _7551,
        _7573,
        _7580,
        _7594,
        _7599,
        _7601,
        _7604,
        _7607,
        _7619,
        _7622,
        _7634,
        _7636,
        _7641,
        _7644,
        _7646,
        _7650,
        _7653,
        _7662,
        _7663,
        _7674,
        _7677,
    )
    from mastapy._private.system_model.connections_and_sockets import _2338

    Self = TypeVar("Self", bound="ConnectionLoadCase")
    CastSelf = TypeVar("CastSelf", bound="ConnectionLoadCase._Cast_ConnectionLoadCase")


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionLoadCase",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConnectionLoadCase:
    """Special nested class for casting ConnectionLoadCase to subclasses."""

    __parent__: "ConnectionLoadCase"

    @property
    def connection_analysis(self: "CastSelf") -> "_2724.ConnectionAnalysis":
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
    def abstract_shaft_to_mountable_component_connection_load_case(
        self: "CastSelf",
    ) -> "_7497.AbstractShaftToMountableComponentConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7497,
        )

        return self.__parent__._cast(
            _7497.AbstractShaftToMountableComponentConnectionLoadCase
        )

    @property
    def agma_gleason_conical_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7502.AGMAGleasonConicalGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7502,
        )

        return self.__parent__._cast(_7502.AGMAGleasonConicalGearMeshLoadCase)

    @property
    def belt_connection_load_case(self: "CastSelf") -> "_7508.BeltConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7508,
        )

        return self.__parent__._cast(_7508.BeltConnectionLoadCase)

    @property
    def bevel_differential_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7511.BevelDifferentialGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7511,
        )

        return self.__parent__._cast(_7511.BevelDifferentialGearMeshLoadCase)

    @property
    def bevel_gear_mesh_load_case(self: "CastSelf") -> "_7516.BevelGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7516,
        )

        return self.__parent__._cast(_7516.BevelGearMeshLoadCase)

    @property
    def clutch_connection_load_case(
        self: "CastSelf",
    ) -> "_7520.ClutchConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7520,
        )

        return self.__parent__._cast(_7520.ClutchConnectionLoadCase)

    @property
    def coaxial_connection_load_case(
        self: "CastSelf",
    ) -> "_7524.CoaxialConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7524,
        )

        return self.__parent__._cast(_7524.CoaxialConnectionLoadCase)

    @property
    def concept_coupling_connection_load_case(
        self: "CastSelf",
    ) -> "_7526.ConceptCouplingConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7526,
        )

        return self.__parent__._cast(_7526.ConceptCouplingConnectionLoadCase)

    @property
    def concept_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7530.ConceptGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7530,
        )

        return self.__parent__._cast(_7530.ConceptGearMeshLoadCase)

    @property
    def conical_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7534.ConicalGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7534,
        )

        return self.__parent__._cast(_7534.ConicalGearMeshLoadCase)

    @property
    def coupling_connection_load_case(
        self: "CastSelf",
    ) -> "_7539.CouplingConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7539,
        )

        return self.__parent__._cast(_7539.CouplingConnectionLoadCase)

    @property
    def cvt_belt_connection_load_case(
        self: "CastSelf",
    ) -> "_7542.CVTBeltConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7542,
        )

        return self.__parent__._cast(_7542.CVTBeltConnectionLoadCase)

    @property
    def cycloidal_disc_central_bearing_connection_load_case(
        self: "CastSelf",
    ) -> "_7546.CycloidalDiscCentralBearingConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7546,
        )

        return self.__parent__._cast(
            _7546.CycloidalDiscCentralBearingConnectionLoadCase
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_load_case(
        self: "CastSelf",
    ) -> "_7548.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7548,
        )

        return self.__parent__._cast(
            _7548.CycloidalDiscPlanetaryBearingConnectionLoadCase
        )

    @property
    def cylindrical_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7551.CylindricalGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7551,
        )

        return self.__parent__._cast(_7551.CylindricalGearMeshLoadCase)

    @property
    def face_gear_mesh_load_case(self: "CastSelf") -> "_7573.FaceGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7573,
        )

        return self.__parent__._cast(_7573.FaceGearMeshLoadCase)

    @property
    def gear_mesh_load_case(self: "CastSelf") -> "_7580.GearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7580,
        )

        return self.__parent__._cast(_7580.GearMeshLoadCase)

    @property
    def hypoid_gear_mesh_load_case(self: "CastSelf") -> "_7594.HypoidGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7594,
        )

        return self.__parent__._cast(_7594.HypoidGearMeshLoadCase)

    @property
    def inter_mountable_component_connection_load_case(
        self: "CastSelf",
    ) -> "_7599.InterMountableComponentConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7599,
        )

        return self.__parent__._cast(_7599.InterMountableComponentConnectionLoadCase)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7601.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7601,
        )

        return self.__parent__._cast(
            _7601.KlingelnbergCycloPalloidConicalGearMeshLoadCase
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7604.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7604,
        )

        return self.__parent__._cast(
            _7604.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7607.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7607,
        )

        return self.__parent__._cast(
            _7607.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
        )

    @property
    def part_to_part_shear_coupling_connection_load_case(
        self: "CastSelf",
    ) -> "_7619.PartToPartShearCouplingConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7619,
        )

        return self.__parent__._cast(_7619.PartToPartShearCouplingConnectionLoadCase)

    @property
    def planetary_connection_load_case(
        self: "CastSelf",
    ) -> "_7622.PlanetaryConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7622,
        )

        return self.__parent__._cast(_7622.PlanetaryConnectionLoadCase)

    @property
    def ring_pins_to_disc_connection_load_case(
        self: "CastSelf",
    ) -> "_7634.RingPinsToDiscConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7634,
        )

        return self.__parent__._cast(_7634.RingPinsToDiscConnectionLoadCase)

    @property
    def rolling_ring_connection_load_case(
        self: "CastSelf",
    ) -> "_7636.RollingRingConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7636,
        )

        return self.__parent__._cast(_7636.RollingRingConnectionLoadCase)

    @property
    def shaft_to_mountable_component_connection_load_case(
        self: "CastSelf",
    ) -> "_7641.ShaftToMountableComponentConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7641,
        )

        return self.__parent__._cast(_7641.ShaftToMountableComponentConnectionLoadCase)

    @property
    def spiral_bevel_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7644.SpiralBevelGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7644,
        )

        return self.__parent__._cast(_7644.SpiralBevelGearMeshLoadCase)

    @property
    def spring_damper_connection_load_case(
        self: "CastSelf",
    ) -> "_7646.SpringDamperConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7646,
        )

        return self.__parent__._cast(_7646.SpringDamperConnectionLoadCase)

    @property
    def straight_bevel_diff_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7650.StraightBevelDiffGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7650,
        )

        return self.__parent__._cast(_7650.StraightBevelDiffGearMeshLoadCase)

    @property
    def straight_bevel_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7653.StraightBevelGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7653,
        )

        return self.__parent__._cast(_7653.StraightBevelGearMeshLoadCase)

    @property
    def torque_converter_connection_load_case(
        self: "CastSelf",
    ) -> "_7663.TorqueConverterConnectionLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7663,
        )

        return self.__parent__._cast(_7663.TorqueConverterConnectionLoadCase)

    @property
    def worm_gear_mesh_load_case(self: "CastSelf") -> "_7674.WormGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7674,
        )

        return self.__parent__._cast(_7674.WormGearMeshLoadCase)

    @property
    def zerol_bevel_gear_mesh_load_case(
        self: "CastSelf",
    ) -> "_7677.ZerolBevelGearMeshLoadCase":
        from mastapy._private.system_model.analyses_and_results.static_loads import (
            _7677,
        )

        return self.__parent__._cast(_7677.ZerolBevelGearMeshLoadCase)

    @property
    def connection_load_case(self: "CastSelf") -> "ConnectionLoadCase":
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
class ConnectionLoadCase(_2724.ConnectionAnalysis):
    """ConnectionLoadCase

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTION_LOAD_CASE

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
    def static_load_case(self: "Self") -> "_7493.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "StaticLoadCase")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case(self: "Self") -> "_7662.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "TimeSeriesLoadCase")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ConnectionLoadCase":
        """Cast to another type.

        Returns:
            _Cast_ConnectionLoadCase
        """
        return _Cast_ConnectionLoadCase(self)
