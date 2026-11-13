from typing import List, String, Date

class Role:
    pass

class User:
    def __init__(self, username: String, password: String, role: Role):
        self.username = username
        self.password = password
        self.role = role

    def resetPassword(self, previous_password: String) -> None:
        raise NotImplementedError

    def receiveNotification(self, message: String) -> None:
        raise NotImplementedError

class Child:
    def __init__(self, name: String, guardian: User, teacher: User, mentor: User):
        self.name = name
        self.guardian = guardian
        self.teacher = teacher
        self.mentor = mentor

    def fillAbsence(self) -> None:
        raise NotImplementedError

    def receiveNotification(self, message: String) -> None:
        raise NotImplementedError

class Absence:
    def __init__(self, date: Date, child: Child):
        self.date = date
        self.child = child

class Message:
    def __init__(self, sender: User, receiver: User, content: String):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def sendMessage(self, use_case: String) -> None:
        raise NotImplementedError

class Notification:
    def __init__(self, user: User, message: String):
        self.user = user
        self.message = message

    def receiveNotification(self, message: String) -> None:
        raise NotImplementedError

class LearningModule:
    def __init__(self, title: String, pages: List[Page], dueDate: Date):
        self.title = title
        self.pages = pages
        self.dueDate = dueDate

    def addPage(self, page: Page) -> None:
        raise NotImplementedError

    def assignDlm(self, user: User) -> None:
        raise NotImplementedError

    def assignDate(self, date: Date) -> None:
        raise NotImplementedError

    def makeSubmissionElement(self) -> Submission:
        raise NotImplementedError

    def gradeDlmSubmission(self, submission: Submission) -> None:
        raise NotImplementedError

    def recordAction(self, action: String) -> None:
        raise NotImplementedError

    def recordAttendance(self, attendance: String) -> None:
        raise NotImplementedError

    def recordBehavior(self, behavior: String) -> None:
        raise NotImplementedError

    def recordGrade(self, grade: String) -> None:
        raise NotImplementedError

    def setAppearanceDate(self, date: Date) -> None:
        raise NotImplementedError

    def setDate(self, date: Date) -> None:
        raise NotImplementedError

    def uploadFile(self, file: String) -> None:
        raise NotImplementedError

class Page:
    def __init__(self, content: String, type: String):
        self.content = content
        self.type = type

class Submission:
    def __init__(self, content: String, student: Child, learningModule: LearningModule):
        self.content = content
        self.student = student
        self.learningModule = learningModule

class Account:
    def __init__(self, username: String, password: String):
        self.username = username
        self.password = password

    def createAccount(self) -> None:
        raise NotImplementedError

class Administrator:
    def __init__(self):
        pass

    def assignSchedule(self, schedule: String) -> None:
        raise NotImplementedError

    def makeUse(self, use_case: String) -> None:
        raise NotImplementedError

    def registerChange(self, change: String) -> None:
        raise NotImplementedError

    def registerAbsence(self, absence: Absence) -> None:
        raise NotImplementedError

class Teacher:
    def __init__(self, class_: List[Child], mentor: Child):
        self.class_ = class_
        self.mentor = mentor

    def messageStudent(self, student: Child, content: String) -> None:
        raise NotImplementedError

    def messageTeacher(self, teacher: User, content: String) -> None:
        raise NotImplementedError

    def recordAction(self, action: String) -> None:
        raise NotImplementedError

    def recordAttendance(self, attendance: String) -> None:
        raise NotImplementedError

    def recordBehavior(self, behavior: String) -> None:
        raise NotImplementedError

    def recordGrade(self, grade: String) -> None:
        raise NotImplementedError

    def setAppearanceDate(self, date: Date) -> None:
        raise NotImplementedError

    def setDate(self, date: Date) -> None:
        raise NotImplementedError

    def uploadFile(self, file: String) -> None:
        raise NotImplementedError

class Guardian:
    def __init__(self, child: Child):
        self.child = child

    def fillAbsence(self) -> None:
        raise NotImplementedError

    def messageTeacher(self, teacher: User, content: String) -> None:
        raise NotImplementedError

    def receiveNotification(self, message: String) -> None:
        raise NotImplementedError

class Student:
    def __init__(self, class_: List[Child], mentor: Child):
        self.class_ = class_
        self.mentor = mentor

    def handHomework(self, submission: Submission) -> None:
        raise NotImplementedError

    def receiveNotification(self, message: String) -> None:
        raise NotImplementedError

    def viewContactInformation(self) -> None:
        raise NotImplementedError

class Administrator:
    def sendBroadcastMessage(self):
        raise NotImplementedError

    def setRole(self):
        raise NotImplementedError

    def uploadSchedule(self):
        raise NotImplementedError

    def viewDetail(self):
        raise NotImplementedError

    def viewStatistic(self):
        raise NotImplementedError

class Account:
    def __init__(self, role: str):
        self.role = role

class Message:
    def send(self):
        raise NotImplementedError

class Schedule:
    def upload(self):
        raise NotImplementedError

class Statistic:
    def view(self):
        raise NotImplementedError