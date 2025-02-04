"""MountableComponentHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.harmonic_analyses import _5827

_MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "MountableComponentHarmonicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5805,
        _5809,
        _5812,
        _5815,
        _5816,
        _5817,
        _5823,
        _5829,
        _5831,
        _5834,
        _5838,
        _5840,
        _5844,
        _5849,
        _5852,
        _5870,
        _5876,
        _5894,
        _5898,
        _5901,
        _5904,
        _5907,
        _5908,
        _5912,
        _5913,
        _5915,
        _5920,
        _5921,
        _5922,
        _5923,
        _5925,
        _5929,
        _5932,
        _5937,
        _5941,
        _5944,
        _5947,
        _5950,
        _5951,
        _5952,
        _5954,
        _5955,
        _5958,
        _5959,
        _5961,
        _5962,
        _5963,
        _5966,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses import _4763
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2859,
    )
    from mastapy._private.system_model.part_model import _2533

    Self = TypeVar("Self", bound="MountableComponentHarmonicAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="MountableComponentHarmonicAnalysis._Cast_MountableComponentHarmonicAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentHarmonicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_MountableComponentHarmonicAnalysis:
    """Special nested class for casting MountableComponentHarmonicAnalysis to subclasses."""

    __parent__: "MountableComponentHarmonicAnalysis"

    @property
    def component_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5827.ComponentHarmonicAnalysis":
        return self.__parent__._cast(_5827.ComponentHarmonicAnalysis)

    @property
    def part_harmonic_analysis(self: "CastSelf") -> "_5913.PartHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5913,
        )

        return self.__parent__._cast(_5913.PartHarmonicAnalysis)

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
    def agma_gleason_conical_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5805.AGMAGleasonConicalGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5805,
        )

        return self.__parent__._cast(_5805.AGMAGleasonConicalGearHarmonicAnalysis)

    @property
    def bearing_harmonic_analysis(self: "CastSelf") -> "_5809.BearingHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5809,
        )

        return self.__parent__._cast(_5809.BearingHarmonicAnalysis)

    @property
    def bevel_differential_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5812.BevelDifferentialGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5812,
        )

        return self.__parent__._cast(_5812.BevelDifferentialGearHarmonicAnalysis)

    @property
    def bevel_differential_planet_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5815.BevelDifferentialPlanetGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5815,
        )

        return self.__parent__._cast(_5815.BevelDifferentialPlanetGearHarmonicAnalysis)

    @property
    def bevel_differential_sun_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5816.BevelDifferentialSunGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5816,
        )

        return self.__parent__._cast(_5816.BevelDifferentialSunGearHarmonicAnalysis)

    @property
    def bevel_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5817.BevelGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5817,
        )

        return self.__parent__._cast(_5817.BevelGearHarmonicAnalysis)

    @property
    def clutch_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5823.ClutchHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5823,
        )

        return self.__parent__._cast(_5823.ClutchHalfHarmonicAnalysis)

    @property
    def concept_coupling_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5829.ConceptCouplingHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5829,
        )

        return self.__parent__._cast(_5829.ConceptCouplingHalfHarmonicAnalysis)

    @property
    def concept_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5831.ConceptGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5831,
        )

        return self.__parent__._cast(_5831.ConceptGearHarmonicAnalysis)

    @property
    def conical_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5834.ConicalGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5834,
        )

        return self.__parent__._cast(_5834.ConicalGearHarmonicAnalysis)

    @property
    def connector_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5838.ConnectorHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5838,
        )

        return self.__parent__._cast(_5838.ConnectorHarmonicAnalysis)

    @property
    def coupling_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5840.CouplingHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5840,
        )

        return self.__parent__._cast(_5840.CouplingHalfHarmonicAnalysis)

    @property
    def cvt_pulley_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5844.CVTPulleyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5844,
        )

        return self.__parent__._cast(_5844.CVTPulleyHarmonicAnalysis)

    @property
    def cylindrical_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5849.CylindricalGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5849,
        )

        return self.__parent__._cast(_5849.CylindricalGearHarmonicAnalysis)

    @property
    def cylindrical_planet_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5852.CylindricalPlanetGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5852,
        )

        return self.__parent__._cast(_5852.CylindricalPlanetGearHarmonicAnalysis)

    @property
    def face_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5870.FaceGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5870,
        )

        return self.__parent__._cast(_5870.FaceGearHarmonicAnalysis)

    @property
    def gear_harmonic_analysis(self: "CastSelf") -> "_5876.GearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5876,
        )

        return self.__parent__._cast(_5876.GearHarmonicAnalysis)

    @property
    def hypoid_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5894.HypoidGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5894,
        )

        return self.__parent__._cast(_5894.HypoidGearHarmonicAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5898.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5898,
        )

        return self.__parent__._cast(
            _5898.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5901.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5901,
        )

        return self.__parent__._cast(
            _5901.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5904.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5904,
        )

        return self.__parent__._cast(
            _5904.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
        )

    @property
    def mass_disc_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5907.MassDiscHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5907,
        )

        return self.__parent__._cast(_5907.MassDiscHarmonicAnalysis)

    @property
    def measurement_component_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5908.MeasurementComponentHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5908,
        )

        return self.__parent__._cast(_5908.MeasurementComponentHarmonicAnalysis)

    @property
    def oil_seal_harmonic_analysis(self: "CastSelf") -> "_5912.OilSealHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5912,
        )

        return self.__parent__._cast(_5912.OilSealHarmonicAnalysis)

    @property
    def part_to_part_shear_coupling_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5915.PartToPartShearCouplingHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5915,
        )

        return self.__parent__._cast(_5915.PartToPartShearCouplingHalfHarmonicAnalysis)

    @property
    def planet_carrier_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5920.PlanetCarrierHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5920,
        )

        return self.__parent__._cast(_5920.PlanetCarrierHarmonicAnalysis)

    @property
    def point_load_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5921.PointLoadHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5921,
        )

        return self.__parent__._cast(_5921.PointLoadHarmonicAnalysis)

    @property
    def power_load_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5922.PowerLoadHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5922,
        )

        return self.__parent__._cast(_5922.PowerLoadHarmonicAnalysis)

    @property
    def pulley_harmonic_analysis(self: "CastSelf") -> "_5923.PulleyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5923,
        )

        return self.__parent__._cast(_5923.PulleyHarmonicAnalysis)

    @property
    def ring_pins_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5925.RingPinsHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5925,
        )

        return self.__parent__._cast(_5925.RingPinsHarmonicAnalysis)

    @property
    def rolling_ring_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5929.RollingRingHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5929,
        )

        return self.__parent__._cast(_5929.RollingRingHarmonicAnalysis)

    @property
    def shaft_hub_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5932.ShaftHubConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5932,
        )

        return self.__parent__._cast(_5932.ShaftHubConnectionHarmonicAnalysis)

    @property
    def spiral_bevel_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5937.SpiralBevelGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5937,
        )

        return self.__parent__._cast(_5937.SpiralBevelGearHarmonicAnalysis)

    @property
    def spring_damper_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5941.SpringDamperHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5941,
        )

        return self.__parent__._cast(_5941.SpringDamperHalfHarmonicAnalysis)

    @property
    def straight_bevel_diff_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5944.StraightBevelDiffGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5944,
        )

        return self.__parent__._cast(_5944.StraightBevelDiffGearHarmonicAnalysis)

    @property
    def straight_bevel_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5947.StraightBevelGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5947,
        )

        return self.__parent__._cast(_5947.StraightBevelGearHarmonicAnalysis)

    @property
    def straight_bevel_planet_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5950.StraightBevelPlanetGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5950,
        )

        return self.__parent__._cast(_5950.StraightBevelPlanetGearHarmonicAnalysis)

    @property
    def straight_bevel_sun_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5951.StraightBevelSunGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5951,
        )

        return self.__parent__._cast(_5951.StraightBevelSunGearHarmonicAnalysis)

    @property
    def synchroniser_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5952.SynchroniserHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5952,
        )

        return self.__parent__._cast(_5952.SynchroniserHalfHarmonicAnalysis)

    @property
    def synchroniser_part_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5954.SynchroniserPartHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5954,
        )

        return self.__parent__._cast(_5954.SynchroniserPartHarmonicAnalysis)

    @property
    def synchroniser_sleeve_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5955.SynchroniserSleeveHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5955,
        )

        return self.__parent__._cast(_5955.SynchroniserSleeveHarmonicAnalysis)

    @property
    def torque_converter_pump_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5958.TorqueConverterPumpHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5958,
        )

        return self.__parent__._cast(_5958.TorqueConverterPumpHarmonicAnalysis)

    @property
    def torque_converter_turbine_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5959.TorqueConverterTurbineHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5959,
        )

        return self.__parent__._cast(_5959.TorqueConverterTurbineHarmonicAnalysis)

    @property
    def unbalanced_mass_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5961.UnbalancedMassHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5961,
        )

        return self.__parent__._cast(_5961.UnbalancedMassHarmonicAnalysis)

    @property
    def virtual_component_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5962.VirtualComponentHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5962,
        )

        return self.__parent__._cast(_5962.VirtualComponentHarmonicAnalysis)

    @property
    def worm_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5963.WormGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5963,
        )

        return self.__parent__._cast(_5963.WormGearHarmonicAnalysis)

    @property
    def zerol_bevel_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5966.ZerolBevelGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5966,
        )

        return self.__parent__._cast(_5966.ZerolBevelGearHarmonicAnalysis)

    @property
    def mountable_component_harmonic_analysis(
        self: "CastSelf",
    ) -> "MountableComponentHarmonicAnalysis":
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
class MountableComponentHarmonicAnalysis(_5827.ComponentHarmonicAnalysis):
    """MountableComponentHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _MOUNTABLE_COMPONENT_HARMONIC_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2533.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def coupled_modal_analysis(self: "Self") -> "_4763.MountableComponentModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CoupledModalAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: "Self",
    ) -> "_2859.MountableComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SystemDeflectionResults")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_MountableComponentHarmonicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_MountableComponentHarmonicAnalysis
        """
        return _Cast_MountableComponentHarmonicAnalysis(self)
