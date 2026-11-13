"""Code skeleton generated from the shared model of D2/MavenProject.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Project:
    """Source: R1"""
    identifier: _t.Optional[str] = None
    artifactIdentifier: _t.Optional[str] = None
    description: _t.Optional[str] = None
    buildConfiguration: _t.Optional["BuildConfiguration"] = None
    resources: _t.List["Resource"] = _dc.field(default_factory=list)
    mailingList: _t.Optional["MailingList"] = None
    contributors: _t.List["Contributor"] = _dc.field(default_factory=list)


@_dc.dataclass
class BuildConfiguration:
    """Source: R9"""
    defaultGoal: _t.Optional[str] = None
    pathToUnitTestSourceDirectory: _t.Optional[str] = None

    def associateWithResources(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Resource:
    """Source: R10"""
    targetPath: _t.Optional[str] = None
    directory: _t.Optional[str] = None
    excludes: _t.Optional[str] = None


@_dc.dataclass
class MailingList:
    """Source: R4"""
    name: _t.Optional[str] = None
    subscribeString: _t.Optional[str] = None
    archiveString: _t.Optional[str] = None


@_dc.dataclass
class Contributor:
    """Source: R7"""
    identifier: _t.Optional[str] = None


@_dc.dataclass
class Person:
    """Source: R5"""
    name: _t.Optional[str] = None
    url: _t.Optional[str] = None
    organizationUrl: _t.Optional[str] = None
    timeZone: _t.Optional[str] = None
