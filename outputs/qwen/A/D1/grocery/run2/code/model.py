"""Code skeleton generated from the shared model of D1/grocery.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Employee:
    """Source: R1, R6, R15, R16, R26, R38, R40, R41, R42, R43, R44, R45, R46, R47, R48, R49"""
    name: _t.Optional[str] = None
    preferredWorkingHours: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    contract: _t.Optional[str] = None
    paymentPreference: _t.Optional[str] = None
    financialStatements: _t.Optional[str] = None
    complaint: _t.Optional["Complaint"] = None

    def receiveSalaryStatement(self) -> None:
        """Realizes UC1 "Receive Salary Statement" (R1, R6, R26, R45)."""
        raise NotImplementedError

    def expressPreferredWorkingHours(self) -> None:
        """Realizes UC7 "Express Preferred Working Hours" (R7)."""
        raise NotImplementedError

    def viewPersonalInbox(self) -> None:
        """Realizes UC23 "View Personal Inbox" (R38)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC25 "Reset Password" (R40)."""
        raise NotImplementedError

    def viewFinancialStatements(self) -> None:
        """Realizes UC30 "View Financial Statements" (R45)."""
        raise NotImplementedError

    def ensurePrivacy(self) -> None:
        """Realizes UC31 "Ensure Privacy" (R46)."""
        raise NotImplementedError

    def updatePersonalInformation(self) -> None:
        """Realizes UC32 "Update Personal Information" (R47)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC33 "View Contract" (R48)."""
        raise NotImplementedError

    def ensureSecurity(self) -> None:
        """Realizes UC34 "Ensure Security" (R49)."""
        raise NotImplementedError


@_dc.dataclass
class Manager:
    """Source: R2, R3, R4, R5, R8, R9, R10, R11, R12, R13, R14, R17, R18, R19, R20, R21, R22, R23, R24, R25, R27, R28, R29, R30, R39, R49"""
    name: _t.Optional[str] = None
    employeeOverview: _t.Optional[str] = None
    complaints: _t.Optional[str] = None
    employees: _t.List["Employee"] = _dc.field(default_factory=list)

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

    def semiAutomateSchedulingProcess(self) -> None:
        """Realizes UC8 "Semi Automate Scheduling Process" (R8)."""
        raise NotImplementedError

    def manuallyEditSchedule(self) -> None:
        """Realizes UC9 "Manually Edit Schedule" (R9)."""
        raise NotImplementedError

    def manuallyAuthorizeSchedule(self) -> None:
        """Realizes UC10 "Manually Authorize Schedule" (R10)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC12 "View Schedule" (R13, R14)."""
        raise NotImplementedError

    def viewEmployeeOverview(self) -> None:
        """Realizes UC16 "View Employee Overview" (R29, R30)."""
        raise NotImplementedError

    def viewEmployeeContracts(self) -> None:
        """Realizes UC17 "View Employee Contracts" (R32)."""
        raise NotImplementedError

    def viewEmployeeCertificates(self) -> None:
        """Realizes UC18 "View Employee Certificates" (R33)."""
        raise NotImplementedError

    def contactManagement(self) -> None:
        """Realizes UC19 "Contact Management" (R34)."""
        raise NotImplementedError

    def contactEmployee(self) -> None:
        """Realizes UC20 "Contact Employee" (R35)."""
        raise NotImplementedError

    def messageOtherEmployees(self) -> None:
        """Realizes UC21 "Message Other Employees" (R36)."""
        raise NotImplementedError

    def forwardMessages(self) -> None:
        """Realizes UC22 "Forward Messages" (R37)."""
        raise NotImplementedError

    def viewPersonalInbox(self) -> None:
        """Realizes UC23 "View Personal Inbox" (R38)."""
        raise NotImplementedError

    def singleLogin(self) -> None:
        """Realizes UC24 "Single Login" (R39)."""
        raise NotImplementedError


@_dc.dataclass
class Complaint:
    """Source: R17, R18, R19, R20, R21, R22, R23, R24, R25"""
    title: _t.Optional[str] = None
    category: _t.Optional[str] = None
    status: _t.Optional[str] = None

    def fileComplaint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def respondToUnsolvedComplaints(self) -> None:
        """Operation."""
        raise NotImplementedError

    def prioritizeComplaints(self) -> None:
        """Operation."""
        raise NotImplementedError
