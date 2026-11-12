"""Code skeleton generated from the shared model of D2/Make.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Makefile:
    """Source: R10, R11"""
    comment: _t.Optional[str] = None
    rules: _t.Optional[str] = None
    elements: _t.List["Element"] = _dc.field(default_factory=list)


@_dc.dataclass
class Rule:
    """Source: R3, R11, R12"""
    name: _t.Optional[str] = None
    dependencies: _t.Optional[str] = None
    ruleDeps: _t.List["RuleDep"] = _dc.field(default_factory=list)

    def addDependency(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RuleDep:
    """Source: R7"""
    rule: _t.Optional[str] = None
    file: _t.Optional[str] = None


@_dc.dataclass
class Comment:
    """Source: R10"""
    text: _t.Optional[str] = None


@_dc.dataclass
class Element:
    """Source: R2"""
    name: _t.Optional[str] = None
