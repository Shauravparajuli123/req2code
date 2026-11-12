"""Code skeleton generated from the shared model of D4/airlines.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Airline:
    """Source: R2"""
    name: _t.Optional[str] = None
    airports: _t.List["Airport"] = _dc.field(default_factory=list)


@_dc.dataclass
class Airport:
    """Source: R2"""
    code: _t.Optional[str] = None
    city: _t.Optional[str] = None


@_dc.dataclass
class OperatingCost:
    """Source: R3, R4"""
    cost: _t.Optional[float] = None
    airlineOperation: _t.Optional["AirlineOperation"] = None
    airline: _t.Optional["Airline"] = None


@_dc.dataclass
class Operation:
    """Source: R4"""
    startDateTime: _t.Optional[str] = None
    stopDateTime: _t.Optional[str] = None
    cost: _t.Optional[str] = None


@_dc.dataclass
class AirlineOperation:
    """Source: R3, R4"""
    airline: _t.Optional[str] = None
    airport: _t.Optional[str] = None
    operation: _t.Optional[str] = None


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError
