from typing import List, Tuple

class Date:
    def __init__(self, day_of_week: str, month: int, hours: int, seconds: int):
        self.day_of_week = day_of_week
        self.month = month
        self.hours = hours
        self.seconds = seconds

class News:
    def __init__(self, title: str, link: str, author: str):
        self.title = title
        self.link = link
        self.author = author
        self.publication_date: Date = None
        self.category: str = None

class Newspaper:
    def __init__(self, language: str, publication_date: Date):
        self.language = language
        self.publication_date = publication_date
        self.news: List[News] = []

    def add_news(self, news: News):
        if news not in self.news:
            self.news.append(news)
        else:
            raise ValueError('News already exists in this newspaper')

    def get_news_by_category(self, category: str) -> List[News]:
        return [news for news in self.news if news.category == category]
