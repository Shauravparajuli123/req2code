from typing import List

class Date:
    def __init__(self, day: int, month: int, year: int, hour: int, minute: int, second: int):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.minute = minute
        self.second = second

class News:
    def __init__(self, title: str, link: str, author: str, date: Date):
        self.title = title
        self.link = link
        self.author = author
        self.date = date

class Newspaper:
    def __init__(self, language: str, publication_date: Date):
        self.language = language
        self.publication_date = publication_date
        self.news = []

    def add_news(self, news: News):
        if news not in self.news:
            self.news.append(news)
        else:
            raise ValueError('News already exists in the newspaper')

    def get_news(self) -> List[News]:
        return self.news
