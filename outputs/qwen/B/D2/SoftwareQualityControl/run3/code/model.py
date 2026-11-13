"""Code skeleton generated from the shared model of D2/SoftwareQualityControl.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Date:
    """Source: R1"""
    day: _t.Optional[int] = None
    year: _t.Optional[int] = None


@_dc.dataclass
class Control:
    """Source: R8, R9, R10"""
    type: _t.Optional[str] = None
    date: _t.Optional[str] = None
    controlsSequences: _t.List["ControlsSequence"] = _dc.field(default_factory=list)


@_dc.dataclass
class ControlsSequence:
    """Source: R7, R8"""
    pass


@_dc.dataclass
class ControlType(Control):
    """Source: R4"""
    pass


@_dc.dataclass
class Bug:
    """Source: R6"""
    number: _t.Optional[int] = None
    description: _t.Optional[str] = None
    originator: _t.Optional[str] = None
    commentsAnswer: _t.Optional[str] = None
    closeDate: _t.Optional[str] = None
    bugTracking: _t.Optional["BugTracking"] = None


@_dc.dataclass
class BugTracking:
    """Source: R12, R13"""
    pass


@_dc.dataclass
class Architecture:
    """Source: R11"""
    pass
