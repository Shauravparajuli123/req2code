"""Code skeleton generated from the shared model of D2/Architectural_Description.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Architecture:
    """Source: R7, R10, R11"""
    architectureDescription: _t.Optional["ArchitectureDescription"] = None


@_dc.dataclass
class ArchitectureDescription:
    """Source: R7, R8, R9"""
    architectureViews: _t.List["ArchitectureView"] = _dc.field(default_factory=list)


@_dc.dataclass
class ArchitectureView:
    """Source: R7, R8, R9, R12"""
    architectureViewPoint: _t.Optional["ArchitectureViewPoint"] = None


@_dc.dataclass
class ArchitectureViewPoint:
    """Source: R10, R11"""
    mainView: _t.Optional["MainView"] = None


@_dc.dataclass
class MainView:
    """Source: R11"""
    architectureView: _t.Optional["ArchitectureView"] = None
