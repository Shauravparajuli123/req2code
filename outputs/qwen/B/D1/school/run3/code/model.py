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
        """Realizes UC1 "Create Game" (R1)."""
        raise NotImplementedError


@_dc.dataclass
class Absence:
    """Source: R2"""
    pass


@_dc.dataclass
class Notification:
    """Source: R3, R12, R48, R53"""
    pass


@_dc.dataclass
class Information:
    """Source: R4, R15"""
    pass


@_dc.dataclass
class ContactInformation:
    """Source: R16"""
    pass


@_dc.dataclass
class Account:
    """Source: R17, R50, R51"""
    role: _t.Optional[str] = None


@_dc.dataclass
class Message:
    """Source: R1, R6, R7, R18, R27, R28, R48"""
    pass


@_dc.dataclass
class Submission:
    """Source: R8, R30, R39"""
    pass


@_dc.dataclass
class Dlm:
    """Source: R20, R21, R22, R26, R30, R31, R44"""
    pass


@_dc.dataclass
class Grade:
    """Source: R37, R40, R41"""
    pass


@_dc.dataclass
class Attendance:
    """Source: R38, R45"""
    pass


class Behavior(_enum.Enum):
    """Source: R35, R36"""
    SUFFICIENT = "SUFFICIENT"
    INSUFFICIENT = "INSUFFICIENT"


@_dc.dataclass
class Schedule:
    """Source: R49, R55"""
    pass


@_dc.dataclass
class User:
    """Source: R47, R50, R51, R53, R56"""
    pass


class Role(_enum.Enum):
    """Source: R47, R50, R51, R53, R56"""
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    ADMINISTRATOR = "ADMINISTRATOR"
    GUARDIAN = "GUARDIAN"


@_dc.dataclass
class Administrator:
    """Source: -"""
    messages: _t.List["Message"] = _dc.field(default_factory=list)
    role: _t.Optional["Role"] = None
    schedules: _t.List["Schedule"] = _dc.field(default_factory=list)

    def sendBroadcastMessage(self) -> None:
        """Realizes UC28 "Send Broadcast Message" (R57)."""
        raise NotImplementedError

    def setRole(self) -> None:
        """Realizes UC29 "Set Role" (R58)."""
        raise NotImplementedError

    def uploadSchedule(self) -> None:
        """Realizes UC30 "Upload Schedule" (R59)."""
        raise NotImplementedError

    def viewDetail(self) -> None:
        """Realizes UC31 "View Detail" (R60)."""
        raise NotImplementedError

    def viewStatistic(self) -> None:
        """Realizes UC32 "View Statistic" (R61)."""
        raise NotImplementedError


@_dc.dataclass
class Participant:
    """Source: R57"""
    pass
