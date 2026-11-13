"""Code skeleton generated from the shared model of D1/camperplus.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Camper:
    """Source: R1, R2, R30, R31"""
    name: _t.Optional[str] = None
    emergencyInformation: _t.Optional[str] = None
    parent: _t.Optional[str] = None

    def addCamper(self) -> None:
        """Realizes UC1 "Add Campers" (R1)."""
        raise NotImplementedError

    def removeCamper(self) -> None:
        """Realizes UC2 "Remove Campers" (R2)."""
        raise NotImplementedError

    def modifyCamperInformation(self) -> None:
        """Realizes UC26 "Modify Camper Information" (R30)."""
        raise NotImplementedError

    def deleteCamper(self) -> None:
        """Realizes UC27 "Delete Campers" (R31)."""
        raise NotImplementedError


@_dc.dataclass
class Parent:
    """Source: R14, R36, R39, R40, R41, R43, R44, R46, R47"""
    name: _t.Optional[str] = None
    account: _t.Optional[str] = None
    children: _t.Optional[str] = None

    def createAccount(self) -> None:
        """Realizes UC17 "Create Registration Forms" (R19)."""
        raise NotImplementedError

    def enrollCamper(self) -> None:
        """Operation."""
        raise NotImplementedError

    def modifyParentInformation(self) -> None:
        """Realizes UC28 "Modify Parent Information" (R32)."""
        raise NotImplementedError

    def deleteParent(self) -> None:
        """Realizes UC29 "Delete Parents" (R33)."""
        raise NotImplementedError


@_dc.dataclass
class CampWorker:
    """Source: R49, R50, R51, R52, R53, R54"""
    name: _t.Optional[str] = None
    assignedCampers: _t.Optional[str] = None

    def takeAttendance(self) -> None:
        """Realizes UC19 "Log Attendance" (R23)."""
        raise NotImplementedError

    def reportCamperBehavior(self) -> None:
        """Operation."""
        raise NotImplementedError

    def reportSuppliesShortage(self) -> None:
        """Operation."""
        raise NotImplementedError

    def reportFacilityRepair(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class CampAdministrator:
    """Source: R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35"""
    campers: _t.List["Camper"] = _dc.field(default_factory=list)
    parents: _t.List["Parent"] = _dc.field(default_factory=list)
    campWorkers: _t.List["CampWorker"] = _dc.field(default_factory=list)

    def addCamper(self) -> None:
        """Realizes UC1 "Add Campers" (R1)."""
        raise NotImplementedError

    def removeCamper(self) -> None:
        """Realizes UC2 "Remove Campers" (R2)."""
        raise NotImplementedError

    def keepCamperRecords(self) -> None:
        """Realizes UC3 "Keep Camper Records" (R3)."""
        raise NotImplementedError

    def uploadConsentForms(self) -> None:
        """Realizes UC4 "Upload Consent Forms" (R4)."""
        raise NotImplementedError

    def trackFormSubmissions(self) -> None:
        """Realizes UC5 "Track Form Submissions" (R5)."""
        raise NotImplementedError

    def scheduleActivities(self) -> None:
        """Realizes UC6 "Schedule Activities" (R6)."""
        raise NotImplementedError

    def createNametags(self) -> None:
        """Realizes UC7 "Create Nametags" (R7)."""
        raise NotImplementedError

    def suspendCamper(self) -> None:
        """Realizes UC8 "Suspend Campers" (R8)."""
        raise NotImplementedError

    def setReminders(self) -> None:
        """Realizes UC9 "Set Reminders" (R9)."""
        raise NotImplementedError

    def assignPositions(self) -> None:
        """Realizes UC10 "Assign Positions" (R10)."""
        raise NotImplementedError

    def warnCampWorker(self) -> None:
        """Realizes UC11 "Warn Camp Workers" (R11)."""
        raise NotImplementedError

    def createRules(self) -> None:
        """Realizes UC12 "Create Rules" (R12)."""
        raise NotImplementedError

    def trackFacilityUsage(self) -> None:
        """Realizes UC13 "Track Facility Usage" (R13)."""
        raise NotImplementedError

    def storeEmergencyInformation(self) -> None:
        """Realizes UC14 "Store Emergency Information" (R15)."""
        raise NotImplementedError

    def storeParentInformation(self) -> None:
        """Realizes UC15 "Store Parent Information" (R16)."""
        raise NotImplementedError

    def provideFeedback(self) -> None:
        """Realizes UC16 "Provide Feedback" (R17)."""
        raise NotImplementedError

    def createRegistrationForms(self) -> None:
        """Realizes UC17 "Create Registration Forms" (R19)."""
        raise NotImplementedError

    def storeCampInformation(self) -> None:
        """Realizes UC18 "Store Camp Information" (R20)."""
        raise NotImplementedError

    def logAttendance(self) -> None:
        """Realizes UC19 "Log Attendance" (R23)."""
        raise NotImplementedError

    def addParent(self) -> None:
        """Realizes UC20 "Add Parents" (R24)."""
        raise NotImplementedError

    def createGroups(self) -> None:
        """Realizes UC21 "Create Groups" (R25)."""
        raise NotImplementedError

    def seeGroupEvents(self) -> None:
        """Realizes UC22 "See Group Events" (R26, R35)."""
        raise NotImplementedError

    def scheduleTasks(self) -> None:
        """Realizes UC23 "Schedule Tasks" (R27)."""
        raise NotImplementedError

    def deleteTasks(self) -> None:
        """Realizes UC24 "Delete Tasks" (R28)."""
        raise NotImplementedError

    def modifyTasks(self) -> None:
        """Realizes UC25 "Modify Tasks" (R29)."""
        raise NotImplementedError

    def modifyCamperInformation(self) -> None:
        """Realizes UC26 "Modify Camper Information" (R30)."""
        raise NotImplementedError

    def deleteCampers(self) -> None:
        """Realizes UC27 "Delete Campers" (R31)."""
        raise NotImplementedError

    def modifyParentInformation(self) -> None:
        """Realizes UC28 "Modify Parent Information" (R32)."""
        raise NotImplementedError

    def deleteParents(self) -> None:
        """Realizes UC29 "Delete Parents" (R33)."""
        raise NotImplementedError

    def modifyGroupInformation(self) -> None:
        """Realizes UC30 "Modify Group Information" (R34)."""
        raise NotImplementedError
