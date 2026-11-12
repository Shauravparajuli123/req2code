class News:
    def __init__(self, title, link, author, date):
        self.title = title
        self.link = link
        self.author = author
        self.date = date

    def publish(self):
        raise NotImplementedError

class Newspaper:
    def __init__(self, language, published_date, category):
        self.language = language
        self.publishedDate = published_date
        self.category = category
        self.news = []

    def publishNews(self, news):
        self.news.append(news)
        raise NotImplementedError