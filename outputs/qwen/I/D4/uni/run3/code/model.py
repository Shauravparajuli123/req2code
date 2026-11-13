from typing import List

class Student:
    def __init__(self, name: str):
        self.name: str = name

class Professor:
    def __init__(self, name: str):
        self.name: str = name

class Course:
    def __init__(self, name: str, credits: int, professors: List[Professor], students: List[Student]):
        self.name: str = name
        self.credits: int = credits
        self.professors: List[Professor] = professors
        self.students: List[Student] = students

class Dormitory:
    def __init__(self, price: float):
        self.price: float = price
        self.students: List[Student] = []
