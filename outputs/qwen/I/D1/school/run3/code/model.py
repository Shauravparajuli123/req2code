from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, role: str):
        self.role = role

    @abstractmethod
define method signatures

class Guardian(User):
    def __init__(self, role: str):
        super().__init__(role)

define method signatures

class Student(User):
    def __init__(self, role: str):
        super().__init__(role)

define method signatures

class Teacher(User):
    def __init__(self, role: str):
        super().__init__(role)

define method signatures

class Administrator(User):
    def __init__(self, role: str):
        super().__init__(role)

define method signatures

class Absence:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Behavior:
    def __init__(self, student: Student, behavior: str):
        self.student = student
        self.behavior = behavior

define method signatures

class Child:
    def __init__(self, guardian: Guardian, student: Student):
        self.guardian = guardian
        self.student = student

define method signatures

class Dlm:
    def __init__(self, teacher: Teacher):
        self.teacher = teacher

define method signatures

class File:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Grade:
    def __init__(self, student: Student, grade: int):
        self.student = student
        self.grade = grade

define method signatures

class Homework:
    def __init__(self, student: Student):
        self.student = student

define method signatures

class Insight:
    def __init__(self, user: User, information: str):
        self.user = user
        self.information = information

define method signatures

class Lms:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Material:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Notification:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Participant:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Performance:
    def __init__(self, user: User, performance: str):
        self.user = user
        self.performance = performance

define method signatures

class Question:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Schedule:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Staff:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Submission:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Timetable:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Work:
    def __init__(self, user: User):
        self.user = user

define method signatures

class Year:
    def __init__(self, user: User):
        self.user = user

define method signatures


from enum import Enum

class Role(Enum):
    student = 'student'
    teacher = 'teacher'
    administrator = 'administrator'
    guardian = 'guardian'

class Account:
    def __init__(self, role: Role):
        self.role = role

class Message:
    def __init__(self, content: str):
        self.content = content

class Schedule:
    def __init__(self, content: str):
        self.content = content

class School:
    def __init__(self):
        self.accounts = []
        self.schedules = []
        self.stats = {
            'grades': {},
            'attendance': {},
            'disciplinary_actions': {}
        }

def send_broadcast_message(self, message: Message, participants: list[Account]):
    raise NotImplementedError

def set_role(self, account: Account, new_role: Role):
    raise NotImplementedError

def upload_schedule(self, schedule: Schedule):
    raise NotImplementedError

def view_detail(self, account: Account):
    raise NotImplementedError

def view_statistic(self):
    raise NotImplementedError
