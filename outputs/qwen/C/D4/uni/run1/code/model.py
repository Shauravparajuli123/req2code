"""Code skeleton generated from the shared model of D4/uni.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Course:
    """Source: R1, R2, R3, R5"""
    name: _t.Optional[str] = None
    credits: _t.Optional[int] = None
    professors: _t.Optional[str] = None
    students: _t.Optional[str] = None

    def addProfessor(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addStudent(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Dormitory:
    """Source: R7, R8"""
    price: _t.Optional[float] = None
    students: _t.Optional[str] = None

    def addStudent(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Professor:
    """Source: R3"""
    name: _t.Optional[str] = None

    def teachCourse(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Student:
    """Source: R5, R6"""
    name: _t.Optional[str] = None

    def enrollInCourse(self) -> None:
        """Operation."""
        raise NotImplementedError
