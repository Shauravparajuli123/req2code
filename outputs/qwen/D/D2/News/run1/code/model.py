"""Code skeleton generated from the shared model of D2/News.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class News:
    """Source: R1, R3, R5, R8, R9"""
    title: _t.Optional[str] = None
    link: _t.Optional[str] = None
    author: _t.Optional[str] = None
    date: _t.Optional[str] = None
    newspaper: _t.Optional[str] = None

    def publish(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Newspaper:
    """Source: R2, R6, R7"""
    language: _t.Optional[str] = None
    publicationDate: _t.Optional[str] = None
    news: _t.Optional[str] = None
    newses: _t.List["News"] = _dc.field(default_factory=list)

    def addNews(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Date:
    """Source: R5, R8"""
    dayOfWeek: _t.Optional[str] = None
    month: _t.Optional[str] = None
    hours: _t.Optional[int] = None
    seconds: _t.Optional[int] = None
