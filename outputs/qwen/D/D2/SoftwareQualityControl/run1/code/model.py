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
    """Source: -"""
    type: _t.Optional[str] = None
    date: _t.Optional[str] = None

    def belongsToSequence(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ControlsSequence:
    """Source: R7, R8"""
    controls: _t.Optional[str] = None


@_dc.dataclass
class Bug:
    """Source: R6, R12"""
    number: _t.Optional[int] = None
    description: _t.Optional[str] = None
    originator: _t.Optional[str] = None
    comments: _t.Optional[str] = None
    closeDate: _t.Optional[str] = None

    def linkedToControlType(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Architecture:
    """Source: R11"""
    pass
