"""Code skeleton generated from the shared model of D1/camperplus.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Camper:
    """Source: R1, R24, R37, R46, R47"""
    name: _t.Optional[str] = None
    guardian: _t.Optional[str] = None
    emergencyInformation: _t.Optional[str] = None
    problem: _t.Optional[str] = None
    behavior: _t.Optional[str] = None
    parent: _t.Optional["Parent"] = None

    def createCamper(self) -> None:
        """Operation."""
        raise NotImplementedError

    def removeCamper(self) -> None:
        """Realizes UC19 "Remove Camper" (R2)."""
        raise NotImplementedError

    def keepCamperRecord(self) -> None:
        """Realizes UC10 "Keep Camper Record" (R3)."""
        raise NotImplementedError

    def enrollCamper(self) -> None:
        """Realizes UC9 "Enroll Camper" (R46)."""
        raise NotImplementedError

    def modifyCamperInformation(self) -> None:
        """Realizes UC15 "Modify Information" (R30, R32, R34)."""
        raise NotImplementedError


@_dc.dataclass
class Parent:
    """Source: R24, R39, R40, R43, R44"""
    name: _t.Optional[str] = None
    camper: _t.Optional[str] = None

    def createAccount(self) -> None:
        """Realizes UC1 "Create Account" (R39)."""
        raise NotImplementedError

    def submitConsentForm(self) -> None:
        """Realizes UC36 "Submit Type" (R38)."""
        raise NotImplementedError

    def seeCamperActivity(self) -> None:
        """Realizes UC23 "See Camper" (R47, R49, R54)."""
        raise NotImplementedError

    def seeCamperSchedule(self) -> None:
        """Realizes UC29 "See Schedule" (R48)."""
        raise NotImplementedError

    def seeCounselor(self) -> None:
        """Realizes UC25 "See Counselor" (R40)."""
        raise NotImplementedError

    def sharePhoto(self) -> None:
        """Realizes UC31 "Share Photo" (R44)."""
        raise NotImplementedError

    def seeConsentForm(self) -> None:
        """Realizes UC24 "See Consent Form" (R36)."""
        raise NotImplementedError

    def seePayment(self) -> None:
        """Realizes UC28 "See Payment" (R43)."""
        raise NotImplementedError


@_dc.dataclass
class CampAdministrator:
    """Source: R20, R21, R22, R23, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35"""
    campers: _t.List["Camper"] = _dc.field(default_factory=list)
    parents: _t.List["Parent"] = _dc.field(default_factory=list)
    campCounselors: _t.List["CampCounselor"] = _dc.field(default_factory=list)

    def createGroup(self) -> None:
        """Realizes UC2 "Create Group" (R25)."""
        raise NotImplementedError

    def addCamperToGroup(self) -> None:
        """Operation."""
        raise NotImplementedError

    def seeCampGroups(self) -> None:
        """Realizes UC22 "See Camp Group" (R26)."""
        raise NotImplementedError

    def scheduleActivity(self) -> None:
        """Realizes UC20 "Schedule Activity" (R6)."""
        raise NotImplementedError

    def scheduleTask(self) -> None:
        """Realizes UC21 "Schedule Task" (R27)."""
        raise NotImplementedError

    def deleteTask(self) -> None:
        """Realizes UC8 "Delete Task" (R28)."""
        raise NotImplementedError

    def modifyTask(self) -> None:
        """Realizes UC16 "Modify Task" (R29)."""
        raise NotImplementedError

    def seeEvent(self) -> None:
        """Realizes UC26 "See Event" (R35)."""
        raise NotImplementedError

    def modifyCamperInformation(self) -> None:
        """Realizes UC15 "Modify Information" (R30, R32, R34)."""
        raise NotImplementedError

    def deleteCamper(self) -> None:
        """Realizes UC6 "Delete Camper" (R31)."""
        raise NotImplementedError

    def deleteParent(self) -> None:
        """Realizes UC7 "Delete Parent" (R33)."""
        raise NotImplementedError

    def modifyParentInformation(self) -> None:
        """Realizes UC15 "Modify Information" (R30, R32, R34)."""
        raise NotImplementedError

    def modifyGroupInformation(self) -> None:
        """Realizes UC15 "Modify Information" (R30, R32, R34)."""
        raise NotImplementedError


@_dc.dataclass
class CampCounselor:
    """Source: R49, R55"""
    campers: _t.List["Camper"] = _dc.field(default_factory=list)

    def takeAttendance(self) -> None:
        """Realizes UC38 "Take Attendance" (R55)."""
        raise NotImplementedError


@_dc.dataclass
class CampWorker:
    """Source: R50, R51, R52, R53"""

    def submitCompletionReport(self) -> None:
        """Realizes UC35 "Submit Completion Report" (R50)."""
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
