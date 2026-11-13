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
    pass


@_dc.dataclass
class Network:
    """Source: R3, R8"""
    pass


@_dc.dataclass
class PetriNet:
    """Source: -"""
    places: _t.List["Place"] = _dc.field(default_factory=list)
    transitions: _t.List["Transition"] = _dc.field(default_factory=list)
