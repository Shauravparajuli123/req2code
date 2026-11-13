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


@_dc.dataclass
class BuildConfiguration:
    """Source: R9"""
    defaultGoal: _t.Optional[str] = None
    testSourceDirectoryPath: _t.Optional[str] = None

    def associateWithResources(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Resource:
    """Source: R3"""
    targetPath: _t.Optional[str] = None
    directory: _t.Optional[str] = None
    excludes: _t.Optional[str] = None
    buildConfiguration: _t.Optional["BuildConfiguration"] = None


@_dc.dataclass
class MailingList:
    """Source: R4"""
    name: _t.Optional[str] = None
    subscribeString: _t.Optional[str] = None
    archiveString: _t.Optional[str] = None


@_dc.dataclass
class Person:
    """Source: R5"""
    name: _t.Optional[str] = None
    url: _t.Optional[str] = None
    organizationUrl: _t.Optional[str] = None
    timeZone: _t.Optional[str] = None


@_dc.dataclass
class Developer:
    """Source: R6"""
    identifier: _t.Optional[int] = None


@_dc.dataclass
class Contribution:
    """Source: R7"""
    person: _t.Optional[str] = None
    developer: _t.Optional[str] = None


@_dc.dataclass
class MavenProject:
    """Source: R8, R9"""
    contributors: _t.Optional[str] = None
    mailingLists: _t.Optional[str] = None
    buildConfiguration: _t.Optional[str] = None
    mailingList: _t.Optional["MailingList"] = None

    def associateWithBuildConfiguration(self) -> None:
        """Operation."""
        raise NotImplementedError
