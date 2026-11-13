"""Code skeleton generated from the shared model of D2/RelationalDBSchema.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Database:
    """Source: -"""
    sgbdName: _t.Optional[str] = None
    tables: _t.Optional[str] = None


@_dc.dataclass
class Table:
    """Source: -"""
    columns: _t.Optional[str] = None
    database: _t.Optional[str] = None
    databases: _t.List["Database"] = _dc.field(default_factory=list)


@_dc.dataclass
class Column:
    """Source: -"""
    dataType: _t.Optional[str] = None
    defaultValue: _t.Optional[str] = None
    owner: _t.Optional[str] = None
    table: _t.Optional["Table"] = None
