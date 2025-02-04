"""ConnectionHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7702

_CONNECTION_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConnectionHarmonicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7699
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5804,
        _5806,
        _5810,
        _5813,
        _5818,
        _5822,
        _5825,
        _5828,
        _5832,
        _5835,
        _5839,
        _5842,
        _5846,
        _5848,
        _5850,
        _5871,
        _5878,
        _5884,
        _5895,
        _5897,
        _5899,
        _5902,
        _5905,
        _5914,
        _5918,
        _5926,
        _5928,
        _5933,
        _5938,
        _5940,
        _5945,
        _5948,
        _5956,
        _5964,
        _5967,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6197,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2802,
    )
    from mastapy._private.system_model.connections_and_sockets import _2338

    Self = TypeVar("Self", bound="ConnectionHarmonicAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="ConnectionHarmonicAnalysis._Cast_ConnectionHarmonicAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionHarmonicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConnectionHarmonicAnalysis:
    """Special nested class for casting ConnectionHarmonicAnalysis to subclasses."""

    __parent__: "ConnectionHarmonicAnalysis"

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
    def abstract_shaft_to_mountable_component_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5804.AbstractShaftToMountableComponentConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5804,
        )

        return self.__parent__._cast(
            _5804.AbstractShaftToMountableComponentConnectionHarmonicAnalysis
        )

    @property
    def agma_gleason_conical_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5806.AGMAGleasonConicalGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5806,
        )

        return self.__parent__._cast(_5806.AGMAGleasonConicalGearMeshHarmonicAnalysis)

    @property
    def belt_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5810.BeltConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5810,
        )

        return self.__parent__._cast(_5810.BeltConnectionHarmonicAnalysis)

    @property
    def bevel_differential_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5813.BevelDifferentialGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5813,
        )

        return self.__parent__._cast(_5813.BevelDifferentialGearMeshHarmonicAnalysis)

    @property
    def bevel_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5818.BevelGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5818,
        )

        return self.__parent__._cast(_5818.BevelGearMeshHarmonicAnalysis)

    @property
    def clutch_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5822.ClutchConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5822,
        )

        return self.__parent__._cast(_5822.ClutchConnectionHarmonicAnalysis)

    @property
    def coaxial_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5825.CoaxialConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5825,
        )

        return self.__parent__._cast(_5825.CoaxialConnectionHarmonicAnalysis)

    @property
    def concept_coupling_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5828.ConceptCouplingConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5828,
        )

        return self.__parent__._cast(_5828.ConceptCouplingConnectionHarmonicAnalysis)

    @property
    def concept_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5832.ConceptGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5832,
        )

        return self.__parent__._cast(_5832.ConceptGearMeshHarmonicAnalysis)

    @property
    def conical_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5835.ConicalGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5835,
        )

        return self.__parent__._cast(_5835.ConicalGearMeshHarmonicAnalysis)

    @property
    def coupling_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5839.CouplingConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5839,
        )

        return self.__parent__._cast(_5839.CouplingConnectionHarmonicAnalysis)

    @property
    def cvt_belt_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5842.CVTBeltConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5842,
        )

        return self.__parent__._cast(_5842.CVTBeltConnectionHarmonicAnalysis)

    @property
    def cycloidal_disc_central_bearing_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5846.CycloidalDiscCentralBearingConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5846,
        )

        return self.__parent__._cast(
            _5846.CycloidalDiscCentralBearingConnectionHarmonicAnalysis
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5848.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5848,
        )

        return self.__parent__._cast(
            _5848.CycloidalDiscPlanetaryBearingConnectionHarmonicAnalysis
        )

    @property
    def cylindrical_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5850.CylindricalGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5850,
        )

        return self.__parent__._cast(_5850.CylindricalGearMeshHarmonicAnalysis)

    @property
    def face_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5871.FaceGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5871,
        )

        return self.__parent__._cast(_5871.FaceGearMeshHarmonicAnalysis)

    @property
    def gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5878.GearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5878,
        )

        return self.__parent__._cast(_5878.GearMeshHarmonicAnalysis)

    @property
    def hypoid_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5895.HypoidGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5895,
        )

        return self.__parent__._cast(_5895.HypoidGearMeshHarmonicAnalysis)

    @property
    def inter_mountable_component_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5897.InterMountableComponentConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5897,
        )

        return self.__parent__._cast(
            _5897.InterMountableComponentConnectionHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5899.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5899,
        )

        return self.__parent__._cast(
            _5899.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5902.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5902,
        )

        return self.__parent__._cast(
            _5902.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5905.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5905,
        )

        return self.__parent__._cast(
            _5905.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
        )

    @property
    def part_to_part_shear_coupling_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5914.PartToPartShearCouplingConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5914,
        )

        return self.__parent__._cast(
            _5914.PartToPartShearCouplingConnectionHarmonicAnalysis
        )

    @property
    def planetary_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5918.PlanetaryConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5918,
        )

        return self.__parent__._cast(_5918.PlanetaryConnectionHarmonicAnalysis)

    @property
    def ring_pins_to_disc_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5926.RingPinsToDiscConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5926,
        )

        return self.__parent__._cast(_5926.RingPinsToDiscConnectionHarmonicAnalysis)

    @property
    def rolling_ring_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5928.RollingRingConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5928,
        )

        return self.__parent__._cast(_5928.RollingRingConnectionHarmonicAnalysis)

    @property
    def shaft_to_mountable_component_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5933.ShaftToMountableComponentConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5933,
        )

        return self.__parent__._cast(
            _5933.ShaftToMountableComponentConnectionHarmonicAnalysis
        )

    @property
    def spiral_bevel_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5938.SpiralBevelGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5938,
        )

        return self.__parent__._cast(_5938.SpiralBevelGearMeshHarmonicAnalysis)

    @property
    def spring_damper_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5940.SpringDamperConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5940,
        )

        return self.__parent__._cast(_5940.SpringDamperConnectionHarmonicAnalysis)

    @property
    def straight_bevel_diff_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5945.StraightBevelDiffGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5945,
        )

        return self.__parent__._cast(_5945.StraightBevelDiffGearMeshHarmonicAnalysis)

    @property
    def straight_bevel_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5948.StraightBevelGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5948,
        )

        return self.__parent__._cast(_5948.StraightBevelGearMeshHarmonicAnalysis)

    @property
    def torque_converter_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5956.TorqueConverterConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5956,
        )

        return self.__parent__._cast(_5956.TorqueConverterConnectionHarmonicAnalysis)

    @property
    def worm_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5964.WormGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5964,
        )

        return self.__parent__._cast(_5964.WormGearMeshHarmonicAnalysis)

    @property
    def zerol_bevel_gear_mesh_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5967.ZerolBevelGearMeshHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5967,
        )

        return self.__parent__._cast(_5967.ZerolBevelGearMeshHarmonicAnalysis)

    @property
    def connection_harmonic_analysis(self: "CastSelf") -> "ConnectionHarmonicAnalysis":
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
class ConnectionHarmonicAnalysis(_7702.ConnectionStaticLoadAnalysisCase):
    """ConnectionHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTION_HARMONIC_ANALYSIS

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
    def harmonic_analysis(self: "Self") -> "_5884.HarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "HarmonicAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analyses_of_single_excitations(
        self: "Self",
    ) -> "List[_6197.HarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "HarmonicAnalysesOfSingleExcitations"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: "Self") -> "_2802.ConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SystemDeflectionResults")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ConnectionHarmonicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ConnectionHarmonicAnalysis
        """
        return _Cast_ConnectionHarmonicAnalysis(self)
