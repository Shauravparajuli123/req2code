from enum import Enum

class Employee:
    def __init__(self, certificate, group, qualification, status):
        self.certificate = certificate
        self.group = group
        self.qualification = qualification
        self.status = status
    def expressHour(self):
        raise NotImplementedError
    def choosePayment(self):
        raise NotImplementedError
    def verifyWorkHour(self):
        raise NotImplementedError
    def viewSchedule(self):
        raise NotImplementedError
    def viewStatement(self):
        raise NotImplementedError
    def changeInformation(self):
        raise NotImplementedError

class Manager:
    def __init__(self):
        pass
    def enableOption(self):
        raise NotImplementedError
    def automatePaymentSystem(self):
        raise NotImplementedError
    def outsourcePart(self):
        raise NotImplementedError
    def hireEmployee(self):
        raise NotImplementedError
    def notifyHiringProcess(self):
        raise NotImplementedError
    def haveOverview(self):
        raise NotImplementedError
    def viewContract(self):
        raise NotImplementedError
    def viewCertificate(self):
        raise NotImplementedError
    def viewSchedule(self):
        raise NotImplementedError
    def viewComplaint(self):
        raise NotImplementedError
    def respondComplaint(self):
        raise NotImplementedError
    def contactEmployee(self):
        raise NotImplementedError
    def contactManagement(self):
        raise NotImplementedError
    def forwardMessage(self):
        raise NotImplementedError
    def haveSystem(self):
        raise NotImplementedError

class OfficeEmployee:
    def __init__(self):
        pass
    def categorizeComplaint(self):
        raise NotImplementedError
    def prioritizeComplaint(self):
        raise NotImplementedError
    def respondComplaint(self):
        raise NotImplementedError

class Applicant:
    def __init__(self):
        pass
    def registerAccount(self):
        raise NotImplementedError

class Complaint:
    def __init__(self, status):
        self.status = status
    def fileComplaint(self):
        raise NotImplementedError
    def respondComplaint(self):
        raise NotImplementedError

class Contract:
    def __init__(self):
        pass
    def viewContract(self):
        raise NotImplementedError

class Schedule:
    def __init__(self):
        pass
    def viewSchedule(self):
        raise NotImplementedError

class Notification:
    def __init__(self):
        pass
    def receiveNotification(self):
        raise NotImplementedError

class SalaryStatement:
    def __init__(self):
        pass
    def viewStatement(self):
        raise NotImplementedError

class WorkHour:
    def __init__(self):
        pass
    def verifyWorkHour(self):
        raise NotImplementedError