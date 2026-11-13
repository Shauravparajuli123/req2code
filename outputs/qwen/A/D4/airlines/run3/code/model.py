"""Code skeleton generated from the shared model of D4/airlines.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Airline:
    """Source: R2, R3"""
    name: _t.Optional[str] = None
    operatingCosts: _t.Optional[str] = None
    airports: _t.List["Airport"] = _dc.field(default_factory=list)
    operatingCost: _t.Optional["OperatingCost"] = None

    def addOperatingCost(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeOperatingCost(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Airport:
    """Source: R2"""
    code: _t.Optional[str] = None
    city: _t.Optional[str] = None


@_dc.dataclass
class OperatingCost:
    """Source: R3"""
    airline: _t.Optional[str] = None
    airport: _t.Optional[str] = None
    cost: _t.Optional[float] = None

    def updateCost(self) -> None:
        """Operation."""
        raise NotImplementedError
