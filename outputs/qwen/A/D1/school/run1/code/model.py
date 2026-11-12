"""Code skeleton generated from the shared model of D1/school.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Guardian:
    """Source: R1, R3, R4"""

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1)."""
        raise NotImplementedError

    def fillAbsence(self) -> None:
        """Realizes UC2 "Fill Absence" (R2)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R18, R19, R3, R34, R53)."""
        raise NotImplementedError


@_dc.dataclass
class Student:
    """Source: R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17"""

    def directMessage(self) -> None:
        """Realizes UC6 "Direct Message Student" (R6, R7)."""
        raise NotImplementedError

    def directMessageMentor(self) -> None:
        """Realizes UC24 "Direct Message Mentor" (R28)."""
        raise NotImplementedError

    def handHomework(self) -> None:
        """Realizes UC7 "Hand Homework" (R8)."""
        raise NotImplementedError

    def viewTimetable(self) -> None:
        """Realizes UC8 "View Timetable" (R9)."""
        raise NotImplementedError

    def viewDLM(self) -> None:
        """Realizes UC9 "Access DLM" (R10)."""
        raise NotImplementedError

    def receiveNotificationDueDate(self) -> None:
        """Realizes UC10 "Receive Notification For Due Date" (R11)."""
        raise NotImplementedError

    def receiveNotificationNewFiles(self) -> None:
        """Realizes UC11 "Receive Notification For New Files" (R13)."""
        raise NotImplementedError

    def receiveNotificationTimetableChanges(self) -> None:
        """Realizes UC12 "Receive Notification For Timetable Changes" (R14)."""
        raise NotImplementedError

    def viewAccountInfo(self) -> None:
        """Realizes UC13 "View Account Information" (R15)."""
        raise NotImplementedError

    def viewContactInfo(self) -> None:
        """Realizes UC14 "View Contact Information" (R16)."""
        raise NotImplementedError

    def changePreferences(self) -> None:
        """Realizes UC15 "Change Preferences" (R17)."""
        raise NotImplementedError


@_dc.dataclass
class Teacher:
    """Source: R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46"""

    def directMessageStudent(self) -> None:
        """Realizes UC6 "Direct Message Student" (R6, R7)."""
        raise NotImplementedError

    def directMessageClass(self) -> None:
        """Realizes UC23 "Direct Message Class" (R27)."""
        raise NotImplementedError

    def directMessageMentor(self) -> None:
        """Realizes UC24 "Direct Message Mentor" (R28)."""
        raise NotImplementedError

    def editDLM(self) -> None:
        """Realizes UC25 "Edit DLM" (R29)."""
        raise NotImplementedError

    def assignSubmissionElements(self) -> None:
        """Realizes UC26 "Assign Submission Elements" (R30)."""
        raise NotImplementedError

    def addAnswerToQuestion(self) -> None:
        """Realizes UC27 "Add Answer To Question" (R31)."""
        raise NotImplementedError

    def confirmFileUpload(self) -> None:
        """Realizes UC28 "Confirm File Upload" (R32)."""
        raise NotImplementedError

    def recordDisciplinaryActions(self) -> None:
        """Realizes UC29 "Record Disciplinary Actions" (R35)."""
        raise NotImplementedError

    def recordBehavior(self) -> None:
        """Realizes UC30 "Record Behavior" (R36)."""
        raise NotImplementedError

    def recordGrades(self) -> None:
        """Realizes UC31 "Record Grades" (R37)."""
        raise NotImplementedError

    def recordAttendance(self) -> None:
        """Realizes UC32 "Record Attendance" (R38)."""
        raise NotImplementedError

    def viewSubmissions(self) -> None:
        """Realizes UC33 "View Submissions" (R39)."""
        raise NotImplementedError

    def viewClassPerformance(self) -> None:
        """Realizes UC34 "View Class Performance" (R40)."""
        raise NotImplementedError

    def viewStudentProgress(self) -> None:
        """Realizes UC35 "View Student Progress" (R41)."""
        raise NotImplementedError

    def setAppearanceDate(self) -> None:
        """Realizes UC36 "Set Appearance Date" (R42)."""
        raise NotImplementedError

    def setAvailableDates(self) -> None:
        """Realizes UC37 "Set Available Dates" (R43)."""
        raise NotImplementedError

    def uploadFiles(self) -> None:
        """Realizes UC38 "Upload Files" (R44)."""
        raise NotImplementedError

    def viewClassInfo(self) -> None:
        """Realizes UC39 "View Class Information" (R45)."""
        raise NotImplementedError

    def viewClassList(self) -> None:
        """Realizes UC40 "View Class List" (R46)."""
        raise NotImplementedError


@_dc.dataclass
class Administrator:
    """Source: R48, R49, R50, R51, R52, R53, R54, R55, R56"""
    accounts: _t.List["Account"] = _dc.field(default_factory=list)
    schedule: _t.Optional["Schedule"] = None
    statistic: _t.Optional["Statistic"] = None
    teachers: _t.List["Teacher"] = _dc.field(default_factory=list)
    students: _t.List["Student"] = _dc.field(default_factory=list)
    guardians: _t.List["Guardian"] = _dc.field(default_factory=list)

    def sendDirectMessage(self) -> None:
        """Realizes UC42 "Send Direct Message" (R48)."""
        raise NotImplementedError

    def assignSchedules(self) -> None:
        """Realizes UC43 "Assign Schedules" (R49)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC44 "Create Account" (R50)."""
        raise NotImplementedError

    def editAccount(self) -> None:
        """Realizes UC45 "Edit Account" (R51)."""
        raise NotImplementedError

    def changeView(self) -> None:
        """Realizes UC46 "Change View" (R52)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R18, R19, R3, R34, R53)."""
        raise NotImplementedError

    def receiveAbsenceForm(self) -> None:
        """Realizes UC47 "Receive Absence Form" (R54)."""
        raise NotImplementedError

    def registerChanges(self) -> None:
        """Realizes UC48 "Register Changes" (R55)."""
        raise NotImplementedError

    def registerAbsence(self) -> None:
        """Realizes UC49 "Register Absence" (R56)."""
        raise NotImplementedError

    def sendBroadcastMessage(self) -> None:
        """Realizes UC50 "Send Broadcast Message" (R57)."""
        raise NotImplementedError

    def setAccountRole(self) -> None:
        """Realizes UC51 "Set Account Role" (R58)."""
        raise NotImplementedError

    def uploadSchedules(self) -> None:
        """Realizes UC52 "Upload Schedules" (R59)."""
        raise NotImplementedError

    def viewAccountDetails(self) -> None:
        """Realizes UC53 "View Account Details" (R60)."""
        raise NotImplementedError

    def viewStatistics(self) -> None:
        """Realizes UC54 "View Statistics" (R61)."""
        raise NotImplementedError


@_dc.dataclass
class Game:
    """Source: R1"""
    name: _t.Optional[str] = None

    def createGame(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Account:
    """Source: R58, R60"""
    role: _t.Optional[str] = None


@_dc.dataclass
class Schedule:
    """Source: R59"""
    teachers: _t.List["Teacher"] = _dc.field(default_factory=list)
    students: _t.List["Student"] = _dc.field(default_factory=list)


@_dc.dataclass
class Statistic:
    """Source: R61"""
    pass
