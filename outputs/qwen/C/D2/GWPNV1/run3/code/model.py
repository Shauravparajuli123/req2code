"""Code skeleton generated from the shared model of D2/GWPNV1.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Place:
    """Source: R1, R4, R5"""
    name: _t.Optional[str] = None
    destination: _t.Optional[str] = None
    transitions: _t.List["Transition"] = _dc.field(default_factory=list)


@_dc.dataclass
class Transition:
    """Source: R2, R6, R7"""
    name: _t.Optional[str] = None
    net: _t.Optional[str] = None
    destination: _t.Optional[str] = None
    places: _t.List["Place"] = _dc.field(default_factory=list)

    def createTransition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Net:
    """Source: R3, R8"""
    name: _t.Optional[str] = None
    places: _t.Optional[str] = None

    def createNet(self) -> None:
        """Operation."""
        raise NotImplementedError
