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
    control: _t.Optional["Control"] = None


class ControlType(_enum.Enum):
    """Source: R4"""
    UNDEFINED = "UNDEFINED"


@_dc.dataclass
class Control:
    """Source: R8, R10"""
    type: _t.Optional[str] = None
    controlsSequences: _t.List["ControlsSequence"] = _dc.field(default_factory=list)
    controlType: _t.Optional["ControlType"] = None

    def createControl(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ControlsSequence:
    """Source: R2, R7, R8"""
    controls: _t.Optional[str] = None

    def addControl(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Bug:
    """Source: R6, R12"""
    number: _t.Optional[int] = None
    description: _t.Optional[str] = None
    originator: _t.Optional[str] = None
    commentsAnswer: _t.Optional[str] = None
    closeDate: _t.Optional[str] = None
    bugTracking: _t.Optional["BugTracking"] = None

    def createBug(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class BugTracking:
    """Source: R5, R12, R13"""
    bugs: _t.Optional[str] = None

    def addBug(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Architecture:
    """Source: R11"""
    pass
