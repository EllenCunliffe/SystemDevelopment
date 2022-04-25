from Instructor import *


# define a class course
class Course:

    def __init__(self, name: str, list_topic: [], ects: float, list_type: [], course_responsible: Instructor):
        self.__name = name  # name could be system development
        self.__list_topic = list_topic  # a topic in system development could be 'objects and classes'
        self.__ects = ects
        self.__list_type = list_type  # lab/theoretical/practical
        self.__course_responsible = course_responsible  # the responsible person

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Name: {self.name}, Topics: {self.list_topic}, Type: {self.list_type}, " \
               f"Responsible Instructor: {self.course_responsible}"
