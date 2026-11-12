"""Code skeleton generated from the shared model of D2/UMLDI-ModelManagement.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class CoreModel:
    """Source: R1, R4, R5, R11"""
    name: _t.Optional[str] = None
    isSpecification: _t.Optional[bool] = None
    classifiers: _t.List["Classifier"] = _dc.field(default_factory=list)
    elements: _t.List["Element"] = _dc.field(default_factory=list)
    generalizations: _t.List["Generalization"] = _dc.field(default_factory=list)
    namespaces: _t.List["Namespace"] = _dc.field(default_factory=list)


@_dc.dataclass
class Element:
    """Source: R2, R3, R10"""
    name: _t.Optional[str] = None
    isRoot: _t.Optional[bool] = None
    isAbstract: _t.Optional[bool] = None
    generalizations: _t.Optional[str] = None

    def createElement(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Namespace:
    """Source: R11"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Classifier:
    """Source: R5, R12, R13"""
    name: _t.Optional[str] = None
    powerTypeRanges: _t.Optional[str] = None

    def createClassifier(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Feature:
    """Source: R6"""
    name: _t.Optional[str] = None
    ownerScope: _t.Optional[str] = None

    def createFeature(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Generalization:
    """Source: R7, R8, R14, R15"""
    name: _t.Optional[str] = None
    discriminator: _t.Optional[bool] = None
    parent: _t.Optional[str] = None
    child: _t.Optional[str] = None

    def createGeneralization(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class GeneralizableElement:
    """Source: R3, R10, R15"""
    name: _t.Optional[str] = None
    isRoot: _t.Optional[bool] = None
    isAbstract: _t.Optional[bool] = None
    generalizations: _t.Optional[str] = None

    def createGeneralizableElement(self) -> None:
        """Operation."""
        raise NotImplementedError
