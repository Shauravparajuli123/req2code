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


@_dc.dataclass
class ObjectTemplateExp:
    """Source: R2"""
    objectContainer: _t.Optional[str] = None
    property: _t.Optional[str] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError
