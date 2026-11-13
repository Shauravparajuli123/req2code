from typing import List, Optional
from datetime import datetime

class Date:
    def __init__(self, dayOfWeek: str, month: str, hour: int, second: int):
        self.dayOfWeek = dayOfWeek
        self.month = month
        self.hour = hour
        self.second = second

    def __str__(self):
        return f'{self.dayOfWeek}, {self.month} at {self.hour}:{self.second:02d}

class News:
    def __init__(self, title: str, link: str, author: str, date: Date):
        self.title = title
        self.link = link
        self.author = author
        self.date = date

    def publish(self) -> None:
        raise NotImplementedError

    def report(self) -> None:
        raise NotImplementedError

    def __str__(self):
        return f'News: {self.title} by {self.author} on {self.date}
'

class Newspaper:
    def __init__(self, language: str):
        self.language = language
        self.news: List[News] = []

    def publishNews(self, news: News) -> None:
        raise NotImplementedError

    def reportNews(self, news: News) -> None:
        raise NotImplementedError

    def addNews(self, news: News) -> None:
        self.news.append(news)

    def __str__(self):
        return f'Newspaper in {self.language} with {len(self.news)} news
'