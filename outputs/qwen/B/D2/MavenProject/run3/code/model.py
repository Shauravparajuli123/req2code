"""Code skeleton generated from the shared model of D2/MavenProject.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class MavenProject:
    """Source: R7, R8, R9"""
    name: _t.Optional[str] = None
    contributors: _t.Optional[str] = None
    mailingLists: _t.Optional[str] = None
    buildConfiguration: _t.Optional[str] = None
    mailingList: _t.Optional["MailingList"] = None
    resources: _t.List["Resource"] = _dc.field(default_factory=list)

    def addContributor(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addMailingList(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Contributor:
    """Source: R5, R6"""
    name: _t.Optional[str] = None
    url: _t.Optional[str] = None
    organizationUrl: _t.Optional[str] = None
    timeZone: _t.Optional[str] = None
    identifier: _t.Optional[str] = None


@_dc.dataclass
class BuildConfiguration:
    """Source: R9"""
    defaultGoal: _t.Optional[str] = None
    path: _t.Optional[str] = None


@_dc.dataclass
class MailingList:
    """Source: R4"""
    name: _t.Optional[str] = None
    subscribeString: _t.Optional[str] = None
    archiveString: _t.Optional[str] = None


@_dc.dataclass
class Resource:
    """Source: R3"""
    targetPath: _t.Optional[str] = None
    directory: _t.Optional[str] = None
    excludes: _t.Optional[str] = None
    mavenProject: _t.Optional["MavenProject"] = None
