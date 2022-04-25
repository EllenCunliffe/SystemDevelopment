from Employee import *


# from DaysOff import *


class Instructor(Employee):

    def __init__(self, uni_id: str, password: str, first_name: str, last_name: str,
                 office_phone: str, email: str, cpr_number: str, list_courses: [], title: str, faculty: str):
        Employee.__init__(self, uni_id, password, first_name, last_name, office_phone, email, cpr_number)
        self.__title = title
        self.__faculty = faculty
        self.__list_courses = list_courses
        # self.list_days_off = list_days_off

    def __str__(self):
        return Employee.__str__(self), + f"Teaches in course: {self.list_courses}"

    def set_title(self, new_title):
        self.__title = new_title

    def get_title(self):
        return self.__title

    def set_faculty(self, faculty, new_faculty):
        self.__faculty = new_faculty

    def get_faculty(self):
        return self.__faculty


