"""Code skeleton generated from the shared model of D2/Architectural_Description.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class ArchitectureDescription:
    """Source: R7, R8, R9, R10, R11"""

    def selectView(self) -> None:
        """Operation."""
        raise NotImplementedError

    def selectViewPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def describeArchitecture(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ArchitectureView:
    """Source: R12, R8, R9, R11"""
    architectureViewPoints: _t.List["ArchitectureViewPoint"] = _dc.field(default_factory=list)

    def projectOnto(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ArchitectureViewPoint:
    """Source: R10, R11"""

    def conformTo(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class MainView:
    """Source: R11, R12"""

    def defineView(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError
