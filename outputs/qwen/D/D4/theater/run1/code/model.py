"""Code skeleton generated from the shared model of D4/theater.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Theater:
    """Source: R2, R11"""
    location: _t.Optional[str] = None
    plays: _t.List["Play"] = _dc.field(default_factory=list)


@_dc.dataclass
class Play:
    """Source: R2, R3, R11"""
    name: _t.Optional[str] = None
    type: _t.Optional[str] = None
    sessions: _t.List["Session"] = _dc.field(default_factory=list)

    def addAuthor(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addParticipant(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Author:
    """Source: R4, R7, R10"""
    name: _t.Optional[str] = None
    play: _t.Optional["Play"] = None

    def writePlay(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Participant:
    """Source: R5, R7, R12"""
    name: _t.Optional[str] = None
    plays: _t.List["Play"] = _dc.field(default_factory=list)

    def actInPlay(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Session:
    """Source: R6, R9"""
    beginTime: _t.Optional[str] = None
    endTime: _t.Optional[str] = None

    def actInSession(self) -> None:
        """Operation."""
        raise NotImplementedError
