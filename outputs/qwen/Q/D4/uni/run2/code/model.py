from typing import List

class Course:
    def __init__(self, name: str, credits: int):
        self.name = name
        self.credits = credits
        self.professors: List[Professor] = []
        self.students: List[Student] = []

    def enrollStudent(self, student: Student):
        # R5
        self.students.append(student)
        if len(self.students) < 5:
            raise ValueError('A course must have at least five students.')

    def accommodateStudent(self, student: Student):
        # R7
        raise NotImplementedError

class Dormitory:
    def __init__(self, price: float):
        self.price = price
        self.students: List[Student] = []

class Professor:
    def __init__(self, name: str):
        self.name = name

class Student:
    def __init__(self, name: str):
        self.name = name

    def enrollInCourse(self, course: Course):
        # R5
        course.students.append(self)

    def accommodateInDormitory(self, dormitory: Dormitory):
        # R7
        dormitory.students.append(self)
        if len(dormitory.students) > 4:
            raise ValueError('A dormitory can accommodate at most four students.')