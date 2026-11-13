"""Code skeleton generated from the shared model of D2/UMLDI-UseCases.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Instance:
    """Source: R1"""
    name: _t.Optional[str] = None
    classifiers: _t.Optional[str] = None
    slots: _t.Optional[str] = None

    def addClassifier(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeClassifier(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addSlot(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeSlot(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class AttributeLink:
    """Source: R10, R11"""
    instance: _t.Optional[str] = None
    linkend: _t.Optional[str] = None


@_dc.dataclass
class Link:
    """Source: R12"""
    association: _t.Optional[str] = None


@_dc.dataclass
class Linkend:
    """Source: R13, R14"""
    link: _t.Optional[str] = None
    instance: _t.Optional[str] = None


@_dc.dataclass
class ComponentInstance:
    """Source: R15"""
    residents: _t.Optional[str] = None


@_dc.dataclass
class NodeInstance:
    """Source: R16"""
    componentInstances: _t.Optional[str] = None
