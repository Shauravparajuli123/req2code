from typing import List

class Agency:
    def deleteObject(self):
        raise NotImplementedError
    def insertObject(self):
        raise NotImplementedError
    def changeData(self):
        raise NotImplementedError
    def returnList(self):
        raise NotImplementedError
    def viewDetail(self):
        raise NotImplementedError
    def viewHistory(self):
        raise NotImplementedError
    def conventionRequest(self):
        raise NotImplementedError
    def editData(self):
        raise NotImplementedError
    def enableAccount(self):
        raise NotImplementedError

class CulturalHeritage:
    def __init__(self, id: str, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description
    def search(self):
        raise NotImplementedError
    def viewDetail(self):
        raise NotImplementedError

class RefreshmentPoint:
    def __init__(self, id: str, name: str, address: str):
        self.id = id
        self.name = name
        self.address = address
    def search(self):
        raise NotImplementedError
    def viewDetail(self):
        raise NotImplementedError
    def viewHistory(self):
        raise NotImplementedError
    def conventionRequest(self):
        raise NotImplementedError
    def editData(self):
        raise NotImplementedError

class TouristAccount:
    def __init__(self, id: str, name: str, status: str):
        self.id = id
        self.name = name
        self.status = status
    def search(self):
        raise NotImplementedError
    def viewDetail(self):
        raise NotImplementedError
    def enableDisable(self):
        raise NotImplementedError

from typing import List, Image, Location, Feedback, Comment

class AccountTourist:
    def __init__(self, data: str):
        self.data = data
        self.feedback: List[Comment] = []

    def modifyData(self) -> None:
        raise NotImplementedError('Change Data')

    def deleteAccount(self) -> None:
        raise NotImplementedError('Delete Account')

class RefreshmentPoint:
    def __init__(self, banners: List[BannerAd], preference: str):
        self.banners: List[BannerAd] = banners
        self.preference = preference

    def checkBanners(self) -> None:
        raise NotImplementedError('Check Point')

    def insertBanner(self) -> None:
        raise NotImplementedError('Insert Banner')

    def removeBanner(self) -> None:
        raise NotImplementedError('Delete BannerAd')

class BannerAd:
    def __init__(self, image: Image, location: Location):
        self.image: Image = image
        self.location: Location = location

    def changeImage(self) -> None:
        raise NotImplementedError('Change Image')

    def insert(self) -> None:
        raise NotImplementedError('Insert Banner')

    def remove(self) -> None:
        raise NotImplementedError('Delete BannerAd')

class News:
    def __init__(self, title: str, content: str):
        self.title: str = title
        self.content: str = content

    def insert(self) -> None:
        raise NotImplementedError('Insert News')

    def delete(self) -> None:
        raise NotImplementedError('Delete News')

    def modify(self) -> None:
        raise NotImplementedError('Change Data')

class Comment:
    def __init__(self, text: str, feedback: Feedback):
        self.text: str = text
        self.feedback: Feedback = feedback

    def edit(self) -> None:
        raise NotImplementedError('Edit Comment')

class Feedback:
    def __init__(self, site: str, comments: List[Comment]):
        self.site: str = site
        self.comments: List[Comment] = comments

    def view(self) -> None:
        raise NotImplementedError('View Feedback')

class Report:
    def __init__(self, location: Location, statistics: str):
        self.location: Location = location
        self.statistics: str = statistics

    def view(self) -> None:
        raise NotImplementedError('View Report')


from typing import String

class User:
    def searchSite(self):
        raise NotImplementedError
    def ensureUser(self):
        raise NotImplementedError
    def supplyLogin(self):
        raise NotImplementedError
    def endSession(self):
        raise NotImplementedError

class GuestUser:
    def requireCreation(self):
        raise NotImplementedError
    def researchHeritage(self):
        raise NotImplementedError

class RegisteredUser:
    def ensureUser(self):
        raise NotImplementedError
    def supplyLogin(self):
        raise NotImplementedError
    def endSession(self):
        raise NotImplementedError

class RestaurantOperator:
    def insertBanner(self):
        raise NotImplementedError
    def changeImage(self):
        raise NotImplementedError
    def deleteBannerAd(self):
        raise NotImplementedError

class SearchTag:
    def removeSearchTag(self):
        raise NotImplementedError
    def insertTagSearch(self):
        raise NotImplementedError

class SystemRequirement:
    def __init__(self, timeLimit: String):
        self.timeLimit = timeLimit
    def searchSite(self):
        raise NotImplementedError

class UseCase:
    pass

from abc import ABC, abstractmethod

class RestaurantOperator:
    @abstractmethod
    def activateEditingFunctionality(self):
        raise NotImplementedError

    @abstractmethod
    def displayMenuForm(self):
        raise NotImplementedError

    @abstractmethod
    def submitForm(self):
        raise NotImplementedError

    @abstractmethod
    def uploadDataMenu(self):
        raise NotImplementedError

    @abstractmethod
    def editMenu(self):
        raise NotImplementedError

    @abstractmethod
    def verifyData(self):
        raise NotImplementedError

    @abstractmethod
    def confirmOperation(self):
        raise NotImplementedError

    @abstractmethod
    def saveChanges(self):
        raise NotImplementedError

    @abstractmethod
    def enableDeletionFunctionality(self):
        raise NotImplementedError

    @abstractmethod
    def displayDeletionForm(self):
        raise NotImplementedError

    @abstractmethod
    def selectDay(self):
        raise NotImplementedError

    @abstractmethod
    def confirmDeletion(self):
        raise NotImplementedError

    @abstractmethod
    def deleteMenu(self):
        raise NotImplementedError

    @abstractmethod
    def enableDataPointFunctionality(self):
        raise NotImplementedError

    @abstractmethod
    def uploadDataPoint(self):
        raise NotImplementedError

    @abstractmethod
    def editDataPoint(self):
        raise NotImplementedError

    @abstractmethod
    def verifyDataPoint(self):
        raise NotImplementedError

    @abstractmethod
    def confirmDataPointChange(self):
        raise NotImplementedError

    @abstractmethod
    def storeDataPoint(self):
        raise NotImplementedError

    @abstractmethod
    def enableConventionRequest(self):
        raise NotImplementedError

    @abstractmethod
    def displayConventionForm(self):
        raise NotImplementedError

    @abstractmethod
    def insertConventionData(self):
        raise NotImplementedError

    @abstractmethod
    def verifyConventionData(self):
        raise NotImplementedError

    @abstractmethod
    def confirmConventionRequest(self):
        raise NotImplementedError

    @abstractmethod
    def sendConventionRequest(self):
        raise NotImplementedError

    @abstractmethod
    def displayStatistics(self):
        raise NotImplementedError

class Tourist:
    @abstractmethod
    def accessSearchPreferences(self):
        raise NotImplementedError

    @abstractmethod
    def uploadSearchPreferences(self):
        raise NotImplementedError

    @abstractmethod
    def editSearchPreferences(self):
        raise NotImplementedError

    @abstractmethod
    def confirmSearchPreferencesChange(self):
        raise NotImplementedError

    @abstractmethod
    def storeSearchPreferences(self):
        raise NotImplementedError

    @abstractmethod
    def accessAccountData(self):
        raise NotImplementedError

    @abstractmethod
    def uploadAccountData(self):
        raise NotImplementedError

    @abstractmethod
    def editAccountData(self):
        raise NotImplementedError

    @abstractmethod
    def verifyAccountData(self):
        raise NotImplementedError

    @abstractmethod
    def confirmAccountDataChange(self):
        raise NotImplementedError

    @abstractmethod
    def storeAccountData(self):
        raise NotImplementedError

    @abstractmethod
    def accessGenericPreferences(self):
        raise NotImplementedError

    @abstractmethod
    def uploadGenericPreferences(self):
        raise NotImplementedError

    @abstractmethod
    def editGenericPreferences(self):
        raise NotImplementedError

    @abstractmethod
    def confirmGenericPreferencesChange(self):
        raise NotImplementedError

    @abstractmethod
    def storeGenericPreferences(self):
        raise NotImplementedError

    @abstractmethod
    def displayFavoriteList(self):
        raise NotImplementedError

    @abstractmethod
    def insertSite(self):
        raise NotImplementedError

    @abstractmethod
    def confirmInsertion(self):
        raise NotImplementedError

    @abstractmethod
    def insertSiteInFavorites(self):
        raise NotImplementedError

    @abstractmethod
    def removeSite(self):
        raise NotImplementedError

    @abstractmethod
    def confirmRemoval(self):
        raise NotImplementedError

    @abstractmethod
    def removeSiteFromFavorites(self):
        raise NotImplementedError

    @abstractmethod
    def activateFeedbackFeature(self):
        raise NotImplementedError

    @abstractmethod
    def verifyFeedback(self):
        raise NotImplementedError

    @abstractmethod
    def submitFeedback(self):
        raise NotImplementedError

    @abstractmethod
    def confirmFeedback(self):
        raise NotImplementedError

    @abstractmethod
    def storeFeedback(self):
        raise NotImplementedError

from typing import List

class Tourist:
    def editComment(self) -> None:
        raise NotImplementedError

    def entryCondition(self) -> None:
        raise NotImplementedError

    def returnPosition(self) -> Location:
        raise NotImplementedError

    def searchSite(self) -> None:
        raise NotImplementedError

    def viewDetail(self) -> None:
        raise NotImplementedError
class Comment:
    def __init__(self, text: str, site: Site):
        self.text = text
        self.site = site

    def edit(self) -> None:
        raise NotImplementedError
class Site:
    def __init__(self, name: str, location: Location):
        self.name = name
        self.location = location

    def search(self) -> None:
        raise NotImplementedError
class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def getPosition(self) -> tuple:
        raise NotImplementedError
class Connection:
    def interrupt(self) -> None:
        raise NotImplementedError