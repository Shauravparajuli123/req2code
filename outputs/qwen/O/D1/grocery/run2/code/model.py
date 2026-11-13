from datetime import Date

class Employee:
    def __init__(self, certificate, group, qualification, status):
        self.certificate = certificate
        self.group = group
        self.qualification = qualification
        self.status = status
    def verifyWorkHour(self):
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
class OfficeEmployee:
    def __init__(self):
        pass
    def categorizeComplaint(self):
        raise NotImplementedError
    def prioritizeComplaint(self):
        raise NotImplementedError
    def respondComplaint(self):
        raise NotImplementedError
class Complaint:
    def __init__(self, status):
        self.status = status
class Notification:
    def __init__(self):
        pass
class SalaryStatement:
    def __init__(self):
        pass
    def sendSalaryStatement(self):
        raise NotImplementedError
class Schedule:
    def __init__(self, hours):
        self.hours = hours
    def viewSchedule(self):
        raise NotImplementedError
class WorkHour:
    def __init__(self, date):
        self.date = date
    def verifyWorkHour(self):
        raise NotImplementedError
class Contract:
    def __init__(self, dueDate):
        self.dueDate = dueDate
    def viewContract(self):
        raise NotImplementedError
class HiringProcess:
    def __init__(self, status):
        self.status = status
    def notifyHiringProcess(self):
        raise NotImplementedError
class Application:
    def __init__(self):
        pass
    def haveApplication(self):
        raise NotImplementedError
class System:
    def __init__(self):
        pass
    def haveSystem(self):
        raise NotImplementedError