from abc import ABC, abstractmethod

class Actor(ABC):
    pass

class Student(Actor):
    def __init__(self, contact_information: str, group: str, knowledge: str):
        self.contact_information = contact_information
        self.group = group
        self.knowledge = knowledge
        self.submissions = []
        self.behavior = []
        self.performance = []
        self.attendance = []

class Guardian(Actor):
    def __init__(self):
        self.children = []

class Teacher(Actor):
    def __init__(self):
        self.students = []
        self.mentees = []
        self.dlms = []

class Administrator(Actor):
    def __init__(self):
        self.users = []
        self.schedules = []

class User(Actor):
    def __init__(self):
        self.password = None

class Absence:
    def __init__(self, user: Actor, date: str):
        self.user = user
        self.date = date

class Action:
    def __init__(self, user: Actor, action_type: str, date: str):
        self.user = user
        self.action_type = action_type
        self.date = date

class Behavior:
    def __init__(self, student: Student, behavior_type: str, date: str):
        self.student = student
        self.behavior_type = behavior_type
        self.date = date

class Change:
    def __init__(self, user: Actor, change_type: str, date: str):
        self.user = user
        self.change_type = change_type
        self.date = date

class Dlm:
    def __init__(self, teacher: Teacher, title: str, appearance_date: str):
        self.teacher = teacher
        self.title = title
        self.appearance_date = appearance_date
        self.pages = []
        self.submissions = []

class File:
    def __init__(self, user: Actor, title: str, content: str):
        self.user = user
        self.title = title
        self.content = content

class Grade:
    def __init__(self, student: Student, grade: int, date: str):
        self.student = student
        self.grade = grade
        self.date = date

class Insight:
    def __init__(self, user: Actor, insight_type: str, date: str):
        self.user = user
        self.insight_type = insight_type
        self.date = date

class Lms:
    def __init__(self):
        self.files = []
        self.dlms = []

class Message:
    def __init__(self, sender: Actor, recipient: Actor, content: str, date: str):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.date = date

class Notification:
    def __init__(self, user: Actor, message: str, date: str):
        self.user = user
        self.message = message
        self.date = date

class Schedule:
    def __init__(self, user: Actor, start_date: str, end_date: str):
        self.user = user
        self.start_date = start_date
        self.end_date = end_date

class Work:
    def __init__(self, student: Student, content: str, date: str):
        self.student = student
        self.content = content
        self.date = date

class Year:
    def __init__(self, student: Student, year: int):
        self.student = student
        self.year = year

class BehaviorType:
    sufficient = 'sufficient'
    insufficient = 'insufficient'

class ActorType:
    student = 'student'
    guardian = 'guardian'
    teacher = 'teacher'
    administrator = 'administrator'

class UseCase:
    def __init__(self, actor: Actor, action: str):
        self.actor = actor
        self.action = action

    @abstractmethod
def perform(self):
        pass

class AccessFile(UseCase):
    def __init__(self, student: Student):
        super().__init__(student, 'access file')

    def perform(self):
        raise NotImplementedError

class AddAnswer(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'add answer')

    def perform(self):
        raise NotImplementedError

class AddPage(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'add page')

    def perform(self):
        raise NotImplementedError

class AssignDate(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'assign date')

    def perform(self):
        raise NotImplementedError

class AssignDlm(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'assign dlm')

    def perform(self):
        raise NotImplementedError

class AssignSchedule(UseCase):
    def __init__(self, administrator: Administrator):
        super().__init__(administrator, 'assign schedule')

    def perform(self):
        raise NotImplementedError

class CreateAccount(UseCase):
    def __init__(self, administrator: Administrator):
        super().__init__(administrator, 'create account')

    def perform(self):
        raise NotImplementedError

class CreateLearningModule(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'create learning module')

    def perform(self):
        raise NotImplementedError

class EditData(UseCase):
    def __init__(self, administrator: Administrator):
        super().__init__(administrator, 'edit data')

    def perform(self):
        raise NotImplementedError

class EditPage(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'edit page')

    def perform(self):
        raise NotImplementedError

class GradeDlmSubmission(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'grade dlm submission')

    def perform(self):
        raise NotImplementedError

class HandHomework(UseCase):
    def __init__(self, student: Student):
        super().__init__(student, 'hand homework')

    def perform(self):
        raise NotImplementedError

class HaveAccess(UseCase):
    def __init__(self, student: Student):
        super().__init__(student, 'have access')

    def perform(self):
        raise NotImplementedError

class MakeSubmissionElement(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'make submission element')

    def perform(self):
        raise NotImplementedError

class MakeUse(UseCase):
    def __init__(self, administrator: Administrator):
        super().__init__(administrator, 'make use')

    def perform(self):
        raise NotImplementedError

class MessageMentor(UseCase):
    def __init__(self, student: Student):
        super().__init__(student, 'message mentor')

    def perform(self):
        raise NotImplementedError

class MessageStudent(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'message student')

    def perform(self):
        raise NotImplementedError

class MessageTeacher(UseCase):
    def __init__(self, guardian: Guardian):
        super().__init__(guardian, 'message teacher')

    def perform(self):
        raise NotImplementedError

class ReceiveConfirmation(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'receive confirmation')

    def perform(self):
        raise NotImplementedError

class ReceiveNotification(UseCase):
    def __init__(self, actor: Actor):
        super().__init__(actor, 'receive notification')

    def perform(self):
        raise NotImplementedError

class RecordAction(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'record action')

    def perform(self):
        raise NotImplementedError

class RecordAttendance(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'record attendance')

    def perform(self):
        raise NotImplementedError

class RecordBehavior(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'record behavior')

    def perform(self):
        raise NotImplementedError

class RecordGrade(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'record grade')

    def perform(self):
        raise NotImplementedError

class RegisterAbsence(UseCase):
    def __init__(self, administrator: Administrator):
        super().__init__(administrator, 'register absence')

    def perform(self):
        raise NotImplementedError

class RegisterChange(UseCase):
    def __init__(self, administrator: Administrator):
        super().__init__(administrator, 'register change')

    def perform(self):
        raise NotImplementedError

class ResetPassword(UseCase):
    def __init__(self, user: User):
        super().__init__(user, 'reset password')

    def perform(self):
        raise NotImplementedError

class SeeAnswer(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'see answer')

    def perform(self):
        raise NotImplementedError

class SeeGrade(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'see grade')

    def perform(self):
        raise NotImplementedError

class SeeProgress(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'see progress')

    def perform(self):
        raise NotImplementedError

class SetAppearanceDate(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'set appearance date')

    def perform(self):
        raise NotImplementedError

class SetDate(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'set date')

    def perform(self):
        raise NotImplementedError

class UploadFile(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'upload file')

    def perform(self):
        raise NotImplementedError

class ViewAttendance(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'view attendance')

    def perform(self):
        raise NotImplementedError

class ViewClass(UseCase):
    def __init__(self, teacher: Teacher):
        super().__init__(teacher, 'view class')

    def perform(self):
        raise NotImplementedError

class ViewContactInformation(UseCase):
    def __init__(self, student: Student):
        super().__init__(student, 'view contact information')

    def perform(self):
        raise NotImplementedError

class ViewInformation(UseCase):
    def __init__(self, guardian: Guardian):
        super().__init__(guardian, 'view information')

    def perform(self):
        raise NotImplementedError

from enum import Enum

class Behavior(Enum):
    sufficient = 'sufficient'
    insufficient = 'insufficient'

class Account:
    def __init__(self, role: str):
        self.role = role

class Participant:
    pass

class Administrator:
    def send_broadcast_message(self, participants: list[Participant], message: str) -> None:
        raise NotImplementedError

class Role(Enum):
    student = 'student'
    teacher = 'teacher'
    administrator = 'administrator'
    guardian = 'guardian'

class Account:
    def __init__(self, role: Role):
        self.role = role

class Schedule:
    pass

class UploadSchedule:
    def __init__(self, schedule: Schedule):
        self.schedule = schedule

class ViewDetail:
    def __init__(self, account: Account):
        self.account = account

class ViewStatistic:
    def __init__(self, performance: Performance):
        self.performance = performance

class Performance:
    pass
