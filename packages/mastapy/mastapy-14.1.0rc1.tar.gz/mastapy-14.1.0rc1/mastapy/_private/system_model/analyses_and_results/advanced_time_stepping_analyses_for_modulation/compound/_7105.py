"""ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7161,
)

_COMPONENT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _6973,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7081,
        _7082,
        _7084,
        _7088,
        _7091,
        _7094,
        _7095,
        _7096,
        _7099,
        _7103,
        _7108,
        _7109,
        _7112,
        _7116,
        _7119,
        _7122,
        _7125,
        _7127,
        _7130,
        _7131,
        _7132,
        _7133,
        _7136,
        _7138,
        _7141,
        _7142,
        _7146,
        _7149,
        _7152,
        _7155,
        _7156,
        _7158,
        _7159,
        _7160,
        _7164,
        _7167,
        _7168,
        _7169,
        _7170,
        _7171,
        _7174,
        _7177,
        _7178,
        _7181,
        _7186,
        _7187,
        _7190,
        _7193,
        _7194,
        _7196,
        _7197,
        _7198,
        _7201,
        _7202,
        _7203,
        _7204,
        _7205,
        _7208,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )

    Self = TypeVar(
        "Self", bound="ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
    )
    CastSelf = TypeVar(
        "CastSelf",
        bound="ComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundAdvancedTimeSteppingAnalysisForModulation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation:
    """Special nested class for casting ComponentCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

    __parent__: "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation"

    @property
    def part_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7161.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self.__parent__._cast(
            _7161.PartCompoundAdvancedTimeSteppingAnalysisForModulation
        )

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
    def abstract_shaft_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7081.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7081,
        )

        return self.__parent__._cast(
            _7081.AbstractShaftCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def abstract_shaft_or_housing_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> (
        "_7082.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7082,
        )

        return self.__parent__._cast(
            _7082.AbstractShaftOrHousingCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> (
        "_7084.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7084,
        )

        return self.__parent__._cast(
            _7084.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bearing_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7088.BearingCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7088,
        )

        return self.__parent__._cast(
            _7088.BearingCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7091.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7091,
        )

        return self.__parent__._cast(
            _7091.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7094.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7094,
        )

        return self.__parent__._cast(
            _7094.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7095.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7095,
        )

        return self.__parent__._cast(
            _7095.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7096.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7096,
        )

        return self.__parent__._cast(
            _7096.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bolt_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7099.BoltCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7099,
        )

        return self.__parent__._cast(
            _7099.BoltCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7103.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7103,
        )

        return self.__parent__._cast(
            _7103.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7108.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7108,
        )

        return self.__parent__._cast(
            _7108.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7109.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7109,
        )

        return self.__parent__._cast(
            _7109.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7112.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7112,
        )

        return self.__parent__._cast(
            _7112.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def connector_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7116.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7116,
        )

        return self.__parent__._cast(
            _7116.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7119.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7119,
        )

        return self.__parent__._cast(
            _7119.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7122.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7122,
        )

        return self.__parent__._cast(
            _7122.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cycloidal_disc_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7125.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7125,
        )

        return self.__parent__._cast(
            _7125.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7127.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7127,
        )

        return self.__parent__._cast(
            _7127.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7130.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7130,
        )

        return self.__parent__._cast(
            _7130.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def datum_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7131.DatumCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7131,
        )

        return self.__parent__._cast(
            _7131.DatumCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def external_cad_model_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7132.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7132,
        )

        return self.__parent__._cast(
            _7132.ExternalCADModelCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def face_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7133.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7133,
        )

        return self.__parent__._cast(
            _7133.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def fe_part_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7136.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7136,
        )

        return self.__parent__._cast(
            _7136.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7138.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7138,
        )

        return self.__parent__._cast(
            _7138.GearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def guide_dxf_model_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7141.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7141,
        )

        return self.__parent__._cast(
            _7141.GuideDxfModelCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7142.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7142,
        )

        return self.__parent__._cast(
            _7142.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7146.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7146,
        )

        return self.__parent__._cast(
            _7146.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7149.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7149,
        )

        return self.__parent__._cast(
            _7149.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7152.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7152,
        )

        return self.__parent__._cast(
            _7152.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def mass_disc_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7155.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7155,
        )

        return self.__parent__._cast(
            _7155.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7156.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7156,
        )

        return self.__parent__._cast(
            _7156.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def microphone_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7158.MicrophoneCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7158,
        )

        return self.__parent__._cast(
            _7158.MicrophoneCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7159.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7159,
        )

        return self.__parent__._cast(
            _7159.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7160.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7160,
        )

        return self.__parent__._cast(
            _7160.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7164.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7164,
        )

        return self.__parent__._cast(
            _7164.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def planet_carrier_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7167.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7167,
        )

        return self.__parent__._cast(
            _7167.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def point_load_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7168.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7168,
        )

        return self.__parent__._cast(
            _7168.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def power_load_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7169.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7169,
        )

        return self.__parent__._cast(
            _7169.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def pulley_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7170.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7170,
        )

        return self.__parent__._cast(
            _7170.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def ring_pins_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7171.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7171,
        )

        return self.__parent__._cast(
            _7171.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7174.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7174,
        )

        return self.__parent__._cast(
            _7174.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def shaft_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7177.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7177,
        )

        return self.__parent__._cast(
            _7177.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def shaft_hub_connection_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7178.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7178,
        )

        return self.__parent__._cast(
            _7178.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7181.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7181,
        )

        return self.__parent__._cast(
            _7181.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7186.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7186,
        )

        return self.__parent__._cast(
            _7186.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7187.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7187,
        )

        return self.__parent__._cast(
            _7187.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7190.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7190,
        )

        return self.__parent__._cast(
            _7190.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> (
        "_7193.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7193,
        )

        return self.__parent__._cast(
            _7193.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7194.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7194,
        )

        return self.__parent__._cast(
            _7194.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7196.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7196,
        )

        return self.__parent__._cast(
            _7196.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7197.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7197,
        )

        return self.__parent__._cast(
            _7197.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7198.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7198,
        )

        return self.__parent__._cast(
            _7198.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7201.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7201,
        )

        return self.__parent__._cast(
            _7201.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> (
        "_7202.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7202,
        )

        return self.__parent__._cast(
            _7202.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def unbalanced_mass_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7203.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7203,
        )

        return self.__parent__._cast(
            _7203.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7204.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7204,
        )

        return self.__parent__._cast(
            _7204.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7205.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7205,
        )

        return self.__parent__._cast(
            _7205.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7208.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
            _7208,
        )

        return self.__parent__._cast(
            _7208.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def component_compound_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
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
class ComponentCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7161.PartCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """ComponentCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = (
        _COMPONENT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
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
    ) -> "List[_6973.ComponentAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ComponentAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_6973.ComponentAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.ComponentAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "_Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        """Cast to another type.

        Returns:
            _Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
        """
        return _Cast_ComponentCompoundAdvancedTimeSteppingAnalysisForModulation(self)
