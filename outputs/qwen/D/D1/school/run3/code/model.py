"""Code skeleton generated from the shared model of D1/school.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Guardian:
    """Source: R1, R2, R3, R4"""
    child: _t.Optional[str] = None
    mentor: _t.Optional[str] = None
    teachers: _t.List["Teacher"] = _dc.field(default_factory=list)
    administrators: _t.List["Administrator"] = _dc.field(default_factory=list)

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28, R6, R7)."""
        raise NotImplementedError

    def fillInAbsence(self) -> None:
        """Realizes UC2 "Fill In Absence" (R2)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R11, R12, R13, R18, R19, R3, R34, R43, R53, R54)."""
        raise NotImplementedError

    def viewInformation(self) -> None:
        """Realizes UC4 "View Information" (R4, R15)."""
        raise NotImplementedError


@_dc.dataclass
class Student:
    """Source: R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17"""
    teacher: _t.Optional[str] = None
    mentor: _t.Optional[str] = None
    class_: _t.Optional[str] = None
    dueDate: _t.Optional[str] = None
    teachers: _t.List["Teacher"] = _dc.field(default_factory=list)
    notifications: _t.List["Notification"] = _dc.field(default_factory=list)
    timetable: _t.Optional["Timetable"] = None
    dLM: _t.Optional["DLM"] = None

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28, R6, R7)."""
        raise NotImplementedError

    def handHomework(self) -> None:
        """Realizes UC6 "Hand Homework" (R8)."""
        raise NotImplementedError

    def viewTimetable(self) -> None:
        """Realizes UC7 "View Timetable" (R9)."""
        raise NotImplementedError

    def viewDLM(self) -> None:
        """Operation."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R11, R12, R13, R18, R19, R3, R34, R43, R53, R54)."""
        raise NotImplementedError

    def viewAccountInformation(self) -> None:
        """Realizes UC8 "View Account Information" (R15)."""
        raise NotImplementedError

    def viewContactInformation(self) -> None:
        """Realizes UC9 "View Contact Information" (R16)."""
        raise NotImplementedError

    def changePreferences(self) -> None:
        """Realizes UC10 "Change Preferences" (R17)."""
        raise NotImplementedError


@_dc.dataclass
class Teacher:
    """Source: R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46"""
    class_: _t.Optional[str] = None
    mentor: _t.Optional[str] = None
    students: _t.List["Student"] = _dc.field(default_factory=list)
    notifications: _t.List["Notification"] = _dc.field(default_factory=list)
    timetable: _t.Optional["Timetable"] = None
    dLM: _t.Optional["DLM"] = None

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28, R6, R7)."""
        raise NotImplementedError

    def addPageToDLM(self) -> None:
        """Realizes UC11 "Add Page To DLM" (R20, R21, R22)."""
        raise NotImplementedError

    def assignDLM(self) -> None:
        """Realizes UC12 "Assign DLM" (R23)."""
        raise NotImplementedError

    def assignDueDate(self) -> None:
        """Realizes UC13 "Assign Due Date" (R24)."""
        raise NotImplementedError

    def automaticallyGradeDLM(self) -> None:
        """Realizes UC14 "Automatically Grade DLM" (R25)."""
        raise NotImplementedError

    def createDLM(self) -> None:
        """Realizes UC15 "Create DLM" (R26)."""
        raise NotImplementedError

    def editDLMPage(self) -> None:
        """Realizes UC16 "Edit DLM Page" (R29)."""
        raise NotImplementedError

    def makeSubmissionElements(self) -> None:
        """Realizes UC17 "Make Submission Elements" (R30)."""
        raise NotImplementedError

    def addAnswerToDLM(self) -> None:
        """Realizes UC18 "Add Answer To DLM" (R31)."""
        raise NotImplementedError

    def confirmFileUpload(self) -> None:
        """Realizes UC19 "Confirm File Upload" (R32)."""
        raise NotImplementedError

    def recordDisciplinaryActions(self) -> None:
        """Realizes UC20 "Record Disciplinary Actions" (R35)."""
        raise NotImplementedError

    def recordBehavior(self) -> None:
        """Realizes UC21 "Record Behavior" (R36)."""
        raise NotImplementedError

    def recordGrades(self) -> None:
        """Realizes UC22 "Record Grades" (R37)."""
        raise NotImplementedError

    def recordAttendance(self) -> None:
        """Realizes UC23 "Record Attendance" (R38)."""
        raise NotImplementedError

    def viewSubmissions(self) -> None:
        """Realizes UC24 "View Submissions" (R39)."""
        raise NotImplementedError

    def viewClassPerformance(self) -> None:
        """Realizes UC25 "View Class Performance" (R40, R41)."""
        raise NotImplementedError

    def setDLMAppearanceDate(self) -> None:
        """Realizes UC26 "Set DLM Appearance Date" (R42)."""
        raise NotImplementedError

    def setDLMAvailability(self) -> None:
        """Realizes UC27 "Set DLM Availability" (R43)."""
        raise NotImplementedError

    def uploadFiles(self) -> None:
        """Realizes UC28 "Upload Files" (R44)."""
        raise NotImplementedError

    def viewStudentData(self) -> None:
        """Realizes UC29 "View Student Data" (R45)."""
        raise NotImplementedError

    def viewClassAttendance(self) -> None:
        """Realizes UC30 "View Class Attendance" (R46)."""
        raise NotImplementedError


@_dc.dataclass
class Administrator:
    """Source: R47, R48, R49, R50, R51, R52, R53, R54, R55, R56"""
    user: _t.Optional[str] = None
    schedule: _t.Optional["Schedule"] = None
    notifications: _t.List["Notification"] = _dc.field(default_factory=list)
    broadcastMessages: _t.List["BroadcastMessage"] = _dc.field(default_factory=list)

    def sendDirectMessage(self) -> None:
        """Realizes UC32 "Send Direct Message" (R48)."""
        raise NotImplementedError

    def assignSchedules(self) -> None:
        """Realizes UC33 "Assign Schedules" (R49)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC34 "Create Account" (R50)."""
        raise NotImplementedError

    def editAccount(self) -> None:
        """Realizes UC35 "Edit Account" (R51)."""
        raise NotImplementedError

    def viewPerformanceData(self) -> None:
        """Realizes UC36 "View Performance Data" (R52)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R11, R12, R13, R18, R19, R3, R34, R43, R53, R54)."""
        raise NotImplementedError

    def registerChanges(self) -> None:
        """Realizes UC37 "Register Changes" (R55)."""
        raise NotImplementedError

    def registerAbsence(self) -> None:
        """Realizes UC38 "Register Absence" (R56)."""
        raise NotImplementedError


@_dc.dataclass
class DLM:
    """Source: R20, R21, R22, R23, R24, R25, R26, R30, R31, R42, R43"""
    pages: _t.Optional[str] = None
    dueDate: _t.Optional[str] = None
    submissionElements: _t.Optional[str] = None
    answers: _t.Optional[str] = None

    def addPage(self) -> None:
        """Realizes UC11 "Add Page To DLM" (R20, R21, R22)."""
        raise NotImplementedError

    def assignDueDate(self) -> None:
        """Realizes UC13 "Assign Due Date" (R24)."""
        raise NotImplementedError

    def automaticallyGrade(self) -> None:
        """Realizes UC14 "Automatically Grade DLM" (R25)."""
        raise NotImplementedError

    def create(self) -> None:
        """Realizes UC15 "Create DLM" (R26)."""
        raise NotImplementedError

    def editPage(self) -> None:
        """Realizes UC16 "Edit DLM Page" (R29)."""
        raise NotImplementedError

    def makeSubmissionElements(self) -> None:
        """Realizes UC17 "Make Submission Elements" (R30)."""
        raise NotImplementedError

    def addAnswer(self) -> None:
        """Realizes UC18 "Add Answer To DLM" (R31)."""
        raise NotImplementedError


@_dc.dataclass
class File:
    """Source: R10, R13, R33, R44"""
    name: _t.Optional[str] = None
    uploadDate: _t.Optional[str] = None

    def upload(self) -> None:
        """Realizes UC28 "Upload Files" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class Message:
    """Source: R1, R6, R7, R18, R27, R28, R48"""
    sender: _t.Optional[str] = None
    receiver: _t.Optional[str] = None
    content: _t.Optional[str] = None

    def send(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28, R6, R7)."""
        raise NotImplementedError


@_dc.dataclass
class Notification:
    """Source: R3, R12, R19, R34, R39, R40, R41, R46"""
    message: _t.Optional[str] = None

    def receive(self) -> None:
        """Realizes UC3 "Receive Notification" (R11, R12, R13, R18, R19, R3, R34, R43, R53, R54)."""
        raise NotImplementedError


@_dc.dataclass
class Schedule:
    """Source: R49, R55"""
    user: _t.Optional[str] = None
    date: _t.Optional[str] = None
    time: _t.Optional[str] = None

    def assign(self) -> None:
        """Realizes UC33 "Assign Schedules" (R49)."""
        raise NotImplementedError

    def uploadSchedule(self) -> None:
        """Realizes UC41 "Upload Schedules" (R59)."""
        raise NotImplementedError


@_dc.dataclass
class Submission:
    """Source: R8, R39"""
    content: _t.Optional[str] = None
    date: _t.Optional[str] = None

    def submit(self) -> None:
        """Realizes UC6 "Hand Homework" (R8)."""
        raise NotImplementedError


@_dc.dataclass
class Timetable:
    """Source: R9, R14, R46"""
    date: _t.Optional[str] = None
    class_: _t.Optional[str] = None

    def view(self) -> None:
        """Realizes UC7 "View Timetable" (R9)."""
        raise NotImplementedError


@_dc.dataclass
class User:
    """Source: R47, R50, R51"""
    username: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def resetPassword(self) -> None:
        """Realizes UC31 "Reset Password" (R47)."""
        raise NotImplementedError


@_dc.dataclass
class Class:
    """Source: R15, R16, R17, R28, R45, R46"""
    students: _t.Optional[str] = None
    teacher: _t.Optional[str] = None

    def view(self) -> None:
        """Realizes UC30 "View Class Attendance" (R46)."""
        raise NotImplementedError


@_dc.dataclass
class Account:
    """Source: R58, R60, R61"""
    role: _t.Optional[str] = None
    details: _t.Optional[str] = None

    def setRole(self) -> None:
        """Realizes UC40 "Set Role Of An Account" (R58)."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Realizes UC42 "View Account Details" (R60)."""
        raise NotImplementedError

    def viewStatistics(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class BroadcastMessage:
    """Source: R57"""
    message: _t.Optional[str] = None
    recipients: _t.Optional[str] = None

    def sendBroadcastMessage(self) -> None:
        """Realizes UC39 "Send Broadcast Messages" (R57)."""
        raise NotImplementedError
