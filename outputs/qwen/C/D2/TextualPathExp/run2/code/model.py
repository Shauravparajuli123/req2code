"""Code skeleton generated from the shared model of D2/TextualPathExp.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class AlternativeTrans:
    """Source: R4"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Path:
    """Source: R6, R7"""
    transitions: _t.Optional[str] = None
    alternativeTranses: _t.List["AlternativeTrans"] = _dc.field(default_factory=list)


@_dc.dataclass
class Transition:
    """Source: R3, R7"""
    pass


@_dc.dataclass
class TextualPathExp:
    """Source: R1"""
    paths: _t.Optional[str] = None
    path: _t.Optional["Path"] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError
