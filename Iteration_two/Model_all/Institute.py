from Faculty import *


class Institute:

    def __init__(self, name: str, address: str, faculty: Faculty, list_classroom: [], list_instructors: []):
        self.name = name
        self.faculty = faculty
        self.address = address
        self.list_classroom = list_classroom
        self.list_instructors = list_instructors

    def __str__(self):
        return f"Name: {self.name}, Address: {self.name}, Faculty: {self.faculty}, Classrooms: {self.list_classroom}," \
               f"Instructors: {self.list_instructors}"
