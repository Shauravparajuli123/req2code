"""Code skeleton generated from the shared model of D2/QVT_SimpleRDBMS.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Schema:
    """Source: -"""
    tables: _t.List["Table"] = _dc.field(default_factory=list)


@_dc.dataclass
class Table:
    """Source: R3, R7, R8, R9"""
    name: _t.Optional[str] = None
    schema: _t.Optional[str] = None
    keys: _t.Optional[str] = None
    columns: _t.Optional[str] = None

    def addKey(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addColumn(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Column:
    """Source: R4, R10, R11"""
    name: _t.Optional[str] = None
    table: _t.Optional[str] = None
    foreignKeys: _t.Optional[str] = None

    def addForeignKey(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Key:
    """Source: R5, R12, R13"""
    name: _t.Optional[str] = None
    table: _t.Optional[str] = None
    oppositeForeignKeys: _t.Optional[str] = None
    foreignKeys: _t.List["ForeignKey"] = _dc.field(default_factory=list)


@_dc.dataclass
class ForeignKey:
    """Source: R6, R14, R15"""
    name: _t.Optional[str] = None
    columns: _t.Optional[str] = None
    key: _t.Optional[str] = None
