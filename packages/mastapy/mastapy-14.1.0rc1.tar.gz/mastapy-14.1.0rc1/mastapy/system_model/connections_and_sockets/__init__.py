"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.connections_and_sockets._2331 import (
        AbstractShaftToMountableComponentConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2332 import (
        BearingInnerSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2333 import (
        BearingOuterSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2334 import (
        BeltConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2335 import (
        CoaxialConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2336 import (
        ComponentConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2337 import (
        ComponentMeasurer,
    )
    from mastapy._private.system_model.connections_and_sockets._2338 import Connection
    from mastapy._private.system_model.connections_and_sockets._2339 import (
        CVTBeltConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2340 import (
        CVTPulleySocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2341 import (
        CylindricalComponentConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2342 import (
        CylindricalSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2343 import (
        DatumMeasurement,
    )
    from mastapy._private.system_model.connections_and_sockets._2344 import (
        ElectricMachineStatorSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2345 import (
        InnerShaftSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2346 import (
        InnerShaftSocketBase,
    )
    from mastapy._private.system_model.connections_and_sockets._2347 import (
        InterMountableComponentConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2348 import (
        MountableComponentInnerSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2349 import (
        MountableComponentOuterSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2350 import (
        MountableComponentSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2351 import (
        OuterShaftSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2352 import (
        OuterShaftSocketBase,
    )
    from mastapy._private.system_model.connections_and_sockets._2353 import (
        PlanetaryConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2354 import (
        PlanetarySocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2355 import (
        PlanetarySocketBase,
    )
    from mastapy._private.system_model.connections_and_sockets._2356 import PulleySocket
    from mastapy._private.system_model.connections_and_sockets._2357 import (
        RealignmentResult,
    )
    from mastapy._private.system_model.connections_and_sockets._2358 import (
        RollingRingConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2359 import (
        RollingRingSocket,
    )
    from mastapy._private.system_model.connections_and_sockets._2360 import ShaftSocket
    from mastapy._private.system_model.connections_and_sockets._2361 import (
        ShaftToMountableComponentConnection,
    )
    from mastapy._private.system_model.connections_and_sockets._2362 import Socket
    from mastapy._private.system_model.connections_and_sockets._2363 import (
        SocketConnectionOptions,
    )
    from mastapy._private.system_model.connections_and_sockets._2364 import (
        SocketConnectionSelection,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.connections_and_sockets._2331": [
            "AbstractShaftToMountableComponentConnection"
        ],
        "_private.system_model.connections_and_sockets._2332": ["BearingInnerSocket"],
        "_private.system_model.connections_and_sockets._2333": ["BearingOuterSocket"],
        "_private.system_model.connections_and_sockets._2334": ["BeltConnection"],
        "_private.system_model.connections_and_sockets._2335": ["CoaxialConnection"],
        "_private.system_model.connections_and_sockets._2336": ["ComponentConnection"],
        "_private.system_model.connections_and_sockets._2337": ["ComponentMeasurer"],
        "_private.system_model.connections_and_sockets._2338": ["Connection"],
        "_private.system_model.connections_and_sockets._2339": ["CVTBeltConnection"],
        "_private.system_model.connections_and_sockets._2340": ["CVTPulleySocket"],
        "_private.system_model.connections_and_sockets._2341": [
            "CylindricalComponentConnection"
        ],
        "_private.system_model.connections_and_sockets._2342": ["CylindricalSocket"],
        "_private.system_model.connections_and_sockets._2343": ["DatumMeasurement"],
        "_private.system_model.connections_and_sockets._2344": [
            "ElectricMachineStatorSocket"
        ],
        "_private.system_model.connections_and_sockets._2345": ["InnerShaftSocket"],
        "_private.system_model.connections_and_sockets._2346": ["InnerShaftSocketBase"],
        "_private.system_model.connections_and_sockets._2347": [
            "InterMountableComponentConnection"
        ],
        "_private.system_model.connections_and_sockets._2348": [
            "MountableComponentInnerSocket"
        ],
        "_private.system_model.connections_and_sockets._2349": [
            "MountableComponentOuterSocket"
        ],
        "_private.system_model.connections_and_sockets._2350": [
            "MountableComponentSocket"
        ],
        "_private.system_model.connections_and_sockets._2351": ["OuterShaftSocket"],
        "_private.system_model.connections_and_sockets._2352": ["OuterShaftSocketBase"],
        "_private.system_model.connections_and_sockets._2353": ["PlanetaryConnection"],
        "_private.system_model.connections_and_sockets._2354": ["PlanetarySocket"],
        "_private.system_model.connections_and_sockets._2355": ["PlanetarySocketBase"],
        "_private.system_model.connections_and_sockets._2356": ["PulleySocket"],
        "_private.system_model.connections_and_sockets._2357": ["RealignmentResult"],
        "_private.system_model.connections_and_sockets._2358": [
            "RollingRingConnection"
        ],
        "_private.system_model.connections_and_sockets._2359": ["RollingRingSocket"],
        "_private.system_model.connections_and_sockets._2360": ["ShaftSocket"],
        "_private.system_model.connections_and_sockets._2361": [
            "ShaftToMountableComponentConnection"
        ],
        "_private.system_model.connections_and_sockets._2362": ["Socket"],
        "_private.system_model.connections_and_sockets._2363": [
            "SocketConnectionOptions"
        ],
        "_private.system_model.connections_and_sockets._2364": [
            "SocketConnectionSelection"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "AbstractShaftToMountableComponentConnection",
    "BearingInnerSocket",
    "BearingOuterSocket",
    "BeltConnection",
    "CoaxialConnection",
    "ComponentConnection",
    "ComponentMeasurer",
    "Connection",
    "CVTBeltConnection",
    "CVTPulleySocket",
    "CylindricalComponentConnection",
    "CylindricalSocket",
    "DatumMeasurement",
    "ElectricMachineStatorSocket",
    "InnerShaftSocket",
    "InnerShaftSocketBase",
    "InterMountableComponentConnection",
    "MountableComponentInnerSocket",
    "MountableComponentOuterSocket",
    "MountableComponentSocket",
    "OuterShaftSocket",
    "OuterShaftSocketBase",
    "PlanetaryConnection",
    "PlanetarySocket",
    "PlanetarySocketBase",
    "PulleySocket",
    "RealignmentResult",
    "RollingRingConnection",
    "RollingRingSocket",
    "ShaftSocket",
    "ShaftToMountableComponentConnection",
    "Socket",
    "SocketConnectionOptions",
    "SocketConnectionSelection",
)
