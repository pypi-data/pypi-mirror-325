"""AbstractAssemblySteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3144,
)

_ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "AbstractAssemblySteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3067,
        _3069,
        _3072,
        _3074,
        _3079,
        _3081,
        _3085,
        _3090,
        _3092,
        _3095,
        _3101,
        _3104,
        _3105,
        _3110,
        _3117,
        _3120,
        _3122,
        _3126,
        _3130,
        _3133,
        _3136,
        _3140,
        _3147,
        _3149,
        _3156,
        _3159,
        _3163,
        _3165,
        _3169,
        _3174,
        _3177,
        _3184,
        _3187,
        _3192,
        _3195,
    )
    from mastapy._private.system_model.part_model import _2501

    Self = TypeVar("Self", bound="AbstractAssemblySteadyStateSynchronousResponse")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractAssemblySteadyStateSynchronousResponse._Cast_AbstractAssemblySteadyStateSynchronousResponse",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblySteadyStateSynchronousResponse",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractAssemblySteadyStateSynchronousResponse:
    """Special nested class for casting AbstractAssemblySteadyStateSynchronousResponse to subclasses."""

    __parent__: "AbstractAssemblySteadyStateSynchronousResponse"

    @property
    def part_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3144.PartSteadyStateSynchronousResponse":
        return self.__parent__._cast(_3144.PartSteadyStateSynchronousResponse)

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7709.PartStaticLoadAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7709,
        )

        return self.__parent__._cast(_7709.PartStaticLoadAnalysisCase)

    @property
    def part_analysis_case(self: "CastSelf") -> "_7706.PartAnalysisCase":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7706,
        )

        return self.__parent__._cast(_7706.PartAnalysisCase)

    @property
    def part_analysis(self: "CastSelf") -> "_2732.PartAnalysis":
        from mastapy._private.system_model.analyses_and_results import _2732

        return self.__parent__._cast(_2732.PartAnalysis)

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
    def agma_gleason_conical_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3067.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3067,
        )

        return self.__parent__._cast(
            _3067.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
        )

    @property
    def assembly_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3069.AssemblySteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3069,
        )

        return self.__parent__._cast(_3069.AssemblySteadyStateSynchronousResponse)

    @property
    def belt_drive_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3072.BeltDriveSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3072,
        )

        return self.__parent__._cast(_3072.BeltDriveSteadyStateSynchronousResponse)

    @property
    def bevel_differential_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3074.BevelDifferentialGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3074,
        )

        return self.__parent__._cast(
            _3074.BevelDifferentialGearSetSteadyStateSynchronousResponse
        )

    @property
    def bevel_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3079.BevelGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3079,
        )

        return self.__parent__._cast(_3079.BevelGearSetSteadyStateSynchronousResponse)

    @property
    def bolted_joint_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3081.BoltedJointSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3081,
        )

        return self.__parent__._cast(_3081.BoltedJointSteadyStateSynchronousResponse)

    @property
    def clutch_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3085.ClutchSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3085,
        )

        return self.__parent__._cast(_3085.ClutchSteadyStateSynchronousResponse)

    @property
    def concept_coupling_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3090.ConceptCouplingSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3090,
        )

        return self.__parent__._cast(
            _3090.ConceptCouplingSteadyStateSynchronousResponse
        )

    @property
    def concept_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3092.ConceptGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3092,
        )

        return self.__parent__._cast(_3092.ConceptGearSetSteadyStateSynchronousResponse)

    @property
    def conical_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3095.ConicalGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3095,
        )

        return self.__parent__._cast(_3095.ConicalGearSetSteadyStateSynchronousResponse)

    @property
    def coupling_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3101.CouplingSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3101,
        )

        return self.__parent__._cast(_3101.CouplingSteadyStateSynchronousResponse)

    @property
    def cvt_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3104.CVTSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3104,
        )

        return self.__parent__._cast(_3104.CVTSteadyStateSynchronousResponse)

    @property
    def cycloidal_assembly_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3105.CycloidalAssemblySteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3105,
        )

        return self.__parent__._cast(
            _3105.CycloidalAssemblySteadyStateSynchronousResponse
        )

    @property
    def cylindrical_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3110.CylindricalGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3110,
        )

        return self.__parent__._cast(
            _3110.CylindricalGearSetSteadyStateSynchronousResponse
        )

    @property
    def face_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3117.FaceGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3117,
        )

        return self.__parent__._cast(_3117.FaceGearSetSteadyStateSynchronousResponse)

    @property
    def flexible_pin_assembly_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3120.FlexiblePinAssemblySteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3120,
        )

        return self.__parent__._cast(
            _3120.FlexiblePinAssemblySteadyStateSynchronousResponse
        )

    @property
    def gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3122.GearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3122,
        )

        return self.__parent__._cast(_3122.GearSetSteadyStateSynchronousResponse)

    @property
    def hypoid_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3126.HypoidGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3126,
        )

        return self.__parent__._cast(_3126.HypoidGearSetSteadyStateSynchronousResponse)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3130.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3130,
        )

        return self.__parent__._cast(
            _3130.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3133.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3133,
        )

        return self.__parent__._cast(
            _3133.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> (
        "_3136.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse"
    ):
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3136,
        )

        return self.__parent__._cast(
            _3136.KlingelnbergCycloPalloidSpiralBevelGearSetSteadyStateSynchronousResponse
        )

    @property
    def microphone_array_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3140.MicrophoneArraySteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3140,
        )

        return self.__parent__._cast(
            _3140.MicrophoneArraySteadyStateSynchronousResponse
        )

    @property
    def part_to_part_shear_coupling_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3147.PartToPartShearCouplingSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3147,
        )

        return self.__parent__._cast(
            _3147.PartToPartShearCouplingSteadyStateSynchronousResponse
        )

    @property
    def planetary_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3149.PlanetaryGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3149,
        )

        return self.__parent__._cast(
            _3149.PlanetaryGearSetSteadyStateSynchronousResponse
        )

    @property
    def rolling_ring_assembly_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3156.RollingRingAssemblySteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3156,
        )

        return self.__parent__._cast(
            _3156.RollingRingAssemblySteadyStateSynchronousResponse
        )

    @property
    def root_assembly_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3159.RootAssemblySteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3159,
        )

        return self.__parent__._cast(_3159.RootAssemblySteadyStateSynchronousResponse)

    @property
    def specialised_assembly_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3163.SpecialisedAssemblySteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3163,
        )

        return self.__parent__._cast(
            _3163.SpecialisedAssemblySteadyStateSynchronousResponse
        )

    @property
    def spiral_bevel_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3165.SpiralBevelGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3165,
        )

        return self.__parent__._cast(
            _3165.SpiralBevelGearSetSteadyStateSynchronousResponse
        )

    @property
    def spring_damper_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3169.SpringDamperSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3169,
        )

        return self.__parent__._cast(_3169.SpringDamperSteadyStateSynchronousResponse)

    @property
    def straight_bevel_diff_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3174.StraightBevelDiffGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3174,
        )

        return self.__parent__._cast(
            _3174.StraightBevelDiffGearSetSteadyStateSynchronousResponse
        )

    @property
    def straight_bevel_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3177.StraightBevelGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3177,
        )

        return self.__parent__._cast(
            _3177.StraightBevelGearSetSteadyStateSynchronousResponse
        )

    @property
    def synchroniser_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3184.SynchroniserSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3184,
        )

        return self.__parent__._cast(_3184.SynchroniserSteadyStateSynchronousResponse)

    @property
    def torque_converter_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3187.TorqueConverterSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3187,
        )

        return self.__parent__._cast(
            _3187.TorqueConverterSteadyStateSynchronousResponse
        )

    @property
    def worm_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3192.WormGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3192,
        )

        return self.__parent__._cast(_3192.WormGearSetSteadyStateSynchronousResponse)

    @property
    def zerol_bevel_gear_set_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "_3195.ZerolBevelGearSetSteadyStateSynchronousResponse":
        from mastapy._private.system_model.analyses_and_results.steady_state_synchronous_responses import (
            _3195,
        )

        return self.__parent__._cast(
            _3195.ZerolBevelGearSetSteadyStateSynchronousResponse
        )

    @property
    def abstract_assembly_steady_state_synchronous_response(
        self: "CastSelf",
    ) -> "AbstractAssemblySteadyStateSynchronousResponse":
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
class AbstractAssemblySteadyStateSynchronousResponse(
    _3144.PartSteadyStateSynchronousResponse
):
    """AbstractAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2501.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: "Self") -> "_2501.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_AbstractAssemblySteadyStateSynchronousResponse":
        """Cast to another type.

        Returns:
            _Cast_AbstractAssemblySteadyStateSynchronousResponse
        """
        return _Cast_AbstractAssemblySteadyStateSynchronousResponse(self)
