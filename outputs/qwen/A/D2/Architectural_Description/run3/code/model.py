"""Code skeleton generated from the shared model of D2/Architectural_Description.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class ArchitectureDescription:
    """Source: R7, R8, R9"""
    architectureViews: _t.List["ArchitectureView"] = _dc.field(default_factory=list)
    architectureViewPoint: _t.Optional["ArchitectureViewPoint"] = None

    def selectView(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ArchitectureView:
    """Source: R7, R8, R9, R12"""
    architectureViewPoints: _t.List["ArchitectureViewPoint"] = _dc.field(default_factory=list)

    def conformToViewPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def projectOntoMainView(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ArchitectureViewPoint:
    """Source: R10"""

    def conformToView(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class MainView:
    """Source: R11, R12"""

    def defineViewPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def projectOntoView(self) -> None:
        """Operation."""
        raise NotImplementedError
