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
    group: _t.Optional[str] = None
    attendance: _t.Optional[bool] = None
    parent: _t.Optional["Parent"] = None
    event: _t.Optional["Event"] = None

    def addCamper(self) -> None:
        """Realizes UC1 "Add Campers" (R1)."""
        raise NotImplementedError

    def removeCamper(self) -> None:
        """Realizes UC2 "Remove Campers" (R2)."""
        raise NotImplementedError

    def modifyCamperInfo(self) -> None:
        """Realizes UC28 "Modify Camper Information" (R30)."""
        raise NotImplementedError

    def deleteCamper(self) -> None:
        """Realizes UC29 "Delete Campers" (R31)."""
        raise NotImplementedError


@_dc.dataclass
class Parent:
    """Source: R14, R16, R17, R36, R39, R40, R43, R44, R46, R47, R48"""
    name: _t.Optional[str] = None
    camper: _t.Optional[str] = None
    payment: _t.Optional[str] = None
    consentForms: _t.Optional[str] = None
    photos: _t.Optional[str] = None
    messages: _t.Optional[str] = None
    consentForm: _t.Optional["ConsentForm"] = None

    def createAccount(self) -> None:
        """Realizes UC17 "Create Registration Forms" (R19)."""
        raise NotImplementedError

    def enrollCamper(self) -> None:
        """Operation."""
        raise NotImplementedError

    def modifyParentInfo(self) -> None:
        """Realizes UC30 "Modify Parent Information" (R32)."""
        raise NotImplementedError

    def deleteParent(self) -> None:
        """Realizes UC31 "Delete Parents" (R33)."""
        raise NotImplementedError

    def viewCamperSchedule(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class CampWorker:
    """Source: R49, R51, R52, R53, R54"""
    name: _t.Optional[str] = None
    assignedCampers: _t.Optional[str] = None
    group: _t.Optional["Group"] = None

    def takeAttendance(self) -> None:
        """Realizes UC21 "Log Attendance" (R23)."""
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
class Group:
    """Source: R25, R26, R34, R35"""
    name: _t.Optional[str] = None
    events: _t.Optional[str] = None
    event: _t.Optional["Event"] = None

    def createGroup(self) -> None:
        """Realizes UC23 "Create Groups" (R25)."""
        raise NotImplementedError

    def modifyGroupInfo(self) -> None:
        """Realizes UC32 "Modify Group Information" (R34)."""
        raise NotImplementedError

    def deleteGroup(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Event:
    """Source: R6, R26, R27, R28, R29, R35"""
    name: _t.Optional[str] = None
    date: _t.Optional[str] = None
    assignedCampers: _t.Optional[str] = None
    tasks: _t.Optional[str] = None
    camper: _t.Optional["Camper"] = None

    def scheduleEvent(self) -> None:
        """Realizes UC25 "Schedule Tasks" (R27)."""
        raise NotImplementedError

    def modifyEvent(self) -> None:
        """Realizes UC27 "Modify Tasks" (R29)."""
        raise NotImplementedError

    def deleteEvent(self) -> None:
        """Realizes UC26 "Delete Tasks" (R28)."""
        raise NotImplementedError


@_dc.dataclass
class ConsentForm:
    """Source: R4, R5, R36"""
    name: _t.Optional[str] = None
    submittedBy: _t.Optional[str] = None

    def uploadConsentForm(self) -> None:
        """Realizes UC4 "Upload Consent Forms" (R4)."""
        raise NotImplementedError

    def trackSubmission(self) -> None:
        """Realizes UC5 "Keep Track Of Form Submissions" (R5)."""
        raise NotImplementedError


@_dc.dataclass
class Rule:
    """Source: R12"""
    name: _t.Optional[str] = None
    description: _t.Optional[str] = None

    def createRule(self) -> None:
        """Realizes UC12 "Create Rules" (R12)."""
        raise NotImplementedError

    def modifyRule(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Facility:
    """Source: R13"""
    name: _t.Optional[str] = None
    usage: _t.Optional[int] = None

    def trackUsage(self) -> None:
        """Realizes UC13 "Track Facility Usage" (R13)."""
        raise NotImplementedError


@_dc.dataclass
class Payment:
    """Source: R16, R43"""
    amount: _t.Optional[float] = None

    def makePayment(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Photo:
    """Source: R44"""
    name: _t.Optional[str] = None
    camper: _t.Optional[str] = None

    def sharePhoto(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Task:
    """Source: R27, R28, R29"""
    name: _t.Optional[str] = None
    status: _t.Optional[str] = None

    def completeTask(self) -> None:
        """Operation."""
        raise NotImplementedError
