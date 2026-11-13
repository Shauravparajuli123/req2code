from datetime import datetime

class User:
    def __init__(self, password, role):
        self.password = password
        self.role = role
    def resetPassword(self, previous_password):
        raise NotImplementedError

class Absence:
    def __init__(self, date):
        self.date = date

class Behavior:
    sufficient = 'sufficient'
    insufficient = 'insufficient'

class Account:
    def __init__(self, role):
        self.role = role
    def editData(self):
        raise NotImplementedError

class Action:
    def __init__(self, description):
        self.description = description

class Answer:
    def __init__(self, text):
        self.text = text
    def addAnswer(self):
        raise NotImplementedError

class AppearanceDate:
    def __init__(self, date):
        self.date = date
    def setAppearanceDate(self):
        raise NotImplementedError

class Assignment:
    def __init__(self, dueDate):
        self.dueDate = dueDate
    def assignDate(self):
        raise NotImplementedError

class Change:
    def __init__(self, description):
        self.description = description
    def registerChange(self):
        raise NotImplementedError

class Child:
    def __init__(self, name):
        self.name = name
    def fillAbsence(self):
        raise NotImplementedError

class Date:
    def __init__(self, date):
        self.date = date
    def setDate(self):
        raise NotImplementedError

class Dlm:
    def __init__(self, title):
        self.title = title
    def addPage(self):
        raise NotImplementedError
    def assignDlm(self):
        raise NotImplementedError
    def editPage(self):
        raise NotImplementedError
    def makeSubmissionElement(self):
        raise NotImplementedError
    def addAnswer(self):
        raise NotImplementedError
    def gradeDlmSubmission(self):
        raise NotImplementedError

class File:
    def __init__(self, name):
        self.name = name
    def uploadFile(self):
        raise NotImplementedError

class Grade:
    def __init__(self, value):
        self.value = value
    def recordGrade(self):
        raise NotImplementedError

class Homework:
    def __init__(self, title):
        self.title = title
    def handHomework(self):
        raise NotImplementedError

class Insight:
    def __init__(self, description):
        self.description = description

class Lms:
    def __init__(self, title):
        self.title = title
    def createLearningModule(self):
        raise NotImplementedError
    def makeUse(self):
        raise NotImplementedError

class Material:
    def __init__(self, type):
        self.type = type

class Mentor:
    def __init__(self, name):
        self.name = name
    def recordAction(self):
        raise NotImplementedError

class Message:
    def __init__(self, content):
        self.content = content
    def sendMessage(self):
        raise NotImplementedError

class Notification:
    def __init__(self, type):
        self.type = type
    def receiveNotification(self):
        raise NotImplementedError

class Participant:
    def __init__(self, name):
        self.name = name
    def viewClass(self):
        raise NotImplementedError
    def viewContactInformation(self):
        raise NotImplementedError

class Performance:
    def __init__(self, description):
        self.description = description

class Question:
    def __init__(self, type):
        self.type = type

class Schedule:
    def __init__(self, date):
        self.date = date
    def assignSchedule(self):
        raise NotImplementedError

class School:
    def __init__(self, name):
        self.name = name

class Staff:
    def __init__(self, name):
        self.name = name
    def registerAbsence(self):
        raise NotImplementedError

class Student:
    def __init__(self, name):
        self.name = name
    def viewPerformance(self):
        raise NotImplementedError
    def viewContactInformation(self):
        raise NotImplementedError

class Submission:
    def __init__(self, content):
        self.content = content
    def makeSubmission(self):
        raise NotImplementedError

class Timetable:
    def __init__(self, date):
        self.date = date
    def setAppearanceDate(self):
        raise NotImplementedError
    def setDate(self):
        raise NotImplementedError

class Year:
    def __init__(self, year):
        self.year = year
    def viewPerformance(self):
        raise NotImplementedError


class Account:
    def __init__(self, role):
        self.role = role

class Role:
    student = 'student'
    teacher = 'teacher'
    administrator = 'administrator'
    guardian = 'guardian'

class Message:
    def __init__(self, content):
        self.content = content
    def send_to_participants(self):
        raise NotImplementedError

class Schedule:
    def __init__(self, details):
        self.details = details
    def upload(self):
        raise NotImplementedError

class Statistic:
    def __init__(self, grades, attendance, disciplinary_actions):
        self.grades = grades
        self.attendance = attendance
        self.disciplinary_actions = disciplinary_actions
    def view(self):
        raise NotImplementedError