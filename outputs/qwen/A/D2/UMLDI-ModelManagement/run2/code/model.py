"""Code skeleton generated from the shared model of D2/UMLDI-ModelManagement.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class CoreModel:
    """Source: R1, R2, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15"""
    name: _t.Optional[str] = None
    isSpecification: _t.Optional[bool] = None
    modelElements: _t.List["ModelElement"] = _dc.field(default_factory=list)
    classifiers: _t.List["Classifier"] = _dc.field(default_factory=list)
    features: _t.List["Feature"] = _dc.field(default_factory=list)
    namespaces: _t.List["Namespace"] = _dc.field(default_factory=list)
    generalizations: _t.List["Generalization"] = _dc.field(default_factory=list)


@_dc.dataclass
class ModelElement:
    """Source: R1, R2, R9"""
    name: _t.Optional[str] = None
    isSpecification: _t.Optional[bool] = None


@_dc.dataclass
class Namespace:
    """Source: R11"""
    name: _t.Optional[str] = None
    modelElements: _t.Optional[str] = None


@_dc.dataclass
class Classifier:
    """Source: R5, R12, R13"""
    name: _t.Optional[str] = None
    isSpecification: _t.Optional[bool] = None
    powerTypeRanges: _t.Optional[str] = None
    owner: _t.Optional[str] = None


@_dc.dataclass
class Feature:
    """Source: R6, R13"""
    name: _t.Optional[str] = None
    ownerScope: _t.Optional[str] = None
    owner: _t.Optional[str] = None
    classifier: _t.Optional["Classifier"] = None


@_dc.dataclass
class GeneralizableElement(Classifier):
    """Source: R3, R10, R15"""
    name: _t.Optional[str] = None
    isRoot: _t.Optional[bool] = None
    isAbstract: _t.Optional[bool] = None
    generalizations: _t.Optional[str] = None
    generalization: _t.Optional[str] = None


@_dc.dataclass
class Generalization:
    """Source: R7, R8, R14"""
    name: _t.Optional[str] = None
    parent: _t.Optional[str] = None
    discriminator: _t.Optional[str] = None
    generalizableElement: _t.Optional["GeneralizableElement"] = None


class ScopeKind(_enum.Enum):
    """Source: R6"""
    CLASS = "CLASS"
    INTERFACE = "INTERFACE"
    VALUE = "VALUE"
