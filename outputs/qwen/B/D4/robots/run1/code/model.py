"""Code skeleton generated from the shared model of D4/robots.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Robot:
    """Source: R1, R2"""
    id: _t.Optional[int] = None


@_dc.dataclass
class Task:
    """Source: R4, R5"""
    id: _t.Optional[int] = None

    def performTask(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class TaskExecution:
    """Source: R5"""
    id: _t.Optional[int] = None
    startTime: _t.Optional[str] = None
    location: _t.Optional[str] = None


@_dc.dataclass
class Location:
    """Source: R6, R7"""
    pass
