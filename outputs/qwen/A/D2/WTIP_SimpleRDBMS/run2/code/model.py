"""Code skeleton generated from the shared model of D2/WTIP_SimpleRDBMS.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Table:
    """Source: R1"""
    name: _t.Optional[str] = None
    columns: _t.List["Column"] = _dc.field(default_factory=list)
    fKeys: _t.List["FKey"] = _dc.field(default_factory=list)

    def createTable(self) -> None:
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class Column:
    """Source: -"""
    name: _t.Optional[str] = None


@_dc.dataclass
class FKey:
    """Source: R3, R4"""
    referencedTable: _t.Optional[str] = None
