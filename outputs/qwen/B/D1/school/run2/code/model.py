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
class Student:
    """Source: R6, R7, R12, R13, R14, R15, R16, R17, R18, R27, R28, R34, R45, R46"""
    name: _t.Optional[str] = None
    contactInformation: _t.Optional[str] = None
    knowledge: _t.Optional[str] = None
    homework: _t.Optional[str] = None
    timetable: _t.Optional[str] = None
    grade: _t.Optional[str] = None
    attendance: _t.Optional[str] = None

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R6, R7, R18, R19, R27, R28)."""
        raise NotImplementedError

    def fillAbsence(self) -> None:
        """Realizes UC2 "Fill Absence" (R2)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R3, R11, R12)."""
        raise NotImplementedError

    def viewInformation(self) -> None:
        """Realizes UC4 "View Information" (R4, R15, R45)."""
        raise NotImplementedError

    def viewClass(self) -> None:
        """Realizes UC21 "View Class" (R46)."""
        raise NotImplementedError

    def viewContactInformation(self) -> None:
        """Realizes UC22 "View Contact Information" (R16)."""
        raise NotImplementedError

    def receiveConfirmation(self) -> None:
        """Realizes UC11 "Receive Confirmation" (R32)."""
        raise NotImplementedError

    def recordBehavior(self) -> None:
        """Realizes UC12 "Record Behavior" (R36)."""
        raise NotImplementedError

    def recordGrade(self) -> None:
        """Realizes UC13 "Record Grade" (R37)."""
        raise NotImplementedError

    def recordAttendance(self) -> None:
        """Realizes UC14 "Record Attendance" (R38)."""
        raise NotImplementedError

    def seeAnswer(self) -> None:
        """Realizes UC15 "See Answer" (R39)."""
        raise NotImplementedError

    def seeProgress(self) -> None:
        """Realizes UC17 "See Progress" (R41)."""
        raise NotImplementedError


@_dc.dataclass
class Teacher:
    """Source: R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R46"""
    name: _t.Optional[str] = None
    class_: _t.Optional[str] = None
    mentor: _t.Optional[str] = None
    timetable: _t.Optional[str] = None

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R6, R7, R18, R19, R27, R28)."""
        raise NotImplementedError

    def assignSchedule(self) -> None:
        """Realizes UC8 "Assign Schedule" (R49)."""
        raise NotImplementedError

    def createDlm(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addPage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def assignDueDate(self) -> None:
        """Operation."""
        raise NotImplementedError

    def autoGrade(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editPage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def makeSubmissionElements(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addAnswer(self) -> None:
        """Operation."""
        raise NotImplementedError

    def receiveConfirmation(self) -> None:
        """Realizes UC11 "Receive Confirmation" (R32)."""
        raise NotImplementedError

    def recordBehavior(self) -> None:
        """Realizes UC12 "Record Behavior" (R36)."""
        raise NotImplementedError

    def recordGrade(self) -> None:
        """Realizes UC13 "Record Grade" (R37)."""
        raise NotImplementedError

    def recordAttendance(self) -> None:
        """Realizes UC14 "Record Attendance" (R38)."""
        raise NotImplementedError

    def seeAnswer(self) -> None:
        """Realizes UC15 "See Answer" (R39)."""
        raise NotImplementedError

    def seeProgress(self) -> None:
        """Realizes UC17 "See Progress" (R41)."""
        raise NotImplementedError

    def setAppearanceDate(self) -> None:
        """Realizes UC18 "Set Appearance Date" (R42)."""
        raise NotImplementedError

    def setAvailableDates(self) -> None:
        """Operation."""
        raise NotImplementedError

    def uploadFiles(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewAttendance(self) -> None:
        """Realizes UC20 "View Attendance" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Administrator:
    """Source: R48, R49, R50, R51, R52, R53, R54, R55, R56"""
    name: _t.Optional[str] = None
    schedule: _t.Optional[str] = None
    messages: _t.List["Message"] = _dc.field(default_factory=list)
    account: _t.Optional["Account"] = None
    game: _t.Optional["Game"] = None

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R6, R7, R18, R19, R27, R28)."""
        raise NotImplementedError

    def assignSchedule(self) -> None:
        """Realizes UC8 "Assign Schedule" (R49)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC6 "Create Account" (R50)."""
        raise NotImplementedError

    def editAccount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def useFilters(self) -> None:
        """Operation."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R3, R11, R12)."""
        raise NotImplementedError

    def registerAbsence(self) -> None:
        """Realizes UC9 "Register Absence" (R56)."""
        raise NotImplementedError

    def registerChange(self) -> None:
        """Realizes UC10 "Register Change" (R55)."""
        raise NotImplementedError

    def setRole(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Guardian:
    """Source: R1, R3, R12, R13, R14, R15, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R46"""
    name: _t.Optional[str] = None
    child: _t.Optional[str] = None
    mentor: _t.Optional[str] = None
    timetable: _t.Optional[str] = None

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R6, R7, R18, R19, R27, R28)."""
        raise NotImplementedError

    def fillAbsence(self) -> None:
        """Realizes UC2 "Fill Absence" (R2)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R3, R11, R12)."""
        raise NotImplementedError

    def viewInformation(self) -> None:
        """Realizes UC4 "View Information" (R4, R15, R45)."""
        raise NotImplementedError

    def viewClass(self) -> None:
        """Realizes UC21 "View Class" (R46)."""
        raise NotImplementedError

    def viewContactInformation(self) -> None:
        """Realizes UC22 "View Contact Information" (R16)."""
        raise NotImplementedError

    def receiveConfirmation(self) -> None:
        """Realizes UC11 "Receive Confirmation" (R32)."""
        raise NotImplementedError

    def recordBehavior(self) -> None:
        """Realizes UC12 "Record Behavior" (R36)."""
        raise NotImplementedError

    def recordGrade(self) -> None:
        """Realizes UC13 "Record Grade" (R37)."""
        raise NotImplementedError

    def recordAttendance(self) -> None:
        """Realizes UC14 "Record Attendance" (R38)."""
        raise NotImplementedError

    def seeAnswer(self) -> None:
        """Realizes UC15 "See Answer" (R39)."""
        raise NotImplementedError

    def seeProgress(self) -> None:
        """Realizes UC17 "See Progress" (R41)."""
        raise NotImplementedError

    def setAppearanceDate(self) -> None:
        """Realizes UC18 "Set Appearance Date" (R42)."""
        raise NotImplementedError

    def setAvailableDates(self) -> None:
        """Operation."""
        raise NotImplementedError

    def uploadFiles(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewAttendance(self) -> None:
        """Realizes UC20 "View Attendance" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Message:
    """Source: R1, R6, R7, R18, R27, R28, R33, R34, R48"""
    sender: _t.Optional[str] = None
    receiver: _t.Optional[str] = None
    content: _t.Optional[str] = None

    def send(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R6, R7, R18, R19, R27, R28)."""
        raise NotImplementedError

    def receive(self) -> None:
        """Realizes UC3 "Receive Notification" (R3, R11, R12)."""
        raise NotImplementedError

    def sendBroadcastMessage(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Notification:
    """Source: R3, R12, R13, R14, R18, R19, R27, R28, R33, R34, R48, R49, R50, R51, R52, R53, R54, R55, R56"""
    sender: _t.Optional[str] = None
    receiver: _t.Optional[str] = None
    content: _t.Optional[str] = None

    def send(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Absence:
    """Source: R2, R12, R13, R14, R18, R19, R27, R28, R33, R34, R48, R49, R50, R51, R52, R53, R54, R55, R56"""
    student: _t.Optional[str] = None
    date: _t.Optional[str] = None

    def register(self) -> None:
        """Realizes UC9 "Register Absence" (R56)."""
        raise NotImplementedError


@_dc.dataclass
class Dlm:
    """Source: R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R46"""
    title: _t.Optional[str] = None
    pages: _t.Optional[str] = None
    dueDate: _t.Optional[str] = None
    appearanceDate: _t.Optional[str] = None
    submissionElements: _t.Optional[str] = None
    answers: _t.Optional[str] = None
    grade: _t.Optional[str] = None
    attendance: _t.Optional[str] = None

    def addPage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def assignDueDate(self) -> None:
        """Operation."""
        raise NotImplementedError

    def autoGrade(self) -> None:
        """Operation."""
        raise NotImplementedError

    def editPage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def makeSubmissionElements(self) -> None:
        """Operation."""
        raise NotImplementedError

    def addAnswer(self) -> None:
        """Operation."""
        raise NotImplementedError

    def receiveConfirmation(self) -> None:
        """Realizes UC11 "Receive Confirmation" (R32)."""
        raise NotImplementedError

    def recordBehavior(self) -> None:
        """Realizes UC12 "Record Behavior" (R36)."""
        raise NotImplementedError

    def recordGrade(self) -> None:
        """Realizes UC13 "Record Grade" (R37)."""
        raise NotImplementedError

    def recordAttendance(self) -> None:
        """Realizes UC14 "Record Attendance" (R38)."""
        raise NotImplementedError

    def seeAnswer(self) -> None:
        """Realizes UC15 "See Answer" (R39)."""
        raise NotImplementedError

    def seeProgress(self) -> None:
        """Realizes UC17 "See Progress" (R41)."""
        raise NotImplementedError

    def setAppearanceDate(self) -> None:
        """Realizes UC18 "Set Appearance Date" (R42)."""
        raise NotImplementedError

    def setAvailableDates(self) -> None:
        """Operation."""
        raise NotImplementedError

    def uploadFiles(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewAttendance(self) -> None:
        """Realizes UC20 "View Attendance" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class File:
    """Source: R5, R10, R13, R14, R18, R19, R27, R28, R33, R34, R48, R49, R50, R51, R52, R53, R54, R55, R56"""
    title: _t.Optional[str] = None
    content: _t.Optional[str] = None

    def upload(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Account:
    """Source: R47, R50, R51, R52, R53, R54, R55, R56"""
    username: _t.Optional[str] = None
    password: _t.Optional[str] = None
    data: _t.Optional[str] = None
    role: _t.Optional[str] = None

    def resetPassword(self) -> None:
        """Realizes UC23 "Reset Password" (R47)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC6 "Create Account" (R50)."""
        raise NotImplementedError

    def editAccount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def useFilters(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewStatistics(self) -> None:
        """Operation."""
        raise NotImplementedError
