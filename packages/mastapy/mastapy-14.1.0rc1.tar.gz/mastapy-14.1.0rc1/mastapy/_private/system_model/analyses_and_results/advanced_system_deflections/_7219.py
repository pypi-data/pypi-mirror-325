"""AGMAGleasonConicalGearMeshAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
    _7247,
)

_AGMA_GLEASON_CONICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7226,
        _7231,
        _7249,
        _7275,
        _7279,
        _7281,
        _7319,
        _7325,
        _7328,
        _7347,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import _2365

    Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection:
    """Special nested class for casting AGMAGleasonConicalGearMeshAdvancedSystemDeflection to subclasses."""

    __parent__: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection"

    @property
    def conical_gear_mesh_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7247.ConicalGearMeshAdvancedSystemDeflection":
        return self.__parent__._cast(_7247.ConicalGearMeshAdvancedSystemDeflection)

    @property
    def gear_mesh_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7275.GearMeshAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7275,
        )

        return self.__parent__._cast(_7275.GearMeshAdvancedSystemDeflection)

    @property
    def inter_mountable_component_connection_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7281.InterMountableComponentConnectionAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7281,
        )

        return self.__parent__._cast(
            _7281.InterMountableComponentConnectionAdvancedSystemDeflection
        )

    @property
    def connection_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7249.ConnectionAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7249,
        )

        return self.__parent__._cast(_7249.ConnectionAdvancedSystemDeflection)

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
    def bevel_differential_gear_mesh_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7226.BevelDifferentialGearMeshAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7226,
        )

        return self.__parent__._cast(
            _7226.BevelDifferentialGearMeshAdvancedSystemDeflection
        )

    @property
    def bevel_gear_mesh_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7231.BevelGearMeshAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7231,
        )

        return self.__parent__._cast(_7231.BevelGearMeshAdvancedSystemDeflection)

    @property
    def hypoid_gear_mesh_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7279.HypoidGearMeshAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7279,
        )

        return self.__parent__._cast(_7279.HypoidGearMeshAdvancedSystemDeflection)

    @property
    def spiral_bevel_gear_mesh_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7319.SpiralBevelGearMeshAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7319,
        )

        return self.__parent__._cast(_7319.SpiralBevelGearMeshAdvancedSystemDeflection)

    @property
    def straight_bevel_diff_gear_mesh_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7325.StraightBevelDiffGearMeshAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7325,
        )

        return self.__parent__._cast(
            _7325.StraightBevelDiffGearMeshAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_mesh_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7328.StraightBevelGearMeshAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7328,
        )

        return self.__parent__._cast(
            _7328.StraightBevelGearMeshAdvancedSystemDeflection
        )

    @property
    def zerol_bevel_gear_mesh_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7347.ZerolBevelGearMeshAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7347,
        )

        return self.__parent__._cast(_7347.ZerolBevelGearMeshAdvancedSystemDeflection)

    @property
    def agma_gleason_conical_gear_mesh_advanced_system_deflection(
        self: "CastSelf",
    ) -> "AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
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
class AGMAGleasonConicalGearMeshAdvancedSystemDeflection(
    _7247.ConicalGearMeshAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _AGMA_GLEASON_CONICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2365.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "_Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection
        """
        return _Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection(self)
