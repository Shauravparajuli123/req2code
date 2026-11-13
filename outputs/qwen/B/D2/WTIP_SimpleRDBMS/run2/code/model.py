"""Code skeleton generated from the shared model of D2/WTIP_SimpleRDBMS.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Table:
    """Source: -"""
    name: _t.Optional[str] = None
    fkeys: _t.Optional[str] = None
    columns: _t.Optional[str] = None
    column: _t.Optional["Column"] = None
    fkey: _t.Optional["Fkey"] = None

    def addFkey(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addColumn(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Column:
    """Source: R2"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Fkey:
    """Source: R3, R4, R6"""
    referencedTable: _t.Optional[str] = None
