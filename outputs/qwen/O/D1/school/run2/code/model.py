class Absence:
    pass

class Account:
    pass

class Action:
    pass

class Administrator:
    pass

class Answer:
    pass

class AppearanceDate:
    pass

class Attendance:
    pass

class Child:
    pass

class Dlm:
    pass

class File:
    pass

class Grade:
    pass

class Guardian:
    pass

class Homework:
    pass

class Lms:
    pass

class Mentor:
    pass

class Message:
    pass

class Notification:
    pass

class Participant:
    pass

class Performance:
    pass

class Question:
    pass

class School:
    pass

class Staff:
    pass

class Student:
    pass

class Teacher:
    pass

class Timetable:
    pass

class User:
    pass


class Administrator:
    def send_broadcast_message(self):
        raise NotImplementedError
    def set_role(self):
        raise NotImplementedError
    def upload_schedule(self):
        raise NotImplementedError
    def view_detail(self):
        raise NotImplementedError
    def view_statistic(self):
        raise NotImplementedError
class Account:
    def __init__(self, role):
        self.role = role
class Message:
    def send_to_participants(self):
        raise NotImplementedError
class Participant:
    pass
class Schedule:
    pass
class Statistic:
    pass