from Employee import *
from Course import Course
from Holidays import Holidays


class Instructor(Employee):

    def __init__(self, uni_id: str, password: str, first_name: str, last_name: str,
                 office_phone: str, email: str, cpr_number: str, title: str, faculty: str
                 , list_courses: list[Course], list_holidays: Holidays):
        Employee.__init__(self, uni_id, password, first_name, last_name, office_phone, email, cpr_number)
        self.__title = title
        self.__faculty = faculty
        self.__courses: list_courses = []
        self.__holidays = list_holidays


    def set_title(self, new_title):
        self.__title = new_title

    def get_title(self):
        return self.__title

    def set_faculty(self, new_faculty):
        self.__faculty = new_faculty

    def get_faculty(self):
        return self.__faculty

    def add_course(self, course: Course):  # public method to add a holiday to the list of holidays
        if course not in self.__courses:  # if it is not already in the list
            self.__courses.append(course)

    def remove_course(self, course: Course):  # public method to add a holiday to the list of holidays
        if course in self.__courses:  # if it is found in the list
            self.__courses.remove(course)

    def contains_course(self, course: Course):  # public method to tell if date is in the list of holidays
        return course in self.__courses

    def get_list_courses(self) -> list[Course]:
        return self.__courses

    def get_holidays(self) -> list[date]:
        return self.__holidays.get_holiday_list()

    def add_preference(self):
        pass

    def __str__(self):
        return Employee.__str__(self) + f"Teaches on {self.__faculty} with the title{self.__title}. " \
                                        f"Teaches in courses: {self.__courses}"

