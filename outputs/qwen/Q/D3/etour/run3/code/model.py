from typing import TypedDict, List

class Agency:
    def deleteObject(self) -> None:
        raise NotImplementedError
    def insertObject(self) -> None:
        raise NotImplementedError
    def changeData(self) -> None:
        raise NotImplementedError
    def returnList(self) -> List[str]:
        raise NotImplementedError
    def viewDetail(self) -> None:
        raise NotImplementedError
    def viewHistory(self) -> None:
        raise NotImplementedError
    def conventionRequest(self) -> None:
        raise NotImplementedError
    def editData(self) -> None:
        raise NotImplementedError
    def enableAccount(self) -> None:
        raise NotImplementedError

class CulturalHeritage(TypedDict):
    id: str
    name: str
    description: str

class RefreshmentPoint(TypedDict):
    id: str
    name: str
    address: str

class TouristAccount(TypedDict):
    id: str
    name: str
    email: str

class System:
    def returnList(self) -> List[str]:
        raise NotImplementedError
    def search(self) -> List[str]:
        raise NotImplementedError


from typing import TypedDict, String, Integer, Image, Point, String, List, Optional

class Agency:
    def searchTourist(self) -> None:
        raise NotImplementedError

    def searchRefreshmentPoint(self) -> None:
        raise NotImplementedError

    def searchSite(self) -> None:
        raise NotImplementedError

    def changeData(self) -> None:
        raise NotImplementedError

    def changeImage(self) -> None:
        raise NotImplementedError

    def checkPoint(self) -> None:
        raise NotImplementedError

    def deleteAccount(self) -> None:
        raise NotImplementedError

    def deleteBannerAd(self) -> None:
        raise NotImplementedError

    def deleteNews(self) -> None:
        raise NotImplementedError

    def editComment(self) -> None:
        raise NotImplementedError

    def insertBanner(self) -> None:
        raise NotImplementedError

    def insertNews(self) -> None:
        raise NotImplementedError

    def viewFeedback(self) -> None:
        raise NotImplementedError

    def viewReport(self) -> None:
        raise NotImplementedError

class AccountTourist(TypedDict):
    id: String
    name: String

class BannerAd:
    id: String
    image: Image
    location: Point

class Banner:
    id: String
    image: Image
    location: Point

class Comment(TypedDict):
    id: String
    text: String

class DataNews(TypedDict):
    id: String
    title: String
    content: String

class Feedback(TypedDict):
    id: String
    text: String
    rating: Integer

class Image(TypedDict):
    id: String
    path: String

class Point(TypedDict):
    id: String
    name: String

class Tourist(TypedDict):
    id: String
    name: String


from typing import TypedDict, List

class GuestUser:
    username: str
    password: str

    def supplyLogin(self) -> None:
        raise NotImplementedError

    def ensureUser(self) -> None:
        raise NotImplementedError

    def researchHeritage(self) -> None:
        raise NotImplementedError

    def searchSite(self) -> List[str]:
        raise NotImplementedError

class RegisteredUser:
    username: str
    password: str

    def login(self) -> None:
        raise NotImplementedError

    def endSession(self) -> None:
        raise NotImplementedError

class RestaurantOperator:
    restaurantName: str

    def insertBanner(self) -> None:
        raise NotImplementedError

    def changeImage(self) -> None:
        raise NotImplementedError

    def deleteBannerAd(self) -> None:
        raise NotImplementedError

class SearchTag:
    tagName: str

    def removeSearchTag(self) -> None:
        raise NotImplementedError

class TagSearch:
    searchCriteria: str

    def insertTagSearch(self) -> None:
        raise NotImplementedError

from typing import TypedDict, Integer

class Day(TypedDict):
    name: str

class Menu:
    def __init__(self, day: Day):
        self.day = day
    def edit(self) -> None:
        raise NotImplementedError
    def delete(self) -> None:
        raise NotImplementedError

class DataPoint:
    def __init__(self, refreshment: str):
        self.refreshment = refreshment
    def change(self) -> None:
        raise NotImplementedError

class Convention:
    def __init__(self, agreement: str):
        self.agreement = agreement
    def request(self) -> None:
        raise NotImplementedError

class Statistic:
    def view(self) -> None:
        raise NotImplementedError

class SearchPreference:
    def edit(self) -> None:
        raise NotImplementedError

class Site:
    def __init__(self, name: str):
        self.name = name
    def insert(self) -> None:
        raise NotImplementedError
    def delete(self) -> None:
        raise NotImplementedError

class Feedback:
    def __init__(self, vote: Integer, comment: str):
        self.vote = vote
        self.comment = comment
    def insert(self) -> None:
        raise NotImplementedError

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
    def insertSite(self) -> None:
        raise NotImplementedError
    def deleteSite(self) -> None:
        raise NotImplementedError
    def viewList(self) -> None:
        raise NotImplementedError
    def insertFeedback(self) -> None:
        raise NotImplementedError

from typing import TypedDict

class Position:
    pass

class Comment:
    def alteration(self) -> None:
        raise NotImplementedError

class Change:
    def confirmation(self) -> None:
        raise NotImplementedError

class Confirmation:
    pass

class Feedback:
    pass

class Connection:
    def interruption(self) -> None:
        raise NotImplementedError

class Etour:
    pass

class EventsUserSystem:
    pass

class Gps:
    def calculatePosition(self) -> None:
        raise NotImplementedError

class Interruption:
    pass

class Notification:
    def reading(self) -> None:
        raise NotImplementedError

class Operation:
    pass

class QualityRequirement:
    pass

class Result:
    pass

class Search:
    def advancedSearch(self) -> None:
        raise NotImplementedError

class SearchForm:
    pass

class Server:
    pass

class Site:
    pass

class State:
    pass

class Transaction:
    pass

class User:
    pass

class UserInteraction:
    pass

class Area:
    pass

class Card:
    pass

class Form:
    pass

class Flow:
    pass

class Tourist:
    def __init__(self, position: Position):
        self.position = position
    def editComment(self) -> None:
        raise NotImplementedError
    def entryEntryCondition(self) -> None:
        raise NotImplementedError
    def returnPosition(self) -> None:
        raise NotImplementedError
    def searchSite(self) -> None:
        raise NotImplementedError
    def viewDetail(self) -> None:
        raise NotImplementedError