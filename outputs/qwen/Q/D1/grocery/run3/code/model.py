from typing import Double, String, Date, Application, Account, WorkHour, SalaryStatement, Notification, Schedule, Complaint, OfficeEmployee, Manager, Employee

class WorkHour:
    def __init__(self, hours: Double):
        self.hours = hours
    def verifyWorkHour(self) -> None:
        raise NotImplementedError

class Employee:
    def __init__(self, name: String, email: String, certificate: String, status: String, workHour: WorkHour):
        self.name = name
        self.email = email
        self.certificate = certificate
        self.status = status
        self.workHour = workHour
    def expressHour(self) -> None:
        raise NotImplementedError
    def verifyWorkHour(self) -> None:
        raise NotImplementedError
    def viewSchedule(self) -> None:
        raise NotImplementedError
    def viewStatement(self) -> None:
        raise NotImplementedError
    def changeInformation(self) -> None:
        raise NotImplementedError
    def resetPassword(self) -> None:
        raise NotImplementedError
    def choosePayment(self) -> None:
        raise NotImplementedError
    def chooseEmail(self) -> None:
        raise NotImplementedError
    def sharePaymentHandler(self) -> None:
        raise NotImplementedError
    def useSystem(self) -> None:
        raise NotImplementedError

class Manager:
    def __init__(self, name: String, email: String):
        self.name = name
        self.email = email
    def sendSalaryStatement(self, salaryStatement: SalaryStatement) -> None:
        raise NotImplementedError
    def enableOption(self) -> None:
        raise NotImplementedError
    def automatePaymentSystem(self) -> None:
        raise NotImplementedError
    def outsourcePart(self) -> None:
        raise NotImplementedError
    def notifyAdjustment(self) -> None:
        raise NotImplementedError
    def hireEmployee(self) -> None:
        raise NotImplementedError
    def viewSchedule(self) -> None:
        raise NotImplementedError
    def viewContract(self) -> None:
        raise NotImplementedError
    def viewCertificate(self) -> None:
        raise NotImplementedError
    def haveOverview(self) -> None:
        raise NotImplementedError
    def haveSystem(self) -> None:
        raise NotImplementedError

class OfficeEmployee:
    def __init__(self, name: String, email: String):
        self.name = name
        self.email = email
    def categorizeComplaint(self) -> None:
        raise NotImplementedError
    def prioritizeComplaint(self) -> None:
        raise NotImplementedError
    def respondComplaint(self) -> None:
        raise NotImplementedError
    def viewComplaint(self) -> None:
        raise NotImplementedError

class Complaint:
    def __init__(self, status: String):
        self.status = status
    def fileComplaint(self) -> None:
        raise NotImplementedError

class SalaryStatement:
    def __init__(self, amount: Double):
        self.amount = amount
    def receiveSalaryStatement(self) -> None:
        raise NotImplementedError

class Notification:
    def __init__(self, message: String):
        self.message = message
    def receiveNotification(self) -> None:
        raise NotImplementedError
    def notifyHiringProcess(self) -> None:
        raise NotImplementedError
    def notifyAdjustment(self) -> None:
        raise NotImplementedError
    def notifyComplaint(self) -> None:
        raise NotImplementedError

class Schedule:
    def __init__(self, date: Date):
        self.date = date
    def semiSchedulingProcess(self) -> None:
        raise NotImplementedError
    def authorizeSchedule(self) -> None:
        raise NotImplementedError

class Application:
    def __init__(self, name: String):
        self.name = name
    def haveApplication(self) -> None:
        raise NotImplementedError

class Account:
    def __init__(self, username: String, password: String):
        self.username = username
        self.password = password
    def registerAccount(self) -> None:
        raise NotImplementedError