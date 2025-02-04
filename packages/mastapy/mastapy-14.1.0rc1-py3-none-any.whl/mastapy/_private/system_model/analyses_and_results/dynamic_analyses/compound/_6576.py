"""ConnectionCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7700

_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7704
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses import (
        _6443,
    )
    from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6544,
        _6546,
        _6550,
        _6553,
        _6558,
        _6563,
        _6565,
        _6568,
        _6571,
        _6574,
        _6579,
        _6581,
        _6585,
        _6587,
        _6589,
        _6595,
        _6600,
        _6604,
        _6606,
        _6608,
        _6611,
        _6614,
        _6624,
        _6626,
        _6633,
        _6636,
        _6640,
        _6643,
        _6646,
        _6649,
        _6652,
        _6661,
        _6667,
        _6670,
    )

    Self = TypeVar("Self", bound="ConnectionCompoundDynamicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundDynamicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConnectionCompoundDynamicAnalysis:
    """Special nested class for casting ConnectionCompoundDynamicAnalysis to subclasses."""

    __parent__: "ConnectionCompoundDynamicAnalysis"

    @property
    def connection_compound_analysis(
        self: "CastSelf",
    ) -> "_7700.ConnectionCompoundAnalysis":
        return self.__parent__._cast(_7700.ConnectionCompoundAnalysis)

    @property
    def design_entity_compound_analysis(
        self: "CastSelf",
    ) -> "_7704.DesignEntityCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7704,
        )

        return self.__parent__._cast(_7704.DesignEntityCompoundAnalysis)

    @property
    def design_entity_analysis(self: "CastSelf") -> "_2726.DesignEntityAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2726

        return self.__parent__._cast(_2726.DesignEntityAnalysis)

    @property
    def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6544.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6544,
        )

        return self.__parent__._cast(
            _6544.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
        )

    @property
    def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6546.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6546,
        )

        return self.__parent__._cast(
            _6546.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
        )

    @property
    def belt_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6550.BeltConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6550,
        )

        return self.__parent__._cast(_6550.BeltConnectionCompoundDynamicAnalysis)

    @property
    def bevel_differential_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6553.BevelDifferentialGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6553,
        )

        return self.__parent__._cast(
            _6553.BevelDifferentialGearMeshCompoundDynamicAnalysis
        )

    @property
    def bevel_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6558.BevelGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6558,
        )

        return self.__parent__._cast(_6558.BevelGearMeshCompoundDynamicAnalysis)

    @property
    def clutch_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6563.ClutchConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6563,
        )

        return self.__parent__._cast(_6563.ClutchConnectionCompoundDynamicAnalysis)

    @property
    def coaxial_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6565.CoaxialConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6565,
        )

        return self.__parent__._cast(_6565.CoaxialConnectionCompoundDynamicAnalysis)

    @property
    def concept_coupling_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6568.ConceptCouplingConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6568,
        )

        return self.__parent__._cast(
            _6568.ConceptCouplingConnectionCompoundDynamicAnalysis
        )

    @property
    def concept_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6571.ConceptGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6571,
        )

        return self.__parent__._cast(_6571.ConceptGearMeshCompoundDynamicAnalysis)

    @property
    def conical_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6574.ConicalGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6574,
        )

        return self.__parent__._cast(_6574.ConicalGearMeshCompoundDynamicAnalysis)

    @property
    def coupling_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6579.CouplingConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6579,
        )

        return self.__parent__._cast(_6579.CouplingConnectionCompoundDynamicAnalysis)

    @property
    def cvt_belt_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6581.CVTBeltConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6581,
        )

        return self.__parent__._cast(_6581.CVTBeltConnectionCompoundDynamicAnalysis)

    @property
    def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6585.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6585,
        )

        return self.__parent__._cast(
            _6585.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6587.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6587,
        )

        return self.__parent__._cast(
            _6587.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis
        )

    @property
    def cylindrical_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6589.CylindricalGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6589,
        )

        return self.__parent__._cast(_6589.CylindricalGearMeshCompoundDynamicAnalysis)

    @property
    def face_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6595.FaceGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6595,
        )

        return self.__parent__._cast(_6595.FaceGearMeshCompoundDynamicAnalysis)

    @property
    def gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6600.GearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6600,
        )

        return self.__parent__._cast(_6600.GearMeshCompoundDynamicAnalysis)

    @property
    def hypoid_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6604.HypoidGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6604,
        )

        return self.__parent__._cast(_6604.HypoidGearMeshCompoundDynamicAnalysis)

    @property
    def inter_mountable_component_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6606.InterMountableComponentConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6606,
        )

        return self.__parent__._cast(
            _6606.InterMountableComponentConnectionCompoundDynamicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6608.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6608,
        )

        return self.__parent__._cast(
            _6608.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6611.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6611,
        )

        return self.__parent__._cast(
            _6611.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6614.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6614,
        )

        return self.__parent__._cast(
            _6614.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
        )

    @property
    def part_to_part_shear_coupling_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6624.PartToPartShearCouplingConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6624,
        )

        return self.__parent__._cast(
            _6624.PartToPartShearCouplingConnectionCompoundDynamicAnalysis
        )

    @property
    def planetary_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6626.PlanetaryConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6626,
        )

        return self.__parent__._cast(_6626.PlanetaryConnectionCompoundDynamicAnalysis)

    @property
    def ring_pins_to_disc_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6633.RingPinsToDiscConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6633,
        )

        return self.__parent__._cast(
            _6633.RingPinsToDiscConnectionCompoundDynamicAnalysis
        )

    @property
    def rolling_ring_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6636.RollingRingConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6636,
        )

        return self.__parent__._cast(_6636.RollingRingConnectionCompoundDynamicAnalysis)

    @property
    def shaft_to_mountable_component_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6640.ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6640,
        )

        return self.__parent__._cast(
            _6640.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
        )

    @property
    def spiral_bevel_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6643.SpiralBevelGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6643,
        )

        return self.__parent__._cast(_6643.SpiralBevelGearMeshCompoundDynamicAnalysis)

    @property
    def spring_damper_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6646.SpringDamperConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6646,
        )

        return self.__parent__._cast(
            _6646.SpringDamperConnectionCompoundDynamicAnalysis
        )

    @property
    def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6649.StraightBevelDiffGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6649,
        )

        return self.__parent__._cast(
            _6649.StraightBevelDiffGearMeshCompoundDynamicAnalysis
        )

    @property
    def straight_bevel_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6652.StraightBevelGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6652,
        )

        return self.__parent__._cast(_6652.StraightBevelGearMeshCompoundDynamicAnalysis)

    @property
    def torque_converter_connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6661.TorqueConverterConnectionCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6661,
        )

        return self.__parent__._cast(
            _6661.TorqueConverterConnectionCompoundDynamicAnalysis
        )

    @property
    def worm_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6667.WormGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6667,
        )

        return self.__parent__._cast(_6667.WormGearMeshCompoundDynamicAnalysis)

    @property
    def zerol_bevel_gear_mesh_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "_6670.ZerolBevelGearMeshCompoundDynamicAnalysis":
        from mastapy._private.system_model.analyses_and_results.dynamic_analyses.compound import (
            _6670,
        )

        return self.__parent__._cast(_6670.ZerolBevelGearMeshCompoundDynamicAnalysis)

    @property
    def connection_compound_dynamic_analysis(
        self: "CastSelf",
    ) -> "ConnectionCompoundDynamicAnalysis":
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
class ConnectionCompoundDynamicAnalysis(_7700.ConnectionCompoundAnalysis):
    """ConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTION_COMPOUND_DYNAMIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_6443.ConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectionDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_6443.ConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectionDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ConnectionCompoundDynamicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ConnectionCompoundDynamicAnalysis
        """
        return _Cast_ConnectionCompoundDynamicAnalysis(self)
