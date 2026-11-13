"""Code skeleton generated from the shared model of D2/GWPNV5.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Place:
    """Source: -"""
    name: _t.Optional[str] = None
    tokens: _t.Optional[int] = None
    net: _t.Optional["Net"] = None

    def addToken(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeToken(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Transition:
    """Source: -"""
    name: _t.Optional[str] = None

    def addOutputArc(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeOutputArc(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Arc:
    """Source: -"""
    weight: _t.Optional[float] = None

    def setDestination(self) -> None:
        """Operation."""
        raise NotImplementedError

    def setSource(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class PlaceTransitionArc:
    """Source: -"""
    transition: _t.Optional["Transition"] = None

    def connectToPlace(self) -> None:
        """Operation."""
        raise NotImplementedError

    def disconnectFromPlace(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class TransitionPlaceArc:
    """Source: -"""

    def connectToTransition(self) -> None:
        """Operation."""
        raise NotImplementedError

    def disconnectFromTransition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Net:
    """Source: R3, R8, R12"""

    def addPlace(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removePlace(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addTransition(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeTransition(self) -> None:
        """Operation."""
        raise NotImplementedError
