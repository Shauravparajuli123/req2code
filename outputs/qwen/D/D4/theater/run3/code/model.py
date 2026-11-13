"""Code skeleton generated from the shared model of D4/theater.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Play:
    """Source: R2, R3, R11"""
    name: _t.Optional[str] = None
    type: _t.Optional[str] = None
    location: _t.Optional[str] = None
    author: _t.Optional[str] = None
    session: _t.Optional[str] = None
    theaters: _t.Optional[str] = None
    theater: _t.Optional["Theater"] = None
    authors: _t.List["Author"] = _dc.field(default_factory=list)
    participants: _t.List["Participant"] = _dc.field(default_factory=list)

    def addAuthor(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addSession(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addTheater(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Author:
    """Source: R4, R7, R10"""
    name: _t.Optional[str] = None

    def writePlay(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Participant:
    """Source: R5, R7, R12"""
    name: _t.Optional[str] = None

    def actInPlay(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Theater:
    """Source: R2, R11"""
    location: _t.Optional[str] = None

    def playPlay(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Session:
    """Source: R6, R9"""
    beginTime: _t.Optional[str] = None
    endTime: _t.Optional[str] = None
    participant: _t.Optional["Participant"] = None

    def actInSession(self) -> None:
        """Operation."""
        raise NotImplementedError
