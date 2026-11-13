"""Code skeleton generated from the shared model of D1/grocery.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Employee:
    """Source: R1, R6, R7, R13, R15, R47, R48"""
    name: _t.Optional[str] = None
    certificate: _t.Optional[str] = None
    status: _t.Optional[str] = None
    group: _t.Optional[str] = None
    qualification: _t.Optional[str] = None
    salaryStatement: _t.Optional["SalaryStatement"] = None
    notifications: _t.List["Notification"] = _dc.field(default_factory=list)
    schedule: _t.Optional["Schedule"] = None
    complaints: _t.List["Complaint"] = _dc.field(default_factory=list)

    def expressWorkingHours(self) -> None:
        """Realizes UC7 "Express Working Hours" (R7)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC12 "View Schedule" (R13, R14)."""
        raise NotImplementedError

    def changeInformation(self) -> None:
        """Realizes UC34 "Change Information" (R47)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC35 "View Contract" (R32)."""
        raise NotImplementedError


@_dc.dataclass
class Manager:
    """Source: R2, R3, R4, R5, R8, R9, R10, R11, R12, R14, R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R39"""
    salaryStatements: _t.List["SalaryStatement"] = _dc.field(default_factory=list)
    notifications: _t.List["Notification"] = _dc.field(default_factory=list)
    schedules: _t.List["Schedule"] = _dc.field(default_factory=list)
    complaints: _t.List["Complaint"] = _dc.field(default_factory=list)
    employees: _t.List["Employee"] = _dc.field(default_factory=list)

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

    def receiveNewScheduleNotification(self) -> None:
        """Realizes UC11 "Receive New Schedule Notification" (R12)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC12 "View Schedule" (R13, R14)."""
        raise NotImplementedError

    def viewEmployeeContracts(self) -> None:
        """Realizes UC23 "View Employee Contracts" (R32)."""
        raise NotImplementedError

    def viewEmployeeCertificates(self) -> None:
        """Realizes UC24 "View Employee Certificates" (R33)."""
        raise NotImplementedError

    def hireEmployee(self) -> None:
        """Realizes UC19 "Hire Employee" (R27)."""
        raise NotImplementedError

    def notifyHiringProcess(self) -> None:
        """Realizes UC20 "Notify Hiring Process" (R28)."""
        raise NotImplementedError

    def haveOverviewOfEmployees(self) -> None:
        """Realizes UC21 "Have Overview Of Employees" (R29)."""
        raise NotImplementedError

    def haveOverviewOfAbsentEmployees(self) -> None:
        """Realizes UC22 "Have Overview Of Absent Employees" (R30)."""
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
class Applicant:
    """Source: R31"""

    def registerAccount(self) -> None:
        """Realizes UC39 "Register Account" (R31)."""
        raise NotImplementedError


@_dc.dataclass
class Complaint:
    """Source: R17, R18, R19, R20, R21, R22, R23, R24, R25, R26"""
    status: _t.Optional[str] = None


@_dc.dataclass
class SalaryStatement:
    """Source: R1, R2"""
    pass


@_dc.dataclass
class Schedule:
    """Source: R7, R12, R13, R14, R27, R28"""

    def semiSchedulingProcess(self) -> None:
        """Realizes UC8 "Semi Scheduling Process" (R8)."""
        raise NotImplementedError

    def manuallyEditSchedule(self) -> None:
        """Realizes UC9 "Manually Edit Schedule" (R9)."""
        raise NotImplementedError

    def notifyAdjustment(self) -> None:
        """Realizes UC10 "Notify Adjustment" (R11)."""
        raise NotImplementedError

    def receiveNewScheduleNotification(self) -> None:
        """Realizes UC11 "Receive New Schedule Notification" (R12)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC12 "View Schedule" (R13, R14)."""
        raise NotImplementedError


@_dc.dataclass
class Notification:
    """Source: R6, R11, R12, R26"""
    pass


@_dc.dataclass
class OfficeEmployee:
    """Source: R17, R21, R22"""
    complaints: _t.List["Complaint"] = _dc.field(default_factory=list)

    def respondComplaint(self) -> None:
        """Realizes UC16 "Respond Complaint" (R23)."""
        raise NotImplementedError

    def categorizeComplaint(self) -> None:
        """Realizes UC17 "Categorize Complaint" (R24)."""
        raise NotImplementedError

    def prioritizeComplaint(self) -> None:
        """Realizes UC18 "Prioritize Complaint" (R25)."""
        raise NotImplementedError
