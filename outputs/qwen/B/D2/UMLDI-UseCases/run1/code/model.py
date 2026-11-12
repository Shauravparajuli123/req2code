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

    def createInstance(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class AttributeLink:
    """Source: R2"""
    link: _t.Optional[str] = None
    instance: _t.Optional[str] = None


@_dc.dataclass
class Linkend:
    """Source: R4"""
    link: _t.Optional[str] = None
    instance: _t.Optional[str] = None


@_dc.dataclass
class Link:
    """Source: R3"""
    association: _t.Optional[str] = None


@_dc.dataclass
class ComponentInstance:
    """Source: R5"""
    residents: _t.Optional[str] = None
    resident: _t.Optional["Resident"] = None


@_dc.dataclass
class NodeInstance:
    """Source: R6"""
    componentInstances: _t.Optional[str] = None


@_dc.dataclass
class Association:
    """Source: -"""
    pass


@_dc.dataclass
class Resident:
    """Source: -"""
    pass
