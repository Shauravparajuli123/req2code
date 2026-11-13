"""Code skeleton generated from the shared model of D2/GWPNV0.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Place:
    """Source: -"""
    name: _t.Optional[str] = None
    destination: _t.Optional[str] = None


@_dc.dataclass
class Transition:
    """Source: R2, R6, R7"""
    name: _t.Optional[str] = None

    def createTransition(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Network:
    """Source: R3, R8"""
    name: _t.Optional[str] = None
    places: _t.Optional[str] = None

    def createNetwork(self) -> None:
        """Operation."""
        raise NotImplementedError
