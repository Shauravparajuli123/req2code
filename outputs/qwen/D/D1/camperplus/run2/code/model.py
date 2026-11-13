"""Code skeleton generated from the shared model of D1/camperplus.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Camper:
    """Source: R1, R2, R30, R34, R49"""
    name: _t.Optional[str] = None
    emergencyInfo: _t.Optional[str] = None
    parent: _t.Optional["Parent"] = None
    event: _t.Optional["Event"] = None
    group: _t.Optional["Group"] = None

    def addCamper(self) -> None:
        """Realizes UC1 "Add Campers" (R1)."""
        raise NotImplementedError

    def removeCamper(self) -> None:
        """Realizes UC31 "Delete Campers" (R31)."""
        raise NotImplementedError

    def modifyCamperInfo(self) -> None:
        """Realizes UC30 "Modify Camper Information" (R30)."""
        raise NotImplementedError


@_dc.dataclass
class Parent:
    """Source: R36, R37, R38, R39, R40, R43, R47, R48"""
    name: _t.Optional[str] = None
    account: _t.Optional[str] = None
    child: _t.Optional[str] = None
    counselor: _t.Optional[str] = None
    event: _t.Optional["Event"] = None
    group: _t.Optional["Group"] = None
    feedback: _t.Optional["Feedback"] = None
    payment: _t.Optional["Payment"] = None
    supplies: _t.Optional["Supplies"] = None

    def submitConsentForm(self) -> None:
        """Realizes UC37 "Submit Forms" (R38)."""
        raise NotImplementedError

    def submitFeedback(self) -> None:
        """Realizes UC17 "Provide Feedback" (R17)."""
        raise NotImplementedError

    def viewCamperActivity(self) -> None:
        """Realizes UC36 "See Camper Activity" (R37)."""
        raise NotImplementedError

    def viewEnrolledCampers(self) -> None:
        """Realizes UC46 "See Enrolled Campers" (R47)."""
        raise NotImplementedError

    def viewActivitySchedule(self) -> None:
        """Realizes UC47 "See Activity Schedule" (R48)."""
        raise NotImplementedError


@_dc.dataclass
class CampWorker:
    """Source: R50, R51, R52, R53, R54, R49"""
    name: _t.Optional[str] = None
    assignedKids: _t.Optional[str] = None

    def submitCompletionReport(self) -> None:
        """Realizes UC49 "Submit Completion Report" (R50)."""
        raise NotImplementedError

    def reportInappropriateBehavior(self) -> None:
        """Realizes UC50 "Report Inappropriate Behavior" (R51)."""
        raise NotImplementedError

    def reportSupplies(self) -> None:
        """Realizes UC51 "Report Supplies" (R52)."""
        raise NotImplementedError

    def reportRepairs(self) -> None:
        """Realizes UC52 "Report Necessary Repairs" (R53)."""
        raise NotImplementedError


@_dc.dataclass
class EmergencyInformation:
    """Source: R15, R16"""
    allergies: _t.Optional[str] = None
    medication: _t.Optional[str] = None


@_dc.dataclass
class Event:
    """Source: R6, R26, R27, R28, R29"""
    date: _t.Optional[str] = None
    description: _t.Optional[str] = None
    group: _t.Optional["Group"] = None

    def scheduleEvent(self) -> None:
        """Realizes UC27 "Schedule Tasks" (R27)."""
        raise NotImplementedError

    def modifyEvent(self) -> None:
        """Realizes UC29 "Modify Tasks" (R29)."""
        raise NotImplementedError

    def deleteEvent(self) -> None:
        """Realizes UC28 "Delete Tasks" (R28)."""
        raise NotImplementedError


@_dc.dataclass
class Group:
    """Source: R25, R26"""
    name: _t.Optional[str] = None
    events: _t.Optional[str] = None
    camper: _t.Optional["Camper"] = None
    event: _t.Optional["Event"] = None

    def addCamperToGroup(self) -> None:
        """Realizes UC25 "Create Groups" (R25)."""
        raise NotImplementedError

    def viewGroupEvents(self) -> None:
        """Realizes UC26 "See Groups And Events" (R26)."""
        raise NotImplementedError


@_dc.dataclass
class Rule:
    """Source: R12"""
    description: _t.Optional[str] = None

    def createRule(self) -> None:
        """Realizes UC12 "Create Rules" (R12)."""
        raise NotImplementedError


@_dc.dataclass
class Facility:
    """Source: R13"""
    name: _t.Optional[str] = None

    def trackUsage(self) -> None:
        """Realizes UC13 "Track Facility Usage" (R13)."""
        raise NotImplementedError


@_dc.dataclass
class Feedback:
    """Source: R14, R21, R36"""
    date: _t.Optional[str] = None
    content: _t.Optional[str] = None

    def submitFeedback(self) -> None:
        """Realizes UC17 "Provide Feedback" (R17)."""
        raise NotImplementedError

    def viewFeedback(self) -> None:
        """Realizes UC21 "See Medical Forms" (R21)."""
        raise NotImplementedError


@_dc.dataclass
class Payment:
    """Source: R43"""
    amount: _t.Optional[float] = None
    status: _t.Optional[str] = None

    def viewPayments(self) -> None:
        """Realizes UC42 "See Payments" (R43)."""
        raise NotImplementedError


@_dc.dataclass
class Supplies:
    """Source: R52"""
    name: _t.Optional[str] = None
    quantity: _t.Optional[int] = None

    def reportSupplies(self) -> None:
        """Realizes UC51 "Report Supplies" (R52)."""
        raise NotImplementedError


@_dc.dataclass
class Repair:
    """Source: R53"""
    description: _t.Optional[str] = None
    status: _t.Optional[str] = None

    def reportRepairs(self) -> None:
        """Realizes UC52 "Report Necessary Repairs" (R53)."""
        raise NotImplementedError
