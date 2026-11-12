"""Code skeleton generated from the shared model of D2/Trace.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Trace:
    """Source: R1"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Level:
    """Source: R2"""
    trace: _t.Optional[str] = None
    traces: _t.List["Trace"] = _dc.field(default_factory=list)


@_dc.dataclass
class Call:
    """Source: R3"""
    methodName: _t.Optional[str] = None
    numberOfRows: _t.Optional[int] = None
    level: _t.Optional[str] = None


@_dc.dataclass
class Index:
    """Source: R4"""
    value: _t.Optional[int] = None


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError
