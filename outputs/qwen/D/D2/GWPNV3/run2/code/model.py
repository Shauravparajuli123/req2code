"""Code skeleton generated from the shared model of D2/GWPNV3.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class PetriNet:
    """Source: R7, R8"""
    name: _t.Optional[str] = None
    nets: _t.Optional[str] = None
    transitions: _t.Optional[str] = None
    net: _t.Optional["Net"] = None
    places: _t.List["Place"] = _dc.field(default_factory=list)

    def addPlace(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addArc(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Net:
    """Source: R11"""
    name: _t.Optional[str] = None
    places: _t.Optional[str] = None
    tPArcs: _t.List["TPArc"] = _dc.field(default_factory=list)


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
class TPArc:
    """Source: R5, R6, R12, R13"""
    name: _t.Optional[str] = None
    srcTransition: _t.Optional[str] = None
    dstTransition: _t.Optional[str] = None


@_dc.dataclass
class PTArc(TPArc):
    """Source: R4"""
    name: _t.Optional[str] = None
    srcPlace: _t.Optional[str] = None
    dstNet: _t.Optional[str] = None
