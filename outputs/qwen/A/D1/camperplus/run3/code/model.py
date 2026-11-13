"""Code skeleton generated from the shared model of D1/camperplus.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class CampAdministrator:
    """Source: -"""
    parents: _t.List["Parent"] = _dc.field(default_factory=list)
    campWorkers: _t.List["CampWorker"] = _dc.field(default_factory=list)

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

    def trackConsentFormSubmissions(self) -> None:
        """Realizes UC5 "Track Consent Form Submissions" (R5)."""
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

    def provideWeeklyFeedback(self) -> None:
        """Realizes UC17 "Provide Weekly Feedback" (R17)."""
        raise NotImplementedError

    def createRegistrationForm(self) -> None:
        """Realizes UC18 "Create Registration Form" (R19)."""
        raise NotImplementedError

    def keepInformationOrganized(self) -> None:
        """Realizes UC19 "Keep Information Organized" (R20)."""
        raise NotImplementedError

    def seeMedicalForms(self) -> None:
        """Realizes UC20 "See Medical Forms" (R21)."""
        raise NotImplementedError

    def notifyParents(self) -> None:
        """Realizes UC21 "Notify Parents" (R22)."""
        raise NotImplementedError

    def logAttendance(self) -> None:
        """Realizes UC22 "Log Attendance" (R23)."""
        raise NotImplementedError

    def addParents(self) -> None:
        """Realizes UC23 "Add Parents" (R24)."""
        raise NotImplementedError

    def createGroups(self) -> None:
        """Realizes UC24 "Create Groups" (R25)."""
        raise NotImplementedError

    def seeCampGroupsAndEvents(self) -> None:
        """Realizes UC25 "See Camp Groups And Events" (R26)."""
        raise NotImplementedError

    def scheduleTasks(self) -> None:
        """Realizes UC26 "Schedule Tasks" (R27)."""
        raise NotImplementedError

    def deleteTasks(self) -> None:
        """Realizes UC27 "Delete Tasks" (R28)."""
        raise NotImplementedError

    def modifyTasks(self) -> None:
        """Realizes UC28 "Modify Tasks" (R29)."""
        raise NotImplementedError

    def modifyCamperInformation(self) -> None:
        """Realizes UC29 "Modify Camper Information" (R30)."""
        raise NotImplementedError

    def deleteCampers(self) -> None:
        """Realizes UC30 "Delete Campers" (R31)."""
        raise NotImplementedError

    def modifyParentInformation(self) -> None:
        """Realizes UC31 "Modify Parent Information" (R32)."""
        raise NotImplementedError

    def deleteParents(self) -> None:
        """Realizes UC32 "Delete Parents" (R33)."""
        raise NotImplementedError

    def modifyGroupInformation(self) -> None:
        """Realizes UC33 "Modify Group Information" (R34)."""
        raise NotImplementedError

    def seeSpecificGroupEvents(self) -> None:
        """Realizes UC34 "See Specific Group Events" (R35)."""
        raise NotImplementedError


@_dc.dataclass
class Parent:
    """Source: -"""

    def seeConsentForms(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeCamperActivity(self) -> None:
        """Realizes UC35 "See Camper Activity" (R37)."""
        raise NotImplementedError

    def seeCamperSchedule(self) -> None:
        """Realizes UC46 "See Camper Schedule" (R48)."""
        raise NotImplementedError

    def enrollCampers(self) -> None:
        """Realizes UC44 "Enroll Campers" (R46)."""
        raise NotImplementedError

    def seeEnrolledCampers(self) -> None:
        """Realizes UC45 "See Enrolled Campers" (R47)."""
        raise NotImplementedError

    def seeAssignedKids(self) -> None:
        """Realizes UC47 "See Assigned Kids" (R49, R54)."""
        raise NotImplementedError

    def submitForms(self) -> None:
        """Realizes UC36 "Submit Forms" (R38)."""
        raise NotImplementedError

    def createAccount(self) -> None:
        """Realizes UC37 "Create Account" (R39)."""
        raise NotImplementedError

    def seeCounselors(self) -> None:
        """Realizes UC38 "See Counselors" (R40)."""
        raise NotImplementedError

    def messageCounselors(self) -> None:
        """Realizes UC39 "Message Counselors" (R41)."""
        raise NotImplementedError

    def signAndSubmitForms(self) -> None:
        """Realizes UC40 "Sign And Submit Forms" (R42)."""
        raise NotImplementedError

    def checkPayments(self) -> None:
        """Realizes UC41 "Check Payments" (R43)."""
        raise NotImplementedError

    def sharePhotos(self) -> None:
        """Realizes UC42 "Share Photos" (R44)."""
        raise NotImplementedError

    def emergencyContact(self) -> None:
        """Realizes UC43 "Emergency Contact" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class CampWorker:
    """Source: -"""
    campAdministrator: _t.Optional["CampAdministrator"] = None

    def seeAssignedKids(self) -> None:
        """Realizes UC47 "See Assigned Kids" (R49, R54)."""
        raise NotImplementedError

    def submitCompletionReport(self) -> None:
        """Realizes UC48 "Submit Completion Report" (R50)."""
        raise NotImplementedError

    def reportInappropriateBehavior(self) -> None:
        """Realizes UC49 "Report Inappropriate Behavior" (R51)."""
        raise NotImplementedError

    def reportSupplies(self) -> None:
        """Realizes UC50 "Report Supplies" (R52)."""
        raise NotImplementedError

    def reportRepairs(self) -> None:
        """Realizes UC51 "Report Repairs" (R53)."""
        raise NotImplementedError
