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
    level: _t.Optional["Level"] = None


@_dc.dataclass
class Level:
    """Source: R2, R5, R6"""
    trace: _t.Optional[str] = None
    value: _t.Optional[int] = None

    def addLevel(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Call:
    """Source: R3, R7"""
    methodName: _t.Optional[str] = None
    numberOfDatabaseRows: _t.Optional[int] = None
    level: _t.Optional[str] = None

    def createCall(self) -> None:
        """Operation."""
        raise NotImplementedError
