"""BevelGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
    _2933,
)

_BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BevelGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7700,
        _7704,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2781,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
        _2940,
        _2961,
        _2963,
        _2988,
        _2994,
        _3032,
        _3038,
        _3041,
        _3059,
    )

    Self = TypeVar("Self", bound="BevelGearMeshCompoundSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelGearMeshCompoundSystemDeflection:
    """Special nested class for casting BevelGearMeshCompoundSystemDeflection to subclasses."""

    __parent__: "BevelGearMeshCompoundSystemDeflection"

    @property
    def agma_gleason_conical_gear_mesh_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2933.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
        return self.__parent__._cast(
            _2933.AGMAGleasonConicalGearMeshCompoundSystemDeflection
        )

    @property
    def conical_gear_mesh_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2961.ConicalGearMeshCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2961,
        )

        return self.__parent__._cast(_2961.ConicalGearMeshCompoundSystemDeflection)

    @property
    def gear_mesh_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2988.GearMeshCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2988,
        )

        return self.__parent__._cast(_2988.GearMeshCompoundSystemDeflection)

    @property
    def inter_mountable_component_connection_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2994.InterMountableComponentConnectionCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2994,
        )

        return self.__parent__._cast(
            _2994.InterMountableComponentConnectionCompoundSystemDeflection
        )

    @property
    def connection_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2963.ConnectionCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2963,
        )

        return self.__parent__._cast(_2963.ConnectionCompoundSystemDeflection)

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
    def bevel_differential_gear_mesh_compound_system_deflection(
        self: "CastSelf",
    ) -> "_2940.BevelDifferentialGearMeshCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _2940,
        )

        return self.__parent__._cast(
            _2940.BevelDifferentialGearMeshCompoundSystemDeflection
        )

    @property
    def spiral_bevel_gear_mesh_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3032.SpiralBevelGearMeshCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3032,
        )

        return self.__parent__._cast(_3032.SpiralBevelGearMeshCompoundSystemDeflection)

    @property
    def straight_bevel_diff_gear_mesh_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3038.StraightBevelDiffGearMeshCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3038,
        )

        return self.__parent__._cast(
            _3038.StraightBevelDiffGearMeshCompoundSystemDeflection
        )

    @property
    def straight_bevel_gear_mesh_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3041.StraightBevelGearMeshCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3041,
        )

        return self.__parent__._cast(
            _3041.StraightBevelGearMeshCompoundSystemDeflection
        )

    @property
    def zerol_bevel_gear_mesh_compound_system_deflection(
        self: "CastSelf",
    ) -> "_3059.ZerolBevelGearMeshCompoundSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections.compound import (
            _3059,
        )

        return self.__parent__._cast(_3059.ZerolBevelGearMeshCompoundSystemDeflection)

    @property
    def bevel_gear_mesh_compound_system_deflection(
        self: "CastSelf",
    ) -> "BevelGearMeshCompoundSystemDeflection":
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
class BevelGearMeshCompoundSystemDeflection(
    _2933.AGMAGleasonConicalGearMeshCompoundSystemDeflection
):
    """BevelGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_2781.BevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection]

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
    ) -> "List[_2781.BevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_BevelGearMeshCompoundSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_BevelGearMeshCompoundSystemDeflection
        """
        return _Cast_BevelGearMeshCompoundSystemDeflection(self)
