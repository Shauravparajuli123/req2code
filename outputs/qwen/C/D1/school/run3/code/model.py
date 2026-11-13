"""Code skeleton generated from the shared model of D1/school.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Guardian:
    """Source: R1, R3, R13, R14, R15, R16, R48"""

    def fillAbsence(self) -> None:
        """Realizes UC21 "Fill Absence" (R2)."""
        raise NotImplementedError

    def messageTeacher(self) -> None:
        """Realizes UC32 "Message Teacher" (R48, R6)."""
        raise NotImplementedError

    def messageMentor(self) -> None:
        """Realizes UC33 "Message Mentor" (R7)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC6 "Receive Notification" (R11, R12, R18, R19, R3, R33, R34, R53, R54)."""
        raise NotImplementedError


@_dc.dataclass
class Student:
    """Source: R5, R6, R7, R8, R11, R12, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46"""
    schedule: _t.Optional["Schedule"] = None

    def handHomework(self) -> None:
        """Realizes UC20 "Hand Homework" (R8)."""
        raise NotImplementedError

    def messageTeacher(self) -> None:
        """Realizes UC32 "Message Teacher" (R48, R6)."""
        raise NotImplementedError

    def fillAbsence(self) -> None:
        """Realizes UC21 "Fill Absence" (R2)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC6 "Receive Notification" (R11, R12, R18, R19, R3, R33, R34, R53, R54)."""
        raise NotImplementedError

    def viewInformation(self) -> None:
        """Realizes UC22 "View Information" (R4, R15)."""
        raise NotImplementedError

    def viewContactInformation(self) -> None:
        """Realizes UC24 "View Contact Information" (R16)."""
        raise NotImplementedError


@_dc.dataclass
class Teacher:
    """Source: R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46"""
    schedule: _t.Optional["Schedule"] = None

    def messageStudent(self) -> None:
        """Realizes UC34 "Message Student" (R27, R28)."""
        raise NotImplementedError

    def messageGuardian(self) -> None:
        """Operation."""
        raise NotImplementedError

    def messageTeacher(self) -> None:
        """Realizes UC32 "Message Teacher" (R48, R6)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC6 "Receive Notification" (R11, R12, R18, R19, R3, R33, R34, R53, R54)."""
        raise NotImplementedError

    def recordBehavior(self) -> None:
        """Realizes UC16 "Record Behavior" (R36)."""
        raise NotImplementedError

    def recordAttendance(self) -> None:
        """Realizes UC17 "Record Attendance" (R38)."""
        raise NotImplementedError

    def recordGrade(self) -> None:
        """Realizes UC15 "Record Grade" (R37)."""
        raise NotImplementedError

    def seeProgress(self) -> None:
        """Realizes UC27 "See Progress" (R41)."""
        raise NotImplementedError

    def setAppearanceDate(self) -> None:
        """Realizes UC29 "Set Appearance Date" (R42)."""
        raise NotImplementedError

    def setDate(self) -> None:
        """Realizes UC30 "Set Date" (R43)."""
        raise NotImplementedError

    def uploadFile(self) -> None:
        """Realizes UC31 "Upload File" (R44)."""
        raise NotImplementedError

    def viewAttendance(self) -> None:
        """Realizes UC25 "View Attendance" (R45)."""
        raise NotImplementedError

    def viewGrade(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewProgress(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewAnswer(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Administrator:
    """Source: R48, R49, R50, R51, R52, R53, R54, R55, R56"""
    messages: _t.List["Message"] = _dc.field(default_factory=list)
    account: _t.Optional["Account"] = None
    schedules: _t.List["Schedule"] = _dc.field(default_factory=list)

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R47, R50)."""
        raise NotImplementedError

    def editData(self) -> None:
        """Realizes UC2 "Edit Data" (R51)."""
        raise NotImplementedError

    def assignSchedule(self) -> None:
        """Realizes UC3 "Assign Schedule" (R49)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC6 "Receive Notification" (R11, R12, R18, R19, R3, R33, R34, R53, R54)."""
        raise NotImplementedError

    def registerChange(self) -> None:
        """Realizes UC4 "Register Change" (R55)."""
        raise NotImplementedError

    def registerAbsence(self) -> None:
        """Realizes UC5 "Register Absence" (R56)."""
        raise NotImplementedError

    def sendBroadcastMessage(self) -> None:
        """Realizes UC35 "Send Broadcast Message" (R57)."""
        raise NotImplementedError

    def setRole(self) -> None:
        """Realizes UC36 "Set Role" (R58)."""
        raise NotImplementedError

    def uploadSchedule(self) -> None:
        """Realizes UC37 "Upload Schedule" (R59)."""
        raise NotImplementedError

    def viewDetail(self) -> None:
        """Realizes UC38 "View Detail" (R60)."""
        raise NotImplementedError

    def viewStatistic(self) -> None:
        """Realizes UC39 "View Statistic" (R61)."""
        raise NotImplementedError


@_dc.dataclass
class Absence:
    """Source: R2, R12, R14, R44, R56"""

    def registerAbsence(self) -> None:
        """Realizes UC5 "Register Absence" (R56)."""
        raise NotImplementedError


@_dc.dataclass
class Notification:
    """Source: R3, R12, R14, R48, R53, R54"""

    def receiveNotification(self) -> None:
        """Realizes UC6 "Receive Notification" (R11, R12, R18, R19, R3, R33, R34, R53, R54)."""
        raise NotImplementedError


@_dc.dataclass
class Account:
    """Source: R58"""
    role: _t.Optional[str] = None
    schedule: _t.Optional["Schedule"] = None


@_dc.dataclass
class Schedule:
    """Source: R59"""

    def uploadSchedule(self) -> None:
        """Realizes UC37 "Upload Schedule" (R59)."""
        raise NotImplementedError


@_dc.dataclass
class Message:
    """Source: R57"""

    def sendBroadcastMessage(self) -> None:
        """Realizes UC35 "Send Broadcast Message" (R57)."""
        raise NotImplementedError


@_dc.dataclass
class Participant:
    """Source: R57"""
    schedule: _t.Optional["Schedule"] = None

    def sendBroadcastMessage(self) -> None:
        """Realizes UC35 "Send Broadcast Message" (R57)."""
        raise NotImplementedError
