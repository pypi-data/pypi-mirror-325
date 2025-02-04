"""InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6170,
)

_INTER_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2724, _2726, _2728
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7699,
        _7702,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6140,
        _6144,
        _6147,
        _6152,
        _6156,
        _6161,
        _6165,
        _6168,
        _6172,
        _6175,
        _6183,
        _6189,
        _6194,
        _6199,
        _6203,
        _6206,
        _6209,
        _6219,
        _6229,
        _6231,
        _6239,
        _6241,
        _6245,
        _6248,
        _6256,
        _6263,
        _6266,
    )
    from mastapy._private.system_model.connections_and_sockets import _2347

    Self = TypeVar(
        "Self",
        bound="InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation._Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation:
    """Special nested class for casting InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation to subclasses."""

    __parent__: "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"

    @property
    def connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6170.ConnectionHarmonicAnalysisOfSingleExcitation":
        return self.__parent__._cast(_6170.ConnectionHarmonicAnalysisOfSingleExcitation)

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
    def agma_gleason_conical_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6140.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6140,
        )

        return self.__parent__._cast(
            _6140.AGMAGleasonConicalGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def belt_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6144.BeltConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6144,
        )

        return self.__parent__._cast(
            _6144.BeltConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_differential_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6147.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6147,
        )

        return self.__parent__._cast(
            _6147.BevelDifferentialGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def bevel_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6152.BevelGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6152,
        )

        return self.__parent__._cast(
            _6152.BevelGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def clutch_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6156.ClutchConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6156,
        )

        return self.__parent__._cast(
            _6156.ClutchConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_coupling_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6161.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6161,
        )

        return self.__parent__._cast(
            _6161.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def concept_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6165.ConceptGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6165,
        )

        return self.__parent__._cast(
            _6165.ConceptGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def conical_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6168.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6168,
        )

        return self.__parent__._cast(
            _6168.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def coupling_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6172.CouplingConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6172,
        )

        return self.__parent__._cast(
            _6172.CouplingConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cvt_belt_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6175.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6175,
        )

        return self.__parent__._cast(
            _6175.CVTBeltConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6183.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6183,
        )

        return self.__parent__._cast(
            _6183.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def face_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6189.FaceGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6189,
        )

        return self.__parent__._cast(
            _6189.FaceGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6194.GearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6194,
        )

        return self.__parent__._cast(_6194.GearMeshHarmonicAnalysisOfSingleExcitation)

    @property
    def hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6199.HypoidGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6199,
        )

        return self.__parent__._cast(
            _6199.HypoidGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6203.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6203,
        )

        return self.__parent__._cast(
            _6203.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> (
        "_6206.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation"
    ):
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6206,
        )

        return self.__parent__._cast(
            _6206.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6209.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6209,
        )

        return self.__parent__._cast(
            _6209.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def part_to_part_shear_coupling_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6219.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6219,
        )

        return self.__parent__._cast(
            _6219.PartToPartShearCouplingConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def ring_pins_to_disc_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6229.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6229,
        )

        return self.__parent__._cast(
            _6229.RingPinsToDiscConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def rolling_ring_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6231.RollingRingConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6231,
        )

        return self.__parent__._cast(
            _6231.RollingRingConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spiral_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6239.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6239,
        )

        return self.__parent__._cast(
            _6239.SpiralBevelGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def spring_damper_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6241.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6241,
        )

        return self.__parent__._cast(
            _6241.SpringDamperConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_diff_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6245.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6245,
        )

        return self.__parent__._cast(
            _6245.StraightBevelDiffGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def straight_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6248.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6248,
        )

        return self.__parent__._cast(
            _6248.StraightBevelGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def torque_converter_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6256.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6256,
        )

        return self.__parent__._cast(
            _6256.TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation
        )

    @property
    def worm_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6263.WormGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6263,
        )

        return self.__parent__._cast(
            _6263.WormGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def zerol_bevel_gear_mesh_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "_6266.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
            _6266,
        )

        return self.__parent__._cast(
            _6266.ZerolBevelGearMeshHarmonicAnalysisOfSingleExcitation
        )

    @property
    def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
        self: "CastSelf",
    ) -> "InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
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
class InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
    _6170.ConnectionHarmonicAnalysisOfSingleExcitation
):
    """InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _INTER_MOUNTABLE_COMPONENT_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def connection_design(self: "Self") -> "_2347.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

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
    ) -> "_Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation":
        """Cast to another type.

        Returns:
            _Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
        """
        return (
            _Cast_InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation(
                self
            )
        )
