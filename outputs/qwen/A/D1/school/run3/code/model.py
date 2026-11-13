"""Code skeleton generated from the shared model of D1/school.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Guardian:
    """Source: R1, R2, R3, R4"""
    teacher: _t.Optional["Teacher"] = None
    administrator: _t.Optional["Administrator"] = None

    def directMessage(self) -> None:
        """Realizes UC1 "Direct Message" (R1)."""
        raise NotImplementedError

    def fillAbsence(self) -> None:
        """Realizes UC2 "Fill Absence" (R2)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC3 "Receive Notification" (R3)."""
        raise NotImplementedError

    def viewInformation(self) -> None:
        """Realizes UC4 "View Information" (R4)."""
        raise NotImplementedError


@_dc.dataclass
class Student:
    """Source: R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17"""
    teacher: _t.Optional["Teacher"] = None
    guardian: _t.Optional["Guardian"] = None

    def accessFilesAndDLM(self) -> None:
        """Realizes UC5 "Access Files And DLM" (R5)."""
        raise NotImplementedError

    def directMessageTeachers(self) -> None:
        """Realizes UC6 "Direct Message Teachers" (R6)."""
        raise NotImplementedError

    def directMessageMentor(self) -> None:
        """Realizes UC7 "Direct Message Mentor" (R7)."""
        raise NotImplementedError

    def handHomework(self) -> None:
        """Realizes UC8 "Hand Homework" (R8)."""
        raise NotImplementedError

    def viewTimetable(self) -> None:
        """Realizes UC9 "View Timetable" (R9)."""
        raise NotImplementedError

    def viewAccountInformation(self) -> None:
        """Realizes UC14 "View Account Information" (R15)."""
        raise NotImplementedError

    def viewContactInformation(self) -> None:
        """Realizes UC15 "View Contact Information" (R16)."""
        raise NotImplementedError

    def changePreferences(self) -> None:
        """Realizes UC16 "Change Preferences" (R17)."""
        raise NotImplementedError

    def receiveNotificationForDueDate(self) -> None:
        """Realizes UC11 "Receive Notification For Due Date" (R11)."""
        raise NotImplementedError

    def receiveNotificationForNewFiles(self) -> None:
        """Realizes UC12 "Receive Notification For New Files" (R13)."""
        raise NotImplementedError

    def receiveNotificationForTimetableChanges(self) -> None:
        """Realizes UC13 "Receive Notification For Timetable Changes" (R14)."""
        raise NotImplementedError


@_dc.dataclass
class Teacher:
    """Source: R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46"""
    students: _t.List["Student"] = _dc.field(default_factory=list)

    def addVideoToDLM(self) -> None:
        """Realizes UC18 "Add Video To DLM" (R20)."""
        raise NotImplementedError

    def addTextAndPicturesToDLM(self) -> None:
        """Realizes UC19 "Add Text And Pictures To DLM" (R21)."""
        raise NotImplementedError

    def addQuestionToDLM(self) -> None:
        """Realizes UC20 "Add Question To DLM" (R22)."""
        raise NotImplementedError

    def assignDLM(self) -> None:
        """Realizes UC21 "Assign DLM" (R23)."""
        raise NotImplementedError

    def assignDueDate(self) -> None:
        """Realizes UC22 "Assign Due Date" (R24)."""
        raise NotImplementedError

    def automaticallyGradeDLM(self) -> None:
        """Realizes UC23 "Automatically Grade DLM" (R25)."""
        raise NotImplementedError

    def createDLM(self) -> None:
        """Realizes UC24 "Create DLM" (R26)."""
        raise NotImplementedError

    def directMessageStudents(self) -> None:
        """Realizes UC25 "Direct Message Students" (R27)."""
        raise NotImplementedError

    def editDLMPage(self) -> None:
        """Realizes UC26 "Edit DLM Page" (R29)."""
        raise NotImplementedError

    def addSubmissionElements(self) -> None:
        """Realizes UC27 "Add Submission Elements" (R30)."""
        raise NotImplementedError

    def addAnswerToQuestion(self) -> None:
        """Realizes UC28 "Add Answer To Question" (R31)."""
        raise NotImplementedError

    def confirmFileUpload(self) -> None:
        """Realizes UC29 "Confirm File Upload" (R32)."""
        raise NotImplementedError

    def recordDisciplinaryActions(self) -> None:
        """Realizes UC30 "Record Disciplinary Actions" (R35)."""
        raise NotImplementedError

    def recordStudentBehavior(self) -> None:
        """Realizes UC31 "Record Student Behavior" (R36)."""
        raise NotImplementedError

    def recordGrades(self) -> None:
        """Realizes UC32 "Record Grades" (R37)."""
        raise NotImplementedError

    def recordAttendance(self) -> None:
        """Realizes UC33 "Record Attendance" (R38)."""
        raise NotImplementedError

    def viewStudentSubmissions(self) -> None:
        """Realizes UC34 "View Student Submissions" (R39)."""
        raise NotImplementedError

    def viewClassPerformance(self) -> None:
        """Realizes UC35 "View Class Performance" (R40)."""
        raise NotImplementedError

    def viewStudentProgress(self) -> None:
        """Realizes UC36 "View Student Progress" (R41)."""
        raise NotImplementedError

    def setAppearanceDate(self) -> None:
        """Realizes UC37 "Set Appearance Date" (R42)."""
        raise NotImplementedError

    def setAvailableDates(self) -> None:
        """Realizes UC38 "Set Available Dates" (R43)."""
        raise NotImplementedError

    def uploadFiles(self) -> None:
        """Realizes UC39 "Upload Files" (R44)."""
        raise NotImplementedError

    def viewClassInformation(self) -> None:
        """Realizes UC40 "View Class Information" (R45)."""
        raise NotImplementedError

    def viewClassAttendance(self) -> None:
        """Realizes UC41 "View Class Attendance" (R46)."""
        raise NotImplementedError


@_dc.dataclass
class Administrator:
    """Source: R48, R49, R50, R51, R52, R53, R54, R55, R56"""
    students: _t.List["Student"] = _dc.field(default_factory=list)
    teachers: _t.List["Teacher"] = _dc.field(default_factory=list)
    guardians: _t.List["Guardian"] = _dc.field(default_factory=list)
    account: _t.Optional["Account"] = None

    def sendDirectMessage(self) -> None:
        """Realizes UC43 "Send Direct Message" (R48)."""
        raise NotImplementedError

    def assignSchedules(self) -> None:
        """Realizes UC44 "Assign Schedules" (R49)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC45 "Create Account" (R50)."""
        raise NotImplementedError

    def editAccountData(self) -> None:
        """Realizes UC46 "Edit Account Data" (R51)."""
        raise NotImplementedError

    def changeView(self) -> None:
        """Realizes UC47 "Change View" (R52)."""
        raise NotImplementedError

    def receiveNotificationForMessages(self) -> None:
        """Realizes UC17 "Receive Notification For Messages" (R18, R28, R34, R53)."""
        raise NotImplementedError

    def receiveNotificationForAbsenceForms(self) -> None:
        """Realizes UC48 "Receive Notification For Absence Forms" (R54)."""
        raise NotImplementedError

    def registerScheduleChanges(self) -> None:
        """Realizes UC49 "Register Schedule Changes" (R55)."""
        raise NotImplementedError

    def registerAbsence(self) -> None:
        """Realizes UC50 "Register Absence" (R56)."""
        raise NotImplementedError

    def sendBroadcastMessage(self) -> None:
        """Realizes UC51 "Send Broadcast Message" (R57)."""
        raise NotImplementedError

    def setAccountRole(self) -> None:
        """Realizes UC52 "Set Account Role" (R58)."""
        raise NotImplementedError

    def uploadSchedules(self) -> None:
        """Realizes UC53 "Upload Schedules" (R59)."""
        raise NotImplementedError

    def viewAccountDetails(self) -> None:
        """Realizes UC54 "View Account Details" (R60)."""
        raise NotImplementedError

    def viewStatistics(self) -> None:
        """Realizes UC55 "View Statistics" (R61)."""
        raise NotImplementedError


@_dc.dataclass
class Account:
    """Source: R58, R60"""
    role: _t.Optional[str] = None
