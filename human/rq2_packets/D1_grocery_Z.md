# Artefact set D1_grocery_Z

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
- Employee: attributes ['preferredWorkingHours', 'certificate', 'status', 'group']; methods ['receiveSalaryStatement', 'receiveNotification', 'viewSchedule', 'viewStatement', 'viewContract', 'changeInformation', 'choosePayment', 'chooseEmail', 'viewComplaint', 'respondComplaint', 'viewInbox']
- Manager: attributes ['hiringProcess', 'schedulingProcess']; methods ['sendSalaryStatement', 'enableOption', 'semiSchedulingProcess', 'authorizeSchedule', 'viewSchedule', 'viewOverview', 'viewComplaint', 'prioritizeComplaint', 'notifyAdjustment', 'notifyHiringProcess', 'outsourcePart', 'viewContract', 'viewCertificate', 'viewComplaint', 'contactEmployee', 'contactManagement', 'forwardMessage', 'haveSystem']
- OfficeEmployee: attributes ['complaints']; methods ['categorizeComplaint', 'prioritizeComplaint', 'respondComplaint', 'viewComplaint']
- Complaint: attributes ['status']; methods []
- HiringProcess: attributes []; methods ['finishHiringProcess']
- SchedulingProcess: attributes []; methods ['semiSchedulingProcess', 'authorizeSchedule']
- Notification: attributes []; methods ['receiveNotification']
- SalaryStatement: attributes []; methods ['receiveSalaryStatement']
- Schedule: attributes []; methods ['viewSchedule']
- WorkHour: attributes []; methods ['verifyWorkHour']
- Employee --has--> WorkHour
- Employee --has--> SalaryStatement
- Employee --has--> Complaint
- Manager --has--> HiringProcess
- Manager --has--> SchedulingProcess
- Manager --has--> Notification
- Manager --has--> Complaint
- OfficeEmployee --has--> Complaint

## Python code
```python
from typing import TypedDict, List, Optional

class Employee(TypedDict):
    certificate: str
    qualification: str
    status: str
    work_hours: List[WorkHour]
    salary_statement: Optional[SalaryStatement]
    preferred_hours: List[Hour]
    notifications: List[Notification]

class Manager(TypedDict):
    employees: List[Employee]
    schedules: List[Schedule]
    complaints: List[Complaint]
    notifications: List[Notification]

class OfficeEmployee(TypedDict):
    notifications: List[Notification]
    complaints: List[Complaint]

class Applicant(TypedDict):
    account: Optional[Account]

class Account(TypedDict):
    username: str
    password: str

class Notification(TypedDict):
    message: str
    recipient: str
    timestamp: str

class Complaint(TypedDict):
    status: str
    category: str
    description: str

class Contract(TypedDict):
    due_date: str

class Schedule(TypedDict):
    date: str
    hours: List[Hour]

class Hour(TypedDict):
    start_time: str
    end_time: str

class SalaryStatement(TypedDict):
    amount: float
    date: str

class WorkHour(TypedDict):
    start_time: str
    end_time: str
    verified: bool

class Payment(TypedDict):
    amount: float
    date: str

class Problem(TypedDict):
    description: str
    status: str

class Operation(TypedDict):
    pass

class Track(TypedDict):
    pass

class Workplace(TypedDict):
    pass

class Operation:
    def __init__(self):
        pass

class Track:
    def __init__(self):
        pass

class Workplace:
    def __init__(self):
        pass

class Employee:
    def __init__(self, certificate: str, qualification: str, status: str, work_hours: List[WorkHour], salary_statement: Optional[SalaryStatement] = None, preferred_hours: List[Hour] = [], notifications: List[Notification] = []):
        self.certificate = certificate
        self.qualification = qualification
        self.status = status
        self.work_hours = work_hours
        self.salary_statement = salary_statement
        self.preferred_hours = preferred_hours
        self.notifications = notifications

class Manager:
    def __init__(self, employees: List[Employee], schedules: List[Schedule], complaints: List[Complaint], notifications: List[Notification] = []):
        self.employees = employees
        self.schedules = schedules
        self.complaints = complaints
        self.notifications = notifications

class OfficeEmployee:
    def __init__(self, notifications: List[Notification] = [], complaints: List[Complaint] = []):
        self.notifications = notifications
        self.complaints = complaints

class Applicant:
    def __init__(self, account: Optional[Account] = None):
        self.account = account

class Account:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class Notification:
    def __init__(self, message: str, recipient: str, timestamp: str):
        self.message = message
        self.recipient = recipient
        self.timestamp = timestamp

class Complaint:
    def __init__(self, status: str, category: str, description: str):
        self.status = status
        self.category = category
        self.description = description

class Contract:
    def __init__(self, due_date: str):
        self.due_date = due_date

class Schedule:
    def __init__(self, date: str, hours: List[Hour]):
        self.date = date
        self.hours = hours

class Hour:
    def __init__(self, start_time: str, end_time: str, verified: bool = False):
        self.start_time = start_time
        self.end_time = end_time
        self.verified = verified

class SalaryStatement:
    def __init__(self, amount: float, date: str):
        self.amount = amount
        self.date = date

class WorkHour:
    def __init__(self, start_time: str, end_time: str):
        self.start_time = start_time
        self.end_time = end_time

class Payment:
    def __init__(self, amount: float, date: str):
        self.amount = amount
        self.date = date

class Problem:
    def __init__(self, description: str, status: str):
        self.description = description
        self.status = status

class Operation:
    def __init__(self):
        pass

class Track:
    def __init__(self):
        pass

class Workplace:
    def __init__(self):
        pass

```