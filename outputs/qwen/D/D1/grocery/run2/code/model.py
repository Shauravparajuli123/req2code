"""Code skeleton generated from the shared model of D1/grocery.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Employee:
    """Source: R1, R6, R7, R15, R26, R38, R40, R43, R44, R45, R46, R47, R48, R49"""
    name: _t.Optional[str] = None
    workingHours: _t.Optional[str] = None
    financialStatements: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    contract: _t.Optional[str] = None

    def expressWorkingHours(self) -> None:
        """Realizes UC7 "Express Working Hours" (R7)."""
        raise NotImplementedError

    def viewFinancialStatements(self) -> None:
        """Realizes UC32 "View Financial Statements" (R45)."""
        raise NotImplementedError

    def changePersonalInformation(self) -> None:
        """Realizes UC34 "Change Personal Information" (R47)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC35 "View Contract" (R48)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC27 "Reset Password" (R40)."""
        raise NotImplementedError

    def chooseNotifications(self) -> None:
        """Realizes UC30 "Choose Notifications" (R43)."""
        raise NotImplementedError

    def choosePaymentFrequency(self) -> None:
        """Realizes UC31 "Choose Payment Frequency" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class Manager:
    """Source: R2, R3, R4, R5, R8, R9, R10, R11, R12, R13, R14, R18, R19, R20, R21, R22, R23, R24, R25, R27, R28, R29, R30, R32, R33, R39, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49"""
    name: _t.Optional[str] = None
    paymentOptions: _t.Optional[str] = None
    paymentSystem: _t.Optional[str] = None
    paymentProcess: _t.Optional[str] = None
    scheduling: _t.Optional[str] = None
    hiringProcess: _t.Optional[str] = None
    employeeContracts: _t.Optional[str] = None
    employees: _t.List["Employee"] = _dc.field(default_factory=list)
    officeEmployees: _t.List["OfficeEmployee"] = _dc.field(default_factory=list)
    applicants: _t.List["Applicant"] = _dc.field(default_factory=list)

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
        """Realizes UC15 "View Complaints" (R22, R29)."""
        raise NotImplementedError

    def respondToComplaints(self) -> None:
        """Realizes UC16 "Respond To Complaints" (R23)."""
        raise NotImplementedError

    def prioritizeComplaints(self) -> None:
        """Realizes UC17 "Prioritize Complaints" (R25)."""
        raise NotImplementedError

    def viewEmployeeContracts(self) -> None:
        """Realizes UC19 "View Employee Contracts" (R32)."""
        raise NotImplementedError

    def viewEmployeeCertificates(self) -> None:
        """Realizes UC20 "View Employee Certificates" (R33)."""
        raise NotImplementedError

    def haveOneLogin(self) -> None:
        """Realizes UC26 "Have One Login" (R39)."""
        raise NotImplementedError

    def viewPersonalInbox(self) -> None:
        """Realizes UC25 "View Personal Inbox" (R38)."""
        raise NotImplementedError


@_dc.dataclass
class OfficeEmployee:
    """Source: R17, R23, R24, R25, R26"""

    def fileComplaint(self) -> None:
        """Realizes UC14 "File Complaint" (R18, R26)."""
        raise NotImplementedError

    def respondToComplaints(self) -> None:
        """Realizes UC16 "Respond To Complaints" (R23)."""
        raise NotImplementedError

    def prioritizeComplaints(self) -> None:
        """Realizes UC17 "Prioritize Complaints" (R25)."""
        raise NotImplementedError


@_dc.dataclass
class Applicant:
    """Source: R31"""

    def registerAccount(self) -> None:
        """Operation."""
        raise NotImplementedError
