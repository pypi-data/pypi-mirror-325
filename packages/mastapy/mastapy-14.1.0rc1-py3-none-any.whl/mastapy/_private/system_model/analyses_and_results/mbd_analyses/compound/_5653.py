"""AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
    _5681,
)

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.mbd_analyses import _5496
    from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
        _5660,
        _5663,
        _5664,
        _5665,
        _5674,
        _5707,
        _5711,
        _5728,
        _5730,
        _5750,
        _5756,
        _5759,
        _5762,
        _5763,
        _5777,
    )

    Self = TypeVar(
        "Self", bound="AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis:
    """Special nested class for casting AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis to subclasses."""

    __parent__: "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis"

    @property
    def conical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5681.ConicalGearCompoundMultibodyDynamicsAnalysis":
        return self.__parent__._cast(_5681.ConicalGearCompoundMultibodyDynamicsAnalysis)

    @property
    def gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5707.GearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5707,
        )

        return self.__parent__._cast(_5707.GearCompoundMultibodyDynamicsAnalysis)

    @property
    def mountable_component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5728.MountableComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5728,
        )

        return self.__parent__._cast(
            _5728.MountableComponentCompoundMultibodyDynamicsAnalysis
        )

    @property
    def component_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5674.ComponentCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5674,
        )

        return self.__parent__._cast(_5674.ComponentCompoundMultibodyDynamicsAnalysis)

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
    def bevel_differential_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5660.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5660,
        )

        return self.__parent__._cast(
            _5660.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5663.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5663,
        )

        return self.__parent__._cast(
            _5663.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5664.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5664,
        )

        return self.__parent__._cast(
            _5664.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5665.BevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5665,
        )

        return self.__parent__._cast(_5665.BevelGearCompoundMultibodyDynamicsAnalysis)

    @property
    def hypoid_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5711.HypoidGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5711,
        )

        return self.__parent__._cast(_5711.HypoidGearCompoundMultibodyDynamicsAnalysis)

    @property
    def spiral_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5750.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5750,
        )

        return self.__parent__._cast(
            _5750.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5756.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5756,
        )

        return self.__parent__._cast(
            _5756.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5759.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5759,
        )

        return self.__parent__._cast(
            _5759.StraightBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5762.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5762,
        )

        return self.__parent__._cast(
            _5762.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5763.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5763,
        )

        return self.__parent__._cast(
            _5763.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def zerol_bevel_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "_5777.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
        from mastapy._private.system_model.analyses_and_results.mbd_analyses.compound import (
            _5777,
        )

        return self.__parent__._cast(
            _5777.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
        )

    @property
    def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
        self: "CastSelf",
    ) -> "AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
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
class AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis(
    _5681.ConicalGearCompoundMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    )

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_5496.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: "Self",
    ) -> "List[_5496.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AGMAGleasonConicalGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: "Self",
    ) -> "_Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
        """Cast to another type.

        Returns:
            _Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
        """
        return _Cast_AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis(self)
