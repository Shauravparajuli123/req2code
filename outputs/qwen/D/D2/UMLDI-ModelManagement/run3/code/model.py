"""Code skeleton generated from the shared model of D2/UMLDI-ModelManagement.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class CoreModel:
    """Source: R1, R2, R4, R5, R10, R12, R14"""
    name: _t.Optional[str] = None
    containsElements: _t.Optional[str] = None
    modelElements: _t.List["ModelElement"] = _dc.field(default_factory=list)
    namespaces: _t.List["Namespace"] = _dc.field(default_factory=list)
    classifiers: _t.List["Classifier"] = _dc.field(default_factory=list)
    features: _t.List["Feature"] = _dc.field(default_factory=list)
    generalizableElements: _t.List["GeneralizableElement"] = _dc.field(default_factory=list)
    generalizations: _t.List["Generalization"] = _dc.field(default_factory=list)

    def addModelElement(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeModelElement(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ModelElement:
    """Source: R2, R9"""
    name: _t.Optional[str] = None
    isASpecification: _t.Optional[bool] = None


@_dc.dataclass
class Namespace:
    """Source: R11"""
    name: _t.Optional[str] = None
    modelElements: _t.Optional[str] = None


@_dc.dataclass
class Classifier:
    """Source: R5, R12, R13"""
    name: _t.Optional[str] = None
    powerTypeRanges: _t.Optional[str] = None


@_dc.dataclass
class Feature:
    """Source: R6, R13"""
    name: _t.Optional[str] = None
    ownerScope: _t.Optional[str] = None
    owner: _t.Optional[str] = None


@_dc.dataclass
class Generalization:
    """Source: R7, R8, R14"""
    name: _t.Optional[str] = None
    discriminator: _t.Optional[str] = None
    parent: _t.Optional[str] = None


@_dc.dataclass
class GeneralizableElement(Generalization):
    """Source: R3, R10, R15"""
    name: _t.Optional[str] = None
    isARoot: _t.Optional[bool] = None
    isAbstract: _t.Optional[bool] = None
    generalizations: _t.Optional[str] = None
