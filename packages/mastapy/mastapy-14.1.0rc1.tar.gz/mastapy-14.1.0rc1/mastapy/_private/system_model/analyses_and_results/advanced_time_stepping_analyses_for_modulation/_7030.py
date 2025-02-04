"""PartAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from mastapy._private._internal import constructor, utility
from mastapy._private._internal.cast_exception import CastException
from mastapy._private._internal.dataclasses import extended_dataclass
from mastapy._private._internal.python_net import (
    python_net_import,
    pythonnet_property_get,
)
from mastapy._private.system_model.analyses_and_results.analysis_cases import _7709

_PART_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "PartAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from typing import Any, Type, TypeVar

    from mastapy._private.system_model.analyses_and_results import _2726, _2728, _2732
    from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _6943,
        _6944,
        _6945,
        _6947,
        _6951,
        _6953,
        _6954,
        _6956,
        _6958,
        _6959,
        _6961,
        _6962,
        _6963,
        _6964,
        _6966,
        _6967,
        _6968,
        _6969,
        _6971,
        _6973,
        _6974,
        _6976,
        _6977,
        _6979,
        _6980,
        _6982,
        _6984,
        _6985,
        _6987,
        _6988,
        _6990,
        _6991,
        _6992,
        _6995,
        _6997,
        _6998,
        _6999,
        _7000,
        _7001,
        _7003,
        _7004,
        _7005,
        _7006,
        _7008,
        _7009,
        _7011,
        _7013,
        _7015,
        _7017,
        _7018,
        _7020,
        _7021,
        _7023,
        _7024,
        _7025,
        _7026,
        _7027,
        _7028,
        _7029,
        _7031,
        _7033,
        _7035,
        _7036,
        _7037,
        _7038,
        _7039,
        _7040,
        _7042,
        _7043,
        _7045,
        _7046,
        _7047,
        _7049,
        _7050,
        _7052,
        _7053,
        _7055,
        _7056,
        _7058,
        _7059,
        _7061,
        _7062,
        _7063,
        _7064,
        _7065,
        _7066,
        _7067,
        _7068,
        _7070,
        _7071,
        _7072,
        _7073,
        _7074,
        _7076,
        _7077,
        _7079,
    )
    from mastapy._private.system_model.analyses_and_results.analysis_cases import _7706
    from mastapy._private.system_model.analyses_and_results.system_deflections import (
        _2862,
    )
    from mastapy._private.system_model.part_model import _2537

    Self = TypeVar("Self", bound="PartAdvancedTimeSteppingAnalysisForModulation")
    CastSelf = TypeVar(
        "CastSelf",
        bound="PartAdvancedTimeSteppingAnalysisForModulation._Cast_PartAdvancedTimeSteppingAnalysisForModulation",
    )


__docformat__ = "restructuredtext en"
__all__ = ("PartAdvancedTimeSteppingAnalysisForModulation",)


@extended_dataclass(frozen=True, slots=True, weakref_slot=True)
class _Cast_PartAdvancedTimeSteppingAnalysisForModulation:
    """Special nested class for casting PartAdvancedTimeSteppingAnalysisForModulation to subclasses."""

    __parent__: "PartAdvancedTimeSteppingAnalysisForModulation"

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
    def abstract_assembly_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6943.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6943,
        )

        return self.__parent__._cast(
            _6943.AbstractAssemblyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def abstract_shaft_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6944.AbstractShaftAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6944,
        )

        return self.__parent__._cast(
            _6944.AbstractShaftAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def abstract_shaft_or_housing_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6945.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6945,
        )

        return self.__parent__._cast(
            _6945.AbstractShaftOrHousingAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6951.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6951,
        )

        return self.__parent__._cast(
            _6951.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def agma_gleason_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6953.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6953,
        )

        return self.__parent__._cast(
            _6953.AGMAGleasonConicalGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def assembly_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6954.AssemblyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6954,
        )

        return self.__parent__._cast(
            _6954.AssemblyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bearing_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6956.BearingAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6956,
        )

        return self.__parent__._cast(
            _6956.BearingAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def belt_drive_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6958.BeltDriveAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6958,
        )

        return self.__parent__._cast(
            _6958.BeltDriveAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6959.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6959,
        )

        return self.__parent__._cast(
            _6959.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6961.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6961,
        )

        return self.__parent__._cast(
            _6961.BevelDifferentialGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6962.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6962,
        )

        return self.__parent__._cast(
            _6962.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6963.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6963,
        )

        return self.__parent__._cast(
            _6963.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6964.BevelGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6964,
        )

        return self.__parent__._cast(
            _6964.BevelGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6966.BevelGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6966,
        )

        return self.__parent__._cast(
            _6966.BevelGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bolt_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6967.BoltAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6967,
        )

        return self.__parent__._cast(
            _6967.BoltAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def bolted_joint_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6968.BoltedJointAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6968,
        )

        return self.__parent__._cast(
            _6968.BoltedJointAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def clutch_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6969.ClutchAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6969,
        )

        return self.__parent__._cast(
            _6969.ClutchAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def clutch_half_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6971.ClutchHalfAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6971,
        )

        return self.__parent__._cast(
            _6971.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def component_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6973.ComponentAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6973,
        )

        return self.__parent__._cast(
            _6973.ComponentAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_coupling_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6974.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6974,
        )

        return self.__parent__._cast(
            _6974.ConceptCouplingAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6976.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6976,
        )

        return self.__parent__._cast(
            _6976.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6977.ConceptGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6977,
        )

        return self.__parent__._cast(
            _6977.ConceptGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def concept_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6979.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6979,
        )

        return self.__parent__._cast(
            _6979.ConceptGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def conical_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6980.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6980,
        )

        return self.__parent__._cast(
            _6980.ConicalGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def conical_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6982.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6982,
        )

        return self.__parent__._cast(
            _6982.ConicalGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def connector_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6984.ConnectorAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6984,
        )

        return self.__parent__._cast(
            _6984.ConnectorAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def coupling_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6985.CouplingAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6985,
        )

        return self.__parent__._cast(
            _6985.CouplingAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def coupling_half_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6987.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6987,
        )

        return self.__parent__._cast(
            _6987.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cvt_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6988.CVTAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6988,
        )

        return self.__parent__._cast(_6988.CVTAdvancedTimeSteppingAnalysisForModulation)

    @property
    def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6990.CVTPulleyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6990,
        )

        return self.__parent__._cast(
            _6990.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cycloidal_assembly_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6991.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6991,
        )

        return self.__parent__._cast(
            _6991.CycloidalAssemblyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cycloidal_disc_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6992.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6992,
        )

        return self.__parent__._cast(
            _6992.CycloidalDiscAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6995.CylindricalGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6995,
        )

        return self.__parent__._cast(
            _6995.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cylindrical_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6997.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6997,
        )

        return self.__parent__._cast(
            _6997.CylindricalGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6998.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6998,
        )

        return self.__parent__._cast(
            _6998.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def datum_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_6999.DatumAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _6999,
        )

        return self.__parent__._cast(
            _6999.DatumAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def external_cad_model_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7000.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7000,
        )

        return self.__parent__._cast(
            _7000.ExternalCADModelAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def face_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7001.FaceGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7001,
        )

        return self.__parent__._cast(
            _7001.FaceGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def face_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7003.FaceGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7003,
        )

        return self.__parent__._cast(
            _7003.FaceGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def fe_part_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7004.FEPartAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7004,
        )

        return self.__parent__._cast(
            _7004.FEPartAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def flexible_pin_assembly_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7005.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7005,
        )

        return self.__parent__._cast(
            _7005.FlexiblePinAssemblyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7006.GearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7006,
        )

        return self.__parent__._cast(
            _7006.GearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7008.GearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7008,
        )

        return self.__parent__._cast(
            _7008.GearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def guide_dxf_model_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7009.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7009,
        )

        return self.__parent__._cast(
            _7009.GuideDxfModelAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7011.HypoidGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7011,
        )

        return self.__parent__._cast(
            _7011.HypoidGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7013.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7013,
        )

        return self.__parent__._cast(
            _7013.HypoidGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7015.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7015,
        )

        return self.__parent__._cast(
            _7015.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_conical_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7017.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7017,
        )

        return self.__parent__._cast(
            _7017.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7018.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7018,
        )

        return self.__parent__._cast(
            _7018.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7020.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7020,
        )

        return self.__parent__._cast(
            _7020.KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7021.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7021,
        )

        return self.__parent__._cast(
            _7021.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7023.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7023,
        )

        return self.__parent__._cast(
            _7023.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def mass_disc_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7024.MassDiscAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7024,
        )

        return self.__parent__._cast(
            _7024.MassDiscAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def measurement_component_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7025.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7025,
        )

        return self.__parent__._cast(
            _7025.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def microphone_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7026.MicrophoneAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7026,
        )

        return self.__parent__._cast(
            _7026.MicrophoneAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def microphone_array_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7027.MicrophoneArrayAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7027,
        )

        return self.__parent__._cast(
            _7027.MicrophoneArrayAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def mountable_component_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7028.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7028,
        )

        return self.__parent__._cast(
            _7028.MountableComponentAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def oil_seal_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7029.OilSealAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7029,
        )

        return self.__parent__._cast(
            _7029.OilSealAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_to_part_shear_coupling_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7031.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7031,
        )

        return self.__parent__._cast(
            _7031.PartToPartShearCouplingAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7033.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7033,
        )

        return self.__parent__._cast(
            _7033.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def planetary_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7035.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7035,
        )

        return self.__parent__._cast(
            _7035.PlanetaryGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def planet_carrier_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7036.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7036,
        )

        return self.__parent__._cast(
            _7036.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def point_load_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7037.PointLoadAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7037,
        )

        return self.__parent__._cast(
            _7037.PointLoadAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def power_load_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7038.PowerLoadAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7038,
        )

        return self.__parent__._cast(
            _7038.PowerLoadAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def pulley_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7039.PulleyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7039,
        )

        return self.__parent__._cast(
            _7039.PulleyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def ring_pins_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7040.RingPinsAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7040,
        )

        return self.__parent__._cast(
            _7040.RingPinsAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def rolling_ring_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7042.RollingRingAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7042,
        )

        return self.__parent__._cast(
            _7042.RollingRingAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def rolling_ring_assembly_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7043.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7043,
        )

        return self.__parent__._cast(
            _7043.RollingRingAssemblyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def root_assembly_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7045.RootAssemblyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7045,
        )

        return self.__parent__._cast(
            _7045.RootAssemblyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def shaft_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7046.ShaftAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7046,
        )

        return self.__parent__._cast(
            _7046.ShaftAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7047.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7047,
        )

        return self.__parent__._cast(
            _7047.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def specialised_assembly_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7049.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7049,
        )

        return self.__parent__._cast(
            _7049.SpecialisedAssemblyAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7050.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7050,
        )

        return self.__parent__._cast(
            _7050.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spiral_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7052.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7052,
        )

        return self.__parent__._cast(
            _7052.SpiralBevelGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spring_damper_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7053.SpringDamperAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7053,
        )

        return self.__parent__._cast(
            _7053.SpringDamperAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7055.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7055,
        )

        return self.__parent__._cast(
            _7055.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7056.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7056,
        )

        return self.__parent__._cast(
            _7056.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_diff_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7058.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7058,
        )

        return self.__parent__._cast(
            _7058.StraightBevelDiffGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7059.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7059,
        )

        return self.__parent__._cast(
            _7059.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7061.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7061,
        )

        return self.__parent__._cast(
            _7061.StraightBevelGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7062.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7062,
        )

        return self.__parent__._cast(
            _7062.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7063.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7063,
        )

        return self.__parent__._cast(
            _7063.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7064.SynchroniserAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7064,
        )

        return self.__parent__._cast(
            _7064.SynchroniserAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7065.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7065,
        )

        return self.__parent__._cast(
            _7065.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7066.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7066,
        )

        return self.__parent__._cast(
            _7066.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7067.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7067,
        )

        return self.__parent__._cast(
            _7067.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def torque_converter_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7068.TorqueConverterAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7068,
        )

        return self.__parent__._cast(
            _7068.TorqueConverterAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7070.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7070,
        )

        return self.__parent__._cast(
            _7070.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7071.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7071,
        )

        return self.__parent__._cast(
            _7071.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7072.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7072,
        )

        return self.__parent__._cast(
            _7072.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def virtual_component_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7073.VirtualComponentAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7073,
        )

        return self.__parent__._cast(
            _7073.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def worm_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7074.WormGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7074,
        )

        return self.__parent__._cast(
            _7074.WormGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def worm_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7076.WormGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7076,
        )

        return self.__parent__._cast(
            _7076.WormGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7077.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7077,
        )

        return self.__parent__._cast(
            _7077.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def zerol_bevel_gear_set_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "_7079.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation":
        from mastapy._private.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
            _7079,
        )

        return self.__parent__._cast(
            _7079.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
        )

    @property
    def part_advanced_time_stepping_analysis_for_modulation(
        self: "CastSelf",
    ) -> "PartAdvancedTimeSteppingAnalysisForModulation":
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
class PartAdvancedTimeSteppingAnalysisForModulation(_7709.PartStaticLoadAnalysisCase):
    """PartAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE: ClassVar["Type"] = _PART_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    wrapped: "Any"

    def __post_init__(self: "Self") -> None:
        """Override of the post initialisation magic method."""
        if not hasattr(self.wrapped, "reference_count"):
            self.wrapped.reference_count = 0

        self.wrapped.reference_count += 1

    @property
    def advanced_time_stepping_analysis_for_modulation(
        self: "Self",
    ) -> "_6947.AdvancedTimeSteppingAnalysisForModulation":
        """mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AdvancedTimeSteppingAnalysisForModulation

        Note:
            This property is readonly.
        """
        temp = pythonnet_property_get(
            self.wrapped, "AdvancedTimeSteppingAnalysisForModulation"
        )

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

    @property
    def cast_to(self: "Self") -> "_Cast_PartAdvancedTimeSteppingAnalysisForModulation":
        """Cast to another type.

        Returns:
            _Cast_PartAdvancedTimeSteppingAnalysisForModulation
        """
        return _Cast_PartAdvancedTimeSteppingAnalysisForModulation(self)
