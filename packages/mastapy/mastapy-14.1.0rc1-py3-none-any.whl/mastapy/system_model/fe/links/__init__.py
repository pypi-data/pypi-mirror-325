"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.fe.links._2485 import FELink
    from mastapy._private.system_model.fe.links._2486 import ElectricMachineStatorFELink
    from mastapy._private.system_model.fe.links._2487 import FELinkWithSelection
    from mastapy._private.system_model.fe.links._2488 import GearMeshFELink
    from mastapy._private.system_model.fe.links._2489 import (
        GearWithDuplicatedMeshesFELink,
    )
    from mastapy._private.system_model.fe.links._2490 import MultiAngleConnectionFELink
    from mastapy._private.system_model.fe.links._2491 import MultiNodeConnectorFELink
    from mastapy._private.system_model.fe.links._2492 import MultiNodeFELink
    from mastapy._private.system_model.fe.links._2493 import (
        PlanetaryConnectorMultiNodeFELink,
    )
    from mastapy._private.system_model.fe.links._2494 import PlanetBasedFELink
    from mastapy._private.system_model.fe.links._2495 import PlanetCarrierFELink
    from mastapy._private.system_model.fe.links._2496 import PointLoadFELink
    from mastapy._private.system_model.fe.links._2497 import RollingRingConnectionFELink
    from mastapy._private.system_model.fe.links._2498 import ShaftHubConnectionFELink
    from mastapy._private.system_model.fe.links._2499 import SingleNodeFELink
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.fe.links._2485": ["FELink"],
        "_private.system_model.fe.links._2486": ["ElectricMachineStatorFELink"],
        "_private.system_model.fe.links._2487": ["FELinkWithSelection"],
        "_private.system_model.fe.links._2488": ["GearMeshFELink"],
        "_private.system_model.fe.links._2489": ["GearWithDuplicatedMeshesFELink"],
        "_private.system_model.fe.links._2490": ["MultiAngleConnectionFELink"],
        "_private.system_model.fe.links._2491": ["MultiNodeConnectorFELink"],
        "_private.system_model.fe.links._2492": ["MultiNodeFELink"],
        "_private.system_model.fe.links._2493": ["PlanetaryConnectorMultiNodeFELink"],
        "_private.system_model.fe.links._2494": ["PlanetBasedFELink"],
        "_private.system_model.fe.links._2495": ["PlanetCarrierFELink"],
        "_private.system_model.fe.links._2496": ["PointLoadFELink"],
        "_private.system_model.fe.links._2497": ["RollingRingConnectionFELink"],
        "_private.system_model.fe.links._2498": ["ShaftHubConnectionFELink"],
        "_private.system_model.fe.links._2499": ["SingleNodeFELink"],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "FELink",
    "ElectricMachineStatorFELink",
    "FELinkWithSelection",
    "GearMeshFELink",
    "GearWithDuplicatedMeshesFELink",
    "MultiAngleConnectionFELink",
    "MultiNodeConnectorFELink",
    "MultiNodeFELink",
    "PlanetaryConnectorMultiNodeFELink",
    "PlanetBasedFELink",
    "PlanetCarrierFELink",
    "PointLoadFELink",
    "RollingRingConnectionFELink",
    "ShaftHubConnectionFELink",
    "SingleNodeFELink",
)
