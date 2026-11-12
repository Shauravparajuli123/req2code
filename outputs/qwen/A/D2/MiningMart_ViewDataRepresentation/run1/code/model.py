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
    attributes: _t.List["Attribute"] = _dc.field(default_factory=list)
    attribute: _t.Optional["Attribute"] = None

    def addAttribute(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Attribute:
    """Source: R6"""
    dataType: _t.Optional[str] = None

    def associateWithClass(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class DataType:
    """Source: R5"""
    attribute: _t.Optional[str] = None

    def createAttribute(self) -> None:
        """Operation."""
        raise NotImplementedError
