"""Code skeleton generated from the shared model of D2/QVT.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class TemplateExp:
    """Source: R1"""
    collectionKind: _t.Optional[str] = None
    variable: _t.Optional[str] = None
    objectTemplateExp: _t.Optional["ObjectTemplateExp"] = None
    collectionTemplateExp: _t.Optional["CollectionTemplateExp"] = None


@_dc.dataclass
class ObjectTemplateExp:
    """Source: R2"""
    propertyTemplateItems: _t.Optional[str] = None


@_dc.dataclass
class CollectionTemplateExp:
    """Source: R3"""
    oclExpressions: _t.Optional[str] = None
    oclExpressionMatch: _t.Optional[str] = None
