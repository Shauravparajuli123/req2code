# Artefact set D1_grocery_X

## Use cases
- Receive SalaryStatement (actor: employee)
- Send SalaryStatement (actor: manager)
- Enable Option (actor: manager)
- Automate PaymentSystem (actor: manager)
- Outsource Part (actor: manager)
- Receive Notification (actor: employee)
- ExpressHour (actor: employee)
- SemiSchedulingProcess (actor: manager)
- Have Ability (actor: manager)
- Authorize Schedule (actor: manager)
- Notify Adjustment (actor: manager)
- File Complaint (actor: employee)
- View Complaint (actor: office employee)
- Categorize Complaint (actor: office employee)
- Prioritize Complaint (actor: office employee)
- Notify HiringProcess (actor: manager)
- Have Overview (actor: manager)
- Register Account (actor: applicant)
- Have Application (actor: employee)
- Navigate Application (actor: employee)
- Choose Email (actor: employee)
- Choose Payment (actor: employee)
- Have System (actor: manager)
- Hire Employee (actor: manager)
- Contact Employee (actor: manager)
- Contact Management (actor: employee)
- Forward Message (actor: manager)
- Respond Complaint (actor: office employee)
- Change Information (actor: employee)
- View Contract (actor: manager)
- View Schedule (actor: employee)
- View Statement (actor: employee)
- Share PaymentHandler (actor: employee)
- Use System (actor: employee)
- Verify WorkHour (actor: employee)

## Class diagram
- Employee: attributes ['name', 'email', 'certificate', 'qualification', 'status']; methods ['receiveSalaryStatement', 'expressHour', 'viewSchedule', 'viewStatement', 'verifyWorkHour', 'changeInformation', 'sharePaymentHandler', 'useSystem']
- Manager: attributes ['name', 'email']; methods ['sendSalaryStatement', 'enableOption', 'automatePaymentSystem', 'outsourcePart', 'notifyAdjustment', 'hireEmployee', 'contactEmployee', 'contactManagement', 'forwardMessage', 'haveOverview']
- OfficeEmployee: attributes ['name', 'email']; methods ['receiveNotification', 'viewComplaint', 'respondComplaint', 'categorizeComplaint', 'prioritizeComplaint']
- Complaint: attributes ['status']; methods []
- SalaryStatement: attributes ['amount']; methods []
- Schedule: attributes ['hours']; methods ['semiSchedulingProcess', 'authorizeSchedule']
- Hour: attributes ['date', 'duration']; methods []
- Notification: attributes ['message']; methods []
- Application: attributes []; methods ['navigateApplication', 'chooseEmail', 'choosePayment']
- Account: attributes []; methods ['registerAccount', 'resetPassword']
- Contract: attributes ['start_date', 'end_date']; methods ['viewContract']
- HiringProcess: attributes []; methods ['notifyHiringProcess']
- Employee --has--> Contract
- Employee --has--> HiringProcess

## Python code
```python
from typing import List, Date, Double, String, Integer

class Employee:
    def __init__(self, name: String, email: String, certificate: String, qualification: String, status: String):
        self.name = name
        self.email = email
        self.certificate = certificate
        self.qualification = qualification
        self.status = status

    def receiveSalaryStatement(self) -> SalaryStatement:
        raise NotImplementedError

    def expressHour(self) -> Hour:
        raise NotImplementedError

    def viewSchedule(self) -> Schedule:
        raise NotImplementedError

    def viewStatement(self) -> String:
        raise NotImplementedError

    def verifyWorkHour(self) -> Boolean:
        raise NotImplementedError

    def changeInformation(self) -> String:
        raise NotImplementedError

    def sharePaymentHandler(self) -> String:
        raise NotImplementedError

    def useSystem(self) -> String:
        raise NotImplementedError

class Manager:
    def __init__(self, name: String, email: String):
        self.name = name
        self.email = email

    def sendSalaryStatement(self, employee: Employee) -> SalaryStatement:
        raise NotImplementedError

    def enableOption(self, option: String) -> Boolean:
        raise NotImplementedError

    def automatePaymentSystem(self) -> Boolean:
        raise NotImplementedError

    def outsourcePart(self) -> Boolean:
        raise NotImplementedError

    def notifyAdjustment(self) -> Boolean:
        raise NotImplementedError

    def hireEmployee(self, employee: Employee) -> Boolean:
        raise NotImplementedError

    def contactEmployee(self, employee: Employee) -> String:
        raise NotImplementedError

    def contactManagement(self) -> String:
        raise NotImplementedError

    def forwardMessage(self, message: String) -> Boolean:
        raise NotImplementedError

    def haveOverview(self) -> Boolean:
        raise NotImplementedError

class OfficeEmployee:
    def __init__(self, name: String, email: String):
        self.name = name
        self.email = email

    def receiveNotification(self, notification: Notification) -> Boolean:
        raise NotImplementedError

    def viewComplaint(self, complaint: Complaint) -> String:
        raise NotImplementedError

    def respondComplaint(self, complaint: Complaint) -> Boolean:
        raise NotImplementedError

    def categorizeComplaint(self, complaint: Complaint) -> String:
        raise NotImplementedError

    def prioritizeComplaint(self, complaint: Complaint) -> Boolean:
        raise NotImplementedError

class Complaint:
    def __init__(self, status: String):
        self.status = status

    def __str__(self) -> String:
        return self.status

class SalaryStatement:
    def __init__(self, amount: Double):
        self.amount = amount

    def __str__(self) -> String:
        return str(self.amount)

class Schedule:
    def __init__(self, hours: List[Hour]):
        self.hours = hours

    def semiSchedulingProcess(self) -> Boolean:
        raise NotImplementedError

    def authorizeSchedule(self) -> Boolean:
        raise NotImplementedError

class Hour:
    def __init__(self, date: Date, duration: Integer):
        self.date = date
        self.duration = duration

    def __str__(self) -> String:
        return f'Date: {self.date}, Duration: {self.duration} hours'

class Notification:
    def __init__(self, message: String):
        self.message = message

    def __str__(self) -> String:
        return self.message

class Application:
    def __init__(self):
        pass

    def navigateApplication(self) -> String:
        raise NotImplementedError

    def chooseEmail(self) -> Boolean:
        raise NotImplementedError

    def choosePayment(self) -> Boolean:
        raise NotImplementedError

class Account:
    def __init__(self):
        pass

    def registerAccount(self) -> Boolean:
        raise NotImplementedError

    def resetPassword(self) -> Boolean:
        raise NotImplementedError

class Contract:
    def __init__(self, start_date: Date, end_date: Date):
        self.start_date = start_date
        self.end_date = end_date

    def viewContract(self) -> String:
        raise NotImplementedError

class HiringProcess:
    def __init__(self):
        pass

    def notifyHiringProcess(self) -> Boolean:
        raise NotImplementedError
```