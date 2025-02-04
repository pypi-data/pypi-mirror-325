"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.part_model.import_from_cad._2563 import (
        AbstractShaftFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2564 import (
        ClutchFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2565 import (
        ComponentFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2566 import (
        ComponentFromCADBase,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2567 import (
        ConceptBearingFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2568 import (
        ConnectorFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2569 import (
        CylindricalGearFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2570 import (
        CylindricalGearInPlanetarySetFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2571 import (
        CylindricalPlanetGearFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2572 import (
        CylindricalRingGearFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2573 import (
        CylindricalSunGearFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2574 import (
        HousedOrMounted,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2575 import (
        MountableComponentFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2576 import (
        PlanetShaftFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2577 import (
        PulleyFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2578 import (
        RigidConnectorFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2579 import (
        RollingBearingFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2580 import (
        ShaftFromCAD,
    )
    from mastapy._private.system_model.part_model.import_from_cad._2581 import (
        ShaftFromCADAuto,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.part_model.import_from_cad._2563": [
            "AbstractShaftFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2564": ["ClutchFromCAD"],
        "_private.system_model.part_model.import_from_cad._2565": ["ComponentFromCAD"],
        "_private.system_model.part_model.import_from_cad._2566": [
            "ComponentFromCADBase"
        ],
        "_private.system_model.part_model.import_from_cad._2567": [
            "ConceptBearingFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2568": ["ConnectorFromCAD"],
        "_private.system_model.part_model.import_from_cad._2569": [
            "CylindricalGearFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2570": [
            "CylindricalGearInPlanetarySetFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2571": [
            "CylindricalPlanetGearFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2572": [
            "CylindricalRingGearFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2573": [
            "CylindricalSunGearFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2574": ["HousedOrMounted"],
        "_private.system_model.part_model.import_from_cad._2575": [
            "MountableComponentFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2576": [
            "PlanetShaftFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2577": ["PulleyFromCAD"],
        "_private.system_model.part_model.import_from_cad._2578": [
            "RigidConnectorFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2579": [
            "RollingBearingFromCAD"
        ],
        "_private.system_model.part_model.import_from_cad._2580": ["ShaftFromCAD"],
        "_private.system_model.part_model.import_from_cad._2581": ["ShaftFromCADAuto"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AbstractShaftFromCAD",
    "ClutchFromCAD",
    "ComponentFromCAD",
    "ComponentFromCADBase",
    "ConceptBearingFromCAD",
    "ConnectorFromCAD",
    "CylindricalGearFromCAD",
    "CylindricalGearInPlanetarySetFromCAD",
    "CylindricalPlanetGearFromCAD",
    "CylindricalRingGearFromCAD",
    "CylindricalSunGearFromCAD",
    "HousedOrMounted",
    "MountableComponentFromCAD",
    "PlanetShaftFromCAD",
    "PulleyFromCAD",
    "RigidConnectorFromCAD",
    "RollingBearingFromCAD",
    "ShaftFromCAD",
    "ShaftFromCADAuto",
)
