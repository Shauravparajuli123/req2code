"""Code skeleton generated from the shared model of D1/grocery.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Employee:
    """Source: R1, R6, R7, R15, R16, R34, R46, R47, R48, R49"""
    personalInformation: _t.Optional[str] = None
    contract: _t.Optional[str] = None
    notification: _t.Optional["Notification"] = None
    schedule: _t.Optional["Schedule"] = None
    complaint: _t.Optional["Complaint"] = None
    application: _t.Optional["Application"] = None

    def expressWorkingHours(self) -> None:
        """Realizes UC7 "Express Working Hours" (R7)."""
        raise NotImplementedError

    def viewPersonalInformation(self) -> None:
        """Realizes UC34 "View Personal Information" (R47)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC35 "View Contract" (R48)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC28 "Reset Password" (R40)."""
        raise NotImplementedError

    def chooseNotifications(self) -> None:
        """Realizes UC31 "Choose Notifications" (R43)."""
        raise NotImplementedError

    def choosePaymentOptions(self) -> None:
        """Realizes UC32 "Choose Payment Options" (R44)."""
        raise NotImplementedError

    def viewFinancialStatements(self) -> None:
        """Realizes UC33 "View Financial Statements" (R45)."""
        raise NotImplementedError


@_dc.dataclass
class Manager:
    """Source: R2, R3, R4, R5, R8, R9, R10, R11, R12, R13, R14, R18, R19, R20, R21, R22, R23, R24, R25, R27, R28, R30, R39, R40, R41, R42"""
    employees: _t.List["Employee"] = _dc.field(default_factory=list)
    schedule: _t.Optional["Schedule"] = None
    complaint: _t.Optional["Complaint"] = None

    def sendSalaryStatements(self) -> None:
        """Realizes UC2 "Send Salary Statements" (R2, R18)."""
        raise NotImplementedError

    def enablePaymentOptions(self) -> None:
        """Realizes UC3 "Enable Payment Options" (R3)."""
        raise NotImplementedError

    def automatePaymentSystem(self) -> None:
        """Realizes UC4 "Automate Payment System" (R4)."""
        raise NotImplementedError

    def outsourcePaymentProcess(self) -> None:
        """Realizes UC5 "Outsource Payment Process" (R5)."""
        raise NotImplementedError

    def semiAutomateScheduling(self) -> None:
        """Realizes UC8 "Semi Automate Scheduling" (R8)."""
        raise NotImplementedError

    def editSchedule(self) -> None:
        """Realizes UC9 "Edit Schedule" (R9)."""
        raise NotImplementedError

    def authorizeSchedule(self) -> None:
        """Realizes UC10 "Authorize Schedule" (R10)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC12 "View Schedule" (R14)."""
        raise NotImplementedError

    def viewComplaints(self) -> None:
        """Realizes UC16 "View Complaints" (R22)."""
        raise NotImplementedError

    def respondToComplaints(self) -> None:
        """Realizes UC17 "Respond To Complaints" (R23)."""
        raise NotImplementedError

    def prioritizeComplaints(self) -> None:
        """Realizes UC18 "Prioritize Complaints" (R25)."""
        raise NotImplementedError

    def hireNewEmployees(self) -> None:
        """Realizes UC19 "Hire New Employees" (R27)."""
        raise NotImplementedError

    def viewEmployeeContracts(self) -> None:
        """Realizes UC20 "View Employee Contracts" (R32)."""
        raise NotImplementedError

    def viewEmployeeCertificates(self) -> None:
        """Realizes UC21 "View Employee Certificates" (R33)."""
        raise NotImplementedError

    def contactManagement(self) -> None:
        """Realizes UC22 "Contact Management" (R34)."""
        raise NotImplementedError

    def contactEmployee(self) -> None:
        """Realizes UC23 "Contact Employee" (R35)."""
        raise NotImplementedError

    def useUserFriendlyApplication(self) -> None:
        """Realizes UC29 "Use User Friendly Application" (R41)."""
        raise NotImplementedError

    def navigateApplication(self) -> None:
        """Realizes UC30 "Navigate Application" (R42)."""
        raise NotImplementedError


@_dc.dataclass
class OfficeEmployee:
    """Source: R17, R26, R31"""
    complaint: _t.Optional["Complaint"] = None

    def fileComplaint(self) -> None:
        """Realizes UC14 "File Complaint" (R18, R26)."""
        raise NotImplementedError

    def viewComplaints(self) -> None:
        """Realizes UC16 "View Complaints" (R22)."""
        raise NotImplementedError

    def respondToComplaints(self) -> None:
        """Realizes UC17 "Respond To Complaints" (R23)."""
        raise NotImplementedError

    def viewComplaintSystem(self) -> None:
        """Realizes UC15 "View Complaint System" (R17)."""
        raise NotImplementedError


@_dc.dataclass
class Complaint:
    """Source: R17, R18, R19, R20, R21, R22, R23, R24, R25, R26"""
    status: _t.Optional[str] = None


@_dc.dataclass
class Notification:
    """Source: R6, R12, R26"""
    type: _t.Optional[str] = None


@_dc.dataclass
class Schedule:
    """Source: R7, R11, R12, R13, R14, R27, R28"""
    status: _t.Optional[str] = None


@_dc.dataclass
class Payment:
    """Source: R3, R4, R5, R15, R16"""
    paymentOption: _t.Optional[str] = None


@_dc.dataclass
class Contract:
    """Source: R28, R32, R33, R48"""
    status: _t.Optional[str] = None


@_dc.dataclass
class Message:
    """Source: R35, R36, R37"""
    type: _t.Optional[str] = None


@_dc.dataclass
class Application:
    """Source: R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49"""
    securityLevel: _t.Optional[str] = None
