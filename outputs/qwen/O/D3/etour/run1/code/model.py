class Agency:
    def __init__(self):
        pass

class Object:
    def __init__(self, id):
        self.id = id
    def delete(self):
        raise NotImplementedError
    def insert(self):
        raise NotImplementedError
    def change(self):
        raise NotImplementedError
class List:
    def __init__(self, criteria):
        self.criteria = criteria
    def search(self):
        raise NotImplementedError
class Detail:
    def __init__(self, id):
        self.id = id
    def view(self):
        raise NotImplementedError
class History:
    def __init__(self, id):
        self.id = id
    def view(self):
        raise NotImplementedError
class Account:
    def __init__(self, id):
        self.id = id
    def enable(self):
        raise NotImplementedError

class Account:
    def __init__(self, data):
        self.data = data

    def changeData(self):
        raise NotImplementedError

class BannerAd:
    def __init__(self, image):
        self.image = image

    def changeImage(self):
        raise NotImplementedError
class News:
    def __init__(self, title):
        self.title = title

    def changeData(self):
        raise NotImplementedError
    def delete(self):
        raise NotImplementedError
class Comment:
    def __init__(self, text):
        self.text = text

    def edit(self):
        raise NotImplementedError
class Image:
    pass
class Connection:
    def __init__(self, interruption):
        self.interruption = interruption

class UseCase:
    pass

class User:
    def __init__(self, username):
        self.username = username
    def login(self):
        pass
    def __str__(self):
        return self.username

class Account:
    def __init__(self, password):
        self.password = password
    def verifyPassword(self, password):
        pass
    def __str__(self):
        return self.password

class Operation:
    def confirm(self):
        pass

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def checkCredentials(self):
        pass

class TagSearch:
    def __init__(self, searchTag):
        self.searchTag = searchTag
    def insert(self):
        pass

class SearchTag:
    def __init__(self, tag):
        self.tag = tag
    def remove(self):
        pass

class BannerAd:
    def __init__(self, image):
        self.image = image
    def edit(self):
        pass
    def delete(self):
        pass

class Image:
    def __init__(self, path):
        self.path = path
    def validate(self):
        pass

class Computer:
    def __init__(self, siteList):
        self.siteList = siteList
    def searchSite(self):
        pass


class Restaurant:
    def __init__(self):
        self.menu = None

    def changeMenu(self, day):
        raise NotImplementedError

class EditMenu:
    def __init__(self, day):
        self.day = day

    def edit(self):
        raise NotImplementedError
class Day:
    def __init__(self, date):
        self.date = date
class MenuSelection:
    def __init__(self, day):
        self.day = day

    def delete(self):
        raise NotImplementedError
class Feedback:
    def __init__(self, site, comment):
        self.site = site
        self.comment = comment

    def insert(self):
        raise NotImplementedError
class Tourist:
    def __init__(self):
        self.searchPreferences = None
        self.data = None

    def editPreferences(self):
        raise NotImplementedError
    def changeData(self):
        raise NotImplementedError
class SearchPreference:
    def __init__(self, preferences):
        self.preferences = preferences

    def edit(self):
        raise NotImplementedError
class Account:
    def __init__(self, data):
        self.data = data

    def change(self):
        raise NotImplementedError

class Comment:
    def __init__(self, alteration):
        self.alteration = alteration
    def editComment(self):
        raise NotImplementedError

class Feedback:
    pass
class Position:
    pass
class SearchForm:
    pass
class Site:
    pass
class Connection:
    def __init__(self, server):
        self.server = server
class EventsUserSystem:
    def __init__(self, flow):
        self.flow = flow
class Notification:
    def __init__(self, reading):
        self.reading = reading
class Gps:
    def calculatePosition(self):
        raise NotImplementedError
class Area:
    pass
class QualityRequirement:
    pass
class Result:
    pass