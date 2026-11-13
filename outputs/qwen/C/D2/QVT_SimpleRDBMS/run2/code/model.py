"""Code skeleton generated from the shared model of D2/QVT_SimpleRDBMS.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class RmodelElement:
    """Source: R1"""
    kind: _t.Optional[str] = None


@_dc.dataclass
class Schema:
    """Source: -"""
    table: _t.Optional["Table"] = None

    def addTable(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Table:
    """Source: -"""
    schema: _t.Optional[str] = None
    keys: _t.Optional[str] = None
    columns: _t.Optional[str] = None
    key: _t.Optional["Key"] = None

    def addColumn(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addKey(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Column:
    """Source: -"""
    type: _t.Optional[str] = None
    table: _t.Optional[str] = None
    foreignKeys: _t.Optional[str] = None

    def addForeignKey(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Key:
    """Source: -"""
    table: _t.Optional[str] = None
    oppositeForeignKeys: _t.Optional[str] = None
    foreignKeys: _t.List["ForeignKey"] = _dc.field(default_factory=list)

    def addForeignKey(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ForeignKey:
    """Source: -"""
    columns: _t.Optional[str] = None
    key: _t.Optional[str] = None
