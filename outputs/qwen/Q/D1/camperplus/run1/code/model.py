from typing import TypedDict, Optional

class String(str):
    pass

class Camper:
    def __init__(self, name: String, emergencyInformation: String, guardian: Parent):
        self.name = name
        self.emergencyInformation = emergencyInformation
        self.guardian = guardian

    def addEmergencyInformation(self, information: String):
        raise NotImplementedError

    def updateGuardian(self, newGuardian: Parent):
        raise NotImplementedError

class Parent:
    def __init__(self, camperBehavior: String, account: String):
        self.camperBehavior = camperBehavior
        self.account = account

    def createAccount(self, account: String):
        raise NotImplementedError

    def submitConsentForm(self, form: ConsentForm):
        raise NotImplementedError

    def seeCamper(self, camper: Camper):
        raise NotImplementedError

    def seeConsentForm(self, form: ConsentForm):
        raise NotImplementedError

    def seeCounselor(self, counselor: CampCounselor):
        raise NotImplementedError

    def seePayment(self, payment: Optional[String]):
        raise NotImplementedError

    def seeSchedule(self, schedule: Optional[String]):
        raise NotImplementedError

class CampAdministrator:
    def __init__(self, name: String):
        self.name = name

    def addCamper(self, camper: Camper):
        raise NotImplementedError

    def removeCamper(self, camper: Camper):
        raise NotImplementedError

    def keepCamperRecord(self, camper: Camper):
        raise NotImplementedError

    def keepInformation(self, information: String):
        raise NotImplementedError

    def keepTrack(self, track: String):
        raise NotImplementedError

    def logAttendance(self, attendance: String):
        raise NotImplementedError

    def modifyInformation(self, information: String):
        raise NotImplementedError

    def notifyParent(self, parent: Parent):
        raise NotImplementedError

    def provideFeedback(self, feedback: Feedback):
        raise NotImplementedError

    def removeParent(self, parent: Parent):
        raise NotImplementedError

    def suspendCamper(self, camper: Camper):
        raise NotImplementedError

    def uploadConsentForm(self, form: ConsentForm):
        raise NotImplementedError

    def createAvenue(self, avenue: String):
        raise NotImplementedError

    def createGroup(self, group: String):
        raise NotImplementedError

    def createNametag(self, nametag: Nametag):
        raise NotImplementedError

    def createRegistrationForm(self, form: String):
        raise NotImplementedError

    def createRule(self, rule: String):
        raise NotImplementedError

    def modifyTask(self, task: Task):
        raise NotImplementedError

    def scheduleActivity(self, activity: Activity):
        raise NotImplementedError

    def scheduleTask(self, task: Task):
        raise NotImplementedError

    def seeCampGroup(self, group: String):
        raise NotImplementedError

    def seeEvent(self, event: String):
        raise NotImplementedError

    def seeForm(self, form: String):
        raise NotImplementedError

    def setReminder(self, reminder: String):
        raise NotImplementedError

class CampCounselor:
    def __init__(self, name: String):
        self.name = name

    def takeAttendance(self, attendance: String):
        raise NotImplementedError

class CampWorker:
    def __init__(self, name: String):
        self.name = name

    def reportCamper(self, camper: Camper):
        raise NotImplementedError

    def reportList(self, supplies: String):
        raise NotImplementedError

    def reportRepair(self, repair: String):
        raise NotImplementedError

class Activity:
    def __init__(self, name: String):
        self.name = name

    def schedule(self, schedule: String):
        raise NotImplementedError

    def unschedule(self, schedule: String):
        raise NotImplementedError

class Task:
    def __init__(self, name: String):
        self.name = name

    def modify(self, modification: String):
        raise NotImplementedError

    def delete(self, task: String):
        raise NotImplementedError

class Event:
    def __init__(self, name: String):
        self.name = name

    def schedule(self, schedule: String):
        raise NotImplementedError

    def unschedule(self, schedule: String):
        raise NotImplementedError

class Nametag:
    def __init__(self, name: String):
        self.name = name

    def create(self, nametag: String):
        raise NotImplementedError

    def make(self, nametag: String):
        raise NotImplementedError

class ConsentForm:
    def __init__(self, name: String):
        self.name = name

    def upload(self, form: String):
        raise NotImplementedError

    def submit(self, signature: String):
        raise NotImplementedError

class Feedback:
    def __init__(self, name: String):
        self.name = name

    def provide(self, feedback: String):
        raise NotImplementedError