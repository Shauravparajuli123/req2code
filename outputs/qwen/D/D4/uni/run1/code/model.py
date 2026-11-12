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

    def createCourse(self) -> None:
        """Realizes UC1 "Teach Course" (R3)."""
        raise NotImplementedError


@_dc.dataclass
class Professor:
    """Source: R3"""
    name: _t.Optional[str] = None


@_dc.dataclass
class Student:
    """Source: R6, R7"""
    name: _t.Optional[str] = None
    dormitory: _t.Optional["Dormitory"] = None

    def enrollInCourse(self) -> None:
        """Realizes UC2 "Enroll In Course" (R6)."""
        raise NotImplementedError


@_dc.dataclass
class Dormitory:
    """Source: R7"""
    students: _t.Optional[str] = None
    price: _t.Optional[float] = None

    def accommodateStudent(self) -> None:
        """Realizes UC3 "Live In Dormitory" (R7)."""
        raise NotImplementedError
