from enum import Enum

class PickType(Enum):
    PickUp = 'PickUp'
    DropOff = 'DropOff'


class User:
    def enterZipCode(self):
        raise NotImplementedError
    def getHour(self):
        raise NotImplementedError

class Admin:
    def addRecyclingCenterInformation(self):
        raise NotImplementedError
    def handleActivity(self):
        raise NotImplementedError

class RecyclingFacility:
    def __init__(self, openingHour):
        self.openingHour = openingHour
    def communicateSite(self):
        raise NotImplementedError

class RecyclingFacilityRepresentative:
    def __init__(self, material):
        self.material = material
    def updateInformation(self):
        raise NotImplementedError

class Superuser:
    def __init__(self, stats):
        self.stats = stats
    def replyUserQuestion(self):
        raise NotImplementedError

class RecyclingCenter:
    def __init__(self, location):
        self.location = location

class Location:
    def __init__(self, area):
        self.area = area

class Notification:
    def __init__(self, emailId):
        self.emailId = emailId
    def giveEmailId(self):
        raise NotImplementedError

class Feedback:
    def __init__(self, errorLogs):
        self.errorLogs = errorLogs
    def getFeedback(self):
        raise NotImplementedError
    def readFeedback(self):
        raise NotImplementedError

class Schedule:
    def __init__(self, pick):
        self.pick = pick
    def uploadSchedule(self):
        raise NotImplementedError