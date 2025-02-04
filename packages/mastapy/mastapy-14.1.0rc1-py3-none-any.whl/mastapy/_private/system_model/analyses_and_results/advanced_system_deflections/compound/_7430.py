"""PartCompoundAdvancedSystemDeflection"""

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

_PART_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "PartCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from typing import Any, List, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections import (
        _7298,
    )
    from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7349,
        _7350,
        _7351,
        _7353,
        _7355,
        _7356,
        _7357,
        _7359,
        _7360,
        _7362,
        _7363,
        _7364,
        _7365,
        _7367,
        _7368,
        _7369,
        _7370,
        _7372,
        _7374,
        _7375,
        _7377,
        _7378,
        _7380,
        _7381,
        _7383,
        _7385,
        _7386,
        _7388,
        _7390,
        _7391,
        _7392,
        _7394,
        _7396,
        _7398,
        _7399,
        _7400,
        _7401,
        _7402,
        _7404,
        _7405,
        _7406,
        _7407,
        _7409,
        _7410,
        _7411,
        _7413,
        _7415,
        _7417,
        _7418,
        _7420,
        _7421,
        _7423,
        _7424,
        _7425,
        _7426,
        _7427,
        _7428,
        _7429,
        _7431,
        _7433,
        _7435,
        _7436,
        _7437,
        _7438,
        _7439,
        _7440,
        _7442,
        _7443,
        _7445,
        _7446,
        _7447,
        _7449,
        _7450,
        _7452,
        _7453,
        _7455,
        _7456,
        _7458,
        _7459,
        _7461,
        _7462,
        _7463,
        _7464,
        _7465,
        _7466,
        _7467,
        _7468,
        _7470,
        _7471,
        _7472,
        _7473,
        _7474,
        _7476,
        _7477,
        _7479,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7704

    Self = TypeVar("Self", bound="PartCompoundAdvancedSystemDeflection")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundAdvancedSystemDeflection",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartCompoundAdvancedSystemDeflection:
    """Special nested class for casting PartCompoundAdvancedSystemDeflection to subclasses."""

    __parent__: "PartCompoundAdvancedSystemDeflection"

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
    def abstract_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7349.AbstractAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7349,
        )

        return self.__parent__._cast(
            _7349.AbstractAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def abstract_shaft_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7350.AbstractShaftCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7350,
        )

        return self.__parent__._cast(
            _7350.AbstractShaftCompoundAdvancedSystemDeflection
        )

    @property
    def abstract_shaft_or_housing_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7351.AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7351,
        )

        return self.__parent__._cast(
            _7351.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7353.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7353,
        )

        return self.__parent__._cast(
            _7353.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
        )

    @property
    def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7355.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7355,
        )

        return self.__parent__._cast(
            _7355.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7356.AssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7356,
        )

        return self.__parent__._cast(_7356.AssemblyCompoundAdvancedSystemDeflection)

    @property
    def bearing_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7357.BearingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7357,
        )

        return self.__parent__._cast(_7357.BearingCompoundAdvancedSystemDeflection)

    @property
    def belt_drive_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7359.BeltDriveCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7359,
        )

        return self.__parent__._cast(_7359.BeltDriveCompoundAdvancedSystemDeflection)

    @property
    def bevel_differential_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7360.BevelDifferentialGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7360,
        )

        return self.__parent__._cast(
            _7360.BevelDifferentialGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7362.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7362,
        )

        return self.__parent__._cast(
            _7362.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7363.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7363,
        )

        return self.__parent__._cast(
            _7363.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_differential_sun_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7364.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7364,
        )

        return self.__parent__._cast(
            _7364.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
        )

    @property
    def bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7365.BevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7365,
        )

        return self.__parent__._cast(_7365.BevelGearCompoundAdvancedSystemDeflection)

    @property
    def bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7367.BevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7367,
        )

        return self.__parent__._cast(_7367.BevelGearSetCompoundAdvancedSystemDeflection)

    @property
    def bolt_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7368.BoltCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7368,
        )

        return self.__parent__._cast(_7368.BoltCompoundAdvancedSystemDeflection)

    @property
    def bolted_joint_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7369.BoltedJointCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7369,
        )

        return self.__parent__._cast(_7369.BoltedJointCompoundAdvancedSystemDeflection)

    @property
    def clutch_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7370.ClutchCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7370,
        )

        return self.__parent__._cast(_7370.ClutchCompoundAdvancedSystemDeflection)

    @property
    def clutch_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7372.ClutchHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7372,
        )

        return self.__parent__._cast(_7372.ClutchHalfCompoundAdvancedSystemDeflection)

    @property
    def component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7374.ComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7374,
        )

        return self.__parent__._cast(_7374.ComponentCompoundAdvancedSystemDeflection)

    @property
    def concept_coupling_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7375.ConceptCouplingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7375,
        )

        return self.__parent__._cast(
            _7375.ConceptCouplingCompoundAdvancedSystemDeflection
        )

    @property
    def concept_coupling_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7377.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7377,
        )

        return self.__parent__._cast(
            _7377.ConceptCouplingHalfCompoundAdvancedSystemDeflection
        )

    @property
    def concept_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7378.ConceptGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7378,
        )

        return self.__parent__._cast(_7378.ConceptGearCompoundAdvancedSystemDeflection)

    @property
    def concept_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7380.ConceptGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7380,
        )

        return self.__parent__._cast(
            _7380.ConceptGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7381.ConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7381,
        )

        return self.__parent__._cast(_7381.ConicalGearCompoundAdvancedSystemDeflection)

    @property
    def conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7383.ConicalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7383,
        )

        return self.__parent__._cast(
            _7383.ConicalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def connector_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7385.ConnectorCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7385,
        )

        return self.__parent__._cast(_7385.ConnectorCompoundAdvancedSystemDeflection)

    @property
    def coupling_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7386.CouplingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7386,
        )

        return self.__parent__._cast(_7386.CouplingCompoundAdvancedSystemDeflection)

    @property
    def coupling_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7388.CouplingHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7388,
        )

        return self.__parent__._cast(_7388.CouplingHalfCompoundAdvancedSystemDeflection)

    @property
    def cvt_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7390.CVTCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7390,
        )

        return self.__parent__._cast(_7390.CVTCompoundAdvancedSystemDeflection)

    @property
    def cvt_pulley_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7391.CVTPulleyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7391,
        )

        return self.__parent__._cast(_7391.CVTPulleyCompoundAdvancedSystemDeflection)

    @property
    def cycloidal_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7392.CycloidalAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7392,
        )

        return self.__parent__._cast(
            _7392.CycloidalAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def cycloidal_disc_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7394.CycloidalDiscCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7394,
        )

        return self.__parent__._cast(
            _7394.CycloidalDiscCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7396.CylindricalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7396,
        )

        return self.__parent__._cast(
            _7396.CylindricalGearCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7398.CylindricalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7398,
        )

        return self.__parent__._cast(
            _7398.CylindricalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def cylindrical_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7399.CylindricalPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7399,
        )

        return self.__parent__._cast(
            _7399.CylindricalPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def datum_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7400.DatumCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7400,
        )

        return self.__parent__._cast(_7400.DatumCompoundAdvancedSystemDeflection)

    @property
    def external_cad_model_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7401.ExternalCADModelCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7401,
        )

        return self.__parent__._cast(
            _7401.ExternalCADModelCompoundAdvancedSystemDeflection
        )

    @property
    def face_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7402.FaceGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7402,
        )

        return self.__parent__._cast(_7402.FaceGearCompoundAdvancedSystemDeflection)

    @property
    def face_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7404.FaceGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7404,
        )

        return self.__parent__._cast(_7404.FaceGearSetCompoundAdvancedSystemDeflection)

    @property
    def fe_part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7405.FEPartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7405,
        )

        return self.__parent__._cast(_7405.FEPartCompoundAdvancedSystemDeflection)

    @property
    def flexible_pin_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7406.FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7406,
        )

        return self.__parent__._cast(
            _7406.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7407.GearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7407,
        )

        return self.__parent__._cast(_7407.GearCompoundAdvancedSystemDeflection)

    @property
    def gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7409.GearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7409,
        )

        return self.__parent__._cast(_7409.GearSetCompoundAdvancedSystemDeflection)

    @property
    def guide_dxf_model_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7410.GuideDxfModelCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7410,
        )

        return self.__parent__._cast(
            _7410.GuideDxfModelCompoundAdvancedSystemDeflection
        )

    @property
    def hypoid_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7411.HypoidGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7411,
        )

        return self.__parent__._cast(_7411.HypoidGearCompoundAdvancedSystemDeflection)

    @property
    def hypoid_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7413.HypoidGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7413,
        )

        return self.__parent__._cast(
            _7413.HypoidGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7415.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7415,
        )

        return self.__parent__._cast(
            _7415.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7417.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7417,
        )

        return self.__parent__._cast(
            _7417.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7418.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7418,
        )

        return self.__parent__._cast(
            _7418.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7420.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7420,
        )

        return self.__parent__._cast(
            _7420.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> (
        "_7421.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"
    ):
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7421,
        )

        return self.__parent__._cast(
            _7421.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7423.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7423,
        )

        return self.__parent__._cast(
            _7423.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def mass_disc_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7424.MassDiscCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7424,
        )

        return self.__parent__._cast(_7424.MassDiscCompoundAdvancedSystemDeflection)

    @property
    def measurement_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7425.MeasurementComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7425,
        )

        return self.__parent__._cast(
            _7425.MeasurementComponentCompoundAdvancedSystemDeflection
        )

    @property
    def microphone_array_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7426.MicrophoneArrayCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7426,
        )

        return self.__parent__._cast(
            _7426.MicrophoneArrayCompoundAdvancedSystemDeflection
        )

    @property
    def microphone_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7427.MicrophoneCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7427,
        )

        return self.__parent__._cast(_7427.MicrophoneCompoundAdvancedSystemDeflection)

    @property
    def mountable_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7428.MountableComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7428,
        )

        return self.__parent__._cast(
            _7428.MountableComponentCompoundAdvancedSystemDeflection
        )

    @property
    def oil_seal_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7429.OilSealCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7429,
        )

        return self.__parent__._cast(_7429.OilSealCompoundAdvancedSystemDeflection)

    @property
    def part_to_part_shear_coupling_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7431.PartToPartShearCouplingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7431,
        )

        return self.__parent__._cast(
            _7431.PartToPartShearCouplingCompoundAdvancedSystemDeflection
        )

    @property
    def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7433.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7433,
        )

        return self.__parent__._cast(
            _7433.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
        )

    @property
    def planetary_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7435.PlanetaryGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7435,
        )

        return self.__parent__._cast(
            _7435.PlanetaryGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def planet_carrier_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7436.PlanetCarrierCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7436,
        )

        return self.__parent__._cast(
            _7436.PlanetCarrierCompoundAdvancedSystemDeflection
        )

    @property
    def point_load_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7437.PointLoadCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7437,
        )

        return self.__parent__._cast(_7437.PointLoadCompoundAdvancedSystemDeflection)

    @property
    def power_load_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7438.PowerLoadCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7438,
        )

        return self.__parent__._cast(_7438.PowerLoadCompoundAdvancedSystemDeflection)

    @property
    def pulley_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7439.PulleyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7439,
        )

        return self.__parent__._cast(_7439.PulleyCompoundAdvancedSystemDeflection)

    @property
    def ring_pins_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7440.RingPinsCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7440,
        )

        return self.__parent__._cast(_7440.RingPinsCompoundAdvancedSystemDeflection)

    @property
    def rolling_ring_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7442.RollingRingAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7442,
        )

        return self.__parent__._cast(
            _7442.RollingRingAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def rolling_ring_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7443.RollingRingCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7443,
        )

        return self.__parent__._cast(_7443.RollingRingCompoundAdvancedSystemDeflection)

    @property
    def root_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7445.RootAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7445,
        )

        return self.__parent__._cast(_7445.RootAssemblyCompoundAdvancedSystemDeflection)

    @property
    def shaft_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7446.ShaftCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7446,
        )

        return self.__parent__._cast(_7446.ShaftCompoundAdvancedSystemDeflection)

    @property
    def shaft_hub_connection_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7447.ShaftHubConnectionCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7447,
        )

        return self.__parent__._cast(
            _7447.ShaftHubConnectionCompoundAdvancedSystemDeflection
        )

    @property
    def specialised_assembly_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7449.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7449,
        )

        return self.__parent__._cast(
            _7449.SpecialisedAssemblyCompoundAdvancedSystemDeflection
        )

    @property
    def spiral_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7450.SpiralBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7450,
        )

        return self.__parent__._cast(
            _7450.SpiralBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def spiral_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7452.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7452,
        )

        return self.__parent__._cast(
            _7452.SpiralBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def spring_damper_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7453.SpringDamperCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7453,
        )

        return self.__parent__._cast(_7453.SpringDamperCompoundAdvancedSystemDeflection)

    @property
    def spring_damper_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7455.SpringDamperHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7455,
        )

        return self.__parent__._cast(
            _7455.SpringDamperHalfCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7456.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7456,
        )

        return self.__parent__._cast(
            _7456.StraightBevelDiffGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7458.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7458,
        )

        return self.__parent__._cast(
            _7458.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7459.StraightBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7459,
        )

        return self.__parent__._cast(
            _7459.StraightBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7461.StraightBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7461,
        )

        return self.__parent__._cast(
            _7461.StraightBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_planet_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7462.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7462,
        )

        return self.__parent__._cast(
            _7462.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
        )

    @property
    def straight_bevel_sun_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7463.StraightBevelSunGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7463,
        )

        return self.__parent__._cast(
            _7463.StraightBevelSunGearCompoundAdvancedSystemDeflection
        )

    @property
    def synchroniser_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7464.SynchroniserCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7464,
        )

        return self.__parent__._cast(_7464.SynchroniserCompoundAdvancedSystemDeflection)

    @property
    def synchroniser_half_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7465.SynchroniserHalfCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7465,
        )

        return self.__parent__._cast(
            _7465.SynchroniserHalfCompoundAdvancedSystemDeflection
        )

    @property
    def synchroniser_part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7466.SynchroniserPartCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7466,
        )

        return self.__parent__._cast(
            _7466.SynchroniserPartCompoundAdvancedSystemDeflection
        )

    @property
    def synchroniser_sleeve_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7467.SynchroniserSleeveCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7467,
        )

        return self.__parent__._cast(
            _7467.SynchroniserSleeveCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7468.TorqueConverterCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7468,
        )

        return self.__parent__._cast(
            _7468.TorqueConverterCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_pump_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7470.TorqueConverterPumpCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7470,
        )

        return self.__parent__._cast(
            _7470.TorqueConverterPumpCompoundAdvancedSystemDeflection
        )

    @property
    def torque_converter_turbine_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7471.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7471,
        )

        return self.__parent__._cast(
            _7471.TorqueConverterTurbineCompoundAdvancedSystemDeflection
        )

    @property
    def unbalanced_mass_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7472.UnbalancedMassCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7472,
        )

        return self.__parent__._cast(
            _7472.UnbalancedMassCompoundAdvancedSystemDeflection
        )

    @property
    def virtual_component_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7473.VirtualComponentCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7473,
        )

        return self.__parent__._cast(
            _7473.VirtualComponentCompoundAdvancedSystemDeflection
        )

    @property
    def worm_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7474.WormGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7474,
        )

        return self.__parent__._cast(_7474.WormGearCompoundAdvancedSystemDeflection)

    @property
    def worm_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7476.WormGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7476,
        )

        return self.__parent__._cast(_7476.WormGearSetCompoundAdvancedSystemDeflection)

    @property
    def zerol_bevel_gear_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7477.ZerolBevelGearCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7477,
        )

        return self.__parent__._cast(
            _7477.ZerolBevelGearCompoundAdvancedSystemDeflection
        )

    @property
    def zerol_bevel_gear_set_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "_7479.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
        from mastapy._private.system_model.analyses_and_results.advanced_system_deflections.compound import (
            _7479,
        )

        return self.__parent__._cast(
            _7479.ZerolBevelGearSetCompoundAdvancedSystemDeflection
        )

    @property
    def part_compound_advanced_system_deflection(
        self: "CastSelf",
    ) -> "PartCompoundAdvancedSystemDeflection":
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
class PartCompoundAdvancedSystemDeflection(_7707.PartCompoundAnalysis):
    """PartCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def component_analysis_cases(
        self: "Self",
    ) -> "List[_7298.PartAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PartAdvancedSystemDeflection]

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
    ) -> "List[_7298.PartAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PartAdvancedSystemDeflection]

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
    def cast_to(self: "Self") -> "_Cast_PartCompoundAdvancedSystemDeflection":
        """Cast to another type.

        Returns:
            _Cast_PartCompoundAdvancedSystemDeflection
        """
        return _Cast_PartCompoundAdvancedSystemDeflection(self)
