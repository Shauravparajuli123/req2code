"""Code skeleton generated from the shared model of D2/BQL.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class BLQModel:
    """Source: R2, R3, R4, R7, R8, R9, R10"""
    queries: _t.Optional[str] = None
    entries: _t.Optional[str] = None
    fields: _t.Optional[str] = None

    def addQuery(self) -> None:
        """Realizes UC1 "Define BQL Model" (R2, R3, R4, R7, R8, R9, R10)."""
        raise NotImplementedError

    def addEntry(self) -> None:
        """Realizes UC1 "Define BQL Model" (R2, R3, R4, R7, R8, R9, R10)."""
        raise NotImplementedError

    def addField(self) -> None:
        """Realizes UC1 "Define BQL Model" (R2, R3, R4, R7, R8, R9, R10)."""
        raise NotImplementedError


@_dc.dataclass
class Query:
    """Source: R7"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Entry:
    """Source: R3, R10"""
    name: _t.Optional[str] = None
    allFields: _t.Optional[bool] = None
    field: _t.Optional["Field"] = None


@_dc.dataclass
class Field:
    """Source: R8, R9"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Predicate:
    """Source: R10"""
    name: _t.Optional[str] = None
    entry: _t.Optional["Entry"] = None
