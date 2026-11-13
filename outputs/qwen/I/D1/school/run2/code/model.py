from enum import Enum

class BehaviorStatus(Enum):
    Sufficient = 'sufficient'
    Insufficient = 'insufficient'

class Account:
    def __init__(self, role: str):
        self.role = role

class Administrator:
    def SendBroadcastMessage(self, participants: list[Participant], message: str):
        raise NotImplementedError

class Participant:
    pass

class Role(Enum):
    Student = 'student'
    Teacher = 'teacher'
    Administrator = 'administrator'
    Guardian = 'guardian'

class UploadSchedule:
    def __init__(self, schedule: dict):
        self.schedule = schedule

class ViewDetail:
    def __init__(self, account_id: str):
        self.account_id = account_id

class ViewStatistic:
    def __init__(self, statistic_type: str):
        self.statistic_type = statistic_type
