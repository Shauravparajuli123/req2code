class Date:
    def __init__(self, day, month, hour, second):
        self.day = day
        self.month = month
        self.hour = hour
        self.second = second

class News:
    def __init__(self, title, link, author, date, newspaper):
        self.title = title
        self.link = link
        self.author = author
        self.date = date
        self.newspaper = newspaper
    def publish(self):
        raise NotImplementedError

class Newspaper:
    def __init__(self, language, category):
        self.language = language
        self.category = category
    def publishNews(self):
        raise NotImplementedError