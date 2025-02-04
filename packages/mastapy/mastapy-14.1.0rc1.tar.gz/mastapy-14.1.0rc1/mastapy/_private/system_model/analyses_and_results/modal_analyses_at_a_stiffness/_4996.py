"""ConicalGearMeshModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _5023,
)

_CONICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "ConicalGearMeshModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4968,
        _4975,
        _4980,
        _4999,
        _5027,
        _5030,
        _5031,
        _5034,
        _5037,
        _5067,
        _5073,
        _5076,
        _5094,
    )
    from mastapy._private.system_model.connections_and_sockets.gears import _2373

    Self = TypeVar("Self", bound="ConicalGearMeshModalAnalysisAtAStiffness")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ConicalGearMeshModalAnalysisAtAStiffness._Cast_ConicalGearMeshModalAnalysisAtAStiffness",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshModalAnalysisAtAStiffness",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConicalGearMeshModalAnalysisAtAStiffness:
    """Special nested class for casting ConicalGearMeshModalAnalysisAtAStiffness to subclasses."""

    __parent__: "ConicalGearMeshModalAnalysisAtAStiffness"

    @property
    def gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5023.GearMeshModalAnalysisAtAStiffness":
        return self.__parent__._cast(_5023.GearMeshModalAnalysisAtAStiffness)

    @property
    def inter_mountable_component_connection_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5030.InterMountableComponentConnectionModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5030,
        )

        return self.__parent__._cast(
            _5030.InterMountableComponentConnectionModalAnalysisAtAStiffness
        )

    @property
    def connection_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4999.ConnectionModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4999,
        )

        return self.__parent__._cast(_4999.ConnectionModalAnalysisAtAStiffness)

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
    def agma_gleason_conical_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4968.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4968,
        )

        return self.__parent__._cast(
            _4968.AGMAGleasonConicalGearMeshModalAnalysisAtAStiffness
        )

    @property
    def bevel_differential_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4975.BevelDifferentialGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4975,
        )

        return self.__parent__._cast(
            _4975.BevelDifferentialGearMeshModalAnalysisAtAStiffness
        )

    @property
    def bevel_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_4980.BevelGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _4980,
        )

        return self.__parent__._cast(_4980.BevelGearMeshModalAnalysisAtAStiffness)

    @property
    def hypoid_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5027.HypoidGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5027,
        )

        return self.__parent__._cast(_5027.HypoidGearMeshModalAnalysisAtAStiffness)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5031.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5031,
        )

        return self.__parent__._cast(
            _5031.KlingelnbergCycloPalloidConicalGearMeshModalAnalysisAtAStiffness
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5034.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5034,
        )

        return self.__parent__._cast(
            _5034.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysisAtAStiffness
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5037.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5037,
        )

        return self.__parent__._cast(
            _5037.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysisAtAStiffness
        )

    @property
    def spiral_bevel_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5067.SpiralBevelGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5067,
        )

        return self.__parent__._cast(_5067.SpiralBevelGearMeshModalAnalysisAtAStiffness)

    @property
    def straight_bevel_diff_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5073.StraightBevelDiffGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5073,
        )

        return self.__parent__._cast(
            _5073.StraightBevelDiffGearMeshModalAnalysisAtAStiffness
        )

    @property
    def straight_bevel_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5076.StraightBevelGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5076,
        )

        return self.__parent__._cast(
            _5076.StraightBevelGearMeshModalAnalysisAtAStiffness
        )

    @property
    def zerol_bevel_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "_5094.ZerolBevelGearMeshModalAnalysisAtAStiffness":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
            _5094,
        )

        return self.__parent__._cast(_5094.ZerolBevelGearMeshModalAnalysisAtAStiffness)

    @property
    def conical_gear_mesh_modal_analysis_at_a_stiffness(
        self: "CastSelf",
    ) -> "ConicalGearMeshModalAnalysisAtAStiffness":
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
class ConicalGearMeshModalAnalysisAtAStiffness(_5023.GearMeshModalAnalysisAtAStiffness):
    """ConicalGearMeshModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_STIFFNESS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2373.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: "Self") -> "List[ConicalGearMeshModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.ConicalGearMeshModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Planetaries")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_ConicalGearMeshModalAnalysisAtAStiffness":
        """Cast to another type.

        Returns:
            _Cast_ConicalGearMeshModalAnalysisAtAStiffness
        """
        return _Cast_ConicalGearMeshModalAnalysisAtAStiffness(self)
