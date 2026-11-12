"""Code skeleton generated from the shared model of D4/amphibious.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Vehicle:
    """Source: R2, R3, R5"""
    position: _t.Optional[str] = None
    speed: _t.Optional[int] = None
    maxSpeed: _t.Optional[int] = None
    environment: _t.Optional[str] = None

    def move(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class LandVehicle(Vehicle):
    """Source: R6"""
    pass


@_dc.dataclass
class MarineVehicle(Vehicle):
    """Source: R6"""
    pass


@_dc.dataclass
class AmphibiousVehicle(Vehicle):
    """Source: R7"""
    pass
