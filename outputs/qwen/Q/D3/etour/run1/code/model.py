from typing import Optional

class Boolean:
    pass

class Agency:
    def __init__(self, logged: bool):
        self.logged = logged
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

class Tourist:
    def returnList(self):
        raise NotImplementedError

class CulturalHeritage:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
    def delete(self):
        raise NotImplementedError
    def insert(self):
        raise NotImplementedError
    def changeData(self):
        raise NotImplementedError
    def viewDetail(self):
        raise NotImplementedError

class RefreshmentPoint:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
    def delete(self):
        raise NotImplementedError
    def viewDetail(self):
        raise NotImplementedError
    def viewHistory(self):
        raise NotImplementedError
    def editData(self):
        raise NotImplementedError

class Account:
    def __init__(self, id: str, status: bool):
        self.id = id
        self.status = status
    def enable(self):
        raise NotImplementedError

class TouristAccount:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
    def viewDetail(self):
        raise NotImplementedError

class SystemRequirement:
    def __init__(self, criteria: str):
        self.criteria = criteria
    def returnList(self):
        raise NotImplementedError

from typing import List, String, Boolean, Image, Comment

class Agency:
    def __init__(self, logged: Boolean):
        self.logged = logged
    def searchTourist(self):
        raise NotImplementedError
    def searchRefreshmentPoint(self):
        raise NotImplementedError
    def changeData(self):
        raise NotImplementedError
    def changeImage(self):
        raise NotImplementedError
    def checkPoint(self):
        raise NotImplementedError
    def deleteAccount(self):
        raise NotImplementedError
    def deleteBannerAd(self):
        raise NotImplementedError
    def deleteNews(self):
        raise NotImplementedError
    def editComment(self):
        raise NotImplementedError
    def insertBanner(self):
        raise NotImplementedError
    def insertNews(self):
        raise NotImplementedError
    def viewFeedback(self):
        raise NotImplementedError
    def viewReport(self):
        raise NotImplementedError

class Account:
    def __init__(self, data: String):
        self.data = data

class BannerAd:
    def __init__(self, image: Image, pointOfRest: Rest):
        self.image = image
        self.pointOfRest = pointOfRest
    def changeImage(self):
        raise NotImplementedError

class Banner:
    def __init__(self, image: Image):
        self.image = image

class Image:
    def __init__(self, path: String):
        self.path = path

class News:
    def __init__(self, content: String, amendment: String):
        self.content = content
        self.amendment = amendment
    def changeData(self):
        raise NotImplementedError
    def insert(self):
        raise NotImplementedError
    def delete(self):
        raise NotImplementedError

class Feedback:
    def __init__(self, comments: List[Comment]):
        self.comments = comments
    def view(self):
        raise NotImplementedError
    def editComment(self):
        raise NotImplementedError

class Comment:
    def __init__(self, text: String):
        self.text = text
    def edit(self):
        raise NotImplementedError

class Rest:
    def __init__(self, banners: List[BannerAd]):
        self.banners = banners
    def checkPoint(self):
        raise NotImplementedError
    def insertBanner(self):
        raise NotImplementedError
    def deleteBannerAd(self):
        raise NotImplementedError

class Site:
    def __init__(self, feedbacks: List[Feedback]):
        self.feedbacks = feedbacks
    def viewFeedback(self):
        raise NotImplementedError

class Report:
    def __init__(self, data: String):
        self.data = data
    def view(self):
        raise NotImplementedError

from typing import List, Optional

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def ensureUser(self):
        raise NotImplementedError

    def supplyLogin(self):
        raise NotImplementedError

    def askSearchTag(self):
        raise NotImplementedError

    def insertTagSearch(self):
        raise NotImplementedError

    def endSession(self):
        raise NotImplementedError

class Visitor:
    def searchSite(self):
        raise NotImplementedError

    def requireCreation(self):
        raise NotImplementedError

    def researchHeritage(self):
        raise NotImplementedError

class RegisteredUser(User):
    def removeSearchTag(self):
        raise NotImplementedError

    def changeImage(self):
        raise NotImplementedError

    def deleteBannerAd(self):
        raise NotImplementedError

    def insertBanner(self):
        raise NotImplementedError

class RestaurantOperator(User):
    def insertBanner(self):
        raise NotImplementedError

    def changeImage(self):
        raise NotImplementedError

    def deleteBannerAd(self):
        raise NotImplementedError

class SearchTag:
    def __init__(self, tag: str):
        self.tag = tag

class TagSearch:
    def __init__(self, searchCriterion: str):
        self.searchCriterion = searchCriterion

class BannerAd:
    def __init__(self, image: Image):
        self.image = image

class Image:
    def __init__(self, path: str):
        self.path = path

from typing import TypedDict, Integer, String, Day, Menu, RestaurantOperator, Tourist, Site, Feedback, Favorite, Statistic, Convention, DataPoint

class Day(TypedDict):
    name: String

class Menu(TypedDict):
    day: Day

class DataPoint(TypedDict):
    refreshment: String

class Convention(TypedDict):
    agreement: String

class Statistic(TypedDict):
    pass

class RestaurantOperator:
    def changeMenu(self) -> None:
        raise NotImplementedError

def deleteMenu(self) -> None:
        raise NotImplementedError

def changeDataPoint(self) -> None:
        raise NotImplementedError

def requireConvention(self) -> None:
        raise NotImplementedError

def viewStatistic(self) -> None:
        raise NotImplementedError

class Tourist:
    def editSearchPreference(self) -> None:
        raise NotImplementedError

def editAccountData(self) -> None:
        raise NotImplementedError

def insertSite(self) -> None:
        raise NotImplementedError

def insertFeedback(self) -> None:
        raise NotImplementedError

def viewFavoriteList(self) -> None:
        raise NotImplementedError

def viewVisitedSites(self) -> None:
        raise NotImplementedError

class Site(TypedDict):
    pass

class Feedback(TypedDict):
    vote: Integer
    comment: String

class Favorite(TypedDict):
    site: Site


from typing import Optional

class Position:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

class Comment:
    def __init__(self, text: str, site: 'Site'):
        self.text = text
        self.site = site
    def alterComment(self):
        raise NotImplementedError('UC54')

class Site:
    def __init__(self, name: str):
        self.name = name

class Tourist:
    def __init__(self, authenticationStatus: bool, position: Position):
        self.authenticationStatus = authenticationStatus
        self.position = position
    def chooseToChangeComment(self):
        raise NotImplementedError('UC54')
    def viewDetails(self):
        raise NotImplementedError('UC58')
    def searchSite(self):
        raise NotImplementedError('UC57')
    def returnPosition(self):
        raise NotImplementedError('UC56')

class Gps:
    def calculatePosition(self) -> Optional[Position]:
        raise NotImplementedError('UC56')

class Connection:
    def notifyInterruption(self):
        raise NotImplementedError('UC54, UC58')

class Feedback:
    pass

class EventsUserSystem:
    pass