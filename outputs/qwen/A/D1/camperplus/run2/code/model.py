"""Code skeleton generated from the shared model of D1/camperplus.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Camper:
    """Source: R1, R2, R36, R37, R46, R47"""
    name: _t.Optional[str] = None
    emergencyContact: _t.Optional[str] = None
    parent: _t.Optional[str] = None
    consentForms: _t.Optional[str] = None
    activitySchedule: _t.Optional[str] = None
    attendance: _t.Optional[bool] = None

    def addCamper(self) -> None:
        """Realizes UC1 "Add Camper" (R1)."""
        raise NotImplementedError

    def removeCamper(self) -> None:
        """Realizes UC2 "Remove Camper" (R2)."""
        raise NotImplementedError

    def modifyCamperInfo(self) -> None:
        """Realizes UC30 "Modify Camper Information" (R30)."""
        raise NotImplementedError

    def deleteCamper(self) -> None:
        """Realizes UC31 "Delete Campers" (R31)."""
        raise NotImplementedError

    def seeCamperActivity(self) -> None:
        """Realizes UC36 "See Camper Activity" (R37)."""
        raise NotImplementedError


@_dc.dataclass
class Parent:
    """Source: R39, R40, R41, R42, R43, R44, R45, R46, R47, R48"""
    name: _t.Optional[str] = None
    children: _t.Optional[str] = None
    consentForms: _t.Optional[str] = None
    payments: _t.Optional[str] = None
    photos: _t.Optional[str] = None
    counselors: _t.Optional[str] = None
    camper: _t.Optional["Camper"] = None

    def createAccount(self) -> None:
        """Realizes UC38 "Create Account" (R39)."""
        raise NotImplementedError

    def submitConsentForms(self) -> None:
        """Realizes UC37 "Submit Forms" (R38)."""
        raise NotImplementedError

    def seeCamperSchedule(self) -> None:
        """Realizes UC47 "See Camper Schedule" (R48)."""
        raise NotImplementedError

    def seeEnrolledCampers(self) -> None:
        """Realizes UC46 "See Enrolled Campers" (R47)."""
        raise NotImplementedError

    def messageCounselors(self) -> None:
        """Realizes UC40 "Message Counselors" (R41)."""
        raise NotImplementedError


@_dc.dataclass
class CampAdministrator:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35"""
    name: _t.Optional[str] = None
    groups: _t.Optional[str] = None
    tasks: _t.Optional[str] = None
    campers: _t.List["Camper"] = _dc.field(default_factory=list)
    parents: _t.List["Parent"] = _dc.field(default_factory=list)

    def addCamper(self) -> None:
        """Realizes UC1 "Add Camper" (R1)."""
        raise NotImplementedError

    def removeCamper(self) -> None:
        """Realizes UC2 "Remove Camper" (R2)."""
        raise NotImplementedError

    def keepCamperRecords(self) -> None:
        """Realizes UC3 "Keep Camper Records" (R3)."""
        raise NotImplementedError

    def uploadConsentForms(self) -> None:
        """Realizes UC4 "Upload Consent Forms" (R4)."""
        raise NotImplementedError

    def trackConsentFormSubmission(self) -> None:
        """Realizes UC5 "Track Consent Form Submission" (R5)."""
        raise NotImplementedError

    def scheduleActivities(self) -> None:
        """Realizes UC6 "Schedule Activities" (R6)."""
        raise NotImplementedError

    def createNametags(self) -> None:
        """Realizes UC7 "Create Nametags" (R7)."""
        raise NotImplementedError

    def suspendCamper(self) -> None:
        """Realizes UC8 "Suspend Camper" (R8)."""
        raise NotImplementedError

    def setReminders(self) -> None:
        """Realizes UC9 "Set Reminders" (R9)."""
        raise NotImplementedError

    def assignStaffPositions(self) -> None:
        """Realizes UC10 "Assign Staff Positions" (R10)."""
        raise NotImplementedError

    def warnStaff(self) -> None:
        """Realizes UC11 "Warn Staff" (R11)."""
        raise NotImplementedError

    def createRules(self) -> None:
        """Realizes UC12 "Create Rules" (R12)."""
        raise NotImplementedError

    def trackFacilityUsage(self) -> None:
        """Realizes UC13 "Track Facility Usage" (R13)."""
        raise NotImplementedError

    def createFeedbackAvenue(self) -> None:
        """Realizes UC14 "Create Feedback Avenue" (R14)."""
        raise NotImplementedError

    def storeEmergencyInformation(self) -> None:
        """Realizes UC15 "Store Emergency Information" (R15)."""
        raise NotImplementedError

    def storeParentInformation(self) -> None:
        """Realizes UC16 "Store Parent Information" (R16)."""
        raise NotImplementedError

    def provideParentFeedback(self) -> None:
        """Realizes UC17 "Provide Parent Feedback" (R17)."""
        raise NotImplementedError

    def makeNametagsFaster(self) -> None:
        """Realizes UC18 "Make Nametags Faster" (R18)."""
        raise NotImplementedError

    def createRegistrationForm(self) -> None:
        """Realizes UC19 "Create Registration Form" (R19)."""
        raise NotImplementedError

    def keepInformationOrganized(self) -> None:
        """Realizes UC20 "Keep Information Organized" (R20)."""
        raise NotImplementedError

    def seeMedicalForms(self) -> None:
        """Realizes UC21 "See Medical Forms" (R21)."""
        raise NotImplementedError

    def notifyParents(self) -> None:
        """Realizes UC22 "Notify Parents" (R22)."""
        raise NotImplementedError

    def logAttendance(self) -> None:
        """Realizes UC23 "Log Attendance" (R23)."""
        raise NotImplementedError

    def addParents(self) -> None:
        """Realizes UC24 "Add Parents" (R24)."""
        raise NotImplementedError

    def createGroups(self) -> None:
        """Realizes UC25 "Create Groups" (R25)."""
        raise NotImplementedError

    def seeCampGroupsAndEvents(self) -> None:
        """Realizes UC26 "See Camp Groups And Events" (R26)."""
        raise NotImplementedError

    def scheduleTasks(self) -> None:
        """Realizes UC27 "Schedule Tasks" (R27)."""
        raise NotImplementedError

    def deleteTasks(self) -> None:
        """Realizes UC28 "Delete Tasks" (R28)."""
        raise NotImplementedError

    def modifyTasks(self) -> None:
        """Realizes UC29 "Modify Tasks" (R29)."""
        raise NotImplementedError

    def modifyCamperInformation(self) -> None:
        """Realizes UC30 "Modify Camper Information" (R30)."""
        raise NotImplementedError

    def deleteCampers(self) -> None:
        """Realizes UC31 "Delete Campers" (R31)."""
        raise NotImplementedError

    def modifyParentInformation(self) -> None:
        """Realizes UC32 "Modify Parent Information" (R32)."""
        raise NotImplementedError

    def deleteParents(self) -> None:
        """Realizes UC33 "Delete Parents" (R33)."""
        raise NotImplementedError

    def modifyGroupInformation(self) -> None:
        """Realizes UC34 "Modify Group Information" (R34)."""
        raise NotImplementedError

    def seeSpecificGroupEvents(self) -> None:
        """Realizes UC35 "See Specific Group Events" (R35)."""
        raise NotImplementedError


@_dc.dataclass
class CampWorker:
    """Source: R49, R50, R51, R52, R53, R54"""
    name: _t.Optional[str] = None
    assignedCampers: _t.Optional[str] = None
    campers: _t.List["Camper"] = _dc.field(default_factory=list)

    def submitCompletionReport(self) -> None:
        """Realizes UC49 "Submit Completion Report" (R50)."""
        raise NotImplementedError

    def reportInappropriateBehavior(self) -> None:
        """Realizes UC50 "Report Inappropriate Behavior" (R51)."""
        raise NotImplementedError

    def reportSuppliesShortage(self) -> None:
        """Realizes UC51 "Report Supplies Shortage" (R52)."""
        raise NotImplementedError

    def reportRepairsNeeded(self) -> None:
        """Realizes UC52 "Report Repairs Needed" (R53)."""
        raise NotImplementedError

    def seeAssignedCampers(self) -> None:
        """Realizes UC48 "See Assigned Campers" (R49, R54)."""
        raise NotImplementedError
