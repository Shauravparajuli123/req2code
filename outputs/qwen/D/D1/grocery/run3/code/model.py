"""Code skeleton generated from the shared model of D1/grocery.
Every class and method records the requirement(s) it traces to."""
from __future__ import annotations

import dataclasses as _dc
import enum as _enum
import typing as _t


@_dc.dataclass
class Employee:
    """Source: R1, R6, R7, R13, R15, R44, R45, R46, R47, R48, R49"""
    name: _t.Optional[str] = None
    workingHours: _t.Optional[str] = None
    personalInbox: _t.Optional[str] = None
    personalInformation: _t.Optional[str] = None
    contract: _t.Optional[str] = None
    dataSecurity: _t.Optional[bool] = None
    application: _t.Optional["Application"] = None

    def expressWorkingHours(self) -> None:
        """Realizes UC7 "Express Working Hours" (R7)."""
        raise NotImplementedError

    def viewPersonalInbox(self) -> None:
        """Realizes UC26 "View Personal Inbox" (R38)."""
        raise NotImplementedError

    def changePersonalInformation(self) -> None:
        """Realizes UC35 "Change Personal Information" (R47)."""
        raise NotImplementedError

    def viewContract(self) -> None:
        """Realizes UC36 "View Contract" (R48)."""
        raise NotImplementedError

    def viewFinancialStatements(self) -> None:
        """Realizes UC33 "View Financial Statements" (R45)."""
        raise NotImplementedError

    def ensureApplicationSecurity(self) -> None:
        """Realizes UC34 "Ensure Application Security" (R46)."""
        raise NotImplementedError


@_dc.dataclass
class Manager:
    """Source: R2, R3, R4, R5, R8, R9, R10, R11, R12, R14, R17, R18, R19, R20, R21, R22, R23, R24, R25, R27, R28, R29, R30, R32, R33, R39, R40, R41, R42"""
    name: _t.Optional[str] = None
    paymentOptions: _t.Optional[str] = None
    paymentSystem: _t.Optional[str] = None
    paymentProcess: _t.Optional[str] = None
    schedulingProcess: _t.Optional[str] = None
    schedule: _t.Optional[str] = None
    newEmployees: _t.Optional[str] = None
    employeeContracts: _t.Optional[str] = None
    employeeCertificates: _t.Optional[str] = None
    oneSystem: _t.Optional[str] = None
    application: _t.Optional["Application"] = None

    def sendSalaryStatements(self) -> None:
        """Realizes UC2 "Send Salary Statements" (R2, R18, R45)."""
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
        """Realizes UC12 "View Schedule" (R13)."""
        raise NotImplementedError

    def viewComplaints(self) -> None:
        """Realizes UC15 "View Complaints" (R21)."""
        raise NotImplementedError

    def respondToComplaints(self) -> None:
        """Realizes UC16 "Respond To Complaints" (R23)."""
        raise NotImplementedError

    def categorizeComplaints(self) -> None:
        """Realizes UC17 "Categorize Complaints" (R24)."""
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

    def messageOtherEmployees(self) -> None:
        """Realizes UC24 "Message Other Employees" (R36)."""
        raise NotImplementedError

    def forwardMessages(self) -> None:
        """Realizes UC25 "Forward Messages" (R37)."""
        raise NotImplementedError

    def resetPassword(self) -> None:
        """Realizes UC28 "Reset Password" (R40)."""
        raise NotImplementedError

    def useUserFriendlyApplication(self) -> None:
        """Realizes UC29 "Use User Friendly Application" (R41)."""
        raise NotImplementedError

    def navigateThroughApplication(self) -> None:
        """Realizes UC30 "Navigate Through Application" (R42)."""
        raise NotImplementedError

    def chooseNotifications(self) -> None:
        """Realizes UC31 "Choose Notifications" (R43)."""
        raise NotImplementedError

    def choosePaymentFrequency(self) -> None:
        """Realizes UC32 "Choose Payment Frequency" (R44)."""
        raise NotImplementedError


@_dc.dataclass
class OfficeEmployee:
    """Source: R17, R26, R23, R24, R25"""
    application: _t.Optional["Application"] = None

    def viewComplaints(self) -> None:
        """Realizes UC15 "View Complaints" (R21)."""
        raise NotImplementedError

    def respondToComplaints(self) -> None:
        """Realizes UC16 "Respond To Complaints" (R23)."""
        raise NotImplementedError

    def categorizeComplaints(self) -> None:
        """Realizes UC17 "Categorize Complaints" (R24)."""
        raise NotImplementedError

    def prioritizeComplaints(self) -> None:
        """Realizes UC18 "Prioritize Complaints" (R25)."""
        raise NotImplementedError

    def fileComplaint(self) -> None:
        """Realizes UC14 "File Complaint" (R19, R20)."""
        raise NotImplementedError


@_dc.dataclass
class Applicant:
    """Source: R31"""

    def registerAccount(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Complaint:
    """Source: R17, R18, R19, R20, R23, R24, R25"""
    title: _t.Optional[str] = None
    description: _t.Optional[str] = None
    status: _t.Optional[str] = None
    application: _t.Optional["Application"] = None

    def fileComplaint(self) -> None:
        """Realizes UC14 "File Complaint" (R19, R20)."""
        raise NotImplementedError

    def respondToComplaint(self) -> None:
        """Realizes UC16 "Respond To Complaints" (R23)."""
        raise NotImplementedError

    def categorizeComplaint(self) -> None:
        """Realizes UC17 "Categorize Complaints" (R24)."""
        raise NotImplementedError

    def prioritizeComplaint(self) -> None:
        """Realizes UC18 "Prioritize Complaints" (R25)."""
        raise NotImplementedError


@_dc.dataclass
class Notification:
    """Source: R6, R12, R26"""
    title: _t.Optional[str] = None
    description: _t.Optional[str] = None
    status: _t.Optional[str] = None
    application: _t.Optional["Application"] = None

    def receiveNotification(self) -> None:
        """Operation."""
        raise NotImplementedError

    def markAsRead(self) -> None:
        """Operation."""
        raise NotImplementedError


@_dc.dataclass
class Schedule:
    """Source: R7, R13, R14, R19, R20, R21, R22"""
    date: _t.Optional[str] = None
    status: _t.Optional[str] = None
    application: _t.Optional["Application"] = None

    def viewSchedule(self) -> None:
        """Realizes UC12 "View Schedule" (R13)."""
        raise NotImplementedError

    def editSchedule(self) -> None:
        """Realizes UC9 "Edit Schedule" (R9)."""
        raise NotImplementedError

    def authorizeSchedule(self) -> None:
        """Realizes UC10 "Authorize Schedule" (R10)."""
        raise NotImplementedError


@_dc.dataclass
class Contract:
    """Source: R29, R30, R32, R33"""
    startDate: _t.Optional[str] = None
    endDate: _t.Optional[str] = None
    status: _t.Optional[str] = None
    application: _t.Optional["Application"] = None

    def viewContract(self) -> None:
        """Realizes UC36 "View Contract" (R48)."""
        raise NotImplementedError

    def viewEmployeeContracts(self) -> None:
        """Realizes UC20 "View Employee Contracts" (R32)."""
        raise NotImplementedError

    def viewEmployeeCertificates(self) -> None:
        """Realizes UC21 "View Employee Certificates" (R33)."""
        raise NotImplementedError


@_dc.dataclass
class Message:
    """Source: R36, R37"""
    sender: _t.Optional[str] = None
    receiver: _t.Optional[str] = None
    content: _t.Optional[str] = None
    status: _t.Optional[str] = None
    application: _t.Optional["Application"] = None

    def sendMessage(self) -> None:
        """Realizes UC24 "Message Other Employees" (R36)."""
        raise NotImplementedError

    def forwardMessage(self) -> None:
        """Realizes UC25 "Forward Messages" (R37)."""
        raise NotImplementedError


@_dc.dataclass
class Application:
    """Source: R41, R42, R43, R44, R45, R46, R47, R48, R49"""
    userFriendly: _t.Optional[bool] = None
    navigation: _t.Optional[str] = None
    notifications: _t.Optional[str] = None
    paymentFrequency: _t.Optional[str] = None
    financialStatements: _t.Optional[str] = None
    dataSecurity: _t.Optional[bool] = None

    def useUserFriendlyApplication(self) -> None:
        """Realizes UC29 "Use User Friendly Application" (R41)."""
        raise NotImplementedError

    def navigateThroughApplication(self) -> None:
        """Realizes UC30 "Navigate Through Application" (R42)."""
        raise NotImplementedError

    def chooseNotifications(self) -> None:
        """Realizes UC31 "Choose Notifications" (R43)."""
        raise NotImplementedError

    def choosePaymentFrequency(self) -> None:
        """Realizes UC32 "Choose Payment Frequency" (R44)."""
        raise NotImplementedError

    def viewFinancialStatements(self) -> None:
        """Realizes UC33 "View Financial Statements" (R45)."""
        raise NotImplementedError

    def ensureApplicationSecurity(self) -> None:
        """Realizes UC34 "Ensure Application Security" (R46)."""
        raise NotImplementedError
