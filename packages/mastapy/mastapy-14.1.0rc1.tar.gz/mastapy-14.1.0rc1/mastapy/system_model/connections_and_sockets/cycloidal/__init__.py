"""Subpackage."""

from typing import TYPE_CHECKING as __tc

if __tc:
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2399 import (
        CycloidalDiscAxialLeftSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2400 import (
        CycloidalDiscAxialRightSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2401 import (
        CycloidalDiscCentralBearingConnection,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2402 import (
        CycloidalDiscInnerSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2403 import (
        CycloidalDiscOuterSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2404 import (
        CycloidalDiscPlanetaryBearingConnection,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2405 import (
        CycloidalDiscPlanetaryBearingSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2406 import (
        RingPinsSocket,
    )
    from mastapy._private.system_model.connections_and_sockets.cycloidal._2407 import (
        RingPinsToDiscConnection,
    )
else:
    import sys as __sys

    from lazy_imports import LazyImporter as __LazyImporter

    __import_structure = {
        "_private.system_model.connections_and_sockets.cycloidal._2399": [
            "CycloidalDiscAxialLeftSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2400": [
            "CycloidalDiscAxialRightSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2401": [
            "CycloidalDiscCentralBearingConnection"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2402": [
            "CycloidalDiscInnerSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2403": [
            "CycloidalDiscOuterSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2404": [
            "CycloidalDiscPlanetaryBearingConnection"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2405": [
            "CycloidalDiscPlanetaryBearingSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2406": [
            "RingPinsSocket"
        ],
        "_private.system_model.connections_and_sockets.cycloidal._2407": [
            "RingPinsToDiscConnection"
        ],
    }

    __sys.modules[__name__] = __LazyImporter(
        "mastapy",
        globals()["__file__"],
        __import_structure,
    )

__all__ = (
    "CycloidalDiscAxialLeftSocket",
    "CycloidalDiscAxialRightSocket",
    "CycloidalDiscCentralBearingConnection",
    "CycloidalDiscInnerSocket",
    "CycloidalDiscOuterSocket",
    "CycloidalDiscPlanetaryBearingConnection",
    "CycloidalDiscPlanetaryBearingSocket",
    "RingPinsSocket",
    "RingPinsToDiscConnection",
)
