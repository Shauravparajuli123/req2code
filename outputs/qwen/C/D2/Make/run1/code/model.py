"""Code skeleton generated from the shared model of D2/Make.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Makefile:
    """Source: R10, R11"""
    fileDependencies: _t.Optional[str] = None
    comment: _t.Optional[str] = None
    rules: _t.List["Rule"] = _dc.field(default_factory=list)

    def addRule(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addFileDependency(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Rule:
    """Source: R11"""
    name: _t.Optional[str] = None

    def addDependency(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class RuleDependency:
    """Source: R13"""
    rule: _t.Optional[str] = None
