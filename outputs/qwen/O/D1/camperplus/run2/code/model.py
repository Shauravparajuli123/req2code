class Camper:
    def __init__(self, name, emergencyInformation, guardian):
        self.name = name
        self.emergencyInformation = emergencyInformation
        self.guardian = guardian

    def addEmergencyInformation(self):
        raise NotImplementedError

    def addGuardian(self):
        raise NotImplementedError

class Parent:
    def __init__(self, name, camperBehavior):
        self.name = name
        self.camperBehavior = camperBehavior

    def submitConsentForm(self):
        raise NotImplementedError

    def submitFeedback(self):
        raise NotImplementedError

class CampAdministrator:
    def addCamper(self):
        raise NotImplementedError

    def addParent(self):
        raise NotImplementedError

    def assignPosition(self):
        raise NotImplementedError

    def createAccount(self):
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

    def enrollCamper(self):
        raise NotImplementedError

    def keepCamperRecord(self):
        raise NotImplementedError

    def keepInformation(self):
        raise NotImplementedError

    def keepTrack(self):
        raise NotImplementedError

    def logAttendance(self):
        raise NotImplementedError

    def makeNametag(self):
        raise NotImplementedError

    def modifyInformation(self):
        raise NotImplementedError

    def modifyTask(self):
        raise NotImplementedError

    def notifyParent(self):
        raise NotImplementedError

    def removeCamper(self):
        raise NotImplementedError

    def reportCamper(self):
        raise NotImplementedError

    def reportList(self):
        raise NotImplementedError

    def reportRepair(self):
        raise NotImplementedError

    def scheduleActivity(self):
        raise NotImplementedError

    def scheduleTask(self):
        raise NotImplementedError

    def seeCampGroup(self):
        raise NotImplementedError

    def seeCamper(self):
        raise NotImplementedError

    def seeConsentForm(self):
        raise NotImplementedError

    def seeCounselor(self):
        raise NotImplementedError

    def seeEvent(self):
        raise NotImplementedError

    def seeForm(self):
        raise NotImplementedError

    def seePayment(self):
        raise NotImplementedError

    def seeSchedule(self):
        raise NotImplementedError

    def setReminder(self):
        raise NotImplementedError

    def sharePhoto(self):
        raise NotImplementedError

    def storeEmergencyInformation(self):
        raise NotImplementedError

    def storeInformation(self):
        raise NotImplementedError

    def submitCompletionReport(self):
        raise NotImplementedError

    def takeAttendance(self):
        raise NotImplementedError

class CampCounselor:
    def __init__(self, name, assignedKids):
        self.name = name
        self.assignedKids = assignedKids

    def takeAttendance(self):
        raise NotImplementedError

class CampWorker:
    def __init__(self, name, assignedKids):
        self.name = name
        self.assignedKids = assignedKids

    def reportCamper(self):
        raise NotImplementedError

    def reportList(self):
        raise NotImplementedError

    def reportRepair(self):
        raise NotImplementedError

    def submitCompletionReport(self):
        raise NotImplementedError