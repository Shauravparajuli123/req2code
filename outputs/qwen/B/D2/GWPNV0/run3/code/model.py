"""Code skeleton generated from the shared model of D2/GWPNV0.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Place:
    """Source: R1, R5, R7, R8"""
    pass


@_dc.dataclass
class Transition:
    """Source: R2, R6, R7"""
    place: _t.Optional["Place"] = None

    def createTransition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Network:
    """Source: R3, R8"""
    places: _t.List["Place"] = _dc.field(default_factory=list)

    def addPlace(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addTransition(self) -> None:
        """Operation."""
        raise NotImplementedError
