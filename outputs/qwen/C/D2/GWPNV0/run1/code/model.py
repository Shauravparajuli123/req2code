"""Code skeleton generated from the shared model of D2/GWPNV0.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class PetriNet:
    """Source: -"""
    place: _t.Optional["Place"] = None
    transition: _t.Optional["Transition"] = None


@_dc.dataclass
class Network:
    """Source: R3"""
    pass


@_dc.dataclass
class Place:
    """Source: R1, R5, R8"""
    name: _t.Optional[str] = None

    def addDestination(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Transition:
    """Source: R2, R6, R7"""
    name: _t.Optional[str] = None

    def setDestination(self) -> None:
        """Operation."""
        raise NotImplementedError
