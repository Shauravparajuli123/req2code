from typing import List, Date, String, NotImplementedError, Child, Page, Answer, Dlm, Notification, Schedule, User, Absence, Submission, Behavior, Guardian, Teacher, Administrator

class User:
    def __init__(self, username: String, password: String):
        self.username = username
        self.password = password

    def reset_password(self, previous_password: String) -> None:
        raise NotImplementedError

class StudentS:
    def __init__(self, name: String, contact_information: String, group: String, knowledge: String):
        self.name = name
        self.contact_information = contact_information
        self.group = group
        self.knowledge = knowledge

    def hand_homework(self, dlm: Dlm) -> None:
        raise NotImplementedError

    def fill_absence(self, absence: Absence) -> None:
        raise NotImplementedError

    def view_contact_information(self, other_student: StudentS) -> None:
        raise NotImplementedError

class Teacher:
    def __init__(self, name: String, subject: String):
        self.name = name
        self.subject = subject

    def add_page(self, page: Page, dlm: Dlm) -> None:
        raise NotImplementedError

    def assign_dlm(self, dlm: Dlm) -> None:
        raise NotImplementedError

    def assign_schedule(self, schedule: Schedule) -> None:
        raise NotImplementedError

    def edit_page(self, page: Page, dlm: Dlm) -> None:
        raise NotImplementedError

    def make_submission_element(self, submission: Submission) -> None:
        raise NotImplementedError

    def message_student(self, student: StudentS) -> None:
        raise NotImplementedError

    def message_teacher(self, teacher: Teacher) -> None:
        raise NotImplementedError

    def record_action(self, action: String) -> None:
        raise NotImplementedError

    def record_attendance(self, student: StudentS) -> None:
        raise NotImplementedError

    def record_behavior(self, behavior: Behavior) -> None:
        raise NotImplementedError

    def record_grade(self, grade: String) -> None:
        raise NotImplementedError

    def see_answer(self, answer: Answer) -> None:
        raise NotImplementedError

    def see_grade(self, grade: String) -> None:
        raise NotImplementedError

    def see_progress(self, student: StudentS) -> None:
        raise NotImplementedError

    def set_appearance_date(self, dlm: Dlm, date: Date) -> None:
        raise NotImplementedError

    def set_date(self, dlm: Dlm, date: Date) -> None:
        raise NotImplementedError

    def upload_file(self, file: String, dlm: Dlm) -> None:
        raise NotImplementedError

    def view_attendance(self, schedule: Schedule) -> None:
        raise NotImplementedError

    def view_class(self, schedule: Schedule) -> None:
        raise NotImplementedError

class Guardian:
    def __init__(self, name: String, child: Child):
        self.name = name
        self.child = child

    def message_mentor(self, mentor: Teacher) -> None:
        raise NotImplementedError

    def fill_absence(self, absence: Absence) -> None:
        raise NotImplementedError

    def receive_notification(self, notification: Notification) -> None:
        raise NotImplementedError

class Administrator:
    def __init__(self, name: String):
        self.name = name

    def create_account(self, user: User) -> None:
        raise NotImplementedError

    def assign_schedule(self, schedule: Schedule) -> None:
        raise NotImplementedError

    def edit_data(self, data: String) -> None:
        raise NotImplementedError

    def make_use(self, use_case: String) -> None:
        raise NotImplementedError

    def register_absence(self, absence: Absence) -> None:
        raise NotImplementedError

    def register_change(self, change: String) -> None:
        raise NotImplementedError

    def receive_notification(self, notification: Notification) -> None:
        raise NotImplementedError

class Absence:
    def __init__(self, date: Date):
        self.date = date

class Answer:
    def __init__(self, text: String):
        self.text = text

    def add_answer(self, answer: Answer) -> None:
        raise NotImplementedError

class Dlm:
    def __init__(self, title: String, pages: List[Page], due_date: Date):
        self.title = title
        self.pages = pages
        self.due_date = due_date

    def add_page(self, page: Page) -> None:
        raise NotImplementedError

    def assign_dlm(self, dlm: Dlm) -> None:
        raise NotImplementedError

    def set_appearance_date(self, date: Date) -> None:
        raise NotImplementedError

    def set_date(self, date: Date) -> None:
        raise NotImplementedError

    def upload_file(self, file: String) -> None:
        raise NotImplementedError

class Page:
    def __init__(self, content: String, type: String):
        self.content = content
        self.type = type

    def add_text(self, text: String) -> None:
        raise NotImplementedError

    def add_video(self, video: String) -> None:
        raise NotImplementedError

    def add_question(self, question: String) -> None:
        raise NotImplementedError

class Submission:
    def __init__(self, content: String, date: Date):
        self.content = content
        self.date = date

    def make_submission(self, dlm: Dlm) -> None:
        raise NotImplementedError

class Notification:
    def __init__(self, message: String):
        self.message = message

    def receive_notification(self, notification: Notification) -> None:
        raise NotImplementedError

class Behavior:
    sufficient = 'sufficient'
    insufficient = 'insufficient'


from typing import TypedDict, List

class Administrator:
    def sendBroadcastMessage(self, recipients: List[str]) -> None:
        raise NotImplementedError

def setRole(self, account: Account, role: str) -> None:
    raise NotImplementedError

def uploadSchedule(self, schedule: Schedule) -> None:
    raise NotImplementedError

def viewDetail(self, account: Account) -> None:
    raise NotImplementedError

def viewStatistic(self, statistics: List[str]) -> None:
    raise NotImplementedError

class Account:
    role: str
class Participant:
    pass
class Schedule:
    pass
class Message:
    pass
class Insight:
    def viewGrade(self) -> Grade:
        raise NotImplementedError

def viewAttendance(self) -> Attendance:
    raise NotImplementedError

def viewDisciplinaryAction(self) -> DisciplinaryAction:
    raise NotImplementedError
class Grade:
    pass
class Attendance:
    pass
class DisciplinaryAction:
    pass
class Student(Participant):
    pass
class Teacher(Participant):
    pass
class Guardian(Participant):
    pass
class School(Participant):
    pass