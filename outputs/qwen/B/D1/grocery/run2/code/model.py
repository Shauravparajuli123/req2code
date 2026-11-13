"""Code skeleton generated from the shared model of D1/grocery.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Employee:
    """Source: R1, R6, R7, R13, R15, R47, R48, R49"""
    name: _t.Optional[str] = None
    certificate: _t.Optional[str] = None
    status: _t.Optional[str] = None
    group: _t.Optional[str] = None
    qualification: _t.Optional[str] = None
    preferredWorkingHours: _t.Optional[str] = None

    def expressHour(self) -> None:
        """Realizes UC7 "Express Hour" (R7)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC26 "View Schedule" (R13, R14)."""
        raise NotImplementedError

    def viewCertificate(self) -> None:
        """Realizes UC28 "View Certificate" (R33)."""
        raise NotImplementedError

    def changeInformation(self) -> None:
        """Realizes UC32 "Change Information" (R47)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC29 "View Contract" (R32, R48)."""
        raise NotImplementedError

    def viewStatement(self) -> None:
        """Realizes UC30 "View Statement" (R45)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC24 "Reset Password" (R40)."""
        raise NotImplementedError

    def navigateApplication(self) -> None:
        """Realizes UC23 "Navigate Application" (R42)."""
        raise NotImplementedError

    def choosePayment(self) -> None:
        """Realizes UC22 "Choose Payment" (R44)."""
        raise NotImplementedError

    def chooseEmail(self) -> None:
        """Realizes UC21 "Choose Email" (R43)."""
        raise NotImplementedError

    def fileComplaint(self) -> None:
        """Realizes UC8 "File Complaint" (R18, R19, R20)."""
        raise NotImplementedError

    def viewComplaint(self) -> None:
        """Realizes UC19 "View Complaint" (R21, R22)."""
        raise NotImplementedError

    def respondComplaint(self) -> None:
        """Realizes UC20 "Respond Complaint" (R23)."""
        raise NotImplementedError

    def viewInbox(self) -> None:
        """Realizes UC33 "View Inbox" (R38)."""
        raise NotImplementedError


@_dc.dataclass
class Manager:
    """Source: R2, R3, R4, R5, R10, R11, R12, R14, R18, R19, R21, R22, R23, R24, R25, R27, R28, R29, R30, R32, R33, R34, R35, R36, R39"""
    name: _t.Optional[str] = None
    hiringProcess: _t.Optional[str] = None
    employeeOverview: _t.Optional[str] = None
    employees: _t.List["Employee"] = _dc.field(default_factory=list)

    def sendSalaryStatement(self) -> None:
        """Realizes UC2 "Send Salary Statement" (R2)."""
        raise NotImplementedError

    def enableOption(self) -> None:
        """Realizes UC4 "Enable Option" (R3)."""
        raise NotImplementedError

    def automatePaymentSystem(self) -> None:
        """Realizes UC3 "Automate Payment System" (R4)."""
        raise NotImplementedError

    def outsourcePart(self) -> None:
        """Realizes UC5 "Outsource Part" (R5)."""
        raise NotImplementedError

    def semiSchedulingProcess(self) -> None:
        """Realizes UC9 "Semi Scheduling Process" (R8)."""
        raise NotImplementedError

    def authorizeSchedule(self) -> None:
        """Realizes UC11 "Authorize Schedule" (R10)."""
        raise NotImplementedError

    def notifyAdjustment(self) -> None:
        """Realizes UC12 "Notify Adjustment" (R11)."""
        raise NotImplementedError

    def notifyHiringProcess(self) -> None:
        """Realizes UC13 "Notify Hiring Process" (R28)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC26 "View Schedule" (R13, R14)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC29 "View Contract" (R32, R48)."""
        raise NotImplementedError

    def viewStatement(self) -> None:
        """Realizes UC30 "View Statement" (R45)."""
        raise NotImplementedError

    def contactEmployee(self) -> None:
        """Realizes UC36 "Contact Employee" (R35)."""
        raise NotImplementedError

    def forwardMessage(self) -> None:
        """Realizes UC37 "Forward Message" (R37)."""
        raise NotImplementedError

    def haveOverview(self) -> None:
        """Realizes UC14 "Have Overview" (R29, R30)."""
        raise NotImplementedError

    def haveSystem(self) -> None:
        """Realizes UC15 "Have System" (R39)."""
        raise NotImplementedError


@_dc.dataclass
class OfficeEmployee:
    """Source: R17, R21, R22, R23, R24"""
    name: _t.Optional[str] = None
    complaints: _t.Optional[str] = None

    def categorizeComplaint(self) -> None:
        """Realizes UC17 "Categorize Complaint" (R24)."""
        raise NotImplementedError

    def prioritizeComplaint(self) -> None:
        """Realizes UC18 "Prioritize Complaint" (R25)."""
        raise NotImplementedError

    def viewComplaint(self) -> None:
        """Realizes UC19 "View Complaint" (R21, R22)."""
        raise NotImplementedError

    def respondComplaint(self) -> None:
        """Realizes UC20 "Respond Complaint" (R23)."""
        raise NotImplementedError


@_dc.dataclass
class Applicant:
    """Source: R31"""
    name: _t.Optional[str] = None
    account: _t.Optional[str] = None

    def registerAccount(self) -> None:
        """Realizes UC34 "Register Account" (R31)."""
        raise NotImplementedError
