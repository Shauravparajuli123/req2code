"""Code skeleton generated from the shared model of D2/GWPNV1.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Place:
    """Source: R1"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: R2, R5, R7"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None
    places: _t.List["Place"] = _dc.field(default_factory=list)

    def addDestinationPlace(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Net:
    """Source: R3, R4, R6"""
    name: _t.Optional[str] = None
    transitions: _t.Optional[str] = None
    places: _t.Optional[str] = None

    def addTransition(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addPlace(self) -> None:
        """Operation."""
        raise NotImplementedError
