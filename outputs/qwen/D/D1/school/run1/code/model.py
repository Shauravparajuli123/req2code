"""Code skeleton generated from the shared model of D1/school.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Guardian:
    """Source: R1, R2, R3, R4"""
    teachers: _t.List["Teacher"] = _dc.field(default_factory=list)
    administrators: _t.List["Administrator"] = _dc.field(default_factory=list)
    notification: _t.Optional["Notification"] = None

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28)."""
        raise NotImplementedError

    def fillInAbsence(self) -> None:
        """Realizes UC2 "Fill In Absence" (R2)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R12, R18, R19, R27, R3, R44, R53, R54)."""
        raise NotImplementedError


@_dc.dataclass
class Student:
    """Source: R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17"""
    teachers: _t.List["Teacher"] = _dc.field(default_factory=list)
    dLM: _t.Optional["DLM"] = None
    notification: _t.Optional["Notification"] = None
    account: _t.Optional["Account"] = None
    class_: _t.Optional["Class"] = None
    guardian: _t.Optional["Guardian"] = None

    def accessFilesAndDLM(self) -> None:
        """Realizes UC5 "Access Files And DLM" (R5, R20, R21)."""
        raise NotImplementedError

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28)."""
        raise NotImplementedError

    def handHomework(self) -> None:
        """Realizes UC6 "Hand Homework" (R8)."""
        raise NotImplementedError

    def viewTimetable(self) -> None:
        """Realizes UC7 "View Timetable" (R9, R14)."""
        raise NotImplementedError

    def receiveNotificationForDueDate(self) -> None:
        """Realizes UC8 "Receive Notification For Due Date" (R11)."""
        raise NotImplementedError

    def viewAccountInformation(self) -> None:
        """Realizes UC9 "View Account Information" (R15)."""
        raise NotImplementedError

    def viewContactInformation(self) -> None:
        """Realizes UC10 "View Contact Information" (R16)."""
        raise NotImplementedError

    def changePreferences(self) -> None:
        """Realizes UC11 "Change Preferences" (R17)."""
        raise NotImplementedError


@_dc.dataclass
class Teacher:
    """Source: R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46"""
    students: _t.List["Student"] = _dc.field(default_factory=list)
    dLM: _t.Optional["DLM"] = None
    notification: _t.Optional["Notification"] = None
    class_: _t.Optional["Class"] = None
    submission: _t.Optional["Submission"] = None
    grade: _t.Optional["Grade"] = None
    attendance: _t.Optional["Attendance"] = None
    answer: _t.Optional["Answer"] = None
    schedule: _t.Optional["Schedule"] = None

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28)."""
        raise NotImplementedError

    def addPageToDLM(self) -> None:
        """Realizes UC12 "Add Page To DLM" (R20, R21, R22)."""
        raise NotImplementedError

    def assignDLM(self) -> None:
        """Realizes UC13 "Assign DLM" (R23)."""
        raise NotImplementedError

    def assignDueDate(self) -> None:
        """Realizes UC14 "Assign Due Date" (R24)."""
        raise NotImplementedError

    def automaticallyGradeDLM(self) -> None:
        """Realizes UC15 "Automatically Grade DLM" (R25)."""
        raise NotImplementedError

    def createDLM(self) -> None:
        """Realizes UC16 "Create DLM" (R26)."""
        raise NotImplementedError

    def makeSubmissionElements(self) -> None:
        """Realizes UC18 "Make Submission Elements" (R30)."""
        raise NotImplementedError

    def addAnswerToDLM(self) -> None:
        """Realizes UC19 "Add Answer To DLM" (R31)."""
        raise NotImplementedError

    def confirmFileUpload(self) -> None:
        """Realizes UC20 "Confirm File Upload" (R32)."""
        raise NotImplementedError

    def recordDisciplinaryActions(self) -> None:
        """Realizes UC21 "Record Disciplinary Actions" (R35)."""
        raise NotImplementedError

    def recordBehavior(self) -> None:
        """Realizes UC22 "Record Behavior" (R36)."""
        raise NotImplementedError

    def recordGrades(self) -> None:
        """Realizes UC23 "Record Grades" (R37)."""
        raise NotImplementedError

    def recordAttendance(self) -> None:
        """Realizes UC24 "Record Attendance" (R38)."""
        raise NotImplementedError

    def viewStudentAnswers(self) -> None:
        """Realizes UC25 "View Student Answers" (R39)."""
        raise NotImplementedError

    def viewClassPerformance(self) -> None:
        """Realizes UC26 "View Class Performance" (R40)."""
        raise NotImplementedError

    def viewStudentProgress(self) -> None:
        """Realizes UC27 "View Student Progress" (R41)."""
        raise NotImplementedError

    def setAppearanceDate(self) -> None:
        """Realizes UC28 "Set Appearance Date" (R42)."""
        raise NotImplementedError

    def setAvailableDates(self) -> None:
        """Realizes UC29 "Set Available Dates" (R43)."""
        raise NotImplementedError

    def uploadFiles(self) -> None:
        """Realizes UC30 "Upload Files" (R44)."""
        raise NotImplementedError

    def viewStudentData(self) -> None:
        """Realizes UC31 "View Student Data" (R45, R46)."""
        raise NotImplementedError


@_dc.dataclass
class Administrator:
    """Source: R47, R48, R49, R50, R51, R52, R53, R54, R55, R56"""
    students: _t.List["Student"] = _dc.field(default_factory=list)
    teachers: _t.List["Teacher"] = _dc.field(default_factory=list)
    guardians: _t.List["Guardian"] = _dc.field(default_factory=list)
    notification: _t.Optional["Notification"] = None
    schedule: _t.Optional["Schedule"] = None
    class_: _t.Optional["Class"] = None
    account: _t.Optional["Account"] = None
    dashboard: _t.Optional["Dashboard"] = None
    messages: _t.List["Message"] = _dc.field(default_factory=list)

    def sendDirectMessage(self) -> None:
        """Realizes UC33 "Send Direct Message" (R48)."""
        raise NotImplementedError

    def assignSchedules(self) -> None:
        """Realizes UC34 "Assign Schedules" (R49)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC35 "Create Account" (R50)."""
        raise NotImplementedError

    def editAccountData(self) -> None:
        """Realizes UC36 "Edit Account Data" (R51)."""
        raise NotImplementedError

    def changeDashboardView(self) -> None:
        """Realizes UC37 "Change Dashboard View" (R52)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R12, R18, R19, R27, R3, R44, R53, R54)."""
        raise NotImplementedError

    def registerChanges(self) -> None:
        """Realizes UC38 "Register Changes" (R55)."""
        raise NotImplementedError

    def registerAbsence(self) -> None:
        """Realizes UC39 "Register Absence" (R56)."""
        raise NotImplementedError


@_dc.dataclass
class Message:
    """Source: R1, R6, R7, R18, R27, R28, R48"""

    def send(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28)."""
        raise NotImplementedError


@_dc.dataclass
class Notification:
    """Source: R3, R12, R18, R19, R34, R43, R48"""

    def send(self) -> None:
        """Realizes UC3 "Receive Notification" (R12, R18, R19, R27, R3, R44, R53, R54)."""
        raise NotImplementedError


@_dc.dataclass
class File:
    """Source: R10, R13, R30, R44"""

    def upload(self) -> None:
        """Realizes UC30 "Upload Files" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class DLM:
    """Source: R20, R21, R22, R23, R24, R26, R30, R31, R44"""

    def addPage(self) -> None:
        """Realizes UC12 "Add Page To DLM" (R20, R21, R22)."""
        raise NotImplementedError

    def assign(self) -> None:
        """Realizes UC13 "Assign DLM" (R23)."""
        raise NotImplementedError

    def assignDueDate(self) -> None:
        """Realizes UC14 "Assign Due Date" (R24)."""
        raise NotImplementedError

    def grade(self) -> None:
        """Realizes UC15 "Automatically Grade DLM" (R25)."""
        raise NotImplementedError

    def create(self) -> None:
        """Realizes UC16 "Create DLM" (R26)."""
        raise NotImplementedError

    def makeSubmissionElements(self) -> None:
        """Realizes UC18 "Make Submission Elements" (R30)."""
        raise NotImplementedError

    def addAnswer(self) -> None:
        """Realizes UC19 "Add Answer To DLM" (R31)."""
        raise NotImplementedError

    def confirmUpload(self) -> None:
        """Realizes UC20 "Confirm File Upload" (R32)."""
        raise NotImplementedError


@_dc.dataclass
class Page:
    """Source: R20, R21, R22, R26"""

    def addContent(self) -> None:
        """Realizes UC12 "Add Page To DLM" (R20, R21, R22)."""
        raise NotImplementedError


@_dc.dataclass
class Submission:
    """Source: R8, R30"""

    def handIn(self) -> None:
        """Realizes UC6 "Hand Homework" (R8)."""
        raise NotImplementedError


@_dc.dataclass
class Answer:
    """Source: R22, R31"""

    def add(self) -> None:
        """Realizes UC19 "Add Answer To DLM" (R31)."""
        raise NotImplementedError


@_dc.dataclass
class Schedule:
    """Source: R49, R50, R51, R52, R53, R54, R55, R56"""
    schedule: _t.Optional[str] = None

    def assign(self) -> None:
        """Realizes UC34 "Assign Schedules" (R49)."""
        raise NotImplementedError

    def uploadSchedule(self) -> None:
        """Realizes UC42 "Upload Schedules" (R59)."""
        raise NotImplementedError


@_dc.dataclass
class Account:
    """Source: R50, R51, R52, R53, R54, R55, R56"""
    role: _t.Optional[str] = None
    details: _t.Optional[str] = None
    schedule: _t.Optional["Schedule"] = None
    message: _t.Optional["Message"] = None
    grade: _t.Optional["Grade"] = None
    attendance: _t.Optional["Attendance"] = None
    behavior: _t.Optional["Behavior"] = None

    def edit(self) -> None:
        """Realizes UC36 "Edit Account Data" (R51)."""
        raise NotImplementedError

    def setRole(self) -> None:
        """Realizes UC41 "Set Role Of An Account" (R58)."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Realizes UC43 "View Account Details" (R60)."""
        raise NotImplementedError

    def viewStatistics(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Class:
    """Source: R45, R46, R52, R53, R54, R55, R56"""

    def view(self) -> None:
        """Realizes UC31 "View Student Data" (R45, R46)."""
        raise NotImplementedError


@_dc.dataclass
class Behavior:
    """Source: R35, R36"""

    def record_(self) -> None:
        """Realizes UC22 "Record Behavior" (R36)."""
        raise NotImplementedError


@_dc.dataclass
class Grade:
    """Source: R37, R38, R39, R40, R41, R42, R43, R44, R45, R46, R52, R53, R54, R55, R56"""

    def record_(self) -> None:
        """Realizes UC23 "Record Grades" (R37)."""
        raise NotImplementedError

    def view(self) -> None:
        """Realizes UC26 "View Class Performance" (R40)."""
        raise NotImplementedError

    def viewProgress(self) -> None:
        """Realizes UC27 "View Student Progress" (R41)."""
        raise NotImplementedError


@_dc.dataclass
class Attendance:
    """Source: R38, R39, R40, R41, R42, R43, R44, R45, R46, R52, R53, R54, R55, R56"""

    def record_(self) -> None:
        """Realizes UC24 "Record Attendance" (R38)."""
        raise NotImplementedError


@_dc.dataclass
class Dashboard:
    """Source: R52, R53, R54, R55, R56"""

    def changeView(self) -> None:
        """Realizes UC37 "Change Dashboard View" (R52)."""
        raise NotImplementedError


@_dc.dataclass
class BroadcastMessage:
    """Source: R57"""
    message: _t.Optional[str] = None
    recipients: _t.Optional[str] = None

    def sendBroadcastMessage(self) -> None:
        """Realizes UC40 "Send Broadcast Messages" (R57)."""
        raise NotImplementedError
