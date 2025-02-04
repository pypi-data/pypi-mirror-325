"""ComponentCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4625,
)

_COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ComponentCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools import (
        _4420,
    )
    from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4545,
        _4546,
        _4548,
        _4552,
        _4555,
        _4558,
        _4559,
        _4560,
        _4563,
        _4567,
        _4572,
        _4573,
        _4576,
        _4580,
        _4583,
        _4586,
        _4589,
        _4591,
        _4594,
        _4595,
        _4596,
        _4597,
        _4600,
        _4602,
        _4605,
        _4606,
        _4610,
        _4613,
        _4616,
        _4619,
        _4620,
        _4622,
        _4623,
        _4624,
        _4628,
        _4631,
        _4632,
        _4633,
        _4634,
        _4635,
        _4638,
        _4641,
        _4642,
        _4645,
        _4650,
        _4651,
        _4654,
        _4657,
        _4658,
        _4660,
        _4661,
        _4662,
        _4665,
        _4666,
        _4667,
        _4668,
        _4669,
        _4672,
    )

    Self = TypeVar("Self", bound="ComponentCompoundParametricStudyTool")
    CastSelf = TypeVar(
        "CastSelf",
        bound="ComponentCompoundParametricStudyTool._Cast_ComponentCompoundParametricStudyTool",
    )


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundParametricStudyTool",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_ComponentCompoundParametricStudyTool:
    """Special nested class for casting ComponentCompoundParametricStudyTool to subclasses."""

    __parent__: "ComponentCompoundParametricStudyTool"

    @property
    def part_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4625.PartCompoundParametricStudyTool":
        return self.__parent__._cast(_4625.PartCompoundParametricStudyTool)

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
    def abstract_shaft_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4545.AbstractShaftCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4545,
        )

        return self.__parent__._cast(_4545.AbstractShaftCompoundParametricStudyTool)

    @property
    def abstract_shaft_or_housing_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4546.AbstractShaftOrHousingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4546,
        )

        return self.__parent__._cast(
            _4546.AbstractShaftOrHousingCompoundParametricStudyTool
        )

    @property
    def agma_gleason_conical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4548.AGMAGleasonConicalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4548,
        )

        return self.__parent__._cast(
            _4548.AGMAGleasonConicalGearCompoundParametricStudyTool
        )

    @property
    def bearing_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4552.BearingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4552,
        )

        return self.__parent__._cast(_4552.BearingCompoundParametricStudyTool)

    @property
    def bevel_differential_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4555.BevelDifferentialGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4555,
        )

        return self.__parent__._cast(
            _4555.BevelDifferentialGearCompoundParametricStudyTool
        )

    @property
    def bevel_differential_planet_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4558.BevelDifferentialPlanetGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4558,
        )

        return self.__parent__._cast(
            _4558.BevelDifferentialPlanetGearCompoundParametricStudyTool
        )

    @property
    def bevel_differential_sun_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4559.BevelDifferentialSunGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4559,
        )

        return self.__parent__._cast(
            _4559.BevelDifferentialSunGearCompoundParametricStudyTool
        )

    @property
    def bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4560.BevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4560,
        )

        return self.__parent__._cast(_4560.BevelGearCompoundParametricStudyTool)

    @property
    def bolt_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4563.BoltCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4563,
        )

        return self.__parent__._cast(_4563.BoltCompoundParametricStudyTool)

    @property
    def clutch_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4567.ClutchHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4567,
        )

        return self.__parent__._cast(_4567.ClutchHalfCompoundParametricStudyTool)

    @property
    def concept_coupling_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4572.ConceptCouplingHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4572,
        )

        return self.__parent__._cast(
            _4572.ConceptCouplingHalfCompoundParametricStudyTool
        )

    @property
    def concept_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4573.ConceptGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4573,
        )

        return self.__parent__._cast(_4573.ConceptGearCompoundParametricStudyTool)

    @property
    def conical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4576.ConicalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4576,
        )

        return self.__parent__._cast(_4576.ConicalGearCompoundParametricStudyTool)

    @property
    def connector_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4580.ConnectorCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4580,
        )

        return self.__parent__._cast(_4580.ConnectorCompoundParametricStudyTool)

    @property
    def coupling_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4583.CouplingHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4583,
        )

        return self.__parent__._cast(_4583.CouplingHalfCompoundParametricStudyTool)

    @property
    def cvt_pulley_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4586.CVTPulleyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4586,
        )

        return self.__parent__._cast(_4586.CVTPulleyCompoundParametricStudyTool)

    @property
    def cycloidal_disc_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4589.CycloidalDiscCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4589,
        )

        return self.__parent__._cast(_4589.CycloidalDiscCompoundParametricStudyTool)

    @property
    def cylindrical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4591.CylindricalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4591,
        )

        return self.__parent__._cast(_4591.CylindricalGearCompoundParametricStudyTool)

    @property
    def cylindrical_planet_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4594.CylindricalPlanetGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4594,
        )

        return self.__parent__._cast(
            _4594.CylindricalPlanetGearCompoundParametricStudyTool
        )

    @property
    def datum_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4595.DatumCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4595,
        )

        return self.__parent__._cast(_4595.DatumCompoundParametricStudyTool)

    @property
    def external_cad_model_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4596.ExternalCADModelCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4596,
        )

        return self.__parent__._cast(_4596.ExternalCADModelCompoundParametricStudyTool)

    @property
    def face_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4597.FaceGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4597,
        )

        return self.__parent__._cast(_4597.FaceGearCompoundParametricStudyTool)

    @property
    def fe_part_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4600.FEPartCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4600,
        )

        return self.__parent__._cast(_4600.FEPartCompoundParametricStudyTool)

    @property
    def gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4602.GearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4602,
        )

        return self.__parent__._cast(_4602.GearCompoundParametricStudyTool)

    @property
    def guide_dxf_model_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4605.GuideDxfModelCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4605,
        )

        return self.__parent__._cast(_4605.GuideDxfModelCompoundParametricStudyTool)

    @property
    def hypoid_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4606.HypoidGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4606,
        )

        return self.__parent__._cast(_4606.HypoidGearCompoundParametricStudyTool)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4610.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4610,
        )

        return self.__parent__._cast(
            _4610.KlingelnbergCycloPalloidConicalGearCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4613.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4613,
        )

        return self.__parent__._cast(
            _4613.KlingelnbergCycloPalloidHypoidGearCompoundParametricStudyTool
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4616.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4616,
        )

        return self.__parent__._cast(
            _4616.KlingelnbergCycloPalloidSpiralBevelGearCompoundParametricStudyTool
        )

    @property
    def mass_disc_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4619.MassDiscCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4619,
        )

        return self.__parent__._cast(_4619.MassDiscCompoundParametricStudyTool)

    @property
    def measurement_component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4620.MeasurementComponentCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4620,
        )

        return self.__parent__._cast(
            _4620.MeasurementComponentCompoundParametricStudyTool
        )

    @property
    def microphone_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4622.MicrophoneCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4622,
        )

        return self.__parent__._cast(_4622.MicrophoneCompoundParametricStudyTool)

    @property
    def mountable_component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4623.MountableComponentCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4623,
        )

        return self.__parent__._cast(
            _4623.MountableComponentCompoundParametricStudyTool
        )

    @property
    def oil_seal_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4624.OilSealCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4624,
        )

        return self.__parent__._cast(_4624.OilSealCompoundParametricStudyTool)

    @property
    def part_to_part_shear_coupling_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4628.PartToPartShearCouplingHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4628,
        )

        return self.__parent__._cast(
            _4628.PartToPartShearCouplingHalfCompoundParametricStudyTool
        )

    @property
    def planet_carrier_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4631.PlanetCarrierCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4631,
        )

        return self.__parent__._cast(_4631.PlanetCarrierCompoundParametricStudyTool)

    @property
    def point_load_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4632.PointLoadCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4632,
        )

        return self.__parent__._cast(_4632.PointLoadCompoundParametricStudyTool)

    @property
    def power_load_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4633.PowerLoadCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4633,
        )

        return self.__parent__._cast(_4633.PowerLoadCompoundParametricStudyTool)

    @property
    def pulley_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4634.PulleyCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4634,
        )

        return self.__parent__._cast(_4634.PulleyCompoundParametricStudyTool)

    @property
    def ring_pins_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4635.RingPinsCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4635,
        )

        return self.__parent__._cast(_4635.RingPinsCompoundParametricStudyTool)

    @property
    def rolling_ring_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4638.RollingRingCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4638,
        )

        return self.__parent__._cast(_4638.RollingRingCompoundParametricStudyTool)

    @property
    def shaft_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4641.ShaftCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4641,
        )

        return self.__parent__._cast(_4641.ShaftCompoundParametricStudyTool)

    @property
    def shaft_hub_connection_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4642.ShaftHubConnectionCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4642,
        )

        return self.__parent__._cast(
            _4642.ShaftHubConnectionCompoundParametricStudyTool
        )

    @property
    def spiral_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4645.SpiralBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4645,
        )

        return self.__parent__._cast(_4645.SpiralBevelGearCompoundParametricStudyTool)

    @property
    def spring_damper_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4650.SpringDamperHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4650,
        )

        return self.__parent__._cast(_4650.SpringDamperHalfCompoundParametricStudyTool)

    @property
    def straight_bevel_diff_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4651.StraightBevelDiffGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4651,
        )

        return self.__parent__._cast(
            _4651.StraightBevelDiffGearCompoundParametricStudyTool
        )

    @property
    def straight_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4654.StraightBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4654,
        )

        return self.__parent__._cast(_4654.StraightBevelGearCompoundParametricStudyTool)

    @property
    def straight_bevel_planet_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4657.StraightBevelPlanetGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4657,
        )

        return self.__parent__._cast(
            _4657.StraightBevelPlanetGearCompoundParametricStudyTool
        )

    @property
    def straight_bevel_sun_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4658.StraightBevelSunGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4658,
        )

        return self.__parent__._cast(
            _4658.StraightBevelSunGearCompoundParametricStudyTool
        )

    @property
    def synchroniser_half_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4660.SynchroniserHalfCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4660,
        )

        return self.__parent__._cast(_4660.SynchroniserHalfCompoundParametricStudyTool)

    @property
    def synchroniser_part_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4661.SynchroniserPartCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4661,
        )

        return self.__parent__._cast(_4661.SynchroniserPartCompoundParametricStudyTool)

    @property
    def synchroniser_sleeve_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4662.SynchroniserSleeveCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4662,
        )

        return self.__parent__._cast(
            _4662.SynchroniserSleeveCompoundParametricStudyTool
        )

    @property
    def torque_converter_pump_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4665.TorqueConverterPumpCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4665,
        )

        return self.__parent__._cast(
            _4665.TorqueConverterPumpCompoundParametricStudyTool
        )

    @property
    def torque_converter_turbine_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4666.TorqueConverterTurbineCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4666,
        )

        return self.__parent__._cast(
            _4666.TorqueConverterTurbineCompoundParametricStudyTool
        )

    @property
    def unbalanced_mass_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4667.UnbalancedMassCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4667,
        )

        return self.__parent__._cast(_4667.UnbalancedMassCompoundParametricStudyTool)

    @property
    def virtual_component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4668.VirtualComponentCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4668,
        )

        return self.__parent__._cast(_4668.VirtualComponentCompoundParametricStudyTool)

    @property
    def worm_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4669.WormGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4669,
        )

        return self.__parent__._cast(_4669.WormGearCompoundParametricStudyTool)

    @property
    def zerol_bevel_gear_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "_4672.ZerolBevelGearCompoundParametricStudyTool":
        from mastapy._private.system_model.analyses_and_results.parametric_study_tools.compound import (
            _4672,
        )

        return self.__parent__._cast(_4672.ZerolBevelGearCompoundParametricStudyTool)

    @property
    def component_compound_parametric_study_tool(
        self: "CastSelf",
    ) -> "ComponentCompoundParametricStudyTool":
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
class ComponentCompoundParametricStudyTool(_4625.PartCompoundParametricStudyTool):
    """ComponentCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _COMPONENT_COMPOUND_PARAMETRIC_STUDY_TOOL

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_4420.ComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ComponentParametricStudyTool]

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
    ) -> "List[_4420.ComponentParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ComponentParametricStudyTool]

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
    def cast_to(self: "Self") -> "_Cast_ComponentCompoundParametricStudyTool":
        """Cast to another type.

        Returns:
            _Cast_ComponentCompoundParametricStudyTool
        """
        return _Cast_ComponentCompoundParametricStudyTool(self)
