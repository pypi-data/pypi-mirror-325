"""FaceGearSetCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
    _5709,
)

_FACE_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "FaceGearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5550
    from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
        _5649,
        _5702,
        _5703,
        _5730,
        _5749,
    )
    from mastapy._private.system_model.part_model.gears import _2601

    Self = TypeVar("Self", bound="FaceGearSetCompoundMultibodyDynamicsAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="FaceGearSetCompoundMultibodyDynamicsAnalysis._Cast_FaceGearSetCompoundMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetCompoundMultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_FaceGearSetCompoundMultibodyDynamicsAnalysis:
    """Special nested class for casting FaceGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "FaceGearSetCompoundMultibodyDynamicsAnalysis"

    @property
    def gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5709.GearSetCompoundMultibodyDynamicsAnalysis":
        return self.__parent__._cast(_5709.GearSetCompoundMultibodyDynamicsAnalysis)

    @property
    def specialised_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5749.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5749,
        )

        return self.__parent__._cast(
            _5749.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def abstract_assembly_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5649.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5649,
        )

        return self.__parent__._cast(
            _5649.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
        )

    @property
    def part_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5730.PartCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5730,
        )

        return self.__parent__._cast(_5730.PartCompoundMultibodyDynamicsAnalysis)

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7707.PartCompoundAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7707,
        )

        return self.__parent__._cast(_7707.PartCompoundAnalysis)

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
    def face_gear_set_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "FaceGearSetCompoundMultibodyDynamicsAnalysis":
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
class FaceGearSetCompoundMultibodyDynamicsAnalysis(
    _5709.GearSetCompoundMultibodyDynamicsAnalysis
):
    """FaceGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _FACE_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2601.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: "Self") -> "_2601.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: "Self",
    ) -> "List[_5550.FaceGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.FaceGearSetMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gears_compound_multibody_dynamics_analysis(
        self: "Self",
    ) -> "List[_5702.FaceGearCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "FaceGearsCompoundMultibodyDynamicsAnalysis"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_compound_multibody_dynamics_analysis(
        self: "Self",
    ) -> "List[_5703.FaceGearMeshCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.FaceGearMeshCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "FaceMeshesCompoundMultibodyDynamicsAnalysis"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: "Self",
    ) -> "List[_5550.FaceGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.FaceGearSetMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_FaceGearSetCompoundMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_FaceGearSetCompoundMultibodyDynamicsAnalysis
        """
        return _Cast_FaceGearSetCompoundMultibodyDynamicsAnalysis(self)
