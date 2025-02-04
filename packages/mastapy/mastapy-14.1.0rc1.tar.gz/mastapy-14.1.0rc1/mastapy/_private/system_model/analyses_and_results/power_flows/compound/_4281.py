"""BevelGearMeshCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
    _4269,
)

_BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "BevelGearMeshCompoundPowerFlow",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7700,
        _7704,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import _4143
    from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
        _4276,
        _4297,
        _4299,
        _4323,
        _4329,
        _4366,
        _4372,
        _4375,
        _4393,
    )

    Self = TypeVar("Self", bound="BevelGearMeshCompoundPowerFlow")
    CastSelf = TypeVar(
        "CastSelf",
        bound="BevelGearMeshCompoundPowerFlow._Cast_BevelGearMeshCompoundPowerFlow",
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_BevelGearMeshCompoundPowerFlow:
    """Special nested class for casting BevelGearMeshCompoundPowerFlow to subclasses."""

    __parent__: "BevelGearMeshCompoundPowerFlow"

    @property
    def agma_gleason_conical_gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "_4269.AGMAGleasonConicalGearMeshCompoundPowerFlow":
        return self.__parent__._cast(_4269.AGMAGleasonConicalGearMeshCompoundPowerFlow)

    @property
    def conical_gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "_4297.ConicalGearMeshCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4297,
        )

        return self.__parent__._cast(_4297.ConicalGearMeshCompoundPowerFlow)

    @property
    def gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "_4323.GearMeshCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4323,
        )

        return self.__parent__._cast(_4323.GearMeshCompoundPowerFlow)

    @property
    def inter_mountable_component_connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4329.InterMountableComponentConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4329,
        )

        return self.__parent__._cast(
            _4329.InterMountableComponentConnectionCompoundPowerFlow
        )

    @property
    def connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4299.ConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4299,
        )

        return self.__parent__._cast(_4299.ConnectionCompoundPowerFlow)

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
    def bevel_differential_gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "_4276.BevelDifferentialGearMeshCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4276,
        )

        return self.__parent__._cast(_4276.BevelDifferentialGearMeshCompoundPowerFlow)

    @property
    def spiral_bevel_gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "_4366.SpiralBevelGearMeshCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4366,
        )

        return self.__parent__._cast(_4366.SpiralBevelGearMeshCompoundPowerFlow)

    @property
    def straight_bevel_diff_gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "_4372.StraightBevelDiffGearMeshCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4372,
        )

        return self.__parent__._cast(_4372.StraightBevelDiffGearMeshCompoundPowerFlow)

    @property
    def straight_bevel_gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "_4375.StraightBevelGearMeshCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4375,
        )

        return self.__parent__._cast(_4375.StraightBevelGearMeshCompoundPowerFlow)

    @property
    def zerol_bevel_gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "_4393.ZerolBevelGearMeshCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4393,
        )

        return self.__parent__._cast(_4393.ZerolBevelGearMeshCompoundPowerFlow)

    @property
    def bevel_gear_mesh_compound_power_flow(
        self: "CastSelf",
    ) -> "BevelGearMeshCompoundPowerFlow":
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
class BevelGearMeshCompoundPowerFlow(_4269.AGMAGleasonConicalGearMeshCompoundPowerFlow):
    """BevelGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _BEVEL_GEAR_MESH_COMPOUND_POWER_FLOW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(self: "Self") -> "List[_4143.BevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelGearMeshPowerFlow]

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
    ) -> "List[_4143.BevelGearMeshPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.BevelGearMeshPowerFlow]

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
    def cast_to(self: "Self") -> "_Cast_BevelGearMeshCompoundPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_BevelGearMeshCompoundPowerFlow
        """
        return _Cast_BevelGearMeshCompoundPowerFlow(self)
