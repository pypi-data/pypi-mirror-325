"""ConnectionCompoundAdvancedSystemDeflection"""

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

_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7249,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7352,
        _7354,
        _7358,
        _7361,
        _7366,
        _7371,
        _7373,
        _7376,
        _7379,
        _7382,
        _7387,
        _7389,
        _7393,
        _7395,
        _7397,
        _7403,
        _7408,
        _7412,
        _7414,
        _7416,
        _7419,
        _7422,
        _7432,
        _7434,
        _7441,
        _7444,
        _7448,
        _7451,
        _7454,
        _7457,
        _7460,
        _7469,
        _7475,
        _7478,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7704

    Self = TypeVar("Self", bound="ConnectionCompoundAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConnectionCompoundAdvancedSystemDeflection:
    """Special nested class for casting ConnectionCompoundAdvancedSystemDeflection to subclasses."""

    __parent__: "ConnectionCompoundAdvancedSystemDeflection"

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
    def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7352.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7352,
        )

        return self.__parent__._cast(
            _7352.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7354.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7354,
        )

        return self.__parent__._cast(
            _7354.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def belt_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7358.BeltConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7358,
        )

        return self.__parent__._cast(
            _7358.BeltConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7361.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7361,
        )

        return self.__parent__._cast(
            _7361.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7366.BevelGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7366,
        )

        return self.__parent__._cast(
            _7366.BevelGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def clutch_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7371.ClutchConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7371,
        )

        return self.__parent__._cast(
            _7371.ClutchConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def coaxial_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7373.CoaxialConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7373,
        )

        return self.__parent__._cast(
            _7373.CoaxialConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def concept_coupling_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7376.ConceptCouplingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7376,
        )

        return self.__parent__._cast(
            _7376.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def concept_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7379.ConceptGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7379,
        )

        return self.__parent__._cast(
            _7379.ConceptGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def conical_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7382.ConicalGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7382,
        )

        return self.__parent__._cast(
            _7382.ConicalGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def coupling_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7387.CouplingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7387,
        )

        return self.__parent__._cast(
            _7387.CouplingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def cvt_belt_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7389.CVTBeltConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7389,
        )

        return self.__parent__._cast(
            _7389.CVTBeltConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7393.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7393,
        )

        return self.__parent__._cast(
            _7393.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> (
        "_7395.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7395,
        )

        return self.__parent__._cast(
            _7395.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7397.CylindricalGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7397,
        )

        return self.__parent__._cast(
            _7397.CylindricalGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def face_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7403.FaceGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7403,
        )

        return self.__parent__._cast(_7403.FaceGearMeshCompoundAdvancedSystemDeflection)

    @property
    def gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7408.GearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7408,
        )

        return self.__parent__._cast(_7408.GearMeshCompoundAdvancedSystemDeflection)

    @property
    def hypoid_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7412.HypoidGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7412,
        )

        return self.__parent__._cast(
            _7412.HypoidGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def inter_mountable_component_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7414.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7414,
        )

        return self.__parent__._cast(
            _7414.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> (
        "_7416.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7416,
        )

        return self.__parent__._cast(
            _7416.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7419.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7419,
        )

        return self.__parent__._cast(
            _7419.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7422.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7422,
        )

        return self.__parent__._cast(
            _7422.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7432.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7432,
        )

        return self.__parent__._cast(
            _7432.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def planetary_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7434.PlanetaryConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7434,
        )

        return self.__parent__._cast(
            _7434.PlanetaryConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def ring_pins_to_disc_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7441.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7441,
        )

        return self.__parent__._cast(
            _7441.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def rolling_ring_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7444.RollingRingConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7444,
        )

        return self.__parent__._cast(
            _7444.RollingRingConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def shaft_to_mountable_component_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7448.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7448,
        )

        return self.__parent__._cast(
            _7448.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7451.SpiralBevelGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7451,
        )

        return self.__parent__._cast(
            _7451.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def spring_damper_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7454.SpringDamperConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7454,
        )

        return self.__parent__._cast(
            _7454.SpringDamperConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7457.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7457,
        )

        return self.__parent__._cast(
            _7457.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7460.StraightBevelGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7460,
        )

        return self.__parent__._cast(
            _7460.StraightBevelGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7469.TorqueConverterConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7469,
        )

        return self.__parent__._cast(
            _7469.TorqueConverterConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def worm_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7475.WormGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7475,
        )

        return self.__parent__._cast(_7475.WormGearMeshCompoundAdvancedSystemDeflection)

    @property
    def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7478.ZerolBevelGearMeshCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7478,
        )

        return self.__parent__._cast(
            _7478.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
        )

    @property
    def connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "ConnectionCompoundAdvancedSystemDeflection":
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
class ConnectionCompoundAdvancedSystemDeflection(_7700.ConnectionCompoundAnalysis):
    """ConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_7249.ConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConnectionAdvancedSystemDeflection]

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
    ) -> "List[_7249.ConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConnectionAdvancedSystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_ConnectionCompoundAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_ConnectionCompoundAdvancedSystemDeflection
        """
        return _Cast_ConnectionCompoundAdvancedSystemDeflection(self)
