"""AGMAGleasonConicalGearSetSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.system_deflections import _2800

_AGMA_GLEASON_CONICAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AGMAGleasonConicalGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7708,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import _4133
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2760,
        _2764,
        _2766,
        _2777,
        _2782,
        _2835,
        _2839,
        _2862,
        _2883,
        _2885,
        _2891,
        _2894,
        _2917,
    )
    from mastapy._private.system_model.part_model.gears import _2586

    Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AGMAGleasonConicalGearSetSystemDeflection:
    """Special nested class for casting AGMAGleasonConicalGearSetSystemDeflection to subclasses."""

    __parent__: "AGMAGleasonConicalGearSetSystemDeflection"

    @property
    def conical_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2800.ConicalGearSetSystemDeflection":
        return self.__parent__._cast(_2800.ConicalGearSetSystemDeflection)

    @property
    def gear_set_system_deflection(self: "CastSelf") -> "_2835.GearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2835,
        )

        return self.__parent__._cast(_2835.GearSetSystemDeflection)

    @property
    def specialised_assembly_system_deflection(
        self: "CastSelf",
    ) -> "_2883.SpecialisedAssemblySystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2883,
        )

        return self.__parent__._cast(_2883.SpecialisedAssemblySystemDeflection)

    @property
    def abstract_assembly_system_deflection(
        self: "CastSelf",
    ) -> "_2760.AbstractAssemblySystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2760,
        )

        return self.__parent__._cast(_2760.AbstractAssemblySystemDeflection)

    @property
    def part_system_deflection(self: "CastSelf") -> "_2862.PartSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2862,
        )

        return self.__parent__._cast(_2862.PartSystemDeflection)

    @property
    def part_fe_analysis(self: "CastSelf") -> "_7708.PartFEAnalysis":
        from mastapy._private.system_model.analyses_and_results.analysis_cases import (
            _7708,
        )

        return self.__parent__._cast(_7708.PartFEAnalysis)

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
    def bevel_differential_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2777.BevelDifferentialGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2777,
        )

        return self.__parent__._cast(_2777.BevelDifferentialGearSetSystemDeflection)

    @property
    def bevel_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2782.BevelGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2782,
        )

        return self.__parent__._cast(_2782.BevelGearSetSystemDeflection)

    @property
    def hypoid_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2839.HypoidGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2839,
        )

        return self.__parent__._cast(_2839.HypoidGearSetSystemDeflection)

    @property
    def spiral_bevel_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2885.SpiralBevelGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2885,
        )

        return self.__parent__._cast(_2885.SpiralBevelGearSetSystemDeflection)

    @property
    def straight_bevel_diff_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2891.StraightBevelDiffGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2891,
        )

        return self.__parent__._cast(_2891.StraightBevelDiffGearSetSystemDeflection)

    @property
    def straight_bevel_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2894.StraightBevelGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2894,
        )

        return self.__parent__._cast(_2894.StraightBevelGearSetSystemDeflection)

    @property
    def zerol_bevel_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "_2917.ZerolBevelGearSetSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.system_deflections import (
            _2917,
        )

        return self.__parent__._cast(_2917.ZerolBevelGearSetSystemDeflection)

    @property
    def agma_gleason_conical_gear_set_system_deflection(
        self: "CastSelf",
    ) -> "AGMAGleasonConicalGearSetSystemDeflection":
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
class AGMAGleasonConicalGearSetSystemDeflection(_2800.ConicalGearSetSystemDeflection):
    """AGMAGleasonConicalGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _AGMA_GLEASON_CONICAL_GEAR_SET_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def assembly_design(self: "Self") -> "_2586.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gears_system_deflection(
        self: "Self",
    ) -> "List[_2766.AGMAGleasonConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConicalGearsSystemDeflection")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_gears_system_deflection(
        self: "Self",
    ) -> "List[_2766.AGMAGleasonConicalGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "AGMAGleasonConicalGearsSystemDeflection"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_system_deflection(
        self: "Self",
    ) -> "List[_2764.AGMAGleasonConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConicalMeshesSystemDeflection")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_system_deflection(
        self: "Self",
    ) -> "List[_2764.AGMAGleasonConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "AGMAGleasonConicalMeshesSystemDeflection"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: "Self") -> "_4133.AGMAGleasonConicalGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "PowerFlowResults")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_AGMAGleasonConicalGearSetSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_AGMAGleasonConicalGearSetSystemDeflection
        """
        return _Cast_AGMAGleasonConicalGearSetSystemDeflection(self)
