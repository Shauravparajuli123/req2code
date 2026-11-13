"""Code skeleton generated from the shared model of D1/camperplus.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Camper:
    """Source: R1, R24, R37, R40, R46, R47"""
    name: _t.Optional[str] = None
    guardian: _t.Optional[str] = None
    emergencyInformation: _t.Optional[str] = None
    problem: _t.Optional[str] = None

    def createCamper(self) -> None:
        """Realizes UC2 "Create Camper" (R1)."""
        raise NotImplementedError

    def deleteCamper(self) -> None:
        """Realizes UC7 "Delete Camper" (R31)."""
        raise NotImplementedError

    def modifyCamperInformation(self) -> None:
        """Realizes UC16 "Modify Information" (R30, R32, R34)."""
        raise NotImplementedError

    def enrollCamper(self) -> None:
        """Realizes UC10 "Enroll Camper" (R46)."""
        raise NotImplementedError

    def seeCamper(self) -> None:
        """Realizes UC24 "See Camper" (R47, R49, R54)."""
        raise NotImplementedError

    def seeConsentForm(self) -> None:
        """Realizes UC25 "See Consent Form" (R36)."""
        raise NotImplementedError

    def seeCounselor(self) -> None:
        """Realizes UC26 "See Counselor" (R40)."""
        raise NotImplementedError


@_dc.dataclass
class Parent:
    """Source: R24, R39, R43, R44, R46, R47"""
    name: _t.Optional[str] = None
    camperBehavior: _t.Optional[str] = None

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R39)."""
        raise NotImplementedError

    def seeCamperActivity(self) -> None:
        """Realizes UC24 "See Camper" (R47, R49, R54)."""
        raise NotImplementedError

    def seeConsentForm(self) -> None:
        """Realizes UC25 "See Consent Form" (R36)."""
        raise NotImplementedError

    def seeCounselor(self) -> None:
        """Realizes UC26 "See Counselor" (R40)."""
        raise NotImplementedError

    def seeSchedule(self) -> None:
        """Realizes UC30 "See Schedule" (R48)."""
        raise NotImplementedError

    def seePayment(self) -> None:
        """Realizes UC29 "See Payment" (R43)."""
        raise NotImplementedError

    def sharePhoto(self) -> None:
        """Realizes UC32 "Share Photo" (R44)."""
        raise NotImplementedError

    def signConsentForm(self) -> None:
        """Realizes UC33 "Sign Consent Form" (R42)."""
        raise NotImplementedError

    def submitForm(self) -> None:
        """Realizes UC37 "Submit Type" (R38)."""
        raise NotImplementedError


@_dc.dataclass
class CampAdministrator:
    """Source: R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22, R23, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R42, R45"""
    campers: _t.List["Camper"] = _dc.field(default_factory=list)
    parents: _t.List["Parent"] = _dc.field(default_factory=list)
    events: _t.List["Event"] = _dc.field(default_factory=list)
    forms: _t.List["Form"] = _dc.field(default_factory=list)

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R39)."""
        raise NotImplementedError

    def createCamper(self) -> None:
        """Realizes UC2 "Create Camper" (R1)."""
        raise NotImplementedError

    def deleteCamper(self) -> None:
        """Realizes UC7 "Delete Camper" (R31)."""
        raise NotImplementedError

    def keepCamperRecord(self) -> None:
        """Realizes UC11 "Keep Camper Record" (R3)."""
        raise NotImplementedError

    def keepInformation(self) -> None:
        """Realizes UC12 "Keep Information" (R20)."""
        raise NotImplementedError

    def keepTrack(self) -> None:
        """Realizes UC13 "Keep Track" (R5, R13)."""
        raise NotImplementedError

    def logAttendance(self) -> None:
        """Realizes UC14 "Log Attendance" (R23)."""
        raise NotImplementedError

    def makeNametag(self) -> None:
        """Realizes UC15 "Make Nametag" (R18)."""
        raise NotImplementedError

    def modifyInformation(self) -> None:
        """Realizes UC16 "Modify Information" (R30, R32, R34)."""
        raise NotImplementedError

    def modifyTask(self) -> None:
        """Realizes UC17 "Modify Task" (R29)."""
        raise NotImplementedError

    def notifyParent(self) -> None:
        """Realizes UC18 "Notify Parent" (R22)."""
        raise NotImplementedError

    def provideFeedback(self) -> None:
        """Realizes UC19 "Provide Feedback" (R17)."""
        raise NotImplementedError

    def removeCamper(self) -> None:
        """Realizes UC20 "Remove Camper" (R2)."""
        raise NotImplementedError

    def scheduleActivity(self) -> None:
        """Realizes UC21 "Schedule Activity" (R6)."""
        raise NotImplementedError

    def scheduleTask(self) -> None:
        """Realizes UC22 "Schedule Task" (R27)."""
        raise NotImplementedError

    def seeCampGroup(self) -> None:
        """Realizes UC23 "See Camp Group" (R26)."""
        raise NotImplementedError

    def seeConsentForm(self) -> None:
        """Realizes UC25 "See Consent Form" (R36)."""
        raise NotImplementedError

    def seeCounselor(self) -> None:
        """Realizes UC26 "See Counselor" (R40)."""
        raise NotImplementedError

    def seeEvent(self) -> None:
        """Realizes UC27 "See Event" (R35)."""
        raise NotImplementedError

    def seeForm(self) -> None:
        """Realizes UC28 "See Form" (R21)."""
        raise NotImplementedError

    def seePayment(self) -> None:
        """Realizes UC29 "See Payment" (R43)."""
        raise NotImplementedError

    def seeSchedule(self) -> None:
        """Realizes UC30 "See Schedule" (R48)."""
        raise NotImplementedError

    def setReminder(self) -> None:
        """Realizes UC31 "Set Reminder" (R9)."""
        raise NotImplementedError

    def storeEmergencyInformation(self) -> None:
        """Realizes UC34 "Store Emergency Information" (R15)."""
        raise NotImplementedError

    def storeInformation(self) -> None:
        """Realizes UC35 "Store Information" (R16)."""
        raise NotImplementedError

    def uploadConsentForm(self) -> None:
        """Realizes UC41 "Upload Consent Form" (R4)."""
        raise NotImplementedError


@_dc.dataclass
class CampCounselor:
    """Source: R49, R50, R51, R52, R53, R54"""
    name: _t.Optional[str] = None
    assignedKids: _t.Optional[str] = None
    campers: _t.List["Camper"] = _dc.field(default_factory=list)

    def takeAttendance(self) -> None:
        """Realizes UC39 "Take Attendance" (R55)."""
        raise NotImplementedError

    def submitCompletionReport(self) -> None:
        """Realizes UC36 "Submit Completion Report" (R50)."""
        raise NotImplementedError

    def reportBehavior(self) -> None:
        """Operation."""
        raise NotImplementedError

    def reportSupplies(self) -> None:
        """Operation."""
        raise NotImplementedError

    def reportRepairs(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class CampWorker:
    """Source: R49, R54"""
    name: _t.Optional[str] = None
    assignedKids: _t.Optional[str] = None
    campers: _t.List["Camper"] = _dc.field(default_factory=list)

    def seeAssignedKids(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Event:
    """Source: R26, R27, R28, R29, R35"""
    name: _t.Optional[str] = None
    date: _t.Optional[str] = None

    def seeEvent(self) -> None:
        """Realizes UC27 "See Event" (R35)."""
        raise NotImplementedError


@_dc.dataclass
class Form:
    """Source: R4, R14, R19, R21, R38, R42, R44"""
    type: _t.Optional[str] = None
    parent: _t.Optional["Parent"] = None

    def uploadConsentForm(self) -> None:
        """Realizes UC41 "Upload Consent Form" (R4)."""
        raise NotImplementedError

    def submitForm(self) -> None:
        """Operation."""
        raise NotImplementedError
