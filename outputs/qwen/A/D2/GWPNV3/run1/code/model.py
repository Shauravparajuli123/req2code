"""Code skeleton generated from the shared model of D2/GWPNV3.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class PetriNet:
    """Source: -"""
    name: _t.Optional[str] = None
    places: _t.Optional[str] = None
    transitions: _t.Optional[str] = None
    nets: _t.List["Net"] = _dc.field(default_factory=list)
    pTArcs: _t.List["PTArc"] = _dc.field(default_factory=list)
    tPArcs: _t.List["TPArc"] = _dc.field(default_factory=list)

    def addPlace(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addTransition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Place:
    """Source: R7"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: R9, R10"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None
    outgoingArcs: _t.Optional[str] = None


@_dc.dataclass
class PTArc:
    """Source: R4, R11, R12"""
    srcPlace: _t.Optional[str] = None
    dstTransition: _t.Optional[str] = None


@_dc.dataclass
class TPArc:
    """Source: R5, R6, R13"""
    srcTransition: _t.Optional[str] = None
    dstTransition: _t.Optional[str] = None


@_dc.dataclass
class Net:
    """Source: R3, R11"""
    name: _t.Optional[str] = None
    places: _t.Optional[str] = None
    transitions: _t.Optional[str] = None
    place: _t.Optional["Place"] = None
