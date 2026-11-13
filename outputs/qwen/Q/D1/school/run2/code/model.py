from enum import Enum

class BehaviorStatus(Enum):
    Sufficient = 'Sufficient'
    Insufficient = 'Insufficient'

class Date:
    pass

class Student:
    def __init__(self, contactInformation: str, group: str, knowledge: str):
        self.contactInformation = contactInformation
        self.group = group
        self.knowledge = knowledge

def directMessage(self, recipient: str):
    raise NotImplementedError

def directMessageMentor(self):
    raise NotImplementedError

def fillAbsence(self):
    raise NotImplementedError

def receiveNotification(self, message: str):
    raise NotImplementedError

def viewInformation(self):
    raise NotImplementedError

def viewContactInformation(self):
    raise NotImplementedError

def handHomework(self):
    raise NotImplementedError

class Teacher:
    def __init__(self, contactInformation: str, group: str, knowledge: str):
        self.contactInformation = contactInformation
        self.group = group
        self.knowledge = knowledge

def directMessageStudent(self, student: str):
    raise NotImplementedError

def directMessageMentor(self):
    raise NotImplementedError

def assignDlm(self, dlm: 'Dlm', class_or_student: str):
    raise NotImplementedError

def assignDate(self, dlm: 'Dlm', dueDate: Date):
    raise NotImplementedError

def makeSubmissionElement(self):
    raise NotImplementedError

def editPage(self, page: 'Page', content: str):
    raise NotImplementedError

def receiveConfirmation(self, file: 'File', uploadDate: Date):
    raise NotImplementedError

def receiveNotification(self, message: str):
    raise NotImplementedError

def recordAction(self, status: BehaviorStatus):
    raise NotImplementedError

def recordAttendance(self, date: Date):
    raise NotImplementedError

def recordBehavior(self, status: BehaviorStatus):
    raise NotImplementedError

def recordGrade(self, value: int):
    raise NotImplementedError

def seeAnswer(self, submission: str):
    raise NotImplementedError

def seeGrade(self, student: str):
    raise NotImplementedError

def seeProgress(self, student: str):
    raise NotImplementedError

def setAppearanceDate(self, dlm: 'Dlm', appearanceDate: Date):
    raise NotImplementedError

def setDate(self, date: Date):
    raise NotImplementedError

def uploadFile(self, file: 'File', uploadDate: Date):
    raise NotImplementedError

def viewAttendance(self, date: Date):
    raise NotImplementedError

def viewClass(self, class_name: str):
    raise NotImplementedError

class Administrator:
    def __init__(self, contactInformation: str, group: str, knowledge: str):
        self.contactInformation = contactInformation
        self.group = group
        self.knowledge = knowledge

def createAccount(self, user: 'User', password: str):
    raise NotImplementedError

def editData(self, data: str):
    raise NotImplementedError

def receiveNotification(self, message: str):
    raise NotImplementedError

def registerAbsence(self, absence: 'Absence', date: Date):
    raise NotImplementedError

def registerChange(self, change: str):
    raise NotImplementedError

def makeUse(self, tool: str):
    raise NotImplementedError

class Absence:
    def __init__(self, date: Date):
        self.date = date

class Action:
    def __init__(self, status: BehaviorStatus):
        self.status = status

class Dlm:
    def __init__(self, dueDate: Date):
        self.dueDate = dueDate

def assignDate(self, dueDate: Date):
    raise NotImplementedError

class File:
    def __init__(self, name: str):
        self.name = name

def upload(self, uploadDate: Date):
    raise NotImplementedError

class Grade:
    def __init__(self, value: int):
        self.value = value

class Notification:
    def __init__(self, message: str):
        self.message = message

class Page:
    def __init__(self, content: str):
        self.content = content

def addText(self, text: str):
    raise NotImplementedError

def addVideo(self, video: str):
    raise NotImplementedError

def addQuestion(self, question: str):
    raise NotImplementedError

class SubmissionElement:
    def __init__(self):
        pass

def makeElement(self):
    raise NotImplementedError

class User:
    def __init__(self, contactInformation: str, group: str, knowledge: str):
        self.contactInformation = contactInformation
        self.group = group
        self.knowledge = knowledge

def resetPassword(self, previousPassword: str):
    raise NotImplementedError

from typing import List

class Administrator:
    def sendBroadcastMessage(self, recipients: List[str]) -> None:
        raise NotImplementedError

    def setRole(self, account: Account, role: str) -> None:
        raise NotImplementedError

    def uploadSchedule(self, schedule: Schedule) -> None:
        raise NotImplementedError

    def viewDetail(self, account: Account) -> None:
        raise NotImplementedError

    def viewStatistic(self) -> Statistic:
        raise NotImplementedError

class Account:
    def __init__(self, role: str):
        self.role = role

class Message:
    def send(self) -> None:
        raise NotImplementedError

class Participant:
    def receiveMessage(self) -> None:
        raise NotImplementedError

class Schedule:
    def upload(self) -> None:
        raise NotImplementedError

class Statistic:
    def view(self) -> None:
        raise NotImplementedError