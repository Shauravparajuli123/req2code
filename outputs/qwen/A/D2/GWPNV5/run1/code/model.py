"""Code skeleton generated from the shared model of D2/GWPNV5.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Place:
    """Source: R9, R13, R15"""
    name: _t.Optional[str] = None
    tokens: _t.Optional[int] = None
    arcs: _t.List["Arc"] = _dc.field(default_factory=list)

    def addToken(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeToken(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Transition:
    """Source: R2, R10, R11, R14"""
    name: _t.Optional[str] = None
    inputArcs: _t.Optional[str] = None
    outputArcs: _t.Optional[str] = None
    net: _t.Optional[str] = None
    arcs: _t.List["Arc"] = _dc.field(default_factory=list)

    def addInputArc(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeInputArc(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addOutputArc(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeOutputArc(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Arc:
    """Source: R4, R5, R6"""
    weight: _t.Optional[int] = None
    source: _t.Optional[str] = None
    destination: _t.Optional[str] = None


@_dc.dataclass
class Net:
    """Source: R3, R8, R12"""
    name: _t.Optional[str] = None
    places: _t.Optional[str] = None
    transitions: _t.Optional[str] = None
    arcs: _t.List["Arc"] = _dc.field(default_factory=list)

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
