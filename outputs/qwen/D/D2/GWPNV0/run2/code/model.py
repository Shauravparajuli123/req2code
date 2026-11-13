"""Code skeleton generated from the shared model of D2/GWPNV0.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Place:
    """Source: R1, R5, R7, R8"""
    name: _t.Optional[str] = None
    destination: _t.Optional[str] = None
    transition: _t.Optional["Transition"] = None


@_dc.dataclass
class Transition:
    """Source: R2, R6, R7"""
    name: _t.Optional[str] = None
    destination: _t.Optional[str] = None
    network: _t.Optional["Network"] = None


@_dc.dataclass
class PetriNet:
    """Source: R1, R2, R3, R4"""
    name: _t.Optional[str] = None
    places: _t.Optional[str] = None
    transitions: _t.Optional[str] = None
    network: _t.Optional["Network"] = None

    def addPlace(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addTransition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Network(PetriNet):
    """Source: R3, R8"""
    name: _t.Optional[str] = None
