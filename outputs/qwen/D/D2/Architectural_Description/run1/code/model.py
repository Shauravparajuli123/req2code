"""Code skeleton generated from the shared model of D2/Architectural_Description.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class ArchitectureDescription:
    """Source: R7, R8, R9"""
    architectureViews: _t.Optional[str] = None

    def selectArchitectureView(self) -> None:
        """Operation."""
        raise NotImplementedError

    def selectArchitectureDescription(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ArchitectureView:
    """Source: R7, R12"""
    architectureViewPoints: _t.Optional[str] = None
    mainView: _t.Optional[str] = None
    architectureViewPoint: _t.Optional["ArchitectureViewPoint"] = None

    def conformToArchitectureViewPoint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def projectOntoMainView(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class MainView:
    """Source: R11, R12"""
    architectureViews: _t.Optional[str] = None
    architectureView: _t.Optional["ArchitectureView"] = None

    def projectOntoArchitectureView(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class ArchitectureViewPoint:
    """Source: R10"""
    architectureViews: _t.Optional[str] = None
    mainView: _t.Optional["MainView"] = None

    def conformToArchitectureView(self) -> None:
        """Operation."""
        raise NotImplementedError
