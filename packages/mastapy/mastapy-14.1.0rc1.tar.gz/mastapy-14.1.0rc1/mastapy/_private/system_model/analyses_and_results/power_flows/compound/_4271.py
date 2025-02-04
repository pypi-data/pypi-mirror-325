"""AssemblyCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, conversion, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
    _4264,
)

_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "AssemblyCompoundPowerFlow",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.gears.analysis import _1275
    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.analysis_cases import (
        _7704,
        _7707,
    )
    from mastapy._private.system_model.analyses_and_results.power_flows import _4134
    from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
        _4272,
        _4274,
        _4277,
        _4283,
        _4284,
        _4285,
        _4290,
        _4295,
        _4305,
        _4307,
        _4309,
        _4313,
        _4319,
        _4320,
        _4321,
        _4328,
        _4335,
        _4338,
        _4339,
        _4340,
        _4342,
        _4344,
        _4345,
        _4346,
        _4351,
        _4352,
        _4353,
        _4355,
        _4357,
        _4360,
        _4361,
        _4362,
        _4367,
        _4368,
        _4373,
        _4376,
        _4379,
        _4383,
        _4387,
        _4391,
        _4394,
    )
    from mastapy._private.system_model.part_model import _2500

    Self = TypeVar("Self", bound="AssemblyCompoundPowerFlow")
    CastSelf = TypeVar(
        "CastSelf", bound="AssemblyCompoundPowerFlow._Cast_AssemblyCompoundPowerFlow"
    )


__docformat__ = "restructuredtext en"
__all__ = ("AssemblyCompoundPowerFlow",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_AssemblyCompoundPowerFlow:
    """Special nested class for casting AssemblyCompoundPowerFlow to subclasses."""

    __parent__: "AssemblyCompoundPowerFlow"

    @property
    def abstract_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4264.AbstractAssemblyCompoundPowerFlow":
        return self.__parent__._cast(_4264.AbstractAssemblyCompoundPowerFlow)

    @property
    def part_compound_power_flow(self: "CastSelf") -> "_4345.PartCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4345,
        )

        return self.__parent__._cast(_4345.PartCompoundPowerFlow)

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
    def root_assembly_compound_power_flow(
        self: "CastSelf",
    ) -> "_4360.RootAssemblyCompoundPowerFlow":
        from mastapy._private.system_model.analyses_and_results.power_flows.compound import (
            _4360,
        )

        return self.__parent__._cast(_4360.RootAssemblyCompoundPowerFlow)

    @property
    def assembly_compound_power_flow(self: "CastSelf") -> "AssemblyCompoundPowerFlow":
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
class AssemblyCompoundPowerFlow(_4264.AbstractAssemblyCompoundPowerFlow):
    """AssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _ASSEMBLY_COMPOUND_POWER_FLOW

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def input_power_load_ratio_warning(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "InputPowerLoadRatioWarning")

        if temp is None:
            return ""

        return temp

    @property
    def output_power_load_ratio_warning(self: "Self") -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "OutputPowerLoadRatioWarning")

        if temp is None:
            return ""

        return temp

    @property
    def component_design(self: "Self") -> "_2500.Assembly":
        """mastapy.system_model.part_model.Assembly

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ComponentDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: "Self") -> "_2500.Assembly":
        """mastapy.system_model.part_model.Assembly

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyDesign")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating_for_all_gear_sets(self: "Self") -> "_1275.GearSetGroupDutyCycle":
        """mastapy.gears.analysis.GearSetGroupDutyCycle

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "RatingForAllGearSets")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(self: "Self") -> "List[_4134.AssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AssemblyPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyAnalysisCasesReady")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bearings(self: "Self") -> "List[_4272.BearingCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BearingCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Bearings")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def belt_drives(self: "Self") -> "List[_4274.BeltDriveCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BeltDriveCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "BeltDrives")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gear_sets(
        self: "Self",
    ) -> "List[_4277.BevelDifferentialGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BevelDifferentialGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "BevelDifferentialGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bolted_joints(self: "Self") -> "List[_4284.BoltedJointCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BoltedJointCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "BoltedJoints")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bolts(self: "Self") -> "List[_4283.BoltCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.BoltCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Bolts")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cv_ts(self: "Self") -> "List[_4305.CVTCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.CVTCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CVTs")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def clutches(self: "Self") -> "List[_4285.ClutchCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ClutchCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Clutches")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_couplings(
        self: "Self",
    ) -> "List[_4290.ConceptCouplingCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptCouplingCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConceptCouplings")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_gear_sets(
        self: "Self",
    ) -> "List[_4295.ConceptGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ConceptGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ConceptGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cycloidal_assemblies(
        self: "Self",
    ) -> "List[_4307.CycloidalAssemblyCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.CycloidalAssemblyCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CycloidalAssemblies")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cycloidal_discs(self: "Self") -> "List[_4309.CycloidalDiscCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.CycloidalDiscCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CycloidalDiscs")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_sets(
        self: "Self",
    ) -> "List[_4313.CylindricalGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.CylindricalGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "CylindricalGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def fe_parts(self: "Self") -> "List[_4320.FEPartCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.FEPartCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "FEParts")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gear_sets(self: "Self") -> "List[_4319.FaceGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.FaceGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "FaceGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def flexible_pin_assemblies(
        self: "Self",
    ) -> "List[_4321.FlexiblePinAssemblyCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.FlexiblePinAssemblyCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "FlexiblePinAssemblies")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_gear_sets(self: "Self") -> "List[_4328.HypoidGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.HypoidGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "HypoidGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(
        self: "Self",
    ) -> "List[_4335.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "KlingelnbergCycloPalloidHypoidGearSets"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(
        self: "Self",
    ) -> "List[_4338.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "KlingelnbergCycloPalloidSpiralBevelGearSets"
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mass_discs(self: "Self") -> "List[_4339.MassDiscCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.MassDiscCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "MassDiscs")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def measurement_components(
        self: "Self",
    ) -> "List[_4340.MeasurementComponentCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.MeasurementComponentCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "MeasurementComponents")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def microphones(self: "Self") -> "List[_4342.MicrophoneCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.MicrophoneCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Microphones")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def oil_seals(self: "Self") -> "List[_4344.OilSealCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.OilSealCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "OilSeals")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def part_to_part_shear_couplings(
        self: "Self",
    ) -> "List[_4346.PartToPartShearCouplingCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.PartToPartShearCouplingCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "PartToPartShearCouplings")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planet_carriers(self: "Self") -> "List[_4351.PlanetCarrierCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.PlanetCarrierCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "PlanetCarriers")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def point_loads(self: "Self") -> "List[_4352.PointLoadCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.PointLoadCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "PointLoads")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_loads(self: "Self") -> "List[_4353.PowerLoadCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.PowerLoadCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "PowerLoads")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def ring_pins(self: "Self") -> "List[_4355.RingPinsCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.RingPinsCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "RingPins")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rolling_ring_assemblies(
        self: "Self",
    ) -> "List[_4357.RollingRingAssemblyCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.RollingRingAssemblyCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "RollingRingAssemblies")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_hub_connections(
        self: "Self",
    ) -> "List[_4362.ShaftHubConnectionCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ShaftHubConnectionCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ShaftHubConnections")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shafts(self: "Self") -> "List[_4361.ShaftCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ShaftCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Shafts")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gear_sets(
        self: "Self",
    ) -> "List[_4367.SpiralBevelGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.SpiralBevelGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SpiralBevelGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spring_dampers(self: "Self") -> "List[_4368.SpringDamperCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.SpringDamperCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "SpringDampers")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_gear_sets(
        self: "Self",
    ) -> "List[_4373.StraightBevelDiffGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelDiffGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "StraightBevelDiffGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gear_sets(
        self: "Self",
    ) -> "List[_4376.StraightBevelGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.StraightBevelGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "StraightBevelGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def synchronisers(self: "Self") -> "List[_4379.SynchroniserCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.SynchroniserCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "Synchronisers")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def torque_converters(
        self: "Self",
    ) -> "List[_4383.TorqueConverterCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.TorqueConverterCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "TorqueConverters")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def unbalanced_masses(
        self: "Self",
    ) -> "List[_4387.UnbalancedMassCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.UnbalancedMassCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "UnbalancedMasses")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def worm_gear_sets(self: "Self") -> "List[_4391.WormGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.WormGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "WormGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gear_sets(
        self: "Self",
    ) -> "List[_4394.ZerolBevelGearSetCompoundPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.compound.ZerolBevelGearSetCompoundPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "ZerolBevelGearSets")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: "Self") -> "List[_4134.AssemblyPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.AssemblyPowerFlow]

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AssemblyAnalysisCases")

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: "Self") -> "_Cast_AssemblyCompoundPowerFlow":
        """Cast to another type.

        Returns:
            _Cast_AssemblyCompoundPowerFlow
        """
        return _Cast_AssemblyCompoundPowerFlow(self)
