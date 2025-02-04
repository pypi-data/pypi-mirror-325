"""InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5395,
)

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
        "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7700,
        _7704,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5293,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5365,
        _5369,
        _5372,
        _5377,
        _5382,
        _5387,
        _5390,
        _5393,
        _5398,
        _5400,
        _5408,
        _5414,
        _5419,
        _5423,
        _5427,
        _5430,
        _5433,
        _5443,
        _5452,
        _5455,
        _5462,
        _5465,
        _5468,
        _5471,
        _5480,
        _5486,
        _5489,
    )

    Self = TypeVar(
        "Self", bound="InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="InterMountableComponentConnectionCompoundModalAnalysisAtASpeed._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundModalAnalysisAtASpeed",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed:
    """Special nested class for casting InterMountableComponentConnectionCompoundModalAnalysisAtASpeed to subclasses."""

    __parent__: "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed"

    @property
    def connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5395.ConnectionCompoundModalAnalysisAtASpeed":
        return self.__parent__._cast(_5395.ConnectionCompoundModalAnalysisAtASpeed)

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
    def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5365.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5365,
        )

        return self.__parent__._cast(
            _5365.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtASpeed
        )

    @property
    def belt_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5369.BeltConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5369,
        )

        return self.__parent__._cast(_5369.BeltConnectionCompoundModalAnalysisAtASpeed)

    @property
    def bevel_differential_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5372.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5372,
        )

        return self.__parent__._cast(
            _5372.BevelDifferentialGearMeshCompoundModalAnalysisAtASpeed
        )

    @property
    def bevel_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5377.BevelGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5377,
        )

        return self.__parent__._cast(_5377.BevelGearMeshCompoundModalAnalysisAtASpeed)

    @property
    def clutch_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5382.ClutchConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5382,
        )

        return self.__parent__._cast(
            _5382.ClutchConnectionCompoundModalAnalysisAtASpeed
        )

    @property
    def concept_coupling_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5387.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5387,
        )

        return self.__parent__._cast(
            _5387.ConceptCouplingConnectionCompoundModalAnalysisAtASpeed
        )

    @property
    def concept_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5390.ConceptGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5390,
        )

        return self.__parent__._cast(_5390.ConceptGearMeshCompoundModalAnalysisAtASpeed)

    @property
    def conical_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5393.ConicalGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5393,
        )

        return self.__parent__._cast(_5393.ConicalGearMeshCompoundModalAnalysisAtASpeed)

    @property
    def coupling_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5398.CouplingConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5398,
        )

        return self.__parent__._cast(
            _5398.CouplingConnectionCompoundModalAnalysisAtASpeed
        )

    @property
    def cvt_belt_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5400.CVTBeltConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5400,
        )

        return self.__parent__._cast(
            _5400.CVTBeltConnectionCompoundModalAnalysisAtASpeed
        )

    @property
    def cylindrical_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5408.CylindricalGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5408,
        )

        return self.__parent__._cast(
            _5408.CylindricalGearMeshCompoundModalAnalysisAtASpeed
        )

    @property
    def face_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5414.FaceGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5414,
        )

        return self.__parent__._cast(_5414.FaceGearMeshCompoundModalAnalysisAtASpeed)

    @property
    def gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5419.GearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5419,
        )

        return self.__parent__._cast(_5419.GearMeshCompoundModalAnalysisAtASpeed)

    @property
    def hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5423.HypoidGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5423,
        )

        return self.__parent__._cast(_5423.HypoidGearMeshCompoundModalAnalysisAtASpeed)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5427.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5427,
        )

        return self.__parent__._cast(
            _5427.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5430.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5430,
        )

        return self.__parent__._cast(
            _5430.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtASpeed
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> (
        "_5433.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed"
    ):
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5433,
        )

        return self.__parent__._cast(
            _5433.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtASpeed
        )

    @property
    def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5443.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5443,
        )

        return self.__parent__._cast(
            _5443.PartToPartShearCouplingConnectionCompoundModalAnalysisAtASpeed
        )

    @property
    def ring_pins_to_disc_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5452.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5452,
        )

        return self.__parent__._cast(
            _5452.RingPinsToDiscConnectionCompoundModalAnalysisAtASpeed
        )

    @property
    def rolling_ring_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5455.RollingRingConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5455,
        )

        return self.__parent__._cast(
            _5455.RollingRingConnectionCompoundModalAnalysisAtASpeed
        )

    @property
    def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5462.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5462,
        )

        return self.__parent__._cast(
            _5462.SpiralBevelGearMeshCompoundModalAnalysisAtASpeed
        )

    @property
    def spring_damper_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5465.SpringDamperConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5465,
        )

        return self.__parent__._cast(
            _5465.SpringDamperConnectionCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5468.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5468,
        )

        return self.__parent__._cast(
            _5468.StraightBevelDiffGearMeshCompoundModalAnalysisAtASpeed
        )

    @property
    def straight_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5471.StraightBevelGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5471,
        )

        return self.__parent__._cast(
            _5471.StraightBevelGearMeshCompoundModalAnalysisAtASpeed
        )

    @property
    def torque_converter_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5480.TorqueConverterConnectionCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5480,
        )

        return self.__parent__._cast(
            _5480.TorqueConverterConnectionCompoundModalAnalysisAtASpeed
        )

    @property
    def worm_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5486.WormGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5486,
        )

        return self.__parent__._cast(_5486.WormGearMeshCompoundModalAnalysisAtASpeed)

    @property
    def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "_5489.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed":
        from mastapy._private.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
            _5489,
        )

        return self.__parent__._cast(
            _5489.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed
        )

    @property
    def inter_mountable_component_connection_compound_modal_analysis_at_a_speed(
        self: "CastSelf",
    ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
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
class InterMountableComponentConnectionCompoundModalAnalysisAtASpeed(
    _5395.ConnectionCompoundModalAnalysisAtASpeed
):
    """InterMountableComponentConnectionCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_analysis_cases(
        self: "Self",
    ) -> "List[_5293.InterMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.InterMountableComponentConnectionModalAnalysisAtASpeed]

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
    ) -> "List[_5293.InterMountableComponentConnectionModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.InterMountableComponentConnectionModalAnalysisAtASpeed]

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
    def cast_to(
        self: "Self",
    ) -> "_Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed":
        """Cast to another type.

        Returns:
            _Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed
        """
        return _Cast_InterMountableComponentConnectionCompoundModalAnalysisAtASpeed(
            self
        )
