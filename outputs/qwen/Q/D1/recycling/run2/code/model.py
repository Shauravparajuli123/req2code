from typing import List, Optional, Union, Literal, TypedDict

class PickType(str, Enum):
    morning = 'morning'
    afternoon = 'afternoon'
    evening = 'evening'

class User(TypedDict):
    emailId: str
    profile: Profile
    activity: str
    stat: User.stat

class Profile(TypedDict):
    favorites: List[RecyclingCenter]

class Admin(TypedDict):
    dashboard: Dashboard
    data: Admin.haveData

class RecyclingFacility(TypedDict):
    openingHour: Hour
    material: Material
    location: Location

class RecyclingfacilityRepresentative(TypedDict):
    material: Material

class Company(TypedDict):
    performance: str

class Executive(TypedDict):
    access: Executive.haveAccess

class Developer(TypedDict):
    apiAccess: bool
    bootstrap: bool

class Employee(TypedDict):
    accessRoutePlanningSystem: bool

class Superuser(TypedDict):
    replyUserQuestion: bool
    viewStat: bool

class RecyclingCenter(TypedDict):
    location: Location

class RecyclingCenterInformation(TypedDict):
    material: Material
    openingHour: Hour

class Notification(TypedDict):
    getNotification: bool

class Feedback(TypedDict):
    pass

class Hour(TypedDict):
    pass

class Pick(TypedDict):
    type: PickType

class Schedule(TypedDict):
    pass

class Location(TypedDict):
    pass

class MapDisplay(TypedDict):
    pass

class DisposalEvent(TypedDict):
    pass

class UserDocumentation(TypedDict):
    pass

class UserErrorLog(TypedDict):
    pass

class ActivityFee(TypedDict):
    pass

class Dashboard(TypedDict):
    pass

class AdminHaveData(TypedDict):
    pass

class UserStat(TypedDict):
    pass

class User:
    def clickAddress(self) -> None:
        raise NotImplementedError
    def enterZipCode(self) -> None:
        raise NotImplementedError
    def getFeedback(self) -> None:
        raise NotImplementedError
    def getHour(self) -> None:
        raise NotImplementedError
    def giveEmailId(self) -> None:
        raise NotImplementedError
    def createAccount(self) -> None:
        raise NotImplementedError
    def browseList(self) -> None:
        raise NotImplementedError
    def checkTransactionHistory(self) -> None:
        raise NotImplementedError
    def choosePick(self) -> None:
        raise NotImplementedError
    def uploadSchedule(self) -> None:
        raise NotImplementedError
    def viewInformation(self) -> None:
        raise NotImplementedError
    def viewLocation(self) -> None:
        raise NotImplementedError
    def viewMapDisplay(self) -> None:
        raise NotImplementedError
    def viewDisposalEvent(self) -> None:
        raise NotImplementedError
    def viewUserDocumentation(self) -> None:
        raise NotImplementedError
    def viewUserErrorLog(self) -> None:
        raise NotImplementedError
    def viewActivityFee(self) -> None:
        raise NotImplementedError
    def viewDashboard(self) -> None:
        raise NotImplementedError
    def viewStat(self) -> None:
        raise NotImplementedError
    def linkEmailAccount(self) -> None:
        raise NotImplementedError
    def contactAdministrator(self) -> None:
        raise NotImplementedError
    def selectType(self) -> None:
        raise NotImplementedError

class Admin:
    def handleActivity(self) -> None:
        raise NotImplementedError
    def haveAccess(self) -> None:
        raise NotImplementedError
    def onboardRecyclingCenter(self) -> None:
        raise NotImplementedError
    def readFeedback(self) -> None:
        raise NotImplementedError
    def viewDashboard(self) -> None:
        raise NotImplementedError

class RecyclingFacility:
    def communicateSite(self) -> None:
        raise NotImplementedError
    def updateInformation(self) -> None:
        raise NotImplementedError

class RecyclingfacilityRepresentative:
    def updateInformation(self) -> None:
        raise NotImplementedError

class Company:
    def haveWebsite(self) -> None:
        raise NotImplementedError

class Executive:
    def haveAccess(self) -> None:
        raise NotImplementedError

class Developer:
    def useBootstrap(self) -> None:
        raise NotImplementedError

class Employee:
    def accessRoutePlanningSystem(self) -> None:
        raise NotImplementedError

class Superuser:
    def replyUserQuestion(self) -> None:
        raise NotImplementedError
    def viewStat(self) -> None:
        raise NotImplementedError

class RecyclingCenter:
    pass

class RecyclingCenterInformation:
    def addRecyclingCenterInformation(self) -> None:
        raise NotImplementedError

class Notification:
    def getNotification(self) -> None:
        raise NotImplementedError
