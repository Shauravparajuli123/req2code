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
    shellLines: _t.Optional[str] = None
    dependencies: _t.List["Dependency"] = _dc.field(default_factory=list)

    def addShellLine(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class File:
    """Source: R9"""
    name: _t.Optional[str] = None
    dependencies: _t.List["Dependency"] = _dc.field(default_factory=list)


@_dc.dataclass
class Comment:
    """Source: R6"""
    text: _t.Optional[str] = None


@_dc.dataclass
class ShellLine:
    """Source: R12"""
    command: _t.Optional[str] = None


@_dc.dataclass
class Dependency:
    """Source: R7"""
    rule: _t.Optional[str] = None
    file: _t.Optional[str] = None


class RuleDep(_enum.Enum):
    """Source: R13"""
    RULE = "RULE"
    FILE = "FILE"
