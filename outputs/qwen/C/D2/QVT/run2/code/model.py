"""Code skeleton generated from the shared model of D2/QVT.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class TemplateExp:
    """Source: R1"""
    pass


@_dc.dataclass
class CollectionTemplateExpression:
    """Source: R3, R7, R8"""
    kind: _t.Optional[str] = None
    oclExpressions: _t.Optional[str] = None
    oclExpression: _t.Optional["OclExpression"] = None


@_dc.dataclass
class ObjectTemplateExp:
    """Source: R2"""
    objectContainer: _t.Optional[str] = None
    propertyTemplateItem: _t.Optional["PropertyTemplateItem"] = None


@_dc.dataclass
class PropertyTemplateItem:
    """Source: R9, R10"""
    objectContainer: _t.Optional[str] = None
    referredProperty: _t.Optional[str] = None
    objectTemplateExp: _t.Optional["ObjectTemplateExp"] = None
    property: _t.Optional["Property"] = None

    def createPropertyTemplateItem(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class OclExpression:
    """Source: R7, R8"""
    pass


@_dc.dataclass
class Property:
    """Source: R10"""
    pass
