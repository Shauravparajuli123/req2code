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
    def __init__(self, role):
        self.role = role
class Message:
    pass
class Participant:
    pass
class Schedule:
    pass
class Insight:
    pass
class Statistic:
    pass