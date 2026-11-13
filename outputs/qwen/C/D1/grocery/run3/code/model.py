"""Code skeleton generated from the shared model of D1/grocery.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Employee:
    """Source: R1, R6, R7, R13, R15, R47, R48, R40, R41, R42, R43, R44, R45, R49"""
    name: _t.Optional[str] = None
    certificate: _t.Optional[str] = None
    status: _t.Optional[str] = None
    group: _t.Optional[str] = None
    qualification: _t.Optional[str] = None
    preferredWorkingHours: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    contract: _t.Optional[str] = None

    def expressWorkingHours(self) -> None:
        """Realizes UC7 "Express Working Hours" (R7)."""
        raise NotImplementedError

    def viewPersonalInbox(self) -> None:
        """Realizes UC29 "View Personal Inbox" (R38)."""
        raise NotImplementedError

    def changeInformation(self) -> None:
        """Realizes UC30 "Change Information" (R47)."""
        raise NotImplementedError

    def viewFinancialAnnualStatements(self) -> None:
        """Realizes UC31 "View Financial Annual Statements" (R45)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC33 "View Contract" (R32, R48)."""
        raise NotImplementedError

    def chooseEmail(self) -> None:
        """Realizes UC27 "Choose Email" (R43)."""
        raise NotImplementedError

    def choosePayment(self) -> None:
        """Realizes UC28 "Choose Payment" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class Manager:
    """Source: R2, R3, R4, R5, R8, R9, R10, R11, R17, R19, R20, R21, R22, R23, R24, R25, R27, R28, R29, R30, R32, R33, R34, R35, R36, R39"""
    name: _t.Optional[str] = None
    hiringProcess: _t.Optional[str] = None
    employeeOverview: _t.Optional[str] = None

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

    def hireEmployee(self) -> None:
        """Realizes UC15 "Hire Employee" (R27)."""
        raise NotImplementedError

    def notifyHiringProcess(self) -> None:
        """Realizes UC16 "Notify Hiring Process" (R28)."""
        raise NotImplementedError

    def haveOverviewOfEmployees(self) -> None:
        """Realizes UC17 "Have Overview Of Employees" (R29)."""
        raise NotImplementedError

    def haveOverviewOfAbsentEmployees(self) -> None:
        """Realizes UC18 "Have Overview Of Absent Employees" (R30)."""
        raise NotImplementedError

    def viewEmployeeContracts(self) -> None:
        """Realizes UC19 "View Employee Contracts" (R32)."""
        raise NotImplementedError

    def viewEmployeeCertificates(self) -> None:
        """Realizes UC20 "View Employee Certificates" (R33)."""
        raise NotImplementedError

    def contactManagement(self) -> None:
        """Realizes UC21 "Contact Management" (R34)."""
        raise NotImplementedError

    def contactEmployee(self) -> None:
        """Realizes UC22 "Contact Employee" (R35)."""
        raise NotImplementedError

    def forwardMessage(self) -> None:
        """Realizes UC23 "Forward Message" (R37)."""
        raise NotImplementedError


@_dc.dataclass
class OfficeEmployee:
    """Source: R17, R18, R19, R21, R22, R23, R24, R25"""

    def fileComplaint(self) -> None:
        """Realizes UC11 "File Complaint" (R18)."""
        raise NotImplementedError

    def viewComplaint(self) -> None:
        """Realizes UC12 "View Complaint" (R21)."""
        raise NotImplementedError

    def categorizeComplaint(self) -> None:
        """Realizes UC13 "Categorize Complaint" (R24)."""
        raise NotImplementedError

    def prioritizeComplaint(self) -> None:
        """Realizes UC14 "Prioritize Complaint" (R25)."""
        raise NotImplementedError


@_dc.dataclass
class Complaint:
    """Source: R17, R18, R19, R21, R22, R23, R24, R25"""
    status: _t.Optional[str] = None


@_dc.dataclass
class SalaryStatement:
    """Source: R1, R2"""
    pass


@_dc.dataclass
class Notification:
    """Source: R6, R11, R12, R26"""
    pass


@_dc.dataclass
class Schedule:
    """Source: R8, R9, R10, R12, R14"""
    pass


@_dc.dataclass
class HiringProcess:
    """Source: R27, R28"""
    pass
