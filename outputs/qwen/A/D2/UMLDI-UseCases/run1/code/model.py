"""Code skeleton generated from the shared model of D2/UMLDI-UseCases.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Instance:
    """Source: R1, R7, R8, R9"""
    name: _t.Optional[str] = None
    classifiers: _t.Optional[str] = None
    slots: _t.Optional[str] = None
    attributeLinks: _t.List["AttributeLink"] = _dc.field(default_factory=list)

    def addClassifier(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addSlot(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class AttributeLink:
    """Source: R10, R11"""
    instance: _t.Optional[str] = None
    linkend: _t.Optional[str] = None


@_dc.dataclass
class Linkend:
    """Source: R11, R13, R14"""
    link: _t.Optional[str] = None
    instance: _t.Optional[str] = None


@_dc.dataclass
class Link:
    """Source: R12"""
    association: _t.Optional[str] = None
    linkends: _t.List["Linkend"] = _dc.field(default_factory=list)


@_dc.dataclass
class ComponentInstance:
    """Source: R5, R15"""
    name: _t.Optional[str] = None
    residents: _t.Optional[str] = None
    nodeInstance: _t.Optional["NodeInstance"] = None


@_dc.dataclass
class NodeInstance:
    """Source: R6, R16"""
    name: _t.Optional[str] = None
    componentInstances: _t.Optional[str] = None


@_dc.dataclass
class Association:
    """Source: R12"""
    pass


@_dc.dataclass
class Classifier:
    """Source: R8"""
    pass
