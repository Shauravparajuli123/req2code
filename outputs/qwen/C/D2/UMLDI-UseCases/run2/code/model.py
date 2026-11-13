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
    instance: _t.Optional["Instance"] = None
    linkend: _t.Optional["Linkend"] = None


@_dc.dataclass
class Linkend:
    """Source: R4"""
    link: _t.Optional[str] = None
    instance: _t.Optional[str] = None


@_dc.dataclass
class Link:
    """Source: R3"""
    linkend: _t.Optional[str] = None
    instance: _t.Optional[str] = None


@_dc.dataclass
class Resident:
    """Source: R15, R16"""
    pass
