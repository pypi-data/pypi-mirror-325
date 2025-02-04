"""ComponentCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
    _6762,
)

_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ComponentCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7706,
        _7709,
    )
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6679,
        _6680,
        _6682,
        _6686,
        _6689,
        _6692,
        _6693,
        _6694,
        _6697,
        _6701,
        _6706,
        _6707,
        _6710,
        _6714,
        _6717,
        _6723,
        _6726,
        _6728,
        _6731,
        _6732,
        _6733,
        _6734,
        _6737,
        _6739,
        _6742,
        _6743,
        _6747,
        _6750,
        _6753,
        _6756,
        _6757,
        _6759,
        _6760,
        _6761,
        _6765,
        _6768,
        _6769,
        _6770,
        _6771,
        _6772,
        _6776,
        _6778,
        _6779,
        _6782,
        _6787,
        _6788,
        _6791,
        _6794,
        _6795,
        _6797,
        _6798,
        _6799,
        _6802,
        _6803,
        _6804,
        _6805,
        _6806,
        _6809,
    )
    from mastapy._private.system_model.part_model import _2511

    Self = TypeVar("Self", bound="ComponentCriticalSpeedAnalysis")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ComponentCriticalSpeedAnalysis._Cast_ComponentCriticalSpeedAnalysis",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ComponentCriticalSpeedAnalysis:
    """Special nested class for casting ComponentCriticalSpeedAnalysis to subclasses."""

    __parent__: "ComponentCriticalSpeedAnalysis"

    @property
    def part_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6762.PartCriticalSpeedAnalysis":
        return self.__parent__._cast(_6762.PartCriticalSpeedAnalysis)

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
    def abstract_shaft_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6679.AbstractShaftCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6679,
        )

        return self.__parent__._cast(_6679.AbstractShaftCriticalSpeedAnalysis)

    @property
    def abstract_shaft_or_housing_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6680.AbstractShaftOrHousingCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6680,
        )

        return self.__parent__._cast(_6680.AbstractShaftOrHousingCriticalSpeedAnalysis)

    @property
    def agma_gleason_conical_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6682.AGMAGleasonConicalGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6682,
        )

        return self.__parent__._cast(_6682.AGMAGleasonConicalGearCriticalSpeedAnalysis)

    @property
    def bearing_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6686.BearingCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6686,
        )

        return self.__parent__._cast(_6686.BearingCriticalSpeedAnalysis)

    @property
    def bevel_differential_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6689.BevelDifferentialGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6689,
        )

        return self.__parent__._cast(_6689.BevelDifferentialGearCriticalSpeedAnalysis)

    @property
    def bevel_differential_planet_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6692.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6692,
        )

        return self.__parent__._cast(
            _6692.BevelDifferentialPlanetGearCriticalSpeedAnalysis
        )

    @property
    def bevel_differential_sun_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6693.BevelDifferentialSunGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6693,
        )

        return self.__parent__._cast(
            _6693.BevelDifferentialSunGearCriticalSpeedAnalysis
        )

    @property
    def bevel_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6694.BevelGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6694,
        )

        return self.__parent__._cast(_6694.BevelGearCriticalSpeedAnalysis)

    @property
    def bolt_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6697.BoltCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6697,
        )

        return self.__parent__._cast(_6697.BoltCriticalSpeedAnalysis)

    @property
    def clutch_half_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6701.ClutchHalfCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6701,
        )

        return self.__parent__._cast(_6701.ClutchHalfCriticalSpeedAnalysis)

    @property
    def concept_coupling_half_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6706.ConceptCouplingHalfCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6706,
        )

        return self.__parent__._cast(_6706.ConceptCouplingHalfCriticalSpeedAnalysis)

    @property
    def concept_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6707.ConceptGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6707,
        )

        return self.__parent__._cast(_6707.ConceptGearCriticalSpeedAnalysis)

    @property
    def conical_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6710.ConicalGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6710,
        )

        return self.__parent__._cast(_6710.ConicalGearCriticalSpeedAnalysis)

    @property
    def connector_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6714.ConnectorCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6714,
        )

        return self.__parent__._cast(_6714.ConnectorCriticalSpeedAnalysis)

    @property
    def coupling_half_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6717.CouplingHalfCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6717,
        )

        return self.__parent__._cast(_6717.CouplingHalfCriticalSpeedAnalysis)

    @property
    def cvt_pulley_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6723.CVTPulleyCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6723,
        )

        return self.__parent__._cast(_6723.CVTPulleyCriticalSpeedAnalysis)

    @property
    def cycloidal_disc_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6726.CycloidalDiscCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6726,
        )

        return self.__parent__._cast(_6726.CycloidalDiscCriticalSpeedAnalysis)

    @property
    def cylindrical_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6728.CylindricalGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6728,
        )

        return self.__parent__._cast(_6728.CylindricalGearCriticalSpeedAnalysis)

    @property
    def cylindrical_planet_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6731.CylindricalPlanetGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6731,
        )

        return self.__parent__._cast(_6731.CylindricalPlanetGearCriticalSpeedAnalysis)

    @property
    def datum_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6732.DatumCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6732,
        )

        return self.__parent__._cast(_6732.DatumCriticalSpeedAnalysis)

    @property
    def external_cad_model_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6733.ExternalCADModelCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6733,
        )

        return self.__parent__._cast(_6733.ExternalCADModelCriticalSpeedAnalysis)

    @property
    def face_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6734.FaceGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6734,
        )

        return self.__parent__._cast(_6734.FaceGearCriticalSpeedAnalysis)

    @property
    def fe_part_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6737.FEPartCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6737,
        )

        return self.__parent__._cast(_6737.FEPartCriticalSpeedAnalysis)

    @property
    def gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6739.GearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6739,
        )

        return self.__parent__._cast(_6739.GearCriticalSpeedAnalysis)

    @property
    def guide_dxf_model_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6742.GuideDxfModelCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6742,
        )

        return self.__parent__._cast(_6742.GuideDxfModelCriticalSpeedAnalysis)

    @property
    def hypoid_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6743.HypoidGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6743,
        )

        return self.__parent__._cast(_6743.HypoidGearCriticalSpeedAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6747.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6747,
        )

        return self.__parent__._cast(
            _6747.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6750.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6750,
        )

        return self.__parent__._cast(
            _6750.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6753.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6753,
        )

        return self.__parent__._cast(
            _6753.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
        )

    @property
    def mass_disc_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6756.MassDiscCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6756,
        )

        return self.__parent__._cast(_6756.MassDiscCriticalSpeedAnalysis)

    @property
    def measurement_component_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6757.MeasurementComponentCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6757,
        )

        return self.__parent__._cast(_6757.MeasurementComponentCriticalSpeedAnalysis)

    @property
    def microphone_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6759.MicrophoneCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6759,
        )

        return self.__parent__._cast(_6759.MicrophoneCriticalSpeedAnalysis)

    @property
    def mountable_component_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6760.MountableComponentCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6760,
        )

        return self.__parent__._cast(_6760.MountableComponentCriticalSpeedAnalysis)

    @property
    def oil_seal_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6761.OilSealCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6761,
        )

        return self.__parent__._cast(_6761.OilSealCriticalSpeedAnalysis)

    @property
    def part_to_part_shear_coupling_half_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6765.PartToPartShearCouplingHalfCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6765,
        )

        return self.__parent__._cast(
            _6765.PartToPartShearCouplingHalfCriticalSpeedAnalysis
        )

    @property
    def planet_carrier_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6768.PlanetCarrierCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6768,
        )

        return self.__parent__._cast(_6768.PlanetCarrierCriticalSpeedAnalysis)

    @property
    def point_load_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6769.PointLoadCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6769,
        )

        return self.__parent__._cast(_6769.PointLoadCriticalSpeedAnalysis)

    @property
    def power_load_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6770.PowerLoadCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6770,
        )

        return self.__parent__._cast(_6770.PowerLoadCriticalSpeedAnalysis)

    @property
    def pulley_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6771.PulleyCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6771,
        )

        return self.__parent__._cast(_6771.PulleyCriticalSpeedAnalysis)

    @property
    def ring_pins_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6772.RingPinsCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6772,
        )

        return self.__parent__._cast(_6772.RingPinsCriticalSpeedAnalysis)

    @property
    def rolling_ring_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6776.RollingRingCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6776,
        )

        return self.__parent__._cast(_6776.RollingRingCriticalSpeedAnalysis)

    @property
    def shaft_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6778.ShaftCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6778,
        )

        return self.__parent__._cast(_6778.ShaftCriticalSpeedAnalysis)

    @property
    def shaft_hub_connection_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6779.ShaftHubConnectionCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6779,
        )

        return self.__parent__._cast(_6779.ShaftHubConnectionCriticalSpeedAnalysis)

    @property
    def spiral_bevel_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6782.SpiralBevelGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6782,
        )

        return self.__parent__._cast(_6782.SpiralBevelGearCriticalSpeedAnalysis)

    @property
    def spring_damper_half_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6787.SpringDamperHalfCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6787,
        )

        return self.__parent__._cast(_6787.SpringDamperHalfCriticalSpeedAnalysis)

    @property
    def straight_bevel_diff_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6788.StraightBevelDiffGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6788,
        )

        return self.__parent__._cast(_6788.StraightBevelDiffGearCriticalSpeedAnalysis)

    @property
    def straight_bevel_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6791.StraightBevelGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6791,
        )

        return self.__parent__._cast(_6791.StraightBevelGearCriticalSpeedAnalysis)

    @property
    def straight_bevel_planet_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6794.StraightBevelPlanetGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6794,
        )

        return self.__parent__._cast(_6794.StraightBevelPlanetGearCriticalSpeedAnalysis)

    @property
    def straight_bevel_sun_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6795.StraightBevelSunGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6795,
        )

        return self.__parent__._cast(_6795.StraightBevelSunGearCriticalSpeedAnalysis)

    @property
    def synchroniser_half_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6797.SynchroniserHalfCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6797,
        )

        return self.__parent__._cast(_6797.SynchroniserHalfCriticalSpeedAnalysis)

    @property
    def synchroniser_part_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6798.SynchroniserPartCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6798,
        )

        return self.__parent__._cast(_6798.SynchroniserPartCriticalSpeedAnalysis)

    @property
    def synchroniser_sleeve_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6799.SynchroniserSleeveCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6799,
        )

        return self.__parent__._cast(_6799.SynchroniserSleeveCriticalSpeedAnalysis)

    @property
    def torque_converter_pump_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6802.TorqueConverterPumpCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6802,
        )

        return self.__parent__._cast(_6802.TorqueConverterPumpCriticalSpeedAnalysis)

    @property
    def torque_converter_turbine_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6803.TorqueConverterTurbineCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6803,
        )

        return self.__parent__._cast(_6803.TorqueConverterTurbineCriticalSpeedAnalysis)

    @property
    def unbalanced_mass_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6804.UnbalancedMassCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6804,
        )

        return self.__parent__._cast(_6804.UnbalancedMassCriticalSpeedAnalysis)

    @property
    def virtual_component_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6805.VirtualComponentCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6805,
        )

        return self.__parent__._cast(_6805.VirtualComponentCriticalSpeedAnalysis)

    @property
    def worm_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6806.WormGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6806,
        )

        return self.__parent__._cast(_6806.WormGearCriticalSpeedAnalysis)

    @property
    def zerol_bevel_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6809.ZerolBevelGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6809,
        )

        return self.__parent__._cast(_6809.ZerolBevelGearCriticalSpeedAnalysis)

    @property
    def component_critical_speed_analysis(
        self: "CastSelf",
    ) -> "ComponentCriticalSpeedAnalysis":
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
class ComponentCriticalSpeedAnalysis(_6762.PartCriticalSpeedAnalysis):
    """ComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPONENT_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2511.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: "Self") -> "_Cast_ComponentCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_ComponentCriticalSpeedAnalysis
        """
        return _Cast_ComponentCriticalSpeedAnalysis(self)
