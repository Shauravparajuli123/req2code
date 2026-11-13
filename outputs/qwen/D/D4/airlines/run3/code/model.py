"""Code skeleton generated from the shared model of D4/airlines.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Airline:
    """Source: R2, R3, R4"""
    name: _t.Optional[str] = None
    airports: _t.List["Airport"] = _dc.field(default_factory=list)
    details: _t.Optional["Details"] = None

    def startOperation(self) -> None:
        """Operation."""
        raise NotImplementedError

    def stopOperation(self) -> None:
        """Operation."""
        raise NotImplementedError

    def updateOperatingCost(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Airport:
    """Source: R2"""
    code: _t.Optional[str] = None
    city: _t.Optional[str] = None


@_dc.dataclass
class Operation:
    """Source: R4"""
    operatingCost: _t.Optional[float] = None
    airport: _t.Optional["Airport"] = None
    airline: _t.Optional["Airline"] = None


@_dc.dataclass
class Details:
    """Source: R5"""
    operation: _t.Optional["Operation"] = None
