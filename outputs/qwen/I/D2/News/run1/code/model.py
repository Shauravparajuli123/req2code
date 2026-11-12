from typing import List, Tuple

class News:
    def __init__(self, title: str, link: str, author: str):
        self.title = title
        self.link = link
        self.author = author
        self.date: Tuple[str, int, int, int] = ('', 0, 0, 0)

    def set_date(self, day_of_week: str, month: int, hours: int, seconds: int):
        self.date = (day_of_week, month, hours, seconds)

    def publish_on(self, newspaper: 'Newspaper', date: Tuple[str, int, int, int]) -> None:
        newspaper.include_news(self, date)

class Newspaper:
    def __init__(self, language: str):
        self.language = language
        self.news: List[News] = []

    def include_news(self, news: News, date: Tuple[str, int, int, int]) -> None:
        if any(n for n in self.news if n.title == news.title):
            raise ValueError("News already included in this newspaper.")
        news.set_date(*date)
        self.news.append(news)
