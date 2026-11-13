from datetime import date

class News:
    def __init__(self, title: str, link: str, author: str, date: date):
        self.title = title
        self.link = link
        self.author = author
        self.date = date

    def display(self):
        raise NotImplementedError('display method not implemented')

class Newspaper:
    def __init__(self, language: str, published_date: date):
        self.language = language
        self.published_date = published_date

    def __str__(self):
        return f'Newspaper(language={self.language}, published_date={self.published_date})'
