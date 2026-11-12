"""Code skeleton generated from the shared model of D2/BQL.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Element:
    """Source: R1"""
    location: _t.Optional[str] = None
    comments: _t.Optional[str] = None


@_dc.dataclass
class BqlModel:
    """Source: R2, R7, R8, R9, R10"""
    queries: _t.Optional[str] = None
    entries: _t.Optional[str] = None
    fields: _t.Optional[str] = None

    def addQuery(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addEntry(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addField(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Query:
    """Source: R7, R10"""
    entries: _t.Optional[str] = None

    def addEntry(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Entry:
    """Source: R1, R3, R10"""
    name: _t.Optional[str] = None
    allFields: _t.Optional[bool] = None
    field: _t.Optional["Field"] = None

    def createEntry(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Field:
    """Source: R4, R8, R9"""
    name: _t.Optional[str] = None

    def createField(self) -> None:
        """Operation."""
        raise NotImplementedError
