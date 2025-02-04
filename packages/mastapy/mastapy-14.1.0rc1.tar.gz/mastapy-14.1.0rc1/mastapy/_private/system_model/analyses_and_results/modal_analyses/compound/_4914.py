"""PartCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7707

_PART_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "PartCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7704
    from mastapy._private.system_model.analyses_and_results.modal_analyses import _4767
    from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
        _4833,
        _4834,
        _4835,
        _4837,
        _4839,
        _4840,
        _4841,
        _4843,
        _4844,
        _4846,
        _4847,
        _4848,
        _4849,
        _4851,
        _4852,
        _4853,
        _4854,
        _4856,
        _4858,
        _4859,
        _4861,
        _4862,
        _4864,
        _4865,
        _4867,
        _4869,
        _4870,
        _4872,
        _4874,
        _4875,
        _4876,
        _4878,
        _4880,
        _4882,
        _4883,
        _4884,
        _4885,
        _4886,
        _4888,
        _4889,
        _4890,
        _4891,
        _4893,
        _4894,
        _4895,
        _4897,
        _4899,
        _4901,
        _4902,
        _4904,
        _4905,
        _4907,
        _4908,
        _4909,
        _4910,
        _4911,
        _4912,
        _4913,
        _4915,
        _4917,
        _4919,
        _4920,
        _4921,
        _4922,
        _4923,
        _4924,
        _4926,
        _4927,
        _4929,
        _4930,
        _4931,
        _4933,
        _4934,
        _4936,
        _4937,
        _4939,
        _4940,
        _4942,
        _4943,
        _4945,
        _4946,
        _4947,
        _4948,
        _4949,
        _4950,
        _4951,
        _4952,
        _4954,
        _4955,
        _4956,
        _4957,
        _4958,
        _4960,
        _4961,
        _4963,
    )

    Self = TypeVar("Self", bound="PartCompoundModalAnalysis")
    CastSelf = TypeVar(
        "CastSelf", bound="PartCompoundModalAnalysis._Cast_PartCompoundModalAnalysis"
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundModalAnalysis",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartCompoundModalAnalysis:
    """Special nested class for casting PartCompoundModalAnalysis to subclasses."""

    __parent__: "PartCompoundModalAnalysis"

    @property
    def part_compound_analysis(self: "CastSelf") -> "_7707.PartCompoundAnalysis":
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
    def abstract_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4833.AbstractAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4833,
        )

        return self.__parent__._cast(_4833.AbstractAssemblyCompoundModalAnalysis)

    @property
    def abstract_shaft_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4834.AbstractShaftCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4834,
        )

        return self.__parent__._cast(_4834.AbstractShaftCompoundModalAnalysis)

    @property
    def abstract_shaft_or_housing_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4835.AbstractShaftOrHousingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4835,
        )

        return self.__parent__._cast(_4835.AbstractShaftOrHousingCompoundModalAnalysis)

    @property
    def agma_gleason_conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4837.AGMAGleasonConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4837,
        )

        return self.__parent__._cast(_4837.AGMAGleasonConicalGearCompoundModalAnalysis)

    @property
    def agma_gleason_conical_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4839.AGMAGleasonConicalGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4839,
        )

        return self.__parent__._cast(
            _4839.AGMAGleasonConicalGearSetCompoundModalAnalysis
        )

    @property
    def assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4840.AssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4840,
        )

        return self.__parent__._cast(_4840.AssemblyCompoundModalAnalysis)

    @property
    def bearing_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4841.BearingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4841,
        )

        return self.__parent__._cast(_4841.BearingCompoundModalAnalysis)

    @property
    def belt_drive_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4843.BeltDriveCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4843,
        )

        return self.__parent__._cast(_4843.BeltDriveCompoundModalAnalysis)

    @property
    def bevel_differential_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4844.BevelDifferentialGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4844,
        )

        return self.__parent__._cast(_4844.BevelDifferentialGearCompoundModalAnalysis)

    @property
    def bevel_differential_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4846.BevelDifferentialGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4846,
        )

        return self.__parent__._cast(
            _4846.BevelDifferentialGearSetCompoundModalAnalysis
        )

    @property
    def bevel_differential_planet_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4847.BevelDifferentialPlanetGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4847,
        )

        return self.__parent__._cast(
            _4847.BevelDifferentialPlanetGearCompoundModalAnalysis
        )

    @property
    def bevel_differential_sun_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4848.BevelDifferentialSunGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4848,
        )

        return self.__parent__._cast(
            _4848.BevelDifferentialSunGearCompoundModalAnalysis
        )

    @property
    def bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4849.BevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4849,
        )

        return self.__parent__._cast(_4849.BevelGearCompoundModalAnalysis)

    @property
    def bevel_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4851.BevelGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4851,
        )

        return self.__parent__._cast(_4851.BevelGearSetCompoundModalAnalysis)

    @property
    def bolt_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4852.BoltCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4852,
        )

        return self.__parent__._cast(_4852.BoltCompoundModalAnalysis)

    @property
    def bolted_joint_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4853.BoltedJointCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4853,
        )

        return self.__parent__._cast(_4853.BoltedJointCompoundModalAnalysis)

    @property
    def clutch_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4854.ClutchCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4854,
        )

        return self.__parent__._cast(_4854.ClutchCompoundModalAnalysis)

    @property
    def clutch_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4856.ClutchHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4856,
        )

        return self.__parent__._cast(_4856.ClutchHalfCompoundModalAnalysis)

    @property
    def component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4858.ComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4858,
        )

        return self.__parent__._cast(_4858.ComponentCompoundModalAnalysis)

    @property
    def concept_coupling_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4859.ConceptCouplingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4859,
        )

        return self.__parent__._cast(_4859.ConceptCouplingCompoundModalAnalysis)

    @property
    def concept_coupling_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4861.ConceptCouplingHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4861,
        )

        return self.__parent__._cast(_4861.ConceptCouplingHalfCompoundModalAnalysis)

    @property
    def concept_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4862.ConceptGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4862,
        )

        return self.__parent__._cast(_4862.ConceptGearCompoundModalAnalysis)

    @property
    def concept_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4864.ConceptGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4864,
        )

        return self.__parent__._cast(_4864.ConceptGearSetCompoundModalAnalysis)

    @property
    def conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4865.ConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4865,
        )

        return self.__parent__._cast(_4865.ConicalGearCompoundModalAnalysis)

    @property
    def conical_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4867.ConicalGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4867,
        )

        return self.__parent__._cast(_4867.ConicalGearSetCompoundModalAnalysis)

    @property
    def connector_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4869.ConnectorCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4869,
        )

        return self.__parent__._cast(_4869.ConnectorCompoundModalAnalysis)

    @property
    def coupling_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4870.CouplingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4870,
        )

        return self.__parent__._cast(_4870.CouplingCompoundModalAnalysis)

    @property
    def coupling_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4872.CouplingHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4872,
        )

        return self.__parent__._cast(_4872.CouplingHalfCompoundModalAnalysis)

    @property
    def cvt_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4874.CVTCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4874,
        )

        return self.__parent__._cast(_4874.CVTCompoundModalAnalysis)

    @property
    def cvt_pulley_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4875.CVTPulleyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4875,
        )

        return self.__parent__._cast(_4875.CVTPulleyCompoundModalAnalysis)

    @property
    def cycloidal_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4876.CycloidalAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4876,
        )

        return self.__parent__._cast(_4876.CycloidalAssemblyCompoundModalAnalysis)

    @property
    def cycloidal_disc_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4878.CycloidalDiscCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4878,
        )

        return self.__parent__._cast(_4878.CycloidalDiscCompoundModalAnalysis)

    @property
    def cylindrical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4880.CylindricalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4880,
        )

        return self.__parent__._cast(_4880.CylindricalGearCompoundModalAnalysis)

    @property
    def cylindrical_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4882.CylindricalGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4882,
        )

        return self.__parent__._cast(_4882.CylindricalGearSetCompoundModalAnalysis)

    @property
    def cylindrical_planet_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4883.CylindricalPlanetGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4883,
        )

        return self.__parent__._cast(_4883.CylindricalPlanetGearCompoundModalAnalysis)

    @property
    def datum_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4884.DatumCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4884,
        )

        return self.__parent__._cast(_4884.DatumCompoundModalAnalysis)

    @property
    def external_cad_model_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4885.ExternalCADModelCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4885,
        )

        return self.__parent__._cast(_4885.ExternalCADModelCompoundModalAnalysis)

    @property
    def face_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4886.FaceGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4886,
        )

        return self.__parent__._cast(_4886.FaceGearCompoundModalAnalysis)

    @property
    def face_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4888.FaceGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4888,
        )

        return self.__parent__._cast(_4888.FaceGearSetCompoundModalAnalysis)

    @property
    def fe_part_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4889.FEPartCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4889,
        )

        return self.__parent__._cast(_4889.FEPartCompoundModalAnalysis)

    @property
    def flexible_pin_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4890.FlexiblePinAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4890,
        )

        return self.__parent__._cast(_4890.FlexiblePinAssemblyCompoundModalAnalysis)

    @property
    def gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4891.GearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4891,
        )

        return self.__parent__._cast(_4891.GearCompoundModalAnalysis)

    @property
    def gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4893.GearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4893,
        )

        return self.__parent__._cast(_4893.GearSetCompoundModalAnalysis)

    @property
    def guide_dxf_model_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4894.GuideDxfModelCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4894,
        )

        return self.__parent__._cast(_4894.GuideDxfModelCompoundModalAnalysis)

    @property
    def hypoid_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4895.HypoidGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4895,
        )

        return self.__parent__._cast(_4895.HypoidGearCompoundModalAnalysis)

    @property
    def hypoid_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4897.HypoidGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4897,
        )

        return self.__parent__._cast(_4897.HypoidGearSetCompoundModalAnalysis)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4899.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4899,
        )

        return self.__parent__._cast(
            _4899.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4901.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4901,
        )

        return self.__parent__._cast(
            _4901.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4902.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4902,
        )

        return self.__parent__._cast(
            _4902.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4904.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4904,
        )

        return self.__parent__._cast(
            _4904.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4905.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4905,
        )

        return self.__parent__._cast(
            _4905.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4907.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4907,
        )

        return self.__parent__._cast(
            _4907.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysis
        )

    @property
    def mass_disc_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4908.MassDiscCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4908,
        )

        return self.__parent__._cast(_4908.MassDiscCompoundModalAnalysis)

    @property
    def measurement_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4909.MeasurementComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4909,
        )

        return self.__parent__._cast(_4909.MeasurementComponentCompoundModalAnalysis)

    @property
    def microphone_array_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4910.MicrophoneArrayCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4910,
        )

        return self.__parent__._cast(_4910.MicrophoneArrayCompoundModalAnalysis)

    @property
    def microphone_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4911.MicrophoneCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4911,
        )

        return self.__parent__._cast(_4911.MicrophoneCompoundModalAnalysis)

    @property
    def mountable_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4912.MountableComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4912,
        )

        return self.__parent__._cast(_4912.MountableComponentCompoundModalAnalysis)

    @property
    def oil_seal_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4913.OilSealCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4913,
        )

        return self.__parent__._cast(_4913.OilSealCompoundModalAnalysis)

    @property
    def part_to_part_shear_coupling_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4915.PartToPartShearCouplingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4915,
        )

        return self.__parent__._cast(_4915.PartToPartShearCouplingCompoundModalAnalysis)

    @property
    def part_to_part_shear_coupling_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4917.PartToPartShearCouplingHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4917,
        )

        return self.__parent__._cast(
            _4917.PartToPartShearCouplingHalfCompoundModalAnalysis
        )

    @property
    def planetary_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4919.PlanetaryGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4919,
        )

        return self.__parent__._cast(_4919.PlanetaryGearSetCompoundModalAnalysis)

    @property
    def planet_carrier_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4920.PlanetCarrierCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4920,
        )

        return self.__parent__._cast(_4920.PlanetCarrierCompoundModalAnalysis)

    @property
    def point_load_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4921.PointLoadCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4921,
        )

        return self.__parent__._cast(_4921.PointLoadCompoundModalAnalysis)

    @property
    def power_load_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4922.PowerLoadCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4922,
        )

        return self.__parent__._cast(_4922.PowerLoadCompoundModalAnalysis)

    @property
    def pulley_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4923.PulleyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4923,
        )

        return self.__parent__._cast(_4923.PulleyCompoundModalAnalysis)

    @property
    def ring_pins_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4924.RingPinsCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4924,
        )

        return self.__parent__._cast(_4924.RingPinsCompoundModalAnalysis)

    @property
    def rolling_ring_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4926.RollingRingAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4926,
        )

        return self.__parent__._cast(_4926.RollingRingAssemblyCompoundModalAnalysis)

    @property
    def rolling_ring_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4927.RollingRingCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4927,
        )

        return self.__parent__._cast(_4927.RollingRingCompoundModalAnalysis)

    @property
    def root_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4929.RootAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4929,
        )

        return self.__parent__._cast(_4929.RootAssemblyCompoundModalAnalysis)

    @property
    def shaft_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4930.ShaftCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4930,
        )

        return self.__parent__._cast(_4930.ShaftCompoundModalAnalysis)

    @property
    def shaft_hub_connection_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4931.ShaftHubConnectionCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4931,
        )

        return self.__parent__._cast(_4931.ShaftHubConnectionCompoundModalAnalysis)

    @property
    def specialised_assembly_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4933.SpecialisedAssemblyCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4933,
        )

        return self.__parent__._cast(_4933.SpecialisedAssemblyCompoundModalAnalysis)

    @property
    def spiral_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4934.SpiralBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4934,
        )

        return self.__parent__._cast(_4934.SpiralBevelGearCompoundModalAnalysis)

    @property
    def spiral_bevel_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4936.SpiralBevelGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4936,
        )

        return self.__parent__._cast(_4936.SpiralBevelGearSetCompoundModalAnalysis)

    @property
    def spring_damper_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4937.SpringDamperCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4937,
        )

        return self.__parent__._cast(_4937.SpringDamperCompoundModalAnalysis)

    @property
    def spring_damper_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4939.SpringDamperHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4939,
        )

        return self.__parent__._cast(_4939.SpringDamperHalfCompoundModalAnalysis)

    @property
    def straight_bevel_diff_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4940.StraightBevelDiffGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4940,
        )

        return self.__parent__._cast(_4940.StraightBevelDiffGearCompoundModalAnalysis)

    @property
    def straight_bevel_diff_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4942.StraightBevelDiffGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4942,
        )

        return self.__parent__._cast(
            _4942.StraightBevelDiffGearSetCompoundModalAnalysis
        )

    @property
    def straight_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4943.StraightBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4943,
        )

        return self.__parent__._cast(_4943.StraightBevelGearCompoundModalAnalysis)

    @property
    def straight_bevel_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4945.StraightBevelGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4945,
        )

        return self.__parent__._cast(_4945.StraightBevelGearSetCompoundModalAnalysis)

    @property
    def straight_bevel_planet_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4946.StraightBevelPlanetGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4946,
        )

        return self.__parent__._cast(_4946.StraightBevelPlanetGearCompoundModalAnalysis)

    @property
    def straight_bevel_sun_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4947.StraightBevelSunGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4947,
        )

        return self.__parent__._cast(_4947.StraightBevelSunGearCompoundModalAnalysis)

    @property
    def synchroniser_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4948.SynchroniserCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4948,
        )

        return self.__parent__._cast(_4948.SynchroniserCompoundModalAnalysis)

    @property
    def synchroniser_half_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4949.SynchroniserHalfCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4949,
        )

        return self.__parent__._cast(_4949.SynchroniserHalfCompoundModalAnalysis)

    @property
    def synchroniser_part_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4950.SynchroniserPartCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4950,
        )

        return self.__parent__._cast(_4950.SynchroniserPartCompoundModalAnalysis)

    @property
    def synchroniser_sleeve_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4951.SynchroniserSleeveCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4951,
        )

        return self.__parent__._cast(_4951.SynchroniserSleeveCompoundModalAnalysis)

    @property
    def torque_converter_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4952.TorqueConverterCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4952,
        )

        return self.__parent__._cast(_4952.TorqueConverterCompoundModalAnalysis)

    @property
    def torque_converter_pump_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4954.TorqueConverterPumpCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4954,
        )

        return self.__parent__._cast(_4954.TorqueConverterPumpCompoundModalAnalysis)

    @property
    def torque_converter_turbine_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4955.TorqueConverterTurbineCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4955,
        )

        return self.__parent__._cast(_4955.TorqueConverterTurbineCompoundModalAnalysis)

    @property
    def unbalanced_mass_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4956.UnbalancedMassCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4956,
        )

        return self.__parent__._cast(_4956.UnbalancedMassCompoundModalAnalysis)

    @property
    def virtual_component_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4957.VirtualComponentCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4957,
        )

        return self.__parent__._cast(_4957.VirtualComponentCompoundModalAnalysis)

    @property
    def worm_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4958.WormGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4958,
        )

        return self.__parent__._cast(_4958.WormGearCompoundModalAnalysis)

    @property
    def worm_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4960.WormGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4960,
        )

        return self.__parent__._cast(_4960.WormGearSetCompoundModalAnalysis)

    @property
    def zerol_bevel_gear_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4961.ZerolBevelGearCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4961,
        )

        return self.__parent__._cast(_4961.ZerolBevelGearCompoundModalAnalysis)

    @property
    def zerol_bevel_gear_set_compound_modal_analysis(
        self: "CastSelf",
    ) -> "_4963.ZerolBevelGearSetCompoundModalAnalysis":
        from mastapy._private.system_model.analyses_and_results.modal_analyses.compound import (
            _4963,
        )

        return self.__parent__._cast(_4963.ZerolBevelGearSetCompoundModalAnalysis)

    @property
    def part_compound_modal_analysis(self: "CastSelf") -> "PartCompoundModalAnalysis":
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
class PartCompoundModalAnalysis(_7707.PartCompoundAnalysis):
    """PartCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_COMPOUND_MODAL_ANALYSIS

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(self: "Self") -> "List[_4767.PartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis]

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
    def component_analysis_cases_ready(self: "Self") -> "List[_4767.PartModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis]

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
    def cast_to(self: "Self") -> "_Cast_PartCompoundModalAnalysis":
        """Cast to another type.

        Returns:
            _Cast_PartCompoundModalAnalysis
        """
        return _Cast_PartCompoundModalAnalysis(self)
