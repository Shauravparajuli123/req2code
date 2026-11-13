from typing import TypedDict, String

class String:
    pass

class Camper:
    def __init__(self, name: String, guardian: Parent, emergencyInformation: String):
        self.name = name
        self.guardian = guardian
        self.emergencyInformation = emergencyInformation

    def addCamper(self):
        raise NotImplementedError

    def removeCamper(self):
        raise NotImplementedError

    def suspendCamper(self):
        raise NotImplementedError

    def modifyCamperInformation(self):
        raise NotImplementedError

    def keepCamperRecord(self):
        raise NotImplementedError

    def logAttendance(self):
        raise NotImplementedError


class Parent:
    def __init__(self, name: String, camperBehavior: String):
        self.name = name
        self.camperBehavior = camperBehavior

    def createAccount(self):
        raise NotImplementedError

    def seeCamper(self):
        raise NotImplementedError

    def seeConsentForm(self):
        raise NotImplementedError

    def seeCounselor(self):
        raise NotImplementedError

    def seePayment(self):
        raise NotImplementedError

    def seeSchedule(self):
        raise NotImplementedError

    def signConsentForm(self):
        raise NotImplementedError

    def submitType(self):
        raise NotImplementedError

    def sharePhoto(self):
        raise NotImplementedError


class CampAdministrator:
    def __init__(self, name: String):
        self.name = name

    def addCamper(self):
        raise NotImplementedError

    def removeCamper(self):
        raise NotImplementedError

    def suspendCamper(self):
        raise NotImplementedError

    def modifyCamperInformation(self):
        raise NotImplementedError

    def keepCamperRecord(self):
        raise NotImplementedError

    def logAttendance(self):
        raise NotImplementedError

    def createAvenue(self):
        raise NotImplementedError

    def createGroup(self):
        raise NotImplementedError

    def createNametag(self):
        raise NotImplementedError

    def createRegistrationForm(self):
        raise NotImplementedError

    def createRule(self):
        raise NotImplementedError

    def deleteCamper(self):
        raise NotImplementedError

    def deleteParent(self):
        raise NotImplementedError

    def deleteTask(self):
        raise NotImplementedError

    def modifyTask(self):
        raise NotImplementedError

    def notifyParent(self):
        raise NotImplementedError

    def provideFeedback(self):
        raise NotImplementedError

    def setReminder(self):
        raise NotImplementedError

    def storeInformation(self):
        raise NotImplementedError

    def seeCampGroup(self):
        raise NotImplementedError

    def seeEvent(self):
        raise NotImplementedError

    def seeForm(self):
        raise NotImplementedError

    def seePayment(self):
        raise NotImplementedError

    def seeSchedule(self):
        raise NotImplementedError

    def storeEmergencyInformation(self):
        raise NotImplementedError


class CampCounselor:
    def __init__(self, name: String):
        self.name = name

    def reportCamper(self):
        raise NotImplementedError

    def reportList(self):
        raise NotImplementedError

    def reportRepair(self):
        raise NotImplementedError

    def takeAttendance(self):
        raise NotImplementedError
