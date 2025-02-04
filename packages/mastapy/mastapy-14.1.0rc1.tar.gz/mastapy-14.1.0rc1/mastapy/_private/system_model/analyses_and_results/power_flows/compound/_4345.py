"""PartCompoundPowerFlow"""

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

_PART_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PartCompoundPowerFlow",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7704
    from mastapy._private.system_model.analyses_and_results.power_flows import _4211
    from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
        _4264,
        _4265,
        _4266,
        _4268,
        _4270,
        _4271,
        _4272,
        _4274,
        _4275,
        _4277,
        _4278,
        _4279,
        _4280,
        _4282,
        _4283,
        _4284,
        _4285,
        _4287,
        _4289,
        _4290,
        _4292,
        _4293,
        _4295,
        _4296,
        _4298,
        _4300,
        _4301,
        _4303,
        _4305,
        _4306,
        _4307,
        _4309,
        _4311,
        _4313,
        _4314,
        _4315,
        _4316,
        _4317,
        _4319,
        _4320,
        _4321,
        _4322,
        _4324,
        _4325,
        _4326,
        _4328,
        _4330,
        _4332,
        _4333,
        _4335,
        _4336,
        _4338,
        _4339,
        _4340,
        _4341,
        _4342,
        _4343,
        _4344,
        _4346,
        _4348,
        _4350,
        _4351,
        _4352,
        _4353,
        _4354,
        _4355,
        _4357,
        _4358,
        _4360,
        _4361,
        _4362,
        _4364,
        _4365,
        _4367,
        _4368,
        _4370,
        _4371,
        _4373,
        _4374,
        _4376,
        _4377,
        _4378,
        _4379,
        _4380,
        _4381,
        _4382,
        _4383,
        _4385,
        _4386,
        _4387,
        _4388,
        _4389,
        _4391,
        _4392,
        _4394,
    )

    Self = TypeVar("Self", bound="PartCompoundPowerFlow")
    CastSelf = TypeVar(
        "CastSelf", bound="PartCompoundPowerFlow._Cast_PartCompoundPowerFlow"
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartCompoundPowerFlow:
    """Special nested class for casting PartCompoundPowerFlow to subclasses."""

    __parent__: "PartCompoundPowerFlow"

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
    def abstract_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4264.AbstractAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4264,
        )

        return self.__parent__._cast(_4264.AbstractAssemblyCompoundPowerFlow)

    @property
    def abstract_shaft_compound_power_flow(
        self: "CastSelf",
    ) -> "_4265.AbstractShaftCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4265,
        )

        return self.__parent__._cast(_4265.AbstractShaftCompoundPowerFlow)

    @property
    def abstract_shaft_or_housing_compound_power_flow(
        self: "CastSelf",
    ) -> "_4266.AbstractShaftOrHousingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4266,
        )

        return self.__parent__._cast(_4266.AbstractShaftOrHousingCompoundPowerFlow)

    @property
    def agma_gleason_conical_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4268.AGMAGleasonConicalGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4268,
        )

        return self.__parent__._cast(_4268.AGMAGleasonConicalGearCompoundPowerFlow)

    @property
    def agma_gleason_conical_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4270.AGMAGleasonConicalGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4270,
        )

        return self.__parent__._cast(_4270.AGMAGleasonConicalGearSetCompoundPowerFlow)

    @property
    def assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4271.AssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4271,
        )

        return self.__parent__._cast(_4271.AssemblyCompoundPowerFlow)

    @property
    def bearing_compound_power_flow(
        self: "CastSelf",
    ) -> "_4272.BearingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4272,
        )

        return self.__parent__._cast(_4272.BearingCompoundPowerFlow)

    @property
    def belt_drive_compound_power_flow(
        self: "CastSelf",
    ) -> "_4274.BeltDriveCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4274,
        )

        return self.__parent__._cast(_4274.BeltDriveCompoundPowerFlow)

    @property
    def bevel_differential_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4275.BevelDifferentialGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4275,
        )

        return self.__parent__._cast(_4275.BevelDifferentialGearCompoundPowerFlow)

    @property
    def bevel_differential_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4277.BevelDifferentialGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4277,
        )

        return self.__parent__._cast(_4277.BevelDifferentialGearSetCompoundPowerFlow)

    @property
    def bevel_differential_planet_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4278.BevelDifferentialPlanetGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4278,
        )

        return self.__parent__._cast(_4278.BevelDifferentialPlanetGearCompoundPowerFlow)

    @property
    def bevel_differential_sun_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4279.BevelDifferentialSunGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4279,
        )

        return self.__parent__._cast(_4279.BevelDifferentialSunGearCompoundPowerFlow)

    @property
    def bevel_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4280.BevelGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4280,
        )

        return self.__parent__._cast(_4280.BevelGearCompoundPowerFlow)

    @property
    def bevel_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4282.BevelGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4282,
        )

        return self.__parent__._cast(_4282.BevelGearSetCompoundPowerFlow)

    @property
    def bolt_compound_power_flow(self: "CastSelf") -> "_4283.BoltCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4283,
        )

        return self.__parent__._cast(_4283.BoltCompoundPowerFlow)

    @property
    def bolted_joint_compound_power_flow(
        self: "CastSelf",
    ) -> "_4284.BoltedJointCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4284,
        )

        return self.__parent__._cast(_4284.BoltedJointCompoundPowerFlow)

    @property
    def clutch_compound_power_flow(self: "CastSelf") -> "_4285.ClutchCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4285,
        )

        return self.__parent__._cast(_4285.ClutchCompoundPowerFlow)

    @property
    def clutch_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4287.ClutchHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4287,
        )

        return self.__parent__._cast(_4287.ClutchHalfCompoundPowerFlow)

    @property
    def component_compound_power_flow(
        self: "CastSelf",
    ) -> "_4289.ComponentCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4289,
        )

        return self.__parent__._cast(_4289.ComponentCompoundPowerFlow)

    @property
    def concept_coupling_compound_power_flow(
        self: "CastSelf",
    ) -> "_4290.ConceptCouplingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4290,
        )

        return self.__parent__._cast(_4290.ConceptCouplingCompoundPowerFlow)

    @property
    def concept_coupling_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4292.ConceptCouplingHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4292,
        )

        return self.__parent__._cast(_4292.ConceptCouplingHalfCompoundPowerFlow)

    @property
    def concept_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4293.ConceptGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4293,
        )

        return self.__parent__._cast(_4293.ConceptGearCompoundPowerFlow)

    @property
    def concept_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4295.ConceptGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4295,
        )

        return self.__parent__._cast(_4295.ConceptGearSetCompoundPowerFlow)

    @property
    def conical_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4296.ConicalGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4296,
        )

        return self.__parent__._cast(_4296.ConicalGearCompoundPowerFlow)

    @property
    def conical_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4298.ConicalGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4298,
        )

        return self.__parent__._cast(_4298.ConicalGearSetCompoundPowerFlow)

    @property
    def connector_compound_power_flow(
        self: "CastSelf",
    ) -> "_4300.ConnectorCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4300,
        )

        return self.__parent__._cast(_4300.ConnectorCompoundPowerFlow)

    @property
    def coupling_compound_power_flow(
        self: "CastSelf",
    ) -> "_4301.CouplingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4301,
        )

        return self.__parent__._cast(_4301.CouplingCompoundPowerFlow)

    @property
    def coupling_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4303.CouplingHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4303,
        )

        return self.__parent__._cast(_4303.CouplingHalfCompoundPowerFlow)

    @property
    def cvt_compound_power_flow(self: "CastSelf") -> "_4305.CVTCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4305,
        )

        return self.__parent__._cast(_4305.CVTCompoundPowerFlow)

    @property
    def cvt_pulley_compound_power_flow(
        self: "CastSelf",
    ) -> "_4306.CVTPulleyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4306,
        )

        return self.__parent__._cast(_4306.CVTPulleyCompoundPowerFlow)

    @property
    def cycloidal_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4307.CycloidalAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4307,
        )

        return self.__parent__._cast(_4307.CycloidalAssemblyCompoundPowerFlow)

    @property
    def cycloidal_disc_compound_power_flow(
        self: "CastSelf",
    ) -> "_4309.CycloidalDiscCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4309,
        )

        return self.__parent__._cast(_4309.CycloidalDiscCompoundPowerFlow)

    @property
    def cylindrical_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4311.CylindricalGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4311,
        )

        return self.__parent__._cast(_4311.CylindricalGearCompoundPowerFlow)

    @property
    def cylindrical_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4313.CylindricalGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4313,
        )

        return self.__parent__._cast(_4313.CylindricalGearSetCompoundPowerFlow)

    @property
    def cylindrical_planet_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4314.CylindricalPlanetGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4314,
        )

        return self.__parent__._cast(_4314.CylindricalPlanetGearCompoundPowerFlow)

    @property
    def datum_compound_power_flow(self: "CastSelf") -> "_4315.DatumCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4315,
        )

        return self.__parent__._cast(_4315.DatumCompoundPowerFlow)

    @property
    def external_cad_model_compound_power_flow(
        self: "CastSelf",
    ) -> "_4316.ExternalCADModelCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4316,
        )

        return self.__parent__._cast(_4316.ExternalCADModelCompoundPowerFlow)

    @property
    def face_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4317.FaceGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4317,
        )

        return self.__parent__._cast(_4317.FaceGearCompoundPowerFlow)

    @property
    def face_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4319.FaceGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4319,
        )

        return self.__parent__._cast(_4319.FaceGearSetCompoundPowerFlow)

    @property
    def fe_part_compound_power_flow(
        self: "CastSelf",
    ) -> "_4320.FEPartCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4320,
        )

        return self.__parent__._cast(_4320.FEPartCompoundPowerFlow)

    @property
    def flexible_pin_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4321.FlexiblePinAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4321,
        )

        return self.__parent__._cast(_4321.FlexiblePinAssemblyCompoundPowerFlow)

    @property
    def gear_compound_power_flow(self: "CastSelf") -> "_4322.GearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4322,
        )

        return self.__parent__._cast(_4322.GearCompoundPowerFlow)

    @property
    def gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4324.GearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4324,
        )

        return self.__parent__._cast(_4324.GearSetCompoundPowerFlow)

    @property
    def guide_dxf_model_compound_power_flow(
        self: "CastSelf",
    ) -> "_4325.GuideDxfModelCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4325,
        )

        return self.__parent__._cast(_4325.GuideDxfModelCompoundPowerFlow)

    @property
    def hypoid_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4326.HypoidGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4326,
        )

        return self.__parent__._cast(_4326.HypoidGearCompoundPowerFlow)

    @property
    def hypoid_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4328.HypoidGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4328,
        )

        return self.__parent__._cast(_4328.HypoidGearSetCompoundPowerFlow)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4330.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4330,
        )

        return self.__parent__._cast(
            _4330.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4332.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4332,
        )

        return self.__parent__._cast(
            _4332.KlingelnbergCycloPalloidConicalGearSetCompoundPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4333.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4333,
        )

        return self.__parent__._cast(
            _4333.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4335.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4335,
        )

        return self.__parent__._cast(
            _4335.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4336.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4336,
        )

        return self.__parent__._cast(
            _4336.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4338.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4338,
        )

        return self.__parent__._cast(
            _4338.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow
        )

    @property
    def mass_disc_compound_power_flow(
        self: "CastSelf",
    ) -> "_4339.MassDiscCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4339,
        )

        return self.__parent__._cast(_4339.MassDiscCompoundPowerFlow)

    @property
    def measurement_component_compound_power_flow(
        self: "CastSelf",
    ) -> "_4340.MeasurementComponentCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4340,
        )

        return self.__parent__._cast(_4340.MeasurementComponentCompoundPowerFlow)

    @property
    def microphone_array_compound_power_flow(
        self: "CastSelf",
    ) -> "_4341.MicrophoneArrayCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4341,
        )

        return self.__parent__._cast(_4341.MicrophoneArrayCompoundPowerFlow)

    @property
    def microphone_compound_power_flow(
        self: "CastSelf",
    ) -> "_4342.MicrophoneCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4342,
        )

        return self.__parent__._cast(_4342.MicrophoneCompoundPowerFlow)

    @property
    def mountable_component_compound_power_flow(
        self: "CastSelf",
    ) -> "_4343.MountableComponentCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4343,
        )

        return self.__parent__._cast(_4343.MountableComponentCompoundPowerFlow)

    @property
    def oil_seal_compound_power_flow(
        self: "CastSelf",
    ) -> "_4344.OilSealCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4344,
        )

        return self.__parent__._cast(_4344.OilSealCompoundPowerFlow)

    @property
    def part_to_part_shear_coupling_compound_power_flow(
        self: "CastSelf",
    ) -> "_4346.PartToPartShearCouplingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4346,
        )

        return self.__parent__._cast(_4346.PartToPartShearCouplingCompoundPowerFlow)

    @property
    def part_to_part_shear_coupling_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4348.PartToPartShearCouplingHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4348,
        )

        return self.__parent__._cast(_4348.PartToPartShearCouplingHalfCompoundPowerFlow)

    @property
    def planetary_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4350.PlanetaryGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4350,
        )

        return self.__parent__._cast(_4350.PlanetaryGearSetCompoundPowerFlow)

    @property
    def planet_carrier_compound_power_flow(
        self: "CastSelf",
    ) -> "_4351.PlanetCarrierCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4351,
        )

        return self.__parent__._cast(_4351.PlanetCarrierCompoundPowerFlow)

    @property
    def point_load_compound_power_flow(
        self: "CastSelf",
    ) -> "_4352.PointLoadCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4352,
        )

        return self.__parent__._cast(_4352.PointLoadCompoundPowerFlow)

    @property
    def power_load_compound_power_flow(
        self: "CastSelf",
    ) -> "_4353.PowerLoadCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4353,
        )

        return self.__parent__._cast(_4353.PowerLoadCompoundPowerFlow)

    @property
    def pulley_compound_power_flow(self: "CastSelf") -> "_4354.PulleyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4354,
        )

        return self.__parent__._cast(_4354.PulleyCompoundPowerFlow)

    @property
    def ring_pins_compound_power_flow(
        self: "CastSelf",
    ) -> "_4355.RingPinsCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4355,
        )

        return self.__parent__._cast(_4355.RingPinsCompoundPowerFlow)

    @property
    def rolling_ring_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4357.RollingRingAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4357,
        )

        return self.__parent__._cast(_4357.RollingRingAssemblyCompoundPowerFlow)

    @property
    def rolling_ring_compound_power_flow(
        self: "CastSelf",
    ) -> "_4358.RollingRingCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4358,
        )

        return self.__parent__._cast(_4358.RollingRingCompoundPowerFlow)

    @property
    def root_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4360.RootAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4360,
        )

        return self.__parent__._cast(_4360.RootAssemblyCompoundPowerFlow)

    @property
    def shaft_compound_power_flow(self: "CastSelf") -> "_4361.ShaftCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4361,
        )

        return self.__parent__._cast(_4361.ShaftCompoundPowerFlow)

    @property
    def shaft_hub_connection_compound_power_flow(
        self: "CastSelf",
    ) -> "_4362.ShaftHubConnectionCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4362,
        )

        return self.__parent__._cast(_4362.ShaftHubConnectionCompoundPowerFlow)

    @property
    def specialised_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4364.SpecialisedAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4364,
        )

        return self.__parent__._cast(_4364.SpecialisedAssemblyCompoundPowerFlow)

    @property
    def spiral_bevel_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4365.SpiralBevelGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4365,
        )

        return self.__parent__._cast(_4365.SpiralBevelGearCompoundPowerFlow)

    @property
    def spiral_bevel_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4367.SpiralBevelGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4367,
        )

        return self.__parent__._cast(_4367.SpiralBevelGearSetCompoundPowerFlow)

    @property
    def spring_damper_compound_power_flow(
        self: "CastSelf",
    ) -> "_4368.SpringDamperCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4368,
        )

        return self.__parent__._cast(_4368.SpringDamperCompoundPowerFlow)

    @property
    def spring_damper_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4370.SpringDamperHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4370,
        )

        return self.__parent__._cast(_4370.SpringDamperHalfCompoundPowerFlow)

    @property
    def straight_bevel_diff_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4371.StraightBevelDiffGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4371,
        )

        return self.__parent__._cast(_4371.StraightBevelDiffGearCompoundPowerFlow)

    @property
    def straight_bevel_diff_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4373.StraightBevelDiffGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4373,
        )

        return self.__parent__._cast(_4373.StraightBevelDiffGearSetCompoundPowerFlow)

    @property
    def straight_bevel_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4374.StraightBevelGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4374,
        )

        return self.__parent__._cast(_4374.StraightBevelGearCompoundPowerFlow)

    @property
    def straight_bevel_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4376.StraightBevelGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4376,
        )

        return self.__parent__._cast(_4376.StraightBevelGearSetCompoundPowerFlow)

    @property
    def straight_bevel_planet_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4377.StraightBevelPlanetGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4377,
        )

        return self.__parent__._cast(_4377.StraightBevelPlanetGearCompoundPowerFlow)

    @property
    def straight_bevel_sun_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4378.StraightBevelSunGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4378,
        )

        return self.__parent__._cast(_4378.StraightBevelSunGearCompoundPowerFlow)

    @property
    def synchroniser_compound_power_flow(
        self: "CastSelf",
    ) -> "_4379.SynchroniserCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4379,
        )

        return self.__parent__._cast(_4379.SynchroniserCompoundPowerFlow)

    @property
    def synchroniser_half_compound_power_flow(
        self: "CastSelf",
    ) -> "_4380.SynchroniserHalfCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4380,
        )

        return self.__parent__._cast(_4380.SynchroniserHalfCompoundPowerFlow)

    @property
    def synchroniser_part_compound_power_flow(
        self: "CastSelf",
    ) -> "_4381.SynchroniserPartCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4381,
        )

        return self.__parent__._cast(_4381.SynchroniserPartCompoundPowerFlow)

    @property
    def synchroniser_sleeve_compound_power_flow(
        self: "CastSelf",
    ) -> "_4382.SynchroniserSleeveCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4382,
        )

        return self.__parent__._cast(_4382.SynchroniserSleeveCompoundPowerFlow)

    @property
    def torque_converter_compound_power_flow(
        self: "CastSelf",
    ) -> "_4383.TorqueConverterCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4383,
        )

        return self.__parent__._cast(_4383.TorqueConverterCompoundPowerFlow)

    @property
    def torque_converter_pump_compound_power_flow(
        self: "CastSelf",
    ) -> "_4385.TorqueConverterPumpCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4385,
        )

        return self.__parent__._cast(_4385.TorqueConverterPumpCompoundPowerFlow)

    @property
    def torque_converter_turbine_compound_power_flow(
        self: "CastSelf",
    ) -> "_4386.TorqueConverterTurbineCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4386,
        )

        return self.__parent__._cast(_4386.TorqueConverterTurbineCompoundPowerFlow)

    @property
    def unbalanced_mass_compound_power_flow(
        self: "CastSelf",
    ) -> "_4387.UnbalancedMassCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4387,
        )

        return self.__parent__._cast(_4387.UnbalancedMassCompoundPowerFlow)

    @property
    def virtual_component_compound_power_flow(
        self: "CastSelf",
    ) -> "_4388.VirtualComponentCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4388,
        )

        return self.__parent__._cast(_4388.VirtualComponentCompoundPowerFlow)

    @property
    def worm_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4389.WormGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4389,
        )

        return self.__parent__._cast(_4389.WormGearCompoundPowerFlow)

    @property
    def worm_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4391.WormGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4391,
        )

        return self.__parent__._cast(_4391.WormGearSetCompoundPowerFlow)

    @property
    def zerol_bevel_gear_compound_power_flow(
        self: "CastSelf",
    ) -> "_4392.ZerolBevelGearCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4392,
        )

        return self.__parent__._cast(_4392.ZerolBevelGearCompoundPowerFlow)

    @property
    def zerol_bevel_gear_set_compound_power_flow(
        self: "CastSelf",
    ) -> "_4394.ZerolBevelGearSetCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4394,
        )

        return self.__parent__._cast(_4394.ZerolBevelGearSetCompoundPowerFlow)

    @property
    def part_compound_power_flow(self: "CastSelf") -> "PartCompoundPowerFlow":
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
class PartCompoundPowerFlow(_7707.PartCompoundAnalysis):
    """PartCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_COMPOUND_POWER_FLOW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(self: "Self") -> "List[_4211.PartPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PartPowerFlow]

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
    def component_analysis_cases_ready(self: "Self") -> "List[_4211.PartPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PartPowerFlow]

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
    def cast_to(self: "Self") -> "_Cast_PartCompoundPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_PartCompoundPowerFlow
        """
        return _Cast_PartCompoundPowerFlow(self)
