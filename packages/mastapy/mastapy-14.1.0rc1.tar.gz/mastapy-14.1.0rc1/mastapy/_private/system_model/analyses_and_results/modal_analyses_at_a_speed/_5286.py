"""GearMeshModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
    _5293,
)

_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "GearMeshModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5232,
        _5239,
        _5244,
        _5257,
        _5260,
        _5263,
        _5275,
        _5281,
        _5290,
        _5294,
        _5297,
        _5300,
        _5330,
        _5336,
        _5339,
        _5354,
        _5357,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import _2379

    Self = TypeVar("Self", bound="GearMeshModalAnalysisAtASpeed")
    CastSelf = TypeVar(
        "CastSelf",
        bound="GearMeshModalAnalysisAtASpeed._Cast_GearMeshModalAnalysisAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshModalAnalysisAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_GearMeshModalAnalysisAtASpeed:
    """Special nested class for casting GearMeshModalAnalysisAtASpeed to subclasses."""

    __parent__: "GearMeshModalAnalysisAtASpeed"

    @property
    def inter_mountable_component_connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5293.InterMountableComponentConnectionModalAnalysisAtASpeed":
        return self.__parent__._cast(
            _5293.InterMountableComponentConnectionModalAnalysisAtASpeed
        )

    @property
    def connection_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5263.ConnectionModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5263,
        )

        return self.__parent__._cast(_5263.ConnectionModalAnalysisAtASpeed)

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
    def agma_gleason_conical_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5232.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5232,
        )

        return self.__parent__._cast(
            _5232.AGMAGleasonConicalGearMeshModalAnalysisAtASpeed
        )

    @property
    def bevel_differential_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5239.BevelDifferentialGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5239,
        )

        return self.__parent__._cast(
            _5239.BevelDifferentialGearMeshModalAnalysisAtASpeed
        )

    @property
    def bevel_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5244.BevelGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5244,
        )

        return self.__parent__._cast(_5244.BevelGearMeshModalAnalysisAtASpeed)

    @property
    def concept_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5257.ConceptGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5257,
        )

        return self.__parent__._cast(_5257.ConceptGearMeshModalAnalysisAtASpeed)

    @property
    def conical_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5260.ConicalGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5260,
        )

        return self.__parent__._cast(_5260.ConicalGearMeshModalAnalysisAtASpeed)

    @property
    def cylindrical_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5275.CylindricalGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5275,
        )

        return self.__parent__._cast(_5275.CylindricalGearMeshModalAnalysisAtASpeed)

    @property
    def face_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5281.FaceGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5281,
        )

        return self.__parent__._cast(_5281.FaceGearMeshModalAnalysisAtASpeed)

    @property
    def hypoid_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5290.HypoidGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5290,
        )

        return self.__parent__._cast(_5290.HypoidGearMeshModalAnalysisAtASpeed)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5294.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5294,
        )

        return self.__parent__._cast(
            _5294.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5297.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5297,
        )

        return self.__parent__._cast(
            _5297.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5300.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5300,
        )

        return self.__parent__._cast(
            _5300.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtASpeed
        )

    @property
    def spiral_bevel_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5330.SpiralBevelGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5330,
        )

        return self.__parent__._cast(_5330.SpiralBevelGearMeshModalAnalysisAtASpeed)

    @property
    def straight_bevel_diff_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5336.StraightBevelDiffGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5336,
        )

        return self.__parent__._cast(
            _5336.StraightBevelDiffGearMeshModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5339.StraightBevelGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5339,
        )

        return self.__parent__._cast(_5339.StraightBevelGearMeshModalAnalysisAtASpeed)

    @property
    def worm_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5354.WormGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5354,
        )

        return self.__parent__._cast(_5354.WormGearMeshModalAnalysisAtASpeed)

    @property
    def zerol_bevel_gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5357.ZerolBevelGearMeshModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
            _5357,
        )

        return self.__parent__._cast(_5357.ZerolBevelGearMeshModalAnalysisAtASpeed)

    @property
    def gear_mesh_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "GearMeshModalAnalysisAtASpeed":
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
class GearMeshModalAnalysisAtASpeed(
    _5293.InterMountableComponentConnectionModalAnalysisAtASpeed
):
    """GearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2379.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_GearMeshModalAnalysisAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_GearMeshModalAnalysisAtASpeed
        """
        return _Cast_GearMeshModalAnalysisAtASpeed(self)
