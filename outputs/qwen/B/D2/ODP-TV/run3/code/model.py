"""Code skeleton generated from the shared model of D2/ODP-TV.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class ImplementableStandard:
    """Source: R5, R8"""
    technologyObjects: _t.List["TechnologyObject"] = _dc.field(default_factory=list)


@_dc.dataclass
class TechnologyObject:
    """Source: R1, R5, R8"""
    pass


@_dc.dataclass
class Implementation:
    """Source: R2, R5, R6, R7"""

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class IXIT:
    """Source: R3, R6, R7"""
    implementations: _t.List["Implementation"] = _dc.field(default_factory=list)
