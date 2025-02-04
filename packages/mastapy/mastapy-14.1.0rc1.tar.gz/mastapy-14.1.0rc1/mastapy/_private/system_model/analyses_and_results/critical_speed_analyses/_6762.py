"""PartCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_method_call,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7709

_PART_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PartCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7706
    from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
        _6678,
        _6679,
        _6680,
        _6682,
        _6684,
        _6685,
        _6686,
        _6688,
        _6689,
        _6691,
        _6692,
        _6693,
        _6694,
        _6696,
        _6697,
        _6698,
        _6700,
        _6701,
        _6703,
        _6705,
        _6706,
        _6707,
        _6709,
        _6710,
        _6712,
        _6714,
        _6716,
        _6717,
        _6718,
        _6722,
        _6723,
        _6724,
        _6726,
        _6728,
        _6730,
        _6731,
        _6732,
        _6733,
        _6734,
        _6736,
        _6737,
        _6738,
        _6739,
        _6741,
        _6742,
        _6743,
        _6745,
        _6747,
        _6749,
        _6750,
        _6752,
        _6753,
        _6755,
        _6756,
        _6757,
        _6758,
        _6759,
        _6760,
        _6761,
        _6764,
        _6765,
        _6767,
        _6768,
        _6769,
        _6770,
        _6771,
        _6772,
        _6774,
        _6776,
        _6777,
        _6778,
        _6779,
        _6781,
        _6782,
        _6784,
        _6786,
        _6787,
        _6788,
        _6790,
        _6791,
        _6793,
        _6794,
        _6795,
        _6796,
        _6797,
        _6798,
        _6799,
        _6801,
        _6802,
        _6803,
        _6804,
        _6805,
        _6806,
        _6808,
        _6809,
        _6811,
    )
    from mastapy._private.system_model.drawing import _2313
    from mastapy._private.system_model.part_model import _2537

    Self = TypeVar("Self", bound="PartCriticalSpeedAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="PartCriticalSpeedAnalysis._Cast_PartCriticalSpeedAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCriticalSpeedAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartCriticalSpeedAnalysis:
    """Special nested class for casting PartCriticalSpeedAnalysis to subclasses."""

    __parent__: "PartCriticalSpeedAnalysis"

    @property
    def part_static_load_analysis_case(
        self: "CastSelf",
    ) -> "_7709.PartStaticLoadAnalysisCase":
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
    def abstract_assembly_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6678.AbstractAssemblyCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6678,
        )

        return self.__parent__._cast(_6678.AbstractAssemblyCriticalSpeedAnalysis)

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
    def agma_gleason_conical_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6684.AGMAGleasonConicalGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6684,
        )

        return self.__parent__._cast(
            _6684.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
        )

    @property
    def assembly_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6685.AssemblyCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6685,
        )

        return self.__parent__._cast(_6685.AssemblyCriticalSpeedAnalysis)

    @property
    def bearing_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6686.BearingCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6686,
        )

        return self.__parent__._cast(_6686.BearingCriticalSpeedAnalysis)

    @property
    def belt_drive_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6688.BeltDriveCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6688,
        )

        return self.__parent__._cast(_6688.BeltDriveCriticalSpeedAnalysis)

    @property
    def bevel_differential_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6689.BevelDifferentialGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6689,
        )

        return self.__parent__._cast(_6689.BevelDifferentialGearCriticalSpeedAnalysis)

    @property
    def bevel_differential_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6691.BevelDifferentialGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6691,
        )

        return self.__parent__._cast(
            _6691.BevelDifferentialGearSetCriticalSpeedAnalysis
        )

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
    def bevel_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6696.BevelGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6696,
        )

        return self.__parent__._cast(_6696.BevelGearSetCriticalSpeedAnalysis)

    @property
    def bolt_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6697.BoltCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6697,
        )

        return self.__parent__._cast(_6697.BoltCriticalSpeedAnalysis)

    @property
    def bolted_joint_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6698.BoltedJointCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6698,
        )

        return self.__parent__._cast(_6698.BoltedJointCriticalSpeedAnalysis)

    @property
    def clutch_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6700.ClutchCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6700,
        )

        return self.__parent__._cast(_6700.ClutchCriticalSpeedAnalysis)

    @property
    def clutch_half_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6701.ClutchHalfCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6701,
        )

        return self.__parent__._cast(_6701.ClutchHalfCriticalSpeedAnalysis)

    @property
    def component_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6703.ComponentCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6703,
        )

        return self.__parent__._cast(_6703.ComponentCriticalSpeedAnalysis)

    @property
    def concept_coupling_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6705.ConceptCouplingCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6705,
        )

        return self.__parent__._cast(_6705.ConceptCouplingCriticalSpeedAnalysis)

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
    def concept_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6709.ConceptGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6709,
        )

        return self.__parent__._cast(_6709.ConceptGearSetCriticalSpeedAnalysis)

    @property
    def conical_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6710.ConicalGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6710,
        )

        return self.__parent__._cast(_6710.ConicalGearCriticalSpeedAnalysis)

    @property
    def conical_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6712.ConicalGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6712,
        )

        return self.__parent__._cast(_6712.ConicalGearSetCriticalSpeedAnalysis)

    @property
    def connector_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6714.ConnectorCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6714,
        )

        return self.__parent__._cast(_6714.ConnectorCriticalSpeedAnalysis)

    @property
    def coupling_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6716.CouplingCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6716,
        )

        return self.__parent__._cast(_6716.CouplingCriticalSpeedAnalysis)

    @property
    def coupling_half_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6717.CouplingHalfCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6717,
        )

        return self.__parent__._cast(_6717.CouplingHalfCriticalSpeedAnalysis)

    @property
    def cvt_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6722.CVTCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6722,
        )

        return self.__parent__._cast(_6722.CVTCriticalSpeedAnalysis)

    @property
    def cvt_pulley_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6723.CVTPulleyCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6723,
        )

        return self.__parent__._cast(_6723.CVTPulleyCriticalSpeedAnalysis)

    @property
    def cycloidal_assembly_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6724.CycloidalAssemblyCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6724,
        )

        return self.__parent__._cast(_6724.CycloidalAssemblyCriticalSpeedAnalysis)

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
    def cylindrical_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6730.CylindricalGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6730,
        )

        return self.__parent__._cast(_6730.CylindricalGearSetCriticalSpeedAnalysis)

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
    def face_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6736.FaceGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6736,
        )

        return self.__parent__._cast(_6736.FaceGearSetCriticalSpeedAnalysis)

    @property
    def fe_part_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6737.FEPartCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6737,
        )

        return self.__parent__._cast(_6737.FEPartCriticalSpeedAnalysis)

    @property
    def flexible_pin_assembly_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6738.FlexiblePinAssemblyCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6738,
        )

        return self.__parent__._cast(_6738.FlexiblePinAssemblyCriticalSpeedAnalysis)

    @property
    def gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6739.GearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6739,
        )

        return self.__parent__._cast(_6739.GearCriticalSpeedAnalysis)

    @property
    def gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6741.GearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6741,
        )

        return self.__parent__._cast(_6741.GearSetCriticalSpeedAnalysis)

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
    def hypoid_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6745.HypoidGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6745,
        )

        return self.__parent__._cast(_6745.HypoidGearSetCriticalSpeedAnalysis)

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
    def klingelnberg_cyclo_palloid_conical_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6749.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6749,
        )

        return self.__parent__._cast(
            _6749.KlingelnbergCycloPalloidConicalGearSetCriticalSpeedAnalysis
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
    def klingelnberg_cyclo_palloid_hypoid_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6752.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6752,
        )

        return self.__parent__._cast(
            _6752.KlingelnbergCycloPalloidHypoidGearSetCriticalSpeedAnalysis
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
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6755.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6755,
        )

        return self.__parent__._cast(
            _6755.KlingelnbergCycloPalloidSpiralBevelGearSetCriticalSpeedAnalysis
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
    def microphone_array_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6758.MicrophoneArrayCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6758,
        )

        return self.__parent__._cast(_6758.MicrophoneArrayCriticalSpeedAnalysis)

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
    def part_to_part_shear_coupling_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6764.PartToPartShearCouplingCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6764,
        )

        return self.__parent__._cast(_6764.PartToPartShearCouplingCriticalSpeedAnalysis)

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
    def planetary_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6767.PlanetaryGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6767,
        )

        return self.__parent__._cast(_6767.PlanetaryGearSetCriticalSpeedAnalysis)

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
    def rolling_ring_assembly_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6774.RollingRingAssemblyCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6774,
        )

        return self.__parent__._cast(_6774.RollingRingAssemblyCriticalSpeedAnalysis)

    @property
    def rolling_ring_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6776.RollingRingCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6776,
        )

        return self.__parent__._cast(_6776.RollingRingCriticalSpeedAnalysis)

    @property
    def root_assembly_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6777.RootAssemblyCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6777,
        )

        return self.__parent__._cast(_6777.RootAssemblyCriticalSpeedAnalysis)

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
    def specialised_assembly_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6781.SpecialisedAssemblyCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6781,
        )

        return self.__parent__._cast(_6781.SpecialisedAssemblyCriticalSpeedAnalysis)

    @property
    def spiral_bevel_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6782.SpiralBevelGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6782,
        )

        return self.__parent__._cast(_6782.SpiralBevelGearCriticalSpeedAnalysis)

    @property
    def spiral_bevel_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6784.SpiralBevelGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6784,
        )

        return self.__parent__._cast(_6784.SpiralBevelGearSetCriticalSpeedAnalysis)

    @property
    def spring_damper_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6786.SpringDamperCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6786,
        )

        return self.__parent__._cast(_6786.SpringDamperCriticalSpeedAnalysis)

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
    def straight_bevel_diff_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6790.StraightBevelDiffGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6790,
        )

        return self.__parent__._cast(
            _6790.StraightBevelDiffGearSetCriticalSpeedAnalysis
        )

    @property
    def straight_bevel_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6791.StraightBevelGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6791,
        )

        return self.__parent__._cast(_6791.StraightBevelGearCriticalSpeedAnalysis)

    @property
    def straight_bevel_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6793.StraightBevelGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6793,
        )

        return self.__parent__._cast(_6793.StraightBevelGearSetCriticalSpeedAnalysis)

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
    def synchroniser_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6796.SynchroniserCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6796,
        )

        return self.__parent__._cast(_6796.SynchroniserCriticalSpeedAnalysis)

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
    def torque_converter_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6801.TorqueConverterCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6801,
        )

        return self.__parent__._cast(_6801.TorqueConverterCriticalSpeedAnalysis)

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
    def worm_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6808.WormGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6808,
        )

        return self.__parent__._cast(_6808.WormGearSetCriticalSpeedAnalysis)

    @property
    def zerol_bevel_gear_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6809.ZerolBevelGearCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6809,
        )

        return self.__parent__._cast(_6809.ZerolBevelGearCriticalSpeedAnalysis)

    @property
    def zerol_bevel_gear_set_critical_speed_analysis(
        self: "CastSelf",
    ) -> "_6811.ZerolBevelGearSetCriticalSpeedAnalysis":
        from mastapy._private.system_model.analyses_and_results.critical_speed_analyses import (
            _6811,
        )

        return self.__parent__._cast(_6811.ZerolBevelGearSetCriticalSpeedAnalysis)

    @property
    def part_critical_speed_analysis(self: "CastSelf") -> "PartCriticalSpeedAnalysis":
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
class PartCriticalSpeedAnalysis(_7709.PartStaticLoadAnalysisCase):
    """PartCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_CRITICAL_SPEED_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_design(self: "Self") -> "_2537.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def critical_speed_analysis(self: "Self") -> "_6718.CriticalSpeedAnalysis":
        """mastapy.system_model.analyses_and_results.critical_speed_analyses.CriticalSpeedAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CriticalSpeedAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: "Self") -> "_2313.CriticalSpeedAnalysisViewable":
        """mastapy.system_model.drawing.CriticalSpeedAnalysisViewable"""
        method_result = pythonnet_method_call(self.wrapped, "CreateViewable")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_PartCriticalSpeedAnalysis":
        """Cast to another type.

        Returns:
            _Cast_PartCriticalSpeedAnalysis
        """
        return _Cast_PartCriticalSpeedAnalysis(self)
