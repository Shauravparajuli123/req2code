"""Code skeleton generated from the shared model of D2/SimpleAirlineDomain.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Airport:
    """Source: R1"""
    name: _t.Optional[str] = None
    flights: _t.List["Flight"] = _dc.field(default_factory=list)


@_dc.dataclass
class Flight:
    """Source: R2, R6, R7, R9"""
    maxPassengers: _t.Optional[int] = None
    departureTime: _t.Optional[str] = None
    originAirport: _t.Optional[str] = None
    passenger: _t.Optional["Passenger"] = None

    def createFlight(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Passenger:
    """Source: R4"""
    name: _t.Optional[str] = None
    gender: _t.Optional[str] = None

    def assignToFlight(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Airline:
    """Source: R10"""
    name: _t.Optional[str] = None
    flights: _t.List["Flight"] = _dc.field(default_factory=list)
