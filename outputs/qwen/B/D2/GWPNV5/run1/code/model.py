"""Code skeleton generated from the shared model of D2/GWPNV5.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Place:
    """Source: R9, R12, R15"""
    name: _t.Optional[str] = None
    tokens: _t.Optional[int] = None
    arcs: _t.List["Arc"] = _dc.field(default_factory=list)


@_dc.dataclass
class Transition:
    """Source: R2, R10, R11"""
    name: _t.Optional[str] = None
    weight: _t.Optional[str] = None
    arcs: _t.List["Arc"] = _dc.field(default_factory=list)

    def createTransition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Net:
    """Source: R3, R8, R12"""

    def createNet(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Arc:
    """Source: R5, R6, R12"""
    weight: _t.Optional[str] = None


@_dc.dataclass
class PlaceTransitionArc:
    """Source: R5, R6, R13, R14"""
    source: _t.Optional[str] = None
    destination: _t.Optional[str] = None
    transition: _t.Optional["Transition"] = None


@_dc.dataclass
class TransitionPlaceArc:
    """Source: R5, R6, R13, R14"""
    source: _t.Optional[str] = None
    destination: _t.Optional[str] = None


@_dc.dataclass
class Weight:
    """Source: R4"""
    pass
