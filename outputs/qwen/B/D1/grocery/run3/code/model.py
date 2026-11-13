"""Code skeleton generated from the shared model of D1/grocery.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Employee:
    """Source: R1, R6, R7, R15, R34, R47, R48, R49"""
    name: _t.Optional[str] = None
    certificate: _t.Optional[str] = None
    status: _t.Optional[str] = None
    group: _t.Optional[str] = None
    salaryStatement: _t.Optional["SalaryStatement"] = None
    schedule: _t.Optional["Schedule"] = None
    complaint: _t.Optional["Complaint"] = None
    notification: _t.Optional["Notification"] = None

    def expressHour(self) -> None:
        """Realizes UC7 "Express Hour" (R7)."""
        raise NotImplementedError

    def changeInformation(self) -> None:
        """Realizes UC27 "Change Information" (R47)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC23 "View Schedule" (R13, R14)."""
        raise NotImplementedError

    def viewStatement(self) -> None:
        """Realizes UC24 "View Statement" (R45)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC25 "View Contract" (R32, R48)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC29 "Reset Password" (R40)."""
        raise NotImplementedError

    def useSystem(self) -> None:
        """Realizes UC30 "Use System" (R36)."""
        raise NotImplementedError

    def verifyWorkHour(self) -> None:
        """Realizes UC31 "Verify Work Hour" (R15, R16)."""
        raise NotImplementedError

    def sharePaymentHandler(self) -> None:
        """Realizes UC32 "Share Payment Handler" (R46)."""
        raise NotImplementedError

    def navigateApplication(self) -> None:
        """Realizes UC33 "Navigate Application" (R42)."""
        raise NotImplementedError

    def chooseEmail(self) -> None:
        """Realizes UC21 "Choose Email" (R43)."""
        raise NotImplementedError

    def choosePayment(self) -> None:
        """Realizes UC22 "Choose Payment" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class Manager:
    """Source: R2, R3, R4, R5, R11, R12, R13, R14, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R32, R33, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49"""
    name: _t.Optional[str] = None
    salaryStatement: _t.Optional["SalaryStatement"] = None
    schedule: _t.Optional["Schedule"] = None
    complaint: _t.Optional["Complaint"] = None
    employee: _t.Optional["Employee"] = None

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

    def notifyHiringProcess(self) -> None:
        """Realizes UC9 "Notify Hiring Process" (R28)."""
        raise NotImplementedError

    def haveOverview(self) -> None:
        """Realizes UC10 "Have Overview" (R29, R30)."""
        raise NotImplementedError

    def haveSystem(self) -> None:
        """Realizes UC11 "Have System" (R39)."""
        raise NotImplementedError

    def hireEmployee(self) -> None:
        """Realizes UC12 "Hire Employee" (R27)."""
        raise NotImplementedError

    def semiSchedulingProcess(self) -> None:
        """Realizes UC13 "Semi Scheduling Process" (R8)."""
        raise NotImplementedError

    def haveAbility(self) -> None:
        """Realizes UC14 "Have Ability" (R9)."""
        raise NotImplementedError

    def authorizeSchedule(self) -> None:
        """Realizes UC15 "Authorize Schedule" (R10)."""
        raise NotImplementedError

    def notifyAdjustment(self) -> None:
        """Realizes UC16 "Notify Adjustment" (R11)."""
        raise NotImplementedError

    def viewComplaint(self) -> None:
        """Realizes UC19 "View Complaint" (R21, R22)."""
        raise NotImplementedError

    def respondComplaint(self) -> None:
        """Realizes UC20 "Respond Complaint" (R23)."""
        raise NotImplementedError

    def prioritizeComplaint(self) -> None:
        """Realizes UC18 "Prioritize Complaint" (R25)."""
        raise NotImplementedError

    def categorizeComplaint(self) -> None:
        """Realizes UC17 "Categorize Complaint" (R24)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC6 "Receive Notification" (R11, R12, R26, R28, R38, R6)."""
        raise NotImplementedError


@_dc.dataclass
class OfficeEmployee:
    """Source: R17, R18, R19, R21, R22, R23, R24, R25, R26"""
    complaint: _t.Optional["Complaint"] = None

    def fileComplaint(self) -> None:
        """Realizes UC8 "File Complaint" (R18, R19, R20)."""
        raise NotImplementedError

    def viewComplaint(self) -> None:
        """Realizes UC19 "View Complaint" (R21, R22)."""
        raise NotImplementedError

    def respondComplaint(self) -> None:
        """Realizes UC20 "Respond Complaint" (R23)."""
        raise NotImplementedError

    def prioritizeComplaint(self) -> None:
        """Realizes UC18 "Prioritize Complaint" (R25)."""
        raise NotImplementedError

    def categorizeComplaint(self) -> None:
        """Realizes UC17 "Categorize Complaint" (R24)."""
        raise NotImplementedError


@_dc.dataclass
class Complaint:
    """Source: R17, R18, R19, R21, R22, R23, R24, R25, R26"""
    status: _t.Optional[str] = None


@_dc.dataclass
class SalaryStatement:
    """Source: R1, R2"""
    pass


@_dc.dataclass
class Schedule:
    """Source: R8, R9, R10, R11, R12, R13, R14"""
    pass


@_dc.dataclass
class Notification:
    """Source: R6, R11, R12, R26, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49"""
    pass
