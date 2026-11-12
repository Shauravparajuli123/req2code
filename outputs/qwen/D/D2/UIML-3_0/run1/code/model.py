"""Code skeleton generated from the shared model of D2/UIML-3_0.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class UIML:
    """Source: R1"""
    head: _t.Optional[str] = None
    header: _t.Optional["Header"] = None


@_dc.dataclass
class Header:
    """Source: R4, R6"""
    metas: _t.Optional[str] = None
    metaDatas: _t.List["MetaData"] = _dc.field(default_factory=list)

    def addMetaData(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class MetaData:
    """Source: R3"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError
