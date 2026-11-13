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
    """Source: R2"""
    table: _t.Optional["Table"] = None


@_dc.dataclass
class Table:
    """Source: R3, R7, R8, R9"""
    schema: _t.Optional["Schema"] = None
    key: _t.Optional["Key"] = None

    def addColumn(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addKey(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Column:
    """Source: R4, R10, R11"""
    type: _t.Optional[str] = None
    table: _t.Optional["Table"] = None
    foreignKeys: _t.List["ForeignKey"] = _dc.field(default_factory=list)

    def addColumn(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Key:
    """Source: R5, R12, R13"""
    table: _t.Optional["Table"] = None
    foreignKeys: _t.List["ForeignKey"] = _dc.field(default_factory=list)

    def addKey(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ForeignKey:
    """Source: R6, R14, R15"""
    key: _t.Optional["Key"] = None
    columns: _t.List["Column"] = _dc.field(default_factory=list)

    def addForeignKey(self) -> None:
        """Operation."""
        raise NotImplementedError
