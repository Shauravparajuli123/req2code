from abc import ABC, abstractmethod

class User:
    def __init__(self, email_id, zip_code):
        self.email_id = email_id
        self.zip_code = zip_code

    def clickAddress(self):
        raise NotImplementedError

    def enterZipCode(self):
        raise NotImplementedError

    def getFeedback(self):
        raise NotImplementedError

    def getHour(self):
        raise NotImplementedError

    def viewLocation(self):
        raise NotImplementedError

    def viewMapDisplay(self):
        raise NotImplementedError

    def viewDisposalEvent(self):
        raise NotImplementedError

    def viewInformation(self):
        raise NotImplementedError

    def viewUserDocumentation(self):
        raise NotImplementedError

    def viewUserErrorLog(self):
        raise NotImplementedError

    def choosePick(self):
        raise NotImplementedError

    def selectType(self):
        raise NotImplementedError

    def uploadSchedule(self):
        raise NotImplementedError

    def linkEmailAccount(self):
        raise NotImplementedError

    def addDonationCenter(self):
        raise NotImplementedError

    def createAccount(self):
        raise NotImplementedError

    def browseList(self):
        raise NotImplementedError

    def viewActivityFee(self):
        raise NotImplementedError

    def viewDashboard(self):
        raise NotImplementedError

    def viewStat(self):
        raise NotImplementedError

    def viewFacilityInformation(self):
        raise NotImplementedError

    def viewUserStats(self):
        raise NotImplementedError

    def viewUserErrorLogs(self):
        raise NotImplementedError

    def viewUserFeedback(self):
        raise NotImplementedError

    def viewUserWaste(self):
        raise NotImplementedError

class Admin:
    def __init__(self):
        pass

    def blockUser(self):
        raise NotImplementedError

    def communicateFacility(self):
        raise NotImplementedError

    def communicateSite(self):
        raise NotImplementedError

    def handleActivity(self):
        raise NotImplementedError

    def viewUserErrorLog(self):
        raise NotImplementedError

    def viewUserFeedback(self):
        raise NotImplementedError

    def viewUserWaste(self):
        raise NotImplementedError

class Superuser:
    def __init__(self):
        pass

    def replyUserQuestion(self):
        raise NotImplementedError

    def updateInformation(self):
        raise NotImplementedError

class RecyclingFacility:
    def __init__(self):
        pass

    def onboardRecyclingCenter(self):
        raise NotImplementedError

    def viewUserStats(self):
        raise NotImplementedError

    def viewFacilityInformation(self):
        raise NotImplementedError

    def viewUserErrorLogs(self):
        raise NotImplementedError

    def viewUserFeedback(self):
        raise NotImplementedError

    def viewUserWaste(self):
        raise NotImplementedError