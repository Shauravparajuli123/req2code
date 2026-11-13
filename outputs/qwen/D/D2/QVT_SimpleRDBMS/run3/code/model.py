"""Code skeleton generated from the shared model of D2/QVT_SimpleRDBMS.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class RModelElement:
    """Source: R1"""
    kind: _t.Optional[str] = None


@_dc.dataclass
class Schema:
    """Source: -"""
    tables: _t.List["Table"] = _dc.field(default_factory=list)


@_dc.dataclass
class Table:
    """Source: -"""
    schema: _t.Optional["Schema"] = None
    key: _t.Optional["Key"] = None


@_dc.dataclass
class Column:
    """Source: -"""
    type: _t.Optional[str] = None
    table: _t.Optional["Table"] = None


@_dc.dataclass
class Key:
    """Source: -"""
    foreignKey: _t.Optional["ForeignKey"] = None


@_dc.dataclass
class ForeignKey:
    """Source: -"""
    column: _t.Optional["Column"] = None
    key: _t.Optional["Key"] = None
