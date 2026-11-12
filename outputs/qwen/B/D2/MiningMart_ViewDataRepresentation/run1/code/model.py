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
    structuralFeature: _t.Optional["StructuralFeature"] = None


@_dc.dataclass
class Attribute:
    """Source: R6"""
    name: _t.Optional[str] = None


@_dc.dataclass
class DataType:
    """Source: R5"""
    name: _t.Optional[str] = None
    attribute: _t.Optional["Attribute"] = None

    def hasAttribute(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ModelElement:
    """Source: R1"""
    pass


@_dc.dataclass
class Classifier:
    """Source: R2"""
    name: _t.Optional[str] = None


@_dc.dataclass
class StructuralFeature:
    """Source: R3"""
    pass
