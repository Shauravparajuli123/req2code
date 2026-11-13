"""Code skeleton generated from the shared model of D2/RelationalDBContent.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class TupleElement:
    """Source: R5"""
    value: _t.Optional[str] = None


@_dc.dataclass
class Tuple:
    """Source: R9"""
    tupleElement: _t.Optional["TupleElement"] = None


@_dc.dataclass
class Database:
    """Source: -"""
    table: _t.Optional["Table"] = None


@_dc.dataclass
class Table:
    """Source: -"""
    tuple: _t.Optional["Tuple"] = None


@_dc.dataclass
class RelationalDBcontent:
    """Source: R3, R4"""
    tables: _t.List["Table"] = _dc.field(default_factory=list)
    tuples: _t.List["Tuple"] = _dc.field(default_factory=list)
