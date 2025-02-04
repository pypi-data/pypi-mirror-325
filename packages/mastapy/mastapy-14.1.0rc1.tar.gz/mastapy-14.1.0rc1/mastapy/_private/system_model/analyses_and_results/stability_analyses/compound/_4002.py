"""BevelDifferentialGearMeshCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
    _4007,
)

_BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BevelDifferentialGearMeshCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7700,
        _7704,
    )
    from mastapy._private.system_model.analyses_and_results.stability_analyses import (
        _3865,
    )
    from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
        _3995,
        _4023,
        _4025,
        _4049,
        _4055,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import _2367

    Self = TypeVar("Self", bound="BevelDifferentialGearMeshCompoundStabilityAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="BevelDifferentialGearMeshCompoundStabilityAnalysis._Cast_BevelDifferentialGearMeshCompoundStabilityAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshCompoundStabilityAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelDifferentialGearMeshCompoundStabilityAnalysis:
    """Special nested class for casting BevelDifferentialGearMeshCompoundStabilityAnalysis to subclasses."""

    __parent__: "BevelDifferentialGearMeshCompoundStabilityAnalysis"

    @property
    def bevel_gear_mesh_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4007.BevelGearMeshCompoundStabilityAnalysis":
        return self.__parent__._cast(_4007.BevelGearMeshCompoundStabilityAnalysis)

    @property
    def agma_gleason_conical_gear_mesh_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_3995.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _3995,
        )

        return self.__parent__._cast(
            _3995.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
        )

    @property
    def conical_gear_mesh_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4023.ConicalGearMeshCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4023,
        )

        return self.__parent__._cast(_4023.ConicalGearMeshCompoundStabilityAnalysis)

    @property
    def gear_mesh_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4049.GearMeshCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4049,
        )

        return self.__parent__._cast(_4049.GearMeshCompoundStabilityAnalysis)

    @property
    def inter_mountable_component_connection_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4055.InterMountableComponentConnectionCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4055,
        )

        return self.__parent__._cast(
            _4055.InterMountableComponentConnectionCompoundStabilityAnalysis
        )

    @property
    def connection_compound_stability_analysis(
        self: "CastSelf",
    ) -> "_4025.ConnectionCompoundStabilityAnalysis":
        from mastapy._private.system_model.analyses_and_results.stability_analyses.compound import (
            _4025,
        )

        return self.__parent__._cast(_4025.ConnectionCompoundStabilityAnalysis)

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
    def bevel_differential_gear_mesh_compound_stability_analysis(
        self: "CastSelf",
    ) -> "BevelDifferentialGearMeshCompoundStabilityAnalysis":
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
class BevelDifferentialGearMeshCompoundStabilityAnalysis(
    _4007.BevelGearMeshCompoundStabilityAnalysis
):
    """BevelDifferentialGearMeshCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEVEL_DIFFERENTIAL_GEAR_MESH_COMPOUND_STABILITY_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2367.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: "Self") -> "_2367.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: "Self",
    ) -> "List[_3865.BevelDifferentialGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialGearMeshStabilityAnalysis]

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
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_3865.BevelDifferentialGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialGearMeshStabilityAnalysis]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_BevelDifferentialGearMeshCompoundStabilityAnalysis":
        """Cast to another type.

        Returns:
            _Cast_BevelDifferentialGearMeshCompoundStabilityAnalysis
        """
        return _Cast_BevelDifferentialGearMeshCompoundStabilityAnalysis(self)
