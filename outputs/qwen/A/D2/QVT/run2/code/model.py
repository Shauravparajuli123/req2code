"""Code skeleton generated from the shared model of D2/QVT.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class TemplateExp:
    """Source: R1"""
    objectTemplateExp: _t.Optional["ObjectTemplateExp"] = None
    propertyTemplateItems: _t.List["PropertyTemplateItem"] = _dc.field(default_factory=list)


@_dc.dataclass
class ObjectTemplateExp(TemplateExp):
    """Source: R2"""
    objectContainer: _t.Optional[str] = None
    referredProperty: _t.Optional[str] = None
    propertyTemplateItem: _t.Optional["PropertyTemplateItem"] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class PropertyTemplateItem:
    """Source: -"""
    objectContainer: _t.Optional[str] = None
    referredProperty: _t.Optional[str] = None
