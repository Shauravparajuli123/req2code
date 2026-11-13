"""Code skeleton generated from the shared model of D2/MiningMart_ViewDataRepresentation.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Class:
    """Source: R4"""
    name: _t.Optional[str] = None
    attributes: _t.Optional[str] = None
    attribute: _t.Optional["Attribute"] = None

    def addAttribute(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Attribute:
    """Source: R6, R8, R9"""
    name: _t.Optional[str] = None
    dataType: _t.Optional[str] = None
    class_: _t.Optional[str] = None


@_dc.dataclass
class DataType:
    """Source: R5, R8"""
    attribute: _t.Optional[str] = None
