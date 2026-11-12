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
    email: _t.Optional[str] = None
    preferredWorkingHours: _t.Optional[str] = None
    contract: _t.Optional[str] = None
    certificates: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    paymentFrequency: _t.Optional[str] = None
    complaint: _t.Optional["Complaint"] = None
    application: _t.Optional["Application"] = None

    def receiveSalaryStatement(self) -> None:
        """Realizes UC1 "Receive Salary Statement" (R1, R6, R26, R45)."""
        raise NotImplementedError

    def receiveNotification(self) -> None:
        """Realizes UC6 "Receive Notification For Payment" (R6, R46)."""
        raise NotImplementedError

    def expressPreferredWorkingHours(self) -> None:
        """Realizes UC7 "Express Preferred Working Hours" (R7, R15)."""
        raise NotImplementedError

    def viewFinancialStatements(self) -> None:
        """Realizes UC30 "View Financial Statements" (R45)."""
        raise NotImplementedError

    def updatePersonalInformation(self) -> None:
        """Realizes UC32 "Update Personal Information" (R47)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC33 "View Contract" (R48)."""
        raise NotImplementedError

    def viewPersonalInbox(self) -> None:
        """Realizes UC23 "View Personal Inbox" (R38)."""
        raise NotImplementedError

    def chooseNotifications(self) -> None:
        """Realizes UC28 "Choose Notifications" (R43)."""
        raise NotImplementedError

    def choosePaymentFrequency(self) -> None:
        """Realizes UC29 "Choose Payment Frequency" (R44)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC13 "View Schedule" (R13, R14)."""
        raise NotImplementedError


@_dc.dataclass
class Manager:
    """Source: R2, R3, R4, R5, R8, R9, R10, R11, R12, R13, R14, R18, R19, R20, R21, R22, R23, R24, R25, R27, R28, R29, R30, R39, R49"""
    name: _t.Optional[str] = None
    password: _t.Optional[str] = None
    employees: _t.List["Employee"] = _dc.field(default_factory=list)
    complaints: _t.List["Complaint"] = _dc.field(default_factory=list)
    application: _t.Optional["Application"] = None

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

    def beNotifiedOfManualAdjustments(self) -> None:
        """Realizes UC11 "Be Notified Of Manual Adjustments" (R11)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC13 "View Schedule" (R13, R14)."""
        raise NotImplementedError

    def viewEmployeeOverview(self) -> None:
        """Realizes UC17 "View Employee Overview" (R29, R30)."""
        raise NotImplementedError

    def viewEmployeeContracts(self) -> None:
        """Realizes UC18 "View Employee Contracts" (R32)."""
        raise NotImplementedError

    def viewEmployeeCertificates(self) -> None:
        """Realizes UC19 "View Employee Certificates" (R33)."""
        raise NotImplementedError

    def contactManagement(self) -> None:
        """Realizes UC20 "Contact Management" (R34)."""
        raise NotImplementedError

    def contactEmployee(self) -> None:
        """Realizes UC21 "Contact Employee" (R35)."""
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
    """Source: R17, R18, R19, R20, R21, R22, R23, R24, R25, R26"""
    title: _t.Optional[str] = None
    description: _t.Optional[str] = None
    status: _t.Optional[str] = None
    priority: _t.Optional[str] = None

    def fileComplaint(self) -> None:
        """Operation."""
        raise NotImplementedError

    def respondToUnsolvedComplaints(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewComplaints(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Application:
    """Source: R17, R18, R19, R20, R21, R22, R23, R24, R25, R26, R31, R39, R41, R42, R43, R44, R45, R46, R49"""
    name: _t.Optional[str] = None
    login: _t.Optional[str] = None

    def registerAccount(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewComplaints(self) -> None:
        """Operation."""
        raise NotImplementedError

    def viewPersonalInbox(self) -> None:
        """Realizes UC23 "View Personal Inbox" (R38)."""
        raise NotImplementedError

    def chooseNotifications(self) -> None:
        """Realizes UC28 "Choose Notifications" (R43)."""
        raise NotImplementedError

    def choosePaymentFrequency(self) -> None:
        """Realizes UC29 "Choose Payment Frequency" (R44)."""
        raise NotImplementedError

    def viewFinancialStatements(self) -> None:
        """Realizes UC30 "View Financial Statements" (R45)."""
        raise NotImplementedError

    def viewSchedule(self) -> None:
        """Realizes UC13 "View Schedule" (R13, R14)."""
        raise NotImplementedError
