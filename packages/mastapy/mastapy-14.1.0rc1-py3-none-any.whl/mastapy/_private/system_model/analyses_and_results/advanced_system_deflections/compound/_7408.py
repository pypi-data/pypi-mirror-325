"""GearMeshCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7414,
)

_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "GearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7275,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7354,
        _7361,
        _7366,
        _7379,
        _7382,
        _7384,
        _7397,
        _7403,
        _7412,
        _7416,
        _7419,
        _7422,
        _7451,
        _7457,
        _7460,
        _7475,
        _7478,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7700,
        _7704,
    )

    Self = TypeVar("Self", bound="GearMeshCompoundAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearMeshCompoundAdvancedSystemDeflection._Cast_GearMeshCompoundAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearMeshCompoundAdvancedSystemDeflection:
    """Special nested class for casting GearMeshCompoundAdvancedSystemDeflection to subclasses."""

    __parent__: "GearMeshCompoundAdvancedSystemDeflection"

    @property
    def inter_mountable_component_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7414.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
        return self.__parent__._cast(
            _7414.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7384.ConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7384,
        )

        return self.__parent__._cast(_7384.ConnectionCompoundAdvancedSystemDeflection)

    @property
    def connection_compound_analysis(
        self: "CastSelf",
    ) -> "_7700.ConnectionCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7700,
        )

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
    def gear_mesh_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "GearMeshCompoundAdvancedSystemDeflection":
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
class GearMeshCompoundAdvancedSystemDeflection(
    _7414.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
):
    """GearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def minimum_separation_left_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "MinimumSeparationLeftFlank")

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_right_flank(self: "Self") -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "MinimumSeparationRightFlank")

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_7275.GearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.GearMeshAdvancedSystemDeflection]

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
    ) -> "List[_7275.GearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.GearMeshAdvancedSystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_GearMeshCompoundAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_GearMeshCompoundAdvancedSystemDeflection
        """
        return _Cast_GearMeshCompoundAdvancedSystemDeflection(self)
