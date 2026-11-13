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
    """Source: -"""
    tupleElement: _t.Optional["TupleElement"] = None

    def addTupleElement(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RelationalDatabase:
    """Source: -"""
    tables: _t.List["Table"] = _dc.field(default_factory=list)

    def addTable(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Table:
    """Source: -"""

    def addTuple(self) -> None:
        """Operation."""
        raise NotImplementedError
