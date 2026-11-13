"""Code skeleton generated from the shared model of D4/theater.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Play:
    """Source: R1, R3, R11"""
    name: _t.Optional[str] = None
    location: _t.Optional[str] = None
    day: _t.Optional[bool] = None
    night: _t.Optional[bool] = None
    authors: _t.List["Author"] = _dc.field(default_factory=list)
    participants: _t.List["Participant"] = _dc.field(default_factory=list)
    sessions: _t.List["Session"] = _dc.field(default_factory=list)


@_dc.dataclass
class Author:
    """Source: R4, R7, R10"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Participant:
    """Source: R5, R7, R12"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Session:
    """Source: R6, R9"""
    beginTime: _t.Optional[str] = None
    endTime: _t.Optional[str] = None


@_dc.dataclass
class Theater:
    """Source: R1, R11"""
    location: _t.Optional[str] = None
    plays: _t.List["Play"] = _dc.field(default_factory=list)
