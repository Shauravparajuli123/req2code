from typing import List, Date

class Camper:
    def __init__(self, name: str, emergencyInformation: str, guardian: Parent):
        self.name = name
        self.emergencyInformation = emergencyInformation
        self.guardian = guardian

    def addEmergencyInformation(self) -> None:
        raise NotImplementedError

    def removeEmergencyInformation(self) -> None:
        raise NotImplementedError

    def updateGuardian(self) -> None:
        raise NotImplementedError

class Parent:
    def __init__(self, camperBehavior: str, camper: Camper):
        self.camperBehavior = camperBehavior
        self.camper = camper

    def enrollCamper(self) -> None:
        raise NotImplementedError

    def seeCamper(self) -> None:
        raise NotImplementedError

    def seeConsentForm(self) -> None:
        raise NotImplementedError

    def seeCounselor(self) -> None:
        raise NotImplementedError

    def seeSchedule(self) -> None:
        raise NotImplementedError

    def submitType(self) -> None:
        raise NotImplementedError

    def signConsentForm(self) -> None:
        raise NotImplementedError

    def seePayment(self) -> None:
        raise NotImplementedError

class CampAdministrator:
    def __init__(self, name: str, camperRecords: List[Camper], groups: List[CampGroup]):
        self.name = name
        self.camperRecords = camperRecords
        self.groups = groups

    def addCamper(self) -> None:
        raise NotImplementedError

    def removeCamper(self) -> None:
        raise NotImplementedError

    def keepCamperRecord(self) -> None:
        raise NotImplementedError

    def keepInformation(self) -> None:
        raise NotImplementedError

    def keepTrack(self) -> None:
        raise NotImplementedError

    def logAttendance(self) -> None:
        raise NotImplementedError

    def makeNametag(self) -> None:
        raise NotImplementedError

    def createRegistrationForm(self) -> None:
        raise NotImplementedError

    def createRule(self) -> None:
        raise NotImplementedError

    def assignPosition(self) -> None:
        raise NotImplementedError

    def scheduleActivity(self) -> None:
        raise NotImplementedError

    def scheduleTask(self) -> None:
        raise NotImplementedError

    def seeCampGroup(self) -> None:
        raise NotImplementedError

    def seeEvent(self) -> None:
        raise NotImplementedError

    def seeForm(self) -> None:
        raise NotImplementedError

    def notifyParent(self) -> None:
        raise NotImplementedError

    def provideFeedback(self) -> None:
        raise NotImplementedError

    def modifyInformation(self) -> None:
        raise NotImplementedError

    def modifyTask(self) -> None:
        raise NotImplementedError

    def deleteTask(self) -> None:
        raise NotImplementedError

    def deleteCamper(self) -> None:
        raise NotImplementedError

    def deleteParent(self) -> None:
        raise NotImplementedError

    def uploadConsentForm(self) -> None:
        raise NotImplementedError

    def suspendCamper(self) -> None:
        raise NotImplementedError

    def setReminder(self) -> None:
        raise NotImplementedError

class CampGroup:
    def __init__(self, name: str, events: List[Event], campers: List[Camper]):
        self.name = name
        self.events = events
        self.campers = campers

    def seeEvent(self) -> None:
        raise NotImplementedError

class Event:
    def __init__(self, name: str, date: Date):
        self.name = name
        self.date = date

class Nametag:
    def __init__(self, name: str):
        self.name = name

    def makeNametag(self) -> None:
        raise NotImplementedError

class ConsentForm:
    def __init__(self, name: str):
        self.name = name

    def uploadConsentForm(self) -> None:
        raise NotImplementedError

class Task:
    def __init__(self, name: str, date: Date):
        self.name = name
        self.date = date

    def scheduleTask(self) -> None:
        raise NotImplementedError

    def modifyTask(self) -> None:
        raise NotImplementedError

    def deleteTask(self) -> None:
        raise NotImplementedError

class Activity:
    def __init__(self, name: str, date: Date):
        self.name = name
        self.date = date

    def scheduleActivity(self) -> None:
        raise NotImplementedError

class Feedback:
    def __init__(self, name: str):
        self.name = name

    def provideFeedback(self) -> None:
        raise NotImplementedError

class Schedule:
    def __init__(self, name: str, activities: List[Activity]):
        self.name = name
        self.activities = activities

class Database:
    def __init__(self):
        pass

    def storeInformation(self) -> None:
        raise NotImplementedError

    def storeEmergencyInformation(self) -> None:
        raise NotImplementedError

class Counselor:
    def __init__(self, name: str, camper: Camper):
        self.name = name
        self.camper = camper

    def takeAttendance(self) -> None:
        raise NotImplementedError

class CampCounselor:
    def __init__(self):
        pass

    def reportCamper(self) -> None:
        raise NotImplementedError

    def reportList(self) -> None:
        raise NotImplementedError

    def reportRepair(self) -> None:
        raise NotImplementedError