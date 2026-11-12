"""Code skeleton generated from the shared model of D1/school.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Guardian:
    """Source: R3, R12, R13, R14, R15, R16, R48"""
    messages: _t.List["Message"] = _dc.field(default_factory=list)

    def directMessage(self) -> None:
        """Realizes UC2 "Direct Message" (R1, R6, R12, R34)."""
        raise NotImplementedError

    def fillAbsence(self) -> None:
        """Realizes UC3 "Fill Absence" (R2)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC19 "Receive Notification" (R3, R11, R12)."""
        raise NotImplementedError

    def viewInformation(self) -> None:
        """Realizes UC4 "View Information" (R4, R15)."""
        raise NotImplementedError


@_dc.dataclass
class Student:
    """Source: R5, R6, R7, R8, R9, R10, R11, R12, R16, R17, R45, R46"""
    messages: _t.List["Message"] = _dc.field(default_factory=list)
    absence: _t.Optional["Absence"] = None
    notifications: _t.List["Notification"] = _dc.field(default_factory=list)
    dlms: _t.List["Dlm"] = _dc.field(default_factory=list)
    schedule: _t.Optional["Schedule"] = None

    def directMessage(self) -> None:
        """Realizes UC2 "Direct Message" (R1, R6, R12, R34)."""
        raise NotImplementedError

    def handHomework(self) -> None:
        """Realizes UC14 "Hand Homework" (R8)."""
        raise NotImplementedError

    def haveAccess(self) -> None:
        """Realizes UC15 "Have Access" (R9, R10)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC19 "Receive Notification" (R3, R11, R12)."""
        raise NotImplementedError

    def viewContactInformation(self) -> None:
        """Realizes UC35 "View Contact Information" (R16)."""
        raise NotImplementedError


@_dc.dataclass
class Teacher:
    """Source: R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46"""
    messages: _t.List["Message"] = _dc.field(default_factory=list)
    notifications: _t.List["Notification"] = _dc.field(default_factory=list)
    dlms: _t.List["Dlm"] = _dc.field(default_factory=list)

    def directMessage(self) -> None:
        """Realizes UC2 "Direct Message" (R1, R6, R12, R34)."""
        raise NotImplementedError

    def editPage(self) -> None:
        """Realizes UC11 "Edit Data" (R51)."""
        raise NotImplementedError

    def makeSubmissionElement(self) -> None:
        """Realizes UC16 "Make Submission Element" (R30)."""
        raise NotImplementedError

    def receiveConfirmation(self) -> None:
        """Realizes UC18 "Receive Confirmation" (R32)."""
        raise NotImplementedError

    def recordAction(self) -> None:
        """Realizes UC20 "Record Action" (R35)."""
        raise NotImplementedError

    def recordBehavior(self) -> None:
        """Realizes UC22 "Record Behavior" (R36)."""
        raise NotImplementedError

    def recordGrade(self) -> None:
        """Realizes UC23 "Record Grade" (R37)."""
        raise NotImplementedError

    def recordAttendance(self) -> None:
        """Realizes UC21 "Record Attendance" (R38)."""
        raise NotImplementedError

    def seeAnswer(self) -> None:
        """Realizes UC27 "See Answer" (R39)."""
        raise NotImplementedError

    def seeProgress(self) -> None:
        """Realizes UC29 "See Progress" (R41)."""
        raise NotImplementedError

    def setAppearanceDate(self) -> None:
        """Realizes UC30 "Set Appearance Date" (R42)."""
        raise NotImplementedError

    def uploadFile(self) -> None:
        """Realizes UC32 "Upload File" (R44)."""
        raise NotImplementedError

    def viewAttendance(self) -> None:
        """Realizes UC33 "View Attendance" (R45)."""
        raise NotImplementedError

    def viewClass(self) -> None:
        """Realizes UC34 "View Class" (R46)."""
        raise NotImplementedError


@_dc.dataclass
class Administrator:
    """Source: R48, R49, R50, R51, R52, R53, R54, R55, R56"""
    messages: _t.List["Message"] = _dc.field(default_factory=list)
    notifications: _t.List["Notification"] = _dc.field(default_factory=list)
    account: _t.Optional["Account"] = None
    schedules: _t.List["Schedule"] = _dc.field(default_factory=list)

    def directMessage(self) -> None:
        """Realizes UC2 "Direct Message" (R1, R6, R12, R34)."""
        raise NotImplementedError

    def assignSchedule(self) -> None:
        """Realizes UC9 "Assign Schedule" (R49)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC10 "Create Account" (R50)."""
        raise NotImplementedError

    def editData(self) -> None:
        """Realizes UC11 "Edit Data" (R51)."""
        raise NotImplementedError

    def makeUse(self) -> None:
        """Realizes UC17 "Make Use" (R52)."""
        raise NotImplementedError

    def registerChange(self) -> None:
        """Realizes UC25 "Register Change" (R55)."""
        raise NotImplementedError

    def registerAbsence(self) -> None:
        """Realizes UC24 "Register Absence" (R56)."""
        raise NotImplementedError

    def sendBroadcastMessage(self) -> None:
        """Realizes UC36 "Send Broadcast Message" (R57)."""
        raise NotImplementedError

    def setRole(self) -> None:
        """Realizes UC37 "Set Role" (R58)."""
        raise NotImplementedError

    def uploadSchedule(self) -> None:
        """Realizes UC38 "Upload Schedule" (R59)."""
        raise NotImplementedError

    def viewDetail(self) -> None:
        """Realizes UC39 "View Detail" (R60)."""
        raise NotImplementedError

    def viewStatistic(self) -> None:
        """Realizes UC40 "View Statistic" (R61)."""
        raise NotImplementedError


@_dc.dataclass
class Message:
    """Source: R1, R6, R7, R18, R19, R27, R28, R34, R48"""
    content: _t.Optional[str] = None
    participants: _t.Optional[str] = None

    def send(self) -> None:
        """Realizes UC2 "Direct Message" (R1, R6, R12, R34)."""
        raise NotImplementedError

    def receive(self) -> None:
        """Realizes UC19 "Receive Notification" (R3, R11, R12)."""
        raise NotImplementedError


@_dc.dataclass
class Notification:
    """Source: R3, R12, R13, R14, R17, R34, R43, R48"""

    def send(self) -> None:
        """Realizes UC19 "Receive Notification" (R3, R11, R12)."""
        raise NotImplementedError


@_dc.dataclass
class Absence:
    """Source: R2, R14, R54"""

    def register(self) -> None:
        """Realizes UC24 "Register Absence" (R56)."""
        raise NotImplementedError


@_dc.dataclass
class Dlm:
    """Source: R20, R21, R22, R23, R24, R26, R29, R30, R31, R32, R36, R37, R44, R45"""

    def addPage(self) -> None:
        """Realizes UC6 "Add Page" (R20, R21, R22)."""
        raise NotImplementedError

    def assign(self) -> None:
        """Realizes UC8 "Assign DLM" (R23)."""
        raise NotImplementedError

    def edit(self) -> None:
        """Realizes UC11 "Edit Data" (R51)."""
        raise NotImplementedError

    def makeSubmissionElement(self) -> None:
        """Realizes UC16 "Make Submission Element" (R30)."""
        raise NotImplementedError

    def setAppearanceDate(self) -> None:
        """Realizes UC30 "Set Appearance Date" (R42)."""
        raise NotImplementedError

    def uploadFile(self) -> None:
        """Realizes UC32 "Upload File" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class File:
    """Source: R5, R10, R17, R44"""

    def upload(self) -> None:
        """Realizes UC32 "Upload File" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class Grade:
    """Source: R37, R40, R41"""

    def record_(self) -> None:
        """Realizes UC23 "Record Grade" (R37)."""
        raise NotImplementedError

    def see(self) -> None:
        """Realizes UC28 "See Grade" (R40)."""
        raise NotImplementedError

    def seeProgress(self) -> None:
        """Realizes UC29 "See Progress" (R41)."""
        raise NotImplementedError


class Behavior(_enum.Enum):
    """Source: R36"""
    SUFFICIENT = "SUFFICIENT"
    INSUFFICIENT = "INSUFFICIENT"


@_dc.dataclass
class Account:
    """Source: R58"""
    role: _t.Optional[str] = None


@_dc.dataclass
class Participant:
    """Source: R57"""
    pass


@_dc.dataclass
class Schedule:
    """Source: R59"""
    date: _t.Optional[str] = None
    details: _t.Optional[str] = None
