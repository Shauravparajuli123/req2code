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
    tupleElements: _t.List["TupleElement"] = _dc.field(default_factory=list)

    def addTupleElement(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Database:
    """Source: R2, R7"""
    sgbdName: _t.Optional[str] = None
    tables: _t.List["Table"] = _dc.field(default_factory=list)


@_dc.dataclass
class Table:
    """Source: R3, R6, R7, R8"""
    tuple: _t.Optional["Tuple"] = None

    def addDatabase(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RelationalDBcontent:
    """Source: R3, R4"""
    tables: _t.List["Table"] = _dc.field(default_factory=list)
    tuples: _t.List["Tuple"] = _dc.field(default_factory=list)
