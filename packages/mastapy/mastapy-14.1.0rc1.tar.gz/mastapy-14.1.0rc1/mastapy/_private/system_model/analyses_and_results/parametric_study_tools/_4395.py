"""AbstractAssemblyParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
    _4494,
)

_ABSTRACT_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "AbstractAssemblyParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7706
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4401,
        _4402,
        _4405,
        _4408,
        _4413,
        _4414,
        _4418,
        _4423,
        _4426,
        _4429,
        _4434,
        _4436,
        _4438,
        _4444,
        _4457,
        _4459,
        _4462,
        _4466,
        _4470,
        _4473,
        _4476,
        _4479,
        _4497,
        _4499,
        _4506,
        _4509,
        _4513,
        _4516,
        _4519,
        _4522,
        _4525,
        _4529,
        _4533,
        _4540,
        _4543,
    )
    from mastapy._private.system_model.part_model import _2501

    Self = TypeVar("Self", bound="AbstractAssemblyParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AbstractAssemblyParametricStudyTool._Cast_AbstractAssemblyParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AbstractAssemblyParametricStudyTool:
    """Special nested class for casting AbstractAssemblyParametricStudyTool to subclasses."""

    __parent__: "AbstractAssemblyParametricStudyTool"

    @property
    def part_parametric_study_tool(self: "CastSelf") -> "_4494.PartParametricStudyTool":
        return self.__parent__._cast(_4494.PartParametricStudyTool)

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
    def agma_gleason_conical_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4401.AGMAGleasonConicalGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4401,
        )

        return self.__parent__._cast(_4401.AGMAGleasonConicalGearSetParametricStudyTool)

    @property
    def assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4402.AssemblyParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4402,
        )

        return self.__parent__._cast(_4402.AssemblyParametricStudyTool)

    @property
    def belt_drive_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4405.BeltDriveParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4405,
        )

        return self.__parent__._cast(_4405.BeltDriveParametricStudyTool)

    @property
    def bevel_differential_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4408.BevelDifferentialGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4408,
        )

        return self.__parent__._cast(_4408.BevelDifferentialGearSetParametricStudyTool)

    @property
    def bevel_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4413.BevelGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4413,
        )

        return self.__parent__._cast(_4413.BevelGearSetParametricStudyTool)

    @property
    def bolted_joint_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4414.BoltedJointParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4414,
        )

        return self.__parent__._cast(_4414.BoltedJointParametricStudyTool)

    @property
    def clutch_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4418.ClutchParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4418,
        )

        return self.__parent__._cast(_4418.ClutchParametricStudyTool)

    @property
    def concept_coupling_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4423.ConceptCouplingParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4423,
        )

        return self.__parent__._cast(_4423.ConceptCouplingParametricStudyTool)

    @property
    def concept_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4426.ConceptGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4426,
        )

        return self.__parent__._cast(_4426.ConceptGearSetParametricStudyTool)

    @property
    def conical_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4429.ConicalGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4429,
        )

        return self.__parent__._cast(_4429.ConicalGearSetParametricStudyTool)

    @property
    def coupling_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4434.CouplingParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4434,
        )

        return self.__parent__._cast(_4434.CouplingParametricStudyTool)

    @property
    def cvt_parametric_study_tool(self: "CastSelf") -> "_4436.CVTParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4436,
        )

        return self.__parent__._cast(_4436.CVTParametricStudyTool)

    @property
    def cycloidal_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4438.CycloidalAssemblyParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4438,
        )

        return self.__parent__._cast(_4438.CycloidalAssemblyParametricStudyTool)

    @property
    def cylindrical_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4444.CylindricalGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4444,
        )

        return self.__parent__._cast(_4444.CylindricalGearSetParametricStudyTool)

    @property
    def face_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4457.FaceGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4457,
        )

        return self.__parent__._cast(_4457.FaceGearSetParametricStudyTool)

    @property
    def flexible_pin_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4459.FlexiblePinAssemblyParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4459,
        )

        return self.__parent__._cast(_4459.FlexiblePinAssemblyParametricStudyTool)

    @property
    def gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4462.GearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4462,
        )

        return self.__parent__._cast(_4462.GearSetParametricStudyTool)

    @property
    def hypoid_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4466.HypoidGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4466,
        )

        return self.__parent__._cast(_4466.HypoidGearSetParametricStudyTool)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4470.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4470,
        )

        return self.__parent__._cast(
            _4470.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4473.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4473,
        )

        return self.__parent__._cast(
            _4473.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4476.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4476,
        )

        return self.__parent__._cast(
            _4476.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
        )

    @property
    def microphone_array_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4479.MicrophoneArrayParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4479,
        )

        return self.__parent__._cast(_4479.MicrophoneArrayParametricStudyTool)

    @property
    def part_to_part_shear_coupling_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4497.PartToPartShearCouplingParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4497,
        )

        return self.__parent__._cast(_4497.PartToPartShearCouplingParametricStudyTool)

    @property
    def planetary_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4499.PlanetaryGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4499,
        )

        return self.__parent__._cast(_4499.PlanetaryGearSetParametricStudyTool)

    @property
    def rolling_ring_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4506.RollingRingAssemblyParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4506,
        )

        return self.__parent__._cast(_4506.RollingRingAssemblyParametricStudyTool)

    @property
    def root_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4509.RootAssemblyParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4509,
        )

        return self.__parent__._cast(_4509.RootAssemblyParametricStudyTool)

    @property
    def specialised_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4513.SpecialisedAssemblyParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4513,
        )

        return self.__parent__._cast(_4513.SpecialisedAssemblyParametricStudyTool)

    @property
    def spiral_bevel_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4516.SpiralBevelGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4516,
        )

        return self.__parent__._cast(_4516.SpiralBevelGearSetParametricStudyTool)

    @property
    def spring_damper_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4519.SpringDamperParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4519,
        )

        return self.__parent__._cast(_4519.SpringDamperParametricStudyTool)

    @property
    def straight_bevel_diff_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4522.StraightBevelDiffGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4522,
        )

        return self.__parent__._cast(_4522.StraightBevelDiffGearSetParametricStudyTool)

    @property
    def straight_bevel_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4525.StraightBevelGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4525,
        )

        return self.__parent__._cast(_4525.StraightBevelGearSetParametricStudyTool)

    @property
    def synchroniser_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4529.SynchroniserParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4529,
        )

        return self.__parent__._cast(_4529.SynchroniserParametricStudyTool)

    @property
    def torque_converter_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4533.TorqueConverterParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4533,
        )

        return self.__parent__._cast(_4533.TorqueConverterParametricStudyTool)

    @property
    def worm_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4540.WormGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4540,
        )

        return self.__parent__._cast(_4540.WormGearSetParametricStudyTool)

    @property
    def zerol_bevel_gear_set_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4543.ZerolBevelGearSetParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
            _4543,
        )

        return self.__parent__._cast(_4543.ZerolBevelGearSetParametricStudyTool)

    @property
    def abstract_assembly_parametric_study_tool(
        self: "CastSelf",
    ) -> "AbstractAssemblyParametricStudyTool":
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
class AbstractAssemblyParametricStudyTool(_4494.PartParametricStudyTool):
    """AbstractAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ABSTRACT_ASSEMBLY_PARAMETRIC_STUDY_TOOL

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
    def cast_to(self: "Self") -> "_Cast_AbstractAssemblyParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_AbstractAssemblyParametricStudyTool
        """
        return _Cast_AbstractAssemblyParametricStudyTool(self)
