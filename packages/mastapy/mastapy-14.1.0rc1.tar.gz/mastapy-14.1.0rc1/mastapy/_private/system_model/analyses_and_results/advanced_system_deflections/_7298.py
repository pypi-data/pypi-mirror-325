"""PartAdvancedSystemDeflection"""

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

_PART_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "PartAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.math_utility.convergence import _1635
    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7211,
        _7212,
        _7213,
        _7215,
        _7218,
        _7220,
        _7221,
        _7222,
        _7224,
        _7225,
        _7227,
        _7228,
        _7229,
        _7230,
        _7232,
        _7233,
        _7234,
        _7235,
        _7237,
        _7239,
        _7240,
        _7242,
        _7243,
        _7245,
        _7246,
        _7248,
        _7250,
        _7252,
        _7254,
        _7255,
        _7257,
        _7258,
        _7259,
        _7262,
        _7264,
        _7266,
        _7267,
        _7268,
        _7269,
        _7271,
        _7272,
        _7273,
        _7274,
        _7276,
        _7277,
        _7278,
        _7280,
        _7282,
        _7284,
        _7285,
        _7287,
        _7288,
        _7290,
        _7292,
        _7293,
        _7294,
        _7295,
        _7296,
        _7297,
        _7299,
        _7301,
        _7303,
        _7304,
        _7305,
        _7306,
        _7307,
        _7308,
        _7310,
        _7311,
        _7313,
        _7314,
        _7315,
        _7317,
        _7318,
        _7320,
        _7321,
        _7323,
        _7324,
        _7326,
        _7327,
        _7329,
        _7330,
        _7331,
        _7332,
        _7333,
        _7334,
        _7335,
        _7336,
        _7338,
        _7339,
        _7341,
        _7342,
        _7343,
        _7345,
        _7346,
        _7348,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7706
    from mastapy._private.system_model.drawing import _2310
    from mastapy._private.system_model.part_model import _2537

    Self = TypeVar("Self", bound="PartAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PartAdvancedSystemDeflection._Cast_PartAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartAdvancedSystemDeflection:
    """Special nested class for casting PartAdvancedSystemDeflection to subclasses."""

    __parent__: "PartAdvancedSystemDeflection"

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
    def abstract_assembly_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7211.AbstractAssemblyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7211,
        )

        return self.__parent__._cast(_7211.AbstractAssemblyAdvancedSystemDeflection)

    @property
    def abstract_shaft_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7212.AbstractShaftAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7212,
        )

        return self.__parent__._cast(_7212.AbstractShaftAdvancedSystemDeflection)

    @property
    def abstract_shaft_or_housing_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7213.AbstractShaftOrHousingAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7213,
        )

        return self.__parent__._cast(
            _7213.AbstractShaftOrHousingAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7218.AGMAGleasonConicalGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7218,
        )

        return self.__parent__._cast(
            _7218.AGMAGleasonConicalGearAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7220.AGMAGleasonConicalGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7220,
        )

        return self.__parent__._cast(
            _7220.AGMAGleasonConicalGearSetAdvancedSystemDeflection
        )

    @property
    def assembly_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7221.AssemblyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7221,
        )

        return self.__parent__._cast(_7221.AssemblyAdvancedSystemDeflection)

    @property
    def bearing_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7222.BearingAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7222,
        )

        return self.__parent__._cast(_7222.BearingAdvancedSystemDeflection)

    @property
    def belt_drive_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7224.BeltDriveAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7224,
        )

        return self.__parent__._cast(_7224.BeltDriveAdvancedSystemDeflection)

    @property
    def bevel_differential_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7225.BevelDifferentialGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7225,
        )

        return self.__parent__._cast(
            _7225.BevelDifferentialGearAdvancedSystemDeflection
        )

    @property
    def bevel_differential_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7227.BevelDifferentialGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7227,
        )

        return self.__parent__._cast(
            _7227.BevelDifferentialGearSetAdvancedSystemDeflection
        )

    @property
    def bevel_differential_planet_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7228.BevelDifferentialPlanetGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7228,
        )

        return self.__parent__._cast(
            _7228.BevelDifferentialPlanetGearAdvancedSystemDeflection
        )

    @property
    def bevel_differential_sun_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7229.BevelDifferentialSunGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7229,
        )

        return self.__parent__._cast(
            _7229.BevelDifferentialSunGearAdvancedSystemDeflection
        )

    @property
    def bevel_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7230.BevelGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7230,
        )

        return self.__parent__._cast(_7230.BevelGearAdvancedSystemDeflection)

    @property
    def bevel_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7232.BevelGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7232,
        )

        return self.__parent__._cast(_7232.BevelGearSetAdvancedSystemDeflection)

    @property
    def bolt_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7233.BoltAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7233,
        )

        return self.__parent__._cast(_7233.BoltAdvancedSystemDeflection)

    @property
    def bolted_joint_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7234.BoltedJointAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7234,
        )

        return self.__parent__._cast(_7234.BoltedJointAdvancedSystemDeflection)

    @property
    def clutch_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7235.ClutchAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7235,
        )

        return self.__parent__._cast(_7235.ClutchAdvancedSystemDeflection)

    @property
    def clutch_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7237.ClutchHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7237,
        )

        return self.__parent__._cast(_7237.ClutchHalfAdvancedSystemDeflection)

    @property
    def component_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7239.ComponentAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7239,
        )

        return self.__parent__._cast(_7239.ComponentAdvancedSystemDeflection)

    @property
    def concept_coupling_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7240.ConceptCouplingAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7240,
        )

        return self.__parent__._cast(_7240.ConceptCouplingAdvancedSystemDeflection)

    @property
    def concept_coupling_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7242.ConceptCouplingHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7242,
        )

        return self.__parent__._cast(_7242.ConceptCouplingHalfAdvancedSystemDeflection)

    @property
    def concept_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7243.ConceptGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7243,
        )

        return self.__parent__._cast(_7243.ConceptGearAdvancedSystemDeflection)

    @property
    def concept_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7245.ConceptGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7245,
        )

        return self.__parent__._cast(_7245.ConceptGearSetAdvancedSystemDeflection)

    @property
    def conical_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7246.ConicalGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7246,
        )

        return self.__parent__._cast(_7246.ConicalGearAdvancedSystemDeflection)

    @property
    def conical_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7248.ConicalGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7248,
        )

        return self.__parent__._cast(_7248.ConicalGearSetAdvancedSystemDeflection)

    @property
    def connector_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7250.ConnectorAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7250,
        )

        return self.__parent__._cast(_7250.ConnectorAdvancedSystemDeflection)

    @property
    def coupling_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7252.CouplingAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7252,
        )

        return self.__parent__._cast(_7252.CouplingAdvancedSystemDeflection)

    @property
    def coupling_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7254.CouplingHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7254,
        )

        return self.__parent__._cast(_7254.CouplingHalfAdvancedSystemDeflection)

    @property
    def cvt_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7255.CVTAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7255,
        )

        return self.__parent__._cast(_7255.CVTAdvancedSystemDeflection)

    @property
    def cvt_pulley_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7257.CVTPulleyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7257,
        )

        return self.__parent__._cast(_7257.CVTPulleyAdvancedSystemDeflection)

    @property
    def cycloidal_assembly_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7258.CycloidalAssemblyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7258,
        )

        return self.__parent__._cast(_7258.CycloidalAssemblyAdvancedSystemDeflection)

    @property
    def cycloidal_disc_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7259.CycloidalDiscAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7259,
        )

        return self.__parent__._cast(_7259.CycloidalDiscAdvancedSystemDeflection)

    @property
    def cylindrical_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7262.CylindricalGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7262,
        )

        return self.__parent__._cast(_7262.CylindricalGearAdvancedSystemDeflection)

    @property
    def cylindrical_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7264.CylindricalGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7264,
        )

        return self.__parent__._cast(_7264.CylindricalGearSetAdvancedSystemDeflection)

    @property
    def cylindrical_planet_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7266.CylindricalPlanetGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7266,
        )

        return self.__parent__._cast(
            _7266.CylindricalPlanetGearAdvancedSystemDeflection
        )

    @property
    def datum_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7267.DatumAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7267,
        )

        return self.__parent__._cast(_7267.DatumAdvancedSystemDeflection)

    @property
    def external_cad_model_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7268.ExternalCADModelAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7268,
        )

        return self.__parent__._cast(_7268.ExternalCADModelAdvancedSystemDeflection)

    @property
    def face_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7269.FaceGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7269,
        )

        return self.__parent__._cast(_7269.FaceGearAdvancedSystemDeflection)

    @property
    def face_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7271.FaceGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7271,
        )

        return self.__parent__._cast(_7271.FaceGearSetAdvancedSystemDeflection)

    @property
    def fe_part_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7272.FEPartAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7272,
        )

        return self.__parent__._cast(_7272.FEPartAdvancedSystemDeflection)

    @property
    def flexible_pin_assembly_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7273.FlexiblePinAssemblyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7273,
        )

        return self.__parent__._cast(_7273.FlexiblePinAssemblyAdvancedSystemDeflection)

    @property
    def gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7274.GearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7274,
        )

        return self.__parent__._cast(_7274.GearAdvancedSystemDeflection)

    @property
    def gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7276.GearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7276,
        )

        return self.__parent__._cast(_7276.GearSetAdvancedSystemDeflection)

    @property
    def guide_dxf_model_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7277.GuideDxfModelAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7277,
        )

        return self.__parent__._cast(_7277.GuideDxfModelAdvancedSystemDeflection)

    @property
    def hypoid_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7278.HypoidGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7278,
        )

        return self.__parent__._cast(_7278.HypoidGearAdvancedSystemDeflection)

    @property
    def hypoid_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7280.HypoidGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7280,
        )

        return self.__parent__._cast(_7280.HypoidGearSetAdvancedSystemDeflection)

    @property
    def klingelnberg_cyclo_palloid_conical_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7282.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7282,
        )

        return self.__parent__._cast(
            _7282.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7284.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7284,
        )

        return self.__parent__._cast(
            _7284.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7285.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7285,
        )

        return self.__parent__._cast(
            _7285.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7287.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7287,
        )

        return self.__parent__._cast(
            _7287.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7288.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7288,
        )

        return self.__parent__._cast(
            _7288.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7290.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7290,
        )

        return self.__parent__._cast(
            _7290.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
        )

    @property
    def mass_disc_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7292.MassDiscAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7292,
        )

        return self.__parent__._cast(_7292.MassDiscAdvancedSystemDeflection)

    @property
    def measurement_component_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7293.MeasurementComponentAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7293,
        )

        return self.__parent__._cast(_7293.MeasurementComponentAdvancedSystemDeflection)

    @property
    def microphone_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7294.MicrophoneAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7294,
        )

        return self.__parent__._cast(_7294.MicrophoneAdvancedSystemDeflection)

    @property
    def microphone_array_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7295.MicrophoneArrayAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7295,
        )

        return self.__parent__._cast(_7295.MicrophoneArrayAdvancedSystemDeflection)

    @property
    def mountable_component_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7296.MountableComponentAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7296,
        )

        return self.__parent__._cast(_7296.MountableComponentAdvancedSystemDeflection)

    @property
    def oil_seal_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7297.OilSealAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7297,
        )

        return self.__parent__._cast(_7297.OilSealAdvancedSystemDeflection)

    @property
    def part_to_part_shear_coupling_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7299.PartToPartShearCouplingAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7299,
        )

        return self.__parent__._cast(
            _7299.PartToPartShearCouplingAdvancedSystemDeflection
        )

    @property
    def part_to_part_shear_coupling_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7301.PartToPartShearCouplingHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7301,
        )

        return self.__parent__._cast(
            _7301.PartToPartShearCouplingHalfAdvancedSystemDeflection
        )

    @property
    def planetary_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7303.PlanetaryGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7303,
        )

        return self.__parent__._cast(_7303.PlanetaryGearSetAdvancedSystemDeflection)

    @property
    def planet_carrier_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7304.PlanetCarrierAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7304,
        )

        return self.__parent__._cast(_7304.PlanetCarrierAdvancedSystemDeflection)

    @property
    def point_load_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7305.PointLoadAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7305,
        )

        return self.__parent__._cast(_7305.PointLoadAdvancedSystemDeflection)

    @property
    def power_load_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7306.PowerLoadAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7306,
        )

        return self.__parent__._cast(_7306.PowerLoadAdvancedSystemDeflection)

    @property
    def pulley_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7307.PulleyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7307,
        )

        return self.__parent__._cast(_7307.PulleyAdvancedSystemDeflection)

    @property
    def ring_pins_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7308.RingPinsAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7308,
        )

        return self.__parent__._cast(_7308.RingPinsAdvancedSystemDeflection)

    @property
    def rolling_ring_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7310.RollingRingAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7310,
        )

        return self.__parent__._cast(_7310.RollingRingAdvancedSystemDeflection)

    @property
    def rolling_ring_assembly_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7311.RollingRingAssemblyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7311,
        )

        return self.__parent__._cast(_7311.RollingRingAssemblyAdvancedSystemDeflection)

    @property
    def root_assembly_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7313.RootAssemblyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7313,
        )

        return self.__parent__._cast(_7313.RootAssemblyAdvancedSystemDeflection)

    @property
    def shaft_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7314.ShaftAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7314,
        )

        return self.__parent__._cast(_7314.ShaftAdvancedSystemDeflection)

    @property
    def shaft_hub_connection_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7315.ShaftHubConnectionAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7315,
        )

        return self.__parent__._cast(_7315.ShaftHubConnectionAdvancedSystemDeflection)

    @property
    def specialised_assembly_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7317.SpecialisedAssemblyAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7317,
        )

        return self.__parent__._cast(_7317.SpecialisedAssemblyAdvancedSystemDeflection)

    @property
    def spiral_bevel_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7318.SpiralBevelGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7318,
        )

        return self.__parent__._cast(_7318.SpiralBevelGearAdvancedSystemDeflection)

    @property
    def spiral_bevel_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7320.SpiralBevelGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7320,
        )

        return self.__parent__._cast(_7320.SpiralBevelGearSetAdvancedSystemDeflection)

    @property
    def spring_damper_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7321.SpringDamperAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7321,
        )

        return self.__parent__._cast(_7321.SpringDamperAdvancedSystemDeflection)

    @property
    def spring_damper_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7323.SpringDamperHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7323,
        )

        return self.__parent__._cast(_7323.SpringDamperHalfAdvancedSystemDeflection)

    @property
    def straight_bevel_diff_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7324.StraightBevelDiffGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7324,
        )

        return self.__parent__._cast(
            _7324.StraightBevelDiffGearAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7326.StraightBevelDiffGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7326,
        )

        return self.__parent__._cast(
            _7326.StraightBevelDiffGearSetAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7327.StraightBevelGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7327,
        )

        return self.__parent__._cast(_7327.StraightBevelGearAdvancedSystemDeflection)

    @property
    def straight_bevel_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7329.StraightBevelGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7329,
        )

        return self.__parent__._cast(_7329.StraightBevelGearSetAdvancedSystemDeflection)

    @property
    def straight_bevel_planet_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7330.StraightBevelPlanetGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7330,
        )

        return self.__parent__._cast(
            _7330.StraightBevelPlanetGearAdvancedSystemDeflection
        )

    @property
    def straight_bevel_sun_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7331.StraightBevelSunGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7331,
        )

        return self.__parent__._cast(_7331.StraightBevelSunGearAdvancedSystemDeflection)

    @property
    def synchroniser_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7332.SynchroniserAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7332,
        )

        return self.__parent__._cast(_7332.SynchroniserAdvancedSystemDeflection)

    @property
    def synchroniser_half_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7333.SynchroniserHalfAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7333,
        )

        return self.__parent__._cast(_7333.SynchroniserHalfAdvancedSystemDeflection)

    @property
    def synchroniser_part_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7334.SynchroniserPartAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7334,
        )

        return self.__parent__._cast(_7334.SynchroniserPartAdvancedSystemDeflection)

    @property
    def synchroniser_sleeve_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7335.SynchroniserSleeveAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7335,
        )

        return self.__parent__._cast(_7335.SynchroniserSleeveAdvancedSystemDeflection)

    @property
    def torque_converter_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7336.TorqueConverterAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7336,
        )

        return self.__parent__._cast(_7336.TorqueConverterAdvancedSystemDeflection)

    @property
    def torque_converter_pump_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7338.TorqueConverterPumpAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7338,
        )

        return self.__parent__._cast(_7338.TorqueConverterPumpAdvancedSystemDeflection)

    @property
    def torque_converter_turbine_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7339.TorqueConverterTurbineAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7339,
        )

        return self.__parent__._cast(
            _7339.TorqueConverterTurbineAdvancedSystemDeflection
        )

    @property
    def unbalanced_mass_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7341.UnbalancedMassAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7341,
        )

        return self.__parent__._cast(_7341.UnbalancedMassAdvancedSystemDeflection)

    @property
    def virtual_component_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7342.VirtualComponentAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7342,
        )

        return self.__parent__._cast(_7342.VirtualComponentAdvancedSystemDeflection)

    @property
    def worm_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7343.WormGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7343,
        )

        return self.__parent__._cast(_7343.WormGearAdvancedSystemDeflection)

    @property
    def worm_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7345.WormGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7345,
        )

        return self.__parent__._cast(_7345.WormGearSetAdvancedSystemDeflection)

    @property
    def zerol_bevel_gear_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7346.ZerolBevelGearAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7346,
        )

        return self.__parent__._cast(_7346.ZerolBevelGearAdvancedSystemDeflection)

    @property
    def zerol_bevel_gear_set_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7348.ZerolBevelGearSetAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
            _7348,
        )

        return self.__parent__._cast(_7348.ZerolBevelGearSetAdvancedSystemDeflection)

    @property
    def part_advanced_system_deflection(
        self: "CastSelf",
    ) -> "PartAdvancedSystemDeflection":
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
class PartAdvancedSystemDeflection(_7709.PartStaticLoadAnalysisCase):
    """PartAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_ADVANCED_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def advanced_system_deflection(self: "Self") -> "_7215.AdvancedSystemDeflection":
        """mastapy.system_model.analyses_and_results.advanced_system_deflections.AdvancedSystemDeflection

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "AdvancedSystemDeflection")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def data_logger(self: "Self") -> "_1635.DataLogger":
        """mastapy.math_utility.convergence.DataLogger

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(self.wrapped, "DataLogger")

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: "Self") -> "_2310.AdvancedSystemDeflectionViewable":
        """mastapy.system_model.drawing.AdvancedSystemDeflectionViewable"""
        method_result = pythonnet_method_call(self.wrapped, "CreateViewable")
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: "Self") -> "_Cast_PartAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_PartAdvancedSystemDeflection
        """
        return _Cast_PartAdvancedSystemDeflection(self)
