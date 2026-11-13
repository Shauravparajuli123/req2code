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
    net: _t.Optional["Net"] = None


@_dc.dataclass
class Transition:
    """Source: R10, R11"""
    name: _t.Optional[str] = None
    weight: _t.Optional[str] = None


@_dc.dataclass
class Arc:
    """Source: R4, R5, R6, R13, R14"""
    weight: _t.Optional[str] = None


@_dc.dataclass
class Weight:
    """Source: R4, R5, R6, R13, R14"""
    pass


@_dc.dataclass
class Net:
    """Source: R3, R7, R8, R12"""
    name: _t.Optional[str] = None
    places: _t.Optional[str] = None
    transitions: _t.Optional[str] = None

    def createPlace(self) -> None:
        """Operation."""
        raise NotImplementedError

    def createTransition(self) -> None:
        """Operation."""
        raise NotImplementedError
