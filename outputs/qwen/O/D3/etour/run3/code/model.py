class CulturalHeritage:
    def __init__(self, id):
        self.id = id
    def delete(self):
        raise NotImplementedError

class RefreshmentPoint:
    def __init__(self, id):
        self.id = id
    def delete(self):
        raise NotImplementedError
    def viewHistory(self):
        raise NotImplementedError
class TouristAccount:
    def __init__(self, id):
        self.id = id
    def enableDisable(self):
        raise NotImplementedError
class SystemRequirement:
    def __init__(self, criteria):
        self.criteria = criteria
class UseCase:
    def __init__(self, description):
        self.description = description

from typing import List

class Account:
    def __init__(self, id: str):
        self.id = id

class AccountTourist(Account):
    pass

class Agency:
    def __init__(self, id: str):
        self.id = id

class Banner:
    def __init__(self, id: str):
        self.id = id

class BannerAd(Banner):
    pass

class Comment:
    def __init__(self, id: str):
        self.id = id

class DataNews:
    def __init__(self, id: str):
        self.id = id

class Feedback:
    def __init__(self, id: str):
        self.id = id

class News:
    def __init__(self, id: str):
        self.id = id

class RefreshmentPoint:
    def __init__(self, id: str):
        self.id = id

class Tourist(AccountTourist):
    pass

class UseCase:
    def __init__(self, id: str):
        self.id = id

# Use case methods

class ChangeData:
    def __init__(self, agency: Agency, tourist: Tourist):
        self.agency = agency
        self.tourist = tourist
    def execute(self):
        raise NotImplementedError

class DeleteAccount:
    def __init__(self, agency: Agency, tourist: Tourist):
        self.agency = agency
        self.tourist = tourist
    def execute(self):
        raise NotImplementedError

class DeleteBannerAd:
    def __init__(self, agency: Agency, banner_ad: BannerAd):
        self.agency = agency
        self.banner_ad = banner_ad
    def execute(self):
        raise NotImplementedError

class DeleteNews:
    def __init__(self, agency: Agency, news: News):
        self.agency = agency
        self.news = news
    def execute(self):
        raise NotImplementedError

class EditComment:
    def __init__(self, agency: Agency, feedback: Feedback, comment: Comment):
        self.agency = agency
        self.feedback = feedback
        self.comment = comment
    def execute(self):
        raise NotImplementedError

class InsertBanner:
    def __init__(self, agency: Agency, banner: Banner):
        self.agency = agency
        self.banner = banner
    def execute(self):
        raise NotImplementedError

class InsertNews:
    def __init__(self, agency: Agency, news: News):
        self.agency = agency
        self.news = news
    def execute(self):
        raise NotImplementedError

class ViewFeedback:
    def __init__(self, agency: Agency, feedback: Feedback):
        self.agency = agency
        self.feedback = feedback
    def execute(self):
        raise NotImplementedError

class ViewReport:
    def __init__(self, agency: Agency, refreshment_point: RefreshmentPoint):
        self.agency = agency
        self.refreshment_point = refreshment_point
    def execute(self):
        raise NotImplementedError

class TagSearch:
    def __init__(self, searchTag):
        self.searchTag = searchTag
    def askSearchTag(self):
        raise NotImplementedError

class SearchTag:
    def __init__(self, tag):
        self.tag = tag
    def removeSearchTag(self):
        raise NotImplementedError

class BannerAd:
    def __init__(self, image):
        self.image = image
    def insertBanner(self):
        raise NotImplementedError
    def changeImage(self):
        raise NotImplementedError
    def deleteBanner(self):
        raise NotImplementedError

class Image:
    def __init__(self, path):
        self.path = path

class Operation:
    def __init__(self, status):
        self.status = status
    def confirmation(self):
        raise NotImplementedError

class RestaurantOperator:
    def __init__(self, username):
        self.username = username
    def changeMenu(self):
        raise NotImplementedError
    def deleteMenu(self):
        raise NotImplementedError
    def changeDataPoint(self):
        raise NotImplementedError
    def requireConvention(self):
        raise NotImplementedError
class Tourist:
    def __init__(self, username):
        self.username = username
    def editPreferences(self):
        raise NotImplementedError
    def editSearchPreference(self):
        raise NotImplementedError
    def changeData(self):
        raise NotImplementedError
    def insertSite(self):
        raise NotImplementedError
    def deleteSite(self):
        raise NotImplementedError
    def insertFeedback(self):
        raise NotImplementedError
class Menu:
    def __init__(self):
        self.days = []
    def editMenu(self):
        raise NotImplementedError
class Day:
    def __init__(self, date):
        self.date = date
    def submitForm(self):
        raise NotImplementedError
class DataPoint:
    def __init__(self):
        self.refreshments = []
    def changeData(self):
        raise NotImplementedError
class Refreshment:
    def __init__(self, name):
        self.name = name
class Convention:
    def __init__(self, agreement):
        self.agreement = agreement
    def requestConvention(self):
        raise NotImplementedError
class Statistic:
    def __init__(self, data):
        self.data = data
    def viewStatistic(self):
        raise NotImplementedError

class Comment:
    def __init__(self, text):
        self.text = text

    def edit(self):
        raise NotImplementedError

class Feedback:
    def __init__(self, tourist):
        self.tourist = tourist

class Position:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class SearchForm:
    def submit(self):
        raise NotImplementedError

class Area:
    def __init__(self, name):
        self.name = name