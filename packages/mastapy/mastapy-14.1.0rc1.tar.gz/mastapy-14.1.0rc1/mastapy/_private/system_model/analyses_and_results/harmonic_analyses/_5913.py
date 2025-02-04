"""PartHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_method_call,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7709

_PART_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PartHarmonicAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7706
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
        _5800,
        _5802,
        _5803,
        _5805,
        _5807,
        _5808,
        _5809,
        _5811,
        _5812,
        _5814,
        _5815,
        _5816,
        _5817,
        _5819,
        _5820,
        _5821,
        _5823,
        _5824,
        _5827,
        _5829,
        _5830,
        _5831,
        _5833,
        _5834,
        _5836,
        _5838,
        _5840,
        _5841,
        _5843,
        _5844,
        _5845,
        _5847,
        _5849,
        _5851,
        _5852,
        _5854,
        _5869,
        _5870,
        _5872,
        _5873,
        _5874,
        _5876,
        _5881,
        _5883,
        _5884,
        _5889,
        _5894,
        _5896,
        _5898,
        _5900,
        _5901,
        _5903,
        _5904,
        _5906,
        _5907,
        _5908,
        _5909,
        _5910,
        _5911,
        _5912,
        _5915,
        _5916,
        _5919,
        _5920,
        _5921,
        _5922,
        _5923,
        _5925,
        _5927,
        _5929,
        _5930,
        _5931,
        _5932,
        _5935,
        _5937,
        _5939,
        _5941,
        _5942,
        _5944,
        _5946,
        _5947,
        _5949,
        _5950,
        _5951,
        _5952,
        _5953,
        _5954,
        _5955,
        _5957,
        _5958,
        _5959,
        _5961,
        _5962,
        _5963,
        _5965,
        _5966,
        _5968,
    )
    from mastapy._private.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6197,
    )
    from mastapy._private.system_model.analyses_and_results.modal_analyses import _4767
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2862,
    )
    from mastapy._private.system_model.drawing import _2315
    from mastapy._private.system_model.part_model import _2537

    Self = TypeVar("Self", bound="PartHarmonicAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="PartHarmonicAnalysis._Cast_PartHarmonicAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartHarmonicAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartHarmonicAnalysis:
    """Special nested class for casting PartHarmonicAnalysis to subclasses."""

    __parent__: "PartHarmonicAnalysis"

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
    def abstract_assembly_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5800.AbstractAssemblyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5800,
        )

        return self.__parent__._cast(_5800.AbstractAssemblyHarmonicAnalysis)

    @property
    def abstract_shaft_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5802.AbstractShaftHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5802,
        )

        return self.__parent__._cast(_5802.AbstractShaftHarmonicAnalysis)

    @property
    def abstract_shaft_or_housing_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5803.AbstractShaftOrHousingHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5803,
        )

        return self.__parent__._cast(_5803.AbstractShaftOrHousingHarmonicAnalysis)

    @property
    def agma_gleason_conical_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5805.AGMAGleasonConicalGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5805,
        )

        return self.__parent__._cast(_5805.AGMAGleasonConicalGearHarmonicAnalysis)

    @property
    def agma_gleason_conical_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5807.AGMAGleasonConicalGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5807,
        )

        return self.__parent__._cast(_5807.AGMAGleasonConicalGearSetHarmonicAnalysis)

    @property
    def assembly_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5808.AssemblyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5808,
        )

        return self.__parent__._cast(_5808.AssemblyHarmonicAnalysis)

    @property
    def bearing_harmonic_analysis(self: "CastSelf") -> "_5809.BearingHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5809,
        )

        return self.__parent__._cast(_5809.BearingHarmonicAnalysis)

    @property
    def belt_drive_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5811.BeltDriveHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5811,
        )

        return self.__parent__._cast(_5811.BeltDriveHarmonicAnalysis)

    @property
    def bevel_differential_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5812.BevelDifferentialGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5812,
        )

        return self.__parent__._cast(_5812.BevelDifferentialGearHarmonicAnalysis)

    @property
    def bevel_differential_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5814.BevelDifferentialGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5814,
        )

        return self.__parent__._cast(_5814.BevelDifferentialGearSetHarmonicAnalysis)

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
    def bevel_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5819.BevelGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5819,
        )

        return self.__parent__._cast(_5819.BevelGearSetHarmonicAnalysis)

    @property
    def bolted_joint_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5820.BoltedJointHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5820,
        )

        return self.__parent__._cast(_5820.BoltedJointHarmonicAnalysis)

    @property
    def bolt_harmonic_analysis(self: "CastSelf") -> "_5821.BoltHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5821,
        )

        return self.__parent__._cast(_5821.BoltHarmonicAnalysis)

    @property
    def clutch_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5823.ClutchHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5823,
        )

        return self.__parent__._cast(_5823.ClutchHalfHarmonicAnalysis)

    @property
    def clutch_harmonic_analysis(self: "CastSelf") -> "_5824.ClutchHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5824,
        )

        return self.__parent__._cast(_5824.ClutchHarmonicAnalysis)

    @property
    def component_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5827.ComponentHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5827,
        )

        return self.__parent__._cast(_5827.ComponentHarmonicAnalysis)

    @property
    def concept_coupling_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5829.ConceptCouplingHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5829,
        )

        return self.__parent__._cast(_5829.ConceptCouplingHalfHarmonicAnalysis)

    @property
    def concept_coupling_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5830.ConceptCouplingHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5830,
        )

        return self.__parent__._cast(_5830.ConceptCouplingHarmonicAnalysis)

    @property
    def concept_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5831.ConceptGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5831,
        )

        return self.__parent__._cast(_5831.ConceptGearHarmonicAnalysis)

    @property
    def concept_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5833.ConceptGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5833,
        )

        return self.__parent__._cast(_5833.ConceptGearSetHarmonicAnalysis)

    @property
    def conical_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5834.ConicalGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5834,
        )

        return self.__parent__._cast(_5834.ConicalGearHarmonicAnalysis)

    @property
    def conical_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5836.ConicalGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5836,
        )

        return self.__parent__._cast(_5836.ConicalGearSetHarmonicAnalysis)

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
    def coupling_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5841.CouplingHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5841,
        )

        return self.__parent__._cast(_5841.CouplingHarmonicAnalysis)

    @property
    def cvt_harmonic_analysis(self: "CastSelf") -> "_5843.CVTHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5843,
        )

        return self.__parent__._cast(_5843.CVTHarmonicAnalysis)

    @property
    def cvt_pulley_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5844.CVTPulleyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5844,
        )

        return self.__parent__._cast(_5844.CVTPulleyHarmonicAnalysis)

    @property
    def cycloidal_assembly_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5845.CycloidalAssemblyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5845,
        )

        return self.__parent__._cast(_5845.CycloidalAssemblyHarmonicAnalysis)

    @property
    def cycloidal_disc_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5847.CycloidalDiscHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5847,
        )

        return self.__parent__._cast(_5847.CycloidalDiscHarmonicAnalysis)

    @property
    def cylindrical_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5849.CylindricalGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5849,
        )

        return self.__parent__._cast(_5849.CylindricalGearHarmonicAnalysis)

    @property
    def cylindrical_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5851.CylindricalGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5851,
        )

        return self.__parent__._cast(_5851.CylindricalGearSetHarmonicAnalysis)

    @property
    def cylindrical_planet_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5852.CylindricalPlanetGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5852,
        )

        return self.__parent__._cast(_5852.CylindricalPlanetGearHarmonicAnalysis)

    @property
    def datum_harmonic_analysis(self: "CastSelf") -> "_5854.DatumHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5854,
        )

        return self.__parent__._cast(_5854.DatumHarmonicAnalysis)

    @property
    def external_cad_model_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5869.ExternalCADModelHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5869,
        )

        return self.__parent__._cast(_5869.ExternalCADModelHarmonicAnalysis)

    @property
    def face_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5870.FaceGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5870,
        )

        return self.__parent__._cast(_5870.FaceGearHarmonicAnalysis)

    @property
    def face_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5872.FaceGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5872,
        )

        return self.__parent__._cast(_5872.FaceGearSetHarmonicAnalysis)

    @property
    def fe_part_harmonic_analysis(self: "CastSelf") -> "_5873.FEPartHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5873,
        )

        return self.__parent__._cast(_5873.FEPartHarmonicAnalysis)

    @property
    def flexible_pin_assembly_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5874.FlexiblePinAssemblyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5874,
        )

        return self.__parent__._cast(_5874.FlexiblePinAssemblyHarmonicAnalysis)

    @property
    def gear_harmonic_analysis(self: "CastSelf") -> "_5876.GearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5876,
        )

        return self.__parent__._cast(_5876.GearHarmonicAnalysis)

    @property
    def gear_set_harmonic_analysis(self: "CastSelf") -> "_5881.GearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5881,
        )

        return self.__parent__._cast(_5881.GearSetHarmonicAnalysis)

    @property
    def guide_dxf_model_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5883.GuideDxfModelHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5883,
        )

        return self.__parent__._cast(_5883.GuideDxfModelHarmonicAnalysis)

    @property
    def hypoid_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5894.HypoidGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5894,
        )

        return self.__parent__._cast(_5894.HypoidGearHarmonicAnalysis)

    @property
    def hypoid_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5896.HypoidGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5896,
        )

        return self.__parent__._cast(_5896.HypoidGearSetHarmonicAnalysis)

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
    def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5900.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5900,
        )

        return self.__parent__._cast(
            _5900.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
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
    def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5903.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5903,
        )

        return self.__parent__._cast(
            _5903.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
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
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5906.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5906,
        )

        return self.__parent__._cast(
            _5906.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
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
    def microphone_array_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5909.MicrophoneArrayHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5909,
        )

        return self.__parent__._cast(_5909.MicrophoneArrayHarmonicAnalysis)

    @property
    def microphone_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5910.MicrophoneHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5910,
        )

        return self.__parent__._cast(_5910.MicrophoneHarmonicAnalysis)

    @property
    def mountable_component_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5911.MountableComponentHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5911,
        )

        return self.__parent__._cast(_5911.MountableComponentHarmonicAnalysis)

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
    def part_to_part_shear_coupling_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5916.PartToPartShearCouplingHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5916,
        )

        return self.__parent__._cast(_5916.PartToPartShearCouplingHarmonicAnalysis)

    @property
    def planetary_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5919.PlanetaryGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5919,
        )

        return self.__parent__._cast(_5919.PlanetaryGearSetHarmonicAnalysis)

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
    def rolling_ring_assembly_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5927.RollingRingAssemblyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5927,
        )

        return self.__parent__._cast(_5927.RollingRingAssemblyHarmonicAnalysis)

    @property
    def rolling_ring_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5929.RollingRingHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5929,
        )

        return self.__parent__._cast(_5929.RollingRingHarmonicAnalysis)

    @property
    def root_assembly_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5930.RootAssemblyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5930,
        )

        return self.__parent__._cast(_5930.RootAssemblyHarmonicAnalysis)

    @property
    def shaft_harmonic_analysis(self: "CastSelf") -> "_5931.ShaftHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5931,
        )

        return self.__parent__._cast(_5931.ShaftHarmonicAnalysis)

    @property
    def shaft_hub_connection_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5932.ShaftHubConnectionHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5932,
        )

        return self.__parent__._cast(_5932.ShaftHubConnectionHarmonicAnalysis)

    @property
    def specialised_assembly_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5935.SpecialisedAssemblyHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5935,
        )

        return self.__parent__._cast(_5935.SpecialisedAssemblyHarmonicAnalysis)

    @property
    def spiral_bevel_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5937.SpiralBevelGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5937,
        )

        return self.__parent__._cast(_5937.SpiralBevelGearHarmonicAnalysis)

    @property
    def spiral_bevel_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5939.SpiralBevelGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5939,
        )

        return self.__parent__._cast(_5939.SpiralBevelGearSetHarmonicAnalysis)

    @property
    def spring_damper_half_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5941.SpringDamperHalfHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5941,
        )

        return self.__parent__._cast(_5941.SpringDamperHalfHarmonicAnalysis)

    @property
    def spring_damper_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5942.SpringDamperHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5942,
        )

        return self.__parent__._cast(_5942.SpringDamperHarmonicAnalysis)

    @property
    def straight_bevel_diff_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5944.StraightBevelDiffGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5944,
        )

        return self.__parent__._cast(_5944.StraightBevelDiffGearHarmonicAnalysis)

    @property
    def straight_bevel_diff_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5946.StraightBevelDiffGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5946,
        )

        return self.__parent__._cast(_5946.StraightBevelDiffGearSetHarmonicAnalysis)

    @property
    def straight_bevel_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5947.StraightBevelGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5947,
        )

        return self.__parent__._cast(_5947.StraightBevelGearHarmonicAnalysis)

    @property
    def straight_bevel_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5949.StraightBevelGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5949,
        )

        return self.__parent__._cast(_5949.StraightBevelGearSetHarmonicAnalysis)

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
    def synchroniser_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5953.SynchroniserHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5953,
        )

        return self.__parent__._cast(_5953.SynchroniserHarmonicAnalysis)

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
    def torque_converter_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5957.TorqueConverterHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5957,
        )

        return self.__parent__._cast(_5957.TorqueConverterHarmonicAnalysis)

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
    def worm_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5965.WormGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5965,
        )

        return self.__parent__._cast(_5965.WormGearSetHarmonicAnalysis)

    @property
    def zerol_bevel_gear_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5966.ZerolBevelGearHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5966,
        )

        return self.__parent__._cast(_5966.ZerolBevelGearHarmonicAnalysis)

    @property
    def zerol_bevel_gear_set_harmonic_analysis(
        self: "CastSelf",
    ) -> "_5968.ZerolBevelGearSetHarmonicAnalysis":
        from mastapy._private.system_model.analyses_and_results.harmonic_analyses import (
            _5968,
        )

        return self.__parent__._cast(_5968.ZerolBevelGearSetHarmonicAnalysis)

    @property
    def part_harmonic_analysis(self: "CastSelf") -> "PartHarmonicAnalysis":
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
class PartHarmonicAnalysis(_7709.PartStaticLoadAnalysisCase):
    """PartHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_HARMONIC_ANALYSIS

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
    def coupled_modal_analysis(self: "Self") -> "_4767.PartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CoupledModalAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis(self: "Self") -> "_5884.HarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "HarmonicAnalysis")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_options(self: "Self") -> "_5889.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "HarmonicAnalysisOptions")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analyses_of_single_excitations(
        self: "Self",
    ) -> "List[_6197.HarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "HarmonicAnalysesOfSingleExcitations"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: "Self") -> "_2862.PartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SystemDeflectionResults")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: "Self") -> "_2315.HarmonicAnalysisViewable":
        """mastapy.system_model.drawing.HarmonicAnalysisViewable"""
        method_result = pythonnet_method_call(self.wrapped, "CreateViewable")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_PartHarmonicAnalysis":
        """Cast to another type.

        Returns:
            _Cast_PartHarmonicAnalysis
        """
        return _Cast_PartHarmonicAnalysis(self)
