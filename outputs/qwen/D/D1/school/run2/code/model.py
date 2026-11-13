"""Code skeleton generated from the shared model of D1/school.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Guardian:
    """Source: R1, R2, R3, R4"""
    students: _t.List["Student"] = _dc.field(default_factory=list)

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28, R34, R6, R7)."""
        raise NotImplementedError

    def fillInAbsence(self) -> None:
        """Realizes UC2 "Fill In Absence" (R2)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R11, R12, R13, R17, R3, R53, R54, R55)."""
        raise NotImplementedError

    def viewInformation(self) -> None:
        """Realizes UC4 "View Information" (R4, R15, R16)."""
        raise NotImplementedError


@_dc.dataclass
class Student:
    """Source: R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17"""
    teachers: _t.List["Teacher"] = _dc.field(default_factory=list)

    def accessFilesAndDLM(self) -> None:
        """Realizes UC5 "Access Files And DLM" (R5, R10, R16)."""
        raise NotImplementedError

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28, R34, R6, R7)."""
        raise NotImplementedError

    def directMessageMentor(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28, R34, R6, R7)."""
        raise NotImplementedError

    def handHomework(self) -> None:
        """Realizes UC6 "Hand Homework" (R8)."""
        raise NotImplementedError

    def viewTimetable(self) -> None:
        """Realizes UC7 "View Timetable" (R9, R46)."""
        raise NotImplementedError

    def viewAccountInformation(self) -> None:
        """Realizes UC8 "View Account Information" (R15, R17, R46)."""
        raise NotImplementedError

    def changePreferences(self) -> None:
        """Realizes UC9 "Change Preferences" (R17)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R11, R12, R13, R17, R3, R53, R54, R55)."""
        raise NotImplementedError

    def receiveNotificationFiles(self) -> None:
        """Realizes UC3 "Receive Notification" (R11, R12, R13, R17, R3, R53, R54, R55)."""
        raise NotImplementedError

    def receiveNotificationTimetable(self) -> None:
        """Realizes UC3 "Receive Notification" (R11, R12, R13, R17, R3, R53, R54, R55)."""
        raise NotImplementedError

    def viewStudentData(self) -> None:
        """Realizes UC19 "View Student Data" (R45, R46)."""
        raise NotImplementedError


@_dc.dataclass
class Teacher:
    """Source: R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46"""
    students: _t.List["Student"] = _dc.field(default_factory=list)

    def viewDLM(self) -> None:
        """Realizes UC10 "View DLM" (R20, R21, R22)."""
        raise NotImplementedError

    def assignDLM(self) -> None:
        """Realizes UC11 "Assign DLM" (R23, R24, R44)."""
        raise NotImplementedError

    def gradeDLM(self) -> None:
        """Realizes UC12 "Grade DLM" (R25, R46)."""
        raise NotImplementedError

    def createDLM(self) -> None:
        """Realizes UC13 "Create DLM" (R26, R46)."""
        raise NotImplementedError

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1, R27, R28, R34, R6, R7)."""
        raise NotImplementedError

    def editDLM(self) -> None:
        """Realizes UC14 "Edit DLM" (R29, R46)."""
        raise NotImplementedError

    def viewStudentInformation(self) -> None:
        """Realizes UC15 "View Student Information" (R35, R36, R37)."""
        raise NotImplementedError

    def viewClass(self) -> None:
        """Realizes UC16 "View Class" (R45, R46)."""
        raise NotImplementedError

    def setDLMDate(self) -> None:
        """Realizes UC17 "Set DLM Date" (R42, R43, R46)."""
        raise NotImplementedError

    def uploadFiles(self) -> None:
        """Realizes UC18 "Upload Files" (R44, R46)."""
        raise NotImplementedError

    def viewStudentData(self) -> None:
        """Realizes UC19 "View Student Data" (R45, R46)."""
        raise NotImplementedError

    def viewStudentProgress(self) -> None:
        """Realizes UC19 "View Student Data" (R45, R46)."""
        raise NotImplementedError

    def viewClassAttendance(self) -> None:
        """Realizes UC16 "View Class" (R45, R46)."""
        raise NotImplementedError


@_dc.dataclass
class Administrator:
    """Source: R47, R48, R49, R50, R51, R52, R53, R54, R55, R56"""

    def sendDirectMessage(self) -> None:
        """Realizes UC20 "Send Direct Message" (R48, R54)."""
        raise NotImplementedError

    def assignSchedule(self) -> None:
        """Realizes UC21 "Assign Schedule" (R49, R55)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC22 "Create Account" (R50)."""
        raise NotImplementedError

    def editAccount(self) -> None:
        """Realizes UC23 "Edit Account" (R51)."""
        raise NotImplementedError

    def viewDashboard(self) -> None:
        """Realizes UC24 "View Dashboard" (R52)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R11, R12, R13, R17, R3, R53, R54, R55)."""
        raise NotImplementedError

    def registerAbsence(self) -> None:
        """Realizes UC25 "Register Absence" (R55, R56)."""
        raise NotImplementedError


@_dc.dataclass
class Account:
    """Source: R58, R60, R61"""
    role: _t.Optional[str] = None
    details: _t.Optional[str] = None

    def setRole(self) -> None:
        """Realizes UC27 "Set Role Of An Account" (R58)."""
        raise NotImplementedError

    def viewDetails(self) -> None:
        """Realizes UC29 "View Account Details" (R60)."""
        raise NotImplementedError

    def viewStatistics(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Schedule:
    """Source: R59"""
    date: _t.Optional[str] = None
    time: _t.Optional[str] = None

    def uploadSchedule(self) -> None:
        """Realizes UC28 "Upload Schedules" (R59)."""
        raise NotImplementedError


@_dc.dataclass
class Statistic:
    """Source: R61"""
    grade: _t.Optional[str] = None
    attendance: _t.Optional[str] = None
    disciplinaryAction: _t.Optional[str] = None
