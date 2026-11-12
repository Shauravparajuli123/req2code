"""Code skeleton generated from the shared model of D1/grocery.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Employee:
    """Source: R1, R13, R15, R16, R26, R47, R48"""
    name: _t.Optional[str] = None
    certificate: _t.Optional[str] = None
    status: _t.Optional[str] = None
    preferredWorkingHours: _t.Optional[str] = None
    emailNotificationPreference: _t.Optional[str] = None
    paymentPreference: _t.Optional[str] = None
    contract: _t.Optional[str] = None

    def expressHour(self) -> None:
        """Realizes UC7 "Express Hour" (R7)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC13 "View Schedule" (R13, R14)."""
        raise NotImplementedError

    def verifyWorkHour(self) -> None:
        """Realizes UC14 "Verify Work Hour" (R15, R16)."""
        raise NotImplementedError

    def changeInformation(self) -> None:
        """Realizes UC26 "Change Information" (R47)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC27 "View Contract" (R32, R48)."""
        raise NotImplementedError

    def viewStatement(self) -> None:
        """Realizes UC25 "View Statement" (R45)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC16 "Respond Complaint" (R23)."""
        raise NotImplementedError


@_dc.dataclass
class Manager:
    """Source: R2, R3, R4, R5, R8, R9, R10, R11, R12, R14, R18, R19, R20, R21, R22, R23, R24, R25, R27, R28, R29, R30, R34, R35, R36, R37, R39, R40, R41, R42, R43, R44, R45, R46, R49"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None

    def sendSalaryStatement(self) -> None:
        """Realizes UC2 "Send Salary Statement" (R2)."""
        raise NotImplementedError

    def enableOption(self) -> None:
        """Realizes UC3 "Enable Option" (R3)."""
        raise NotImplementedError

    def automatePaymentSystem(self) -> None:
        """Realizes UC4 "Automate Payment System" (R4)."""
        raise NotImplementedError

    def outsourcePart(self) -> None:
        """Realizes UC5 "Outsource Part" (R5)."""
        raise NotImplementedError

    def semiSchedulingProcess(self) -> None:
        """Realizes UC8 "Semi Scheduling Process" (R8)."""
        raise NotImplementedError

    def manuallyEditSchedule(self) -> None:
        """Realizes UC9 "Manually Edit Schedule" (R9)."""
        raise NotImplementedError

    def notifyAdjustment(self) -> None:
        """Realizes UC10 "Notify Adjustment" (R11)."""
        raise NotImplementedError

    def notifyHiringProcess(self) -> None:
        """Realizes UC11 "Notify Hiring Process" (R28)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC13 "View Schedule" (R13, R14)."""
        raise NotImplementedError

    def viewCertificate(self) -> None:
        """Realizes UC33 "View Certificate" (R33)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC27 "View Contract" (R32, R48)."""
        raise NotImplementedError

    def forwardMessage(self) -> None:
        """Realizes UC28 "Forward Message" (R37)."""
        raise NotImplementedError

    def contactEmployee(self) -> None:
        """Realizes UC30 "Contact Employee" (R35)."""
        raise NotImplementedError

    def haveSystem(self) -> None:
        """Realizes UC31 "Have System" (R39)."""
        raise NotImplementedError

    def hireEmployee(self) -> None:
        """Realizes UC32 "Hire Employee" (R27)."""
        raise NotImplementedError

    def viewInbox(self) -> None:
        """Realizes UC34 "View Inbox" (R38)."""
        raise NotImplementedError


@_dc.dataclass
class Applicant:
    """Source: R31"""
    name: _t.Optional[str] = None
    email: _t.Optional[str] = None

    def registerAccount(self) -> None:
        """Realizes UC20 "Register Account" (R31)."""
        raise NotImplementedError


@_dc.dataclass
class Complaint:
    """Source: R17, R18, R19, R20, R21, R22, R23, R24, R25"""
    status: _t.Optional[str] = None
    category: _t.Optional[str] = None
    priority: _t.Optional[str] = None

    def fileComplaint(self) -> None:
        """Realizes UC15 "File Complaint" (R18)."""
        raise NotImplementedError

    def respondComplaint(self) -> None:
        """Realizes UC16 "Respond Complaint" (R23)."""
        raise NotImplementedError

    def categorizeComplaint(self) -> None:
        """Realizes UC17 "Categorize Complaint" (R24)."""
        raise NotImplementedError

    def prioritizeComplaint(self) -> None:
        """Realizes UC18 "Prioritize Complaint" (R25)."""
        raise NotImplementedError


@_dc.dataclass
class SalaryStatement:
    """Source: R1, R2"""
    employeeName: _t.Optional[str] = None
    paymentDate: _t.Optional[str] = None

    def receiveSalaryStatement(self) -> None:
        """Realizes UC1 "Receive Salary Statement" (R1)."""
        raise NotImplementedError

    def sendSalaryStatement(self) -> None:
        """Realizes UC2 "Send Salary Statement" (R2)."""
        raise NotImplementedError


@_dc.dataclass
class Schedule:
    """Source: R7, R8, R9, R10, R11, R12, R14"""
    employeeName: _t.Optional[str] = None
    workingHours: _t.Optional[str] = None
    status: _t.Optional[str] = None

    def semiSchedulingProcess(self) -> None:
        """Realizes UC8 "Semi Scheduling Process" (R8)."""
        raise NotImplementedError

    def manuallyEditSchedule(self) -> None:
        """Realizes UC9 "Manually Edit Schedule" (R9)."""
        raise NotImplementedError

    def notifyAdjustment(self) -> None:
        """Realizes UC10 "Notify Adjustment" (R11)."""
        raise NotImplementedError
