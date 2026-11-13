"""Code skeleton generated from the shared model of D1/school.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Absence:
    """Source: R2"""
    pass


@_dc.dataclass
class AbsenceForm:
    """Source: R2"""
    pass


@_dc.dataclass
class Account:
    """Source: R50"""
    role: _t.Optional[str] = None


@_dc.dataclass
class Administrator:
    """Source: R48, R50, R51, R52, R53, R54, R55, R56"""
    messages: _t.List["Message"] = _dc.field(default_factory=list)
    account: _t.Optional["Account"] = None
    schedules: _t.List["Schedule"] = _dc.field(default_factory=list)
    performances: _t.List["Performance"] = _dc.field(default_factory=list)

    def sendBroadcastMessage(self) -> None:
        """Realizes UC12 "Send Broadcast Message" (R57)."""
        raise NotImplementedError

    def setRole(self) -> None:
        """Realizes UC13 "Set Role" (R58)."""
        raise NotImplementedError

    def uploadSchedule(self) -> None:
        """Realizes UC14 "Upload Schedule" (R59)."""
        raise NotImplementedError

    def viewDetail(self) -> None:
        """Realizes UC15 "View Detail" (R60)."""
        raise NotImplementedError

    def viewStatistic(self) -> None:
        """Realizes UC16 "View Statistic" (R61)."""
        raise NotImplementedError


@_dc.dataclass
class Answer:
    """Source: R22, R30, R31"""
    pass


@_dc.dataclass
class AppearanceDate:
    """Source: R26, R36, R42, R43"""
    pass


@_dc.dataclass
class Assignment:
    """Source: R8, R20, R21, R22, R26, R30, R31, R36, R40, R41, R42, R43"""
    pass


@_dc.dataclass
class Attendance:
    """Source: R18, R19, R27, R28, R38, R44, R45, R46"""
    pass


@_dc.dataclass
class Behavior:
    """Source: R35, R36, R40, R41"""
    pass


@_dc.dataclass
class Change:
    """Source: R55"""
    pass


@_dc.dataclass
class Child:
    """Source: R1, R5, R6, R7, R8, R15, R16, R17, R18, R19, R27, R28, R38, R45"""
    pass


@_dc.dataclass
class Date:
    """Source: R2, R18, R19, R27, R28, R38, R42, R43"""
    pass


@_dc.dataclass
class Dlm:
    """Source: R20, R21, R22, R26, R30, R31, R36, R40, R41, R42, R43"""
    pass


@_dc.dataclass
class File:
    """Source: R44"""
    pass


@_dc.dataclass
class Grade:
    """Source: R37, R40, R41"""
    pass


@_dc.dataclass
class Guardian:
    """Source: R1, R3, R4, R12, R15, R16, R17"""
    pass


@_dc.dataclass
class Homework:
    """Source: R8, R40"""
    pass


@_dc.dataclass
class Insight:
    """Source: R15, R16, R17, R18, R19, R27, R28, R38, R45, R46"""
    pass


@_dc.dataclass
class Lms:
    """Source: R5, R6, R7, R8, R10, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R26, R27, R28, R30, R31, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46"""
    pass


@_dc.dataclass
class Manner:
    """Source: R22, R30, R31"""
    pass


@_dc.dataclass
class Material:
    """Source: R20, R21, R22, R26, R30, R31, R36, R40, R41, R42, R43"""
    pass


@_dc.dataclass
class Mentor:
    """Source: R1, R18, R19, R27, R28, R38, R45"""
    pass


@_dc.dataclass
class Message:
    """Source: R1, R3, R4, R5, R6, R7, R8, R12, R15, R16, R17, R18, R19, R27, R28, R34, R38, R45, R46"""
    pass


@_dc.dataclass
class Notification:
    """Source: R2, R3, R4, R5, R6, R7, R8, R12, R15, R16, R17, R18, R19, R27, R28, R34, R38, R45, R46"""
    pass


@_dc.dataclass
class Participant:
    """Source: R18, R19, R27, R28, R38, R45, R46"""
    pass


@_dc.dataclass
class Performance:
    """Source: R15, R16, R17, R18, R19, R27, R28, R38, R45, R46"""
    pass


@_dc.dataclass
class Question:
    """Source: R22, R30, R31, R36, R40, R41"""
    pass


@_dc.dataclass
class Schedule:
    """Source: R19, R29, R32, R33, R34, R38, R45, R46"""
    student: _t.Optional["Student"] = None


@_dc.dataclass
class School:
    """Source: R1, R3, R4, R5, R6, R7, R8, R12, R15, R16, R17, R18, R19, R27, R28, R34, R38, R45, R46"""
    pass


@_dc.dataclass
class Staff:
    """Source: R1, R3, R4, R5, R6, R7, R8, R12, R15, R16, R17, R18, R19, R27, R28, R34, R38, R45, R46"""
    pass


@_dc.dataclass
class Student:
    """Source: R1, R5, R6, R7, R8, R12, R15, R16, R17, R18, R19, R27, R28, R38, R45, R46"""
    pass


@_dc.dataclass
class Submission:
    """Source: R8, R30, R31, R36, R40, R41, R42, R43"""
    pass


@_dc.dataclass
class Teacher:
    """Source: R1, R3, R4, R5, R6, R7, R8, R12, R15, R16, R17, R18, R19, R27, R28, R34, R38, R45, R46"""
    pass


@_dc.dataclass
class Timetable:
    """Source: R19, R29, R32, R33, R34, R38, R45, R46"""
    pass


@_dc.dataclass
class User:
    """Source: R1, R3, R4, R5, R6, R7, R8, R12, R15, R16, R17, R18, R19, R27, R28, R34, R38, R45, R46"""
    pass


@_dc.dataclass
class Work:
    """Source: R8, R40"""
    pass


@_dc.dataclass
class Year:
    """Source: R17, R40"""
    pass
