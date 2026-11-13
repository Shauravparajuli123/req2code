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
    slots: _t.List["Slot"] = _dc.field(default_factory=list)

    def addClassifier(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class AttributeLink:
    """Source: R2"""
    instance: _t.Optional[str] = None
    linkend: _t.Optional[str] = None

    def createLink(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Link:
    """Source: R3"""
    association: _t.Optional[str] = None

    def addLinkend(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Linkend:
    """Source: R4"""
    link: _t.Optional[str] = None
    instance: _t.Optional[str] = None

    def connectToInstance(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ComponentInstance:
    """Source: R5"""
    name: _t.Optional[str] = None
    residents: _t.Optional[str] = None

    def addResident(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class NodeInstance:
    """Source: R6"""
    name: _t.Optional[str] = None
    componentInstances: _t.Optional[str] = None
    componentInstance: _t.Optional["ComponentInstance"] = None

    def addComponentInstance(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Association:
    """Source: -"""
    pass


@_dc.dataclass
class Slot:
    """Source: -"""
    pass


@_dc.dataclass
class Resident:
    """Source: -"""
    pass
