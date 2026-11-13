"""Code skeleton generated from the shared model of D2/GWPNV3.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Net:
    """Source: R3, R7, R9"""
    name: _t.Optional[str] = None
    places: _t.Optional[str] = None
    transitions: _t.Optional[str] = None
    tparcses: _t.List["Tparcs"] = _dc.field(default_factory=list)

    def addPlace(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addTransition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Place:
    """Source: R1, R7"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: R2, R9, R10, R13"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None
    outgoingArcs: _t.Optional[str] = None


@_dc.dataclass
class Tparcs:
    """Source: R4, R12, R13"""
    srcTransition: _t.Optional[str] = None
    dstTransition: _t.Optional[str] = None
