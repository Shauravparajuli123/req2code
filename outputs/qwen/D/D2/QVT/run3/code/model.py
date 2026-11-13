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


@_dc.dataclass
class ObjectTemplateExp:
    """Source: R2"""
    propertyTemplateItems: _t.Optional[str] = None


@_dc.dataclass
class CollectionTemplateExp:
    """Source: R3"""
    oclExpressions: _t.Optional[str] = None
    templateExp: _t.Optional["TemplateExp"] = None


@_dc.dataclass
class PropertyTemplateItem:
    """Source: R9, R10"""
    objectContainer: _t.Optional[str] = None
    referredProperty: _t.Optional[str] = None
    objectTemplateExp: _t.Optional["ObjectTemplateExp"] = None
