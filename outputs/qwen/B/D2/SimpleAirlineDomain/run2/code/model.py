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
    flight: _t.Optional["Flight"] = None


@_dc.dataclass
class Flight:
    """Source: R2, R6, R7, R9, R10"""
    name: _t.Optional[str] = None
    departureTime: _t.Optional[str] = None
    originAirport: _t.Optional[str] = None
    maxPassengers: _t.Optional[int] = None
    passengers: _t.Optional[str] = None
    passenger: _t.Optional["Passenger"] = None

    def addPassenger(self) -> None:
        """Operation."""
        raise NotImplementedError

    def createFlight(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Passenger:
    """Source: R4, R11"""
    name: _t.Optional[str] = None
    gender: _t.Optional[str] = None
    flight: _t.Optional[str] = None

    def assignToFlight(self) -> None:
        """Operation."""
        raise NotImplementedError
