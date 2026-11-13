class Cultural:
    def __init__(self, id):
        self.id = id

    def delete(self):
        raise NotImplementedError

    def insert(self):
        raise NotImplementedError

    def change(self):
        raise NotImplementedError

    def search(self):
        raise NotImplementedError

    def viewDetail(self):
        raise NotImplementedError

    def viewHistory(self):
        raise NotImplementedError

class RefreshmentPoint:
    def __init__(self, id):
        self.id = id

    def delete(self):
        raise NotImplementedError

    def insert(self):
        raise NotImplementedError

    def change(self):
        raise NotImplementedError

    def search(self):
        raise NotImplementedError

    def viewDetail(self):
        raise NotImplementedError

    def viewHistory(self):
        raise NotImplementedError
class Account:
    def __init__(self, id):
        self.id = id

    def enable(self):
        raise NotImplementedError
class Tourist:
    def __init__(self, id):
        self.id = id
class Connection:
    def __init__(self, status):
        self.status = status
class QualityRequirement:
    def __init__(self, criteria):
        self.criteria = criteria

from typing import List, Optional

class Account:
    pass
class AccountTourist:
    def __init__(self, id: int):
        self.id = id
    def changeData(self):
        raise NotImplementedError
class BannerAd:
    def __init__(self, id: int, image: Image):
        self.id = id
        self.image = image
    def changeImage(self):
        raise NotImplementedError
class Characteristics:
    def __init__(self, valid: bool):
        self.valid = valid
class Computer:
    def __init__(self, connection: Connection):
        self.connection = connection
class Connection:
    def __init__(self, interruption: Interruption):
        self.interruption = interruption
class DataNews:
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content
    def insert(self):
        raise NotImplementedError
    def delete(self):
        raise NotImplementedError
    def changeData(self):
        raise NotImplementedError
class Image:
    def __init__(self, path: str):
        self.path = path
    def change(self):
        raise NotImplementedError
class Interruption:
    pass
class Location:
    def __init__(self, id: int):
        self.id = id
    def viewReport(self):
        raise NotImplementedError
class RefreshmentPoint:
    def __init__(self, id: int, banners: List[BannerAd]):
        self.id = id
        self.banners = banners
    def checkPoint(self):
        raise NotImplementedError
    def insertBanner(self):
        raise NotImplementedError
    def removeBanner(self):
        raise NotImplementedError
class Report:
    def __init__(self, location: Location, feedback: List[Feedback]):
        self.location = location
        self.feedback = feedback
    def generate(self):
        raise NotImplementedError
class Restaurant:
    def __init__(self, id: int, refreshmentPoints: List[RefreshmentPoint]):
        self.id = id
        self.refreshmentPoints = refreshmentPoints
class SearchSite:
    def search(self):
        raise NotImplementedError
class SearchTourist:
    def search(self):
        raise NotImplementedError
class State:
    def __init__(self, valid: bool):
        self.valid = valid
class Transaction:
    def __init__(self, request: Request):
        self.request = request
    def confirm(self):
        raise NotImplementedError
class UseCase:
    pass
class UserInteraction:
    def __init__(self, computer: Computer):
        self.computer = computer
    def activateUseCase(self, use_case: UseCase):
        raise NotImplementedError

class SearchTag:
    def __init__(self, tag):
        self.tag = tag
    def askSearchTag(self):
        raise NotImplementedError

class TagSearch:
    def __init__(self, searchTag):
        self.searchTag = searchTag
    def insertTagSearch(self):
        raise NotImplementedError

class SearchSite:
    def __init__(self, site):
        self.site = site
    def searchSite(self):
        raise NotImplementedError

class RestaurantOperator:
    def __init__(self):
        pass
    def insertBanner(self):
        raise NotImplementedError
    def changeImage(self):
        raise NotImplementedError
    def deleteBannerAd(self):
        raise NotImplementedError

class GuestUser:
    def __init__(self):
        pass
    def requireCreation(self):
        raise NotImplementedError
    def searchSite(self):
        raise NotImplementedError

class RegisteredUser:
    def __init__(self):
        pass
    def ensureUser(self):
        raise NotImplementedError
    def supplyLogin(self):
        raise NotImplementedError
    def endSession(self):
        raise NotImplementedError


class Menu:
    def __init__(self):
        self.days = []
    def editMenu(self):
        raise NotImplementedError

class Day:
    def __init__(self, date):
        self.date = date
        self.menuItems = []

class MenuItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Operator:
    def __init__(self, username):
        self.username = username

class Tourist:
    def __init__(self, username):
        self.username = username

class Preference:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class SearchPreference(Preference):
    def __init__(self, type, value):
        super().__init__(type, value)

class Account:
    def __init__(self, username, preferences):
        self.username = username
        self.preferences = preferences

class RefreshmentPoint:
    def __init__(self, name, operator):
        self.name = name
        self.operator = operator

class Convention:
    def __init__(self, date, operator):
        self.date = date
        self.operator = operator

class User:
    def __init__(self):
        pass

class Connection:
    def __init__(self):
        pass

class QualityRequirement:
    def __init__(self):
        pass

class Visitor:
    def __init__(self):
        pass

class AdvancedSearchForm:
    def __init__(self):
        pass

class Feedback:
    def __init__(self):
        pass

class Site:
    def __init__(self):
        pass

class SearchResult:
    def __init__(self):
        pass

class Position:
    def __init__(self):
        pass

class Comment:
    def __init__(self):
        pass

# Use case methods

class EditComment:
    def __init__(self, user, feedback):
        self.user = user
        self.feedback = feedback
    def edit_comment(self):
        raise NotImplementedError

class EntryCondition:
    def __init__(self, user, feedback):
        self.user = user
        self.feedback = feedback
    def entry_condition(self):
        raise NotImplementedError

class ReturnPosition:
    def __init__(self, user, site):
        self.user = user
        self.site = site
    def return_position(self):
        raise NotImplementedError

class SearchSite:
    def __init__(self, user, site):
        self.user = user
        self.site = site
    def search_site(self):
        raise NotImplementedError

class ViewDetail:
    def __init__(self, user, site):
        self.user = user
        self.site = site
    def view_detail(self):
        raise NotImplementedError