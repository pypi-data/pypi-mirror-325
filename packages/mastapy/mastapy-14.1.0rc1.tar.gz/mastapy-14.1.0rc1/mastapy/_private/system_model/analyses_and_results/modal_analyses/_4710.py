"""ConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7702

_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7699
    from mastapy._private.system_model.analyses_and_results.modal_analyses import (
        _4678,
        _4679,
        _4684,
        _4686,
        _4691,
        _4696,
        _4699,
        _4701,
        _4704,
        _4707,
        _4713,
        _4716,
        _4720,
        _4722,
        _4723,
        _4732,
        _4738,
        _4742,
        _4745,
        _4746,
        _4749,
        _4752,
        _4759,
        _4768,
        _4771,
        _4778,
        _4780,
        _4786,
        _4788,
        _4791,
        _4794,
        _4797,
        _4806,
        _4815,
        _4818,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses.reporting import (
        _4831,
    )
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2802,
    )
    from mastapy._private.system_model.connections_and_sockets import _2338

    Self = TypeVar("Self", bound="ConnectionModalAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="ConnectionModalAnalysis._Cast_ConnectionModalAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionModalAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ConnectionModalAnalysis:
    """Special nested class for casting ConnectionModalAnalysis to subclasses."""

    __parent__: "ConnectionModalAnalysis"

    @property
    def connection_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7702.ConnectionStaticLoadAnalysisCase":
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
    def abstract_shaft_to_mountable_component_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4678.AbstractShaftToMountableComponentConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4678,
        )

        return self.__parent__._cast(
            _4678.AbstractShaftToMountableComponentConnectionModalAnalysis
        )

    @property
    def agma_gleason_conical_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4679.AGMAGleasonConicalGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4679,
        )

        return self.__parent__._cast(_4679.AGMAGleasonConicalGearMeshModalAnalysis)

    @property
    def belt_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4684.BeltConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4684,
        )

        return self.__parent__._cast(_4684.BeltConnectionModalAnalysis)

    @property
    def bevel_differential_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4686.BevelDifferentialGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4686,
        )

        return self.__parent__._cast(_4686.BevelDifferentialGearMeshModalAnalysis)

    @property
    def bevel_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4691.BevelGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4691,
        )

        return self.__parent__._cast(_4691.BevelGearMeshModalAnalysis)

    @property
    def clutch_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4696.ClutchConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4696,
        )

        return self.__parent__._cast(_4696.ClutchConnectionModalAnalysis)

    @property
    def coaxial_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4699.CoaxialConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4699,
        )

        return self.__parent__._cast(_4699.CoaxialConnectionModalAnalysis)

    @property
    def concept_coupling_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4701.ConceptCouplingConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4701,
        )

        return self.__parent__._cast(_4701.ConceptCouplingConnectionModalAnalysis)

    @property
    def concept_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4704.ConceptGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4704,
        )

        return self.__parent__._cast(_4704.ConceptGearMeshModalAnalysis)

    @property
    def conical_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4707.ConicalGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4707,
        )

        return self.__parent__._cast(_4707.ConicalGearMeshModalAnalysis)

    @property
    def coupling_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4713.CouplingConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4713,
        )

        return self.__parent__._cast(_4713.CouplingConnectionModalAnalysis)

    @property
    def cvt_belt_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4716.CVTBeltConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4716,
        )

        return self.__parent__._cast(_4716.CVTBeltConnectionModalAnalysis)

    @property
    def cycloidal_disc_central_bearing_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4720.CycloidalDiscCentralBearingConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4720,
        )

        return self.__parent__._cast(
            _4720.CycloidalDiscCentralBearingConnectionModalAnalysis
        )

    @property
    def cycloidal_disc_planetary_bearing_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4722.CycloidalDiscPlanetaryBearingConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4722,
        )

        return self.__parent__._cast(
            _4722.CycloidalDiscPlanetaryBearingConnectionModalAnalysis
        )

    @property
    def cylindrical_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4723.CylindricalGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4723,
        )

        return self.__parent__._cast(_4723.CylindricalGearMeshModalAnalysis)

    @property
    def face_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4732.FaceGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4732,
        )

        return self.__parent__._cast(_4732.FaceGearMeshModalAnalysis)

    @property
    def gear_mesh_modal_analysis(self: "CastSelf") -> "_4738.GearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4738,
        )

        return self.__parent__._cast(_4738.GearMeshModalAnalysis)

    @property
    def hypoid_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4742.HypoidGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4742,
        )

        return self.__parent__._cast(_4742.HypoidGearMeshModalAnalysis)

    @property
    def inter_mountable_component_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4745.InterMountableComponentConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4745,
        )

        return self.__parent__._cast(
            _4745.InterMountableComponentConnectionModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4746.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4746,
        )

        return self.__parent__._cast(
            _4746.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4749.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4749,
        )

        return self.__parent__._cast(
            _4749.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4752.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4752,
        )

        return self.__parent__._cast(
            _4752.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
        )

    @property
    def part_to_part_shear_coupling_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4768.PartToPartShearCouplingConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4768,
        )

        return self.__parent__._cast(
            _4768.PartToPartShearCouplingConnectionModalAnalysis
        )

    @property
    def planetary_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4771.PlanetaryConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4771,
        )

        return self.__parent__._cast(_4771.PlanetaryConnectionModalAnalysis)

    @property
    def ring_pins_to_disc_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4778.RingPinsToDiscConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4778,
        )

        return self.__parent__._cast(_4778.RingPinsToDiscConnectionModalAnalysis)

    @property
    def rolling_ring_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4780.RollingRingConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4780,
        )

        return self.__parent__._cast(_4780.RollingRingConnectionModalAnalysis)

    @property
    def shaft_to_mountable_component_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4786.ShaftToMountableComponentConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4786,
        )

        return self.__parent__._cast(
            _4786.ShaftToMountableComponentConnectionModalAnalysis
        )

    @property
    def spiral_bevel_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4788.SpiralBevelGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4788,
        )

        return self.__parent__._cast(_4788.SpiralBevelGearMeshModalAnalysis)

    @property
    def spring_damper_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4791.SpringDamperConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4791,
        )

        return self.__parent__._cast(_4791.SpringDamperConnectionModalAnalysis)

    @property
    def straight_bevel_diff_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4794.StraightBevelDiffGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4794,
        )

        return self.__parent__._cast(_4794.StraightBevelDiffGearMeshModalAnalysis)

    @property
    def straight_bevel_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4797.StraightBevelGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4797,
        )

        return self.__parent__._cast(_4797.StraightBevelGearMeshModalAnalysis)

    @property
    def torque_converter_connection_modal_analysis(
        self: "CastSelf",
    ) -> "_4806.TorqueConverterConnectionModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4806,
        )

        return self.__parent__._cast(_4806.TorqueConverterConnectionModalAnalysis)

    @property
    def worm_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4815.WormGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4815,
        )

        return self.__parent__._cast(_4815.WormGearMeshModalAnalysis)

    @property
    def zerol_bevel_gear_mesh_modal_analysis(
        self: "CastSelf",
    ) -> "_4818.ZerolBevelGearMeshModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses import (
            _4818,
        )

        return self.__parent__._cast(_4818.ZerolBevelGearMeshModalAnalysis)

    @property
    def connection_modal_analysis(self: "CastSelf") -> "ConnectionModalAnalysis":
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
class ConnectionModalAnalysis(_7702.ConnectionStaticLoadAnalysisCase):
    """ConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _CONNECTION_MODAL_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2338.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: "Self") -> "_2338.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConnectionDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis(self: "Self") -> "_4759.ModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ModalAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def excited_modes_summary(
        self: "Self",
    ) -> "List[_4831.SingleExcitationResultsModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.SingleExcitationResultsModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ExcitedModesSummary")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: "Self") -> "_2802.ConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SystemDeflectionResults")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ConnectionModalAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ConnectionModalAnalysis
        """
        return _Cast_ConnectionModalAnalysis(self)
