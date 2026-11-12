# Artefact set D1_grocery_W

## Use cases
- Send SalaryStatement (actor: manager)
- Enable Option (actor: manager)
- Automate PaymentSystem (actor: manager)
- Outsource Part (actor: manager)
- Receive Notification (actor: employee)
- Express Hour (actor: employee)
- File Complaint (actor: employee)
- Hire Employee (actor: manager)
- Notify HiringProcess (actor: manager)
- Have Overview (actor: manager)
- Have Application (actor: employee)
- Have Ability (actor: manager)
- Notify Adjustment (actor: manager)
- Register Account (actor: applicant)
- Reset Password (actor: employee)
- Respond Complaint (actor: office_employee)
- Semi SchedulingProcess (actor: manager)
- Authorize Schedule (actor: manager)
- View Schedule (actor: employee)
- View Complaint (actor: office_employee)
- View Contract (actor: manager)
- Change Information (actor: employee)
- View Statement (actor: employee)
- View Certificate (actor: manager)
- Verify WorkHour (actor: employee)
- Use System (actor: employee)
- Navigate Application (actor: employee)
- Choose Email (actor: employee)
- Choose Payment (actor: employee)
- Share PaymentHandler (actor: employee)
- Receive SalaryStatement (actor: employee)
- Contact Employee (actor: manager)
- Contact Management (actor: employee)
- Forward Message (actor: manager)
- Have System (actor: manager)

## Class diagram
- Employee: attributes ['certificate', 'group', 'qualification', 'status']; methods ['expressHour', 'choosePayment', 'verifyWorkHour', 'viewSchedule', 'viewStatement', 'changeInformation']
- Manager: attributes []; methods ['enableOption', 'automatePaymentSystem', 'outsourcePart', 'hireEmployee', 'notifyHiringProcess', 'haveOverview', 'viewContract', 'viewCertificate', 'viewSchedule', 'viewComplaint', 'respondComplaint', 'contactEmployee', 'contactManagement', 'forwardMessage', 'haveSystem']
- OfficeEmployee: attributes []; methods ['categorizeComplaint', 'prioritizeComplaint', 'respondComplaint']
- Applicant: attributes []; methods ['registerAccount']
- Complaint: attributes ['status']; methods ['fileComplaint', 'respondComplaint']
- Contract: attributes []; methods ['viewContract']
- Schedule: attributes []; methods ['viewSchedule']
- Complaint: attributes ['status']; methods ['fileComplaint', 'respondComplaint']
- Notification: attributes []; methods ['receiveNotification']
- SalaryStatement: attributes []; methods ['viewStatement']
- WorkHour: attributes []; methods ['verifyWorkHour']
- Employee --association--> Contract
- Employee --association--> HiringProcess
- Employee --association--> Problem
- Employee --association--> SalaryStatement
- Employee --association--> WorkHour
- Employee --association--> Workplace
- Manager --association--> Employee
- Manager --association--> Complaint
- Manager --association--> Schedule
- Manager --association--> Complaint
- OfficeEmployee --association--> Complaint
- OfficeEmployee --association--> Complaint
- OfficeEmployee --association--> Complaint

## Python code
```python
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
```