from Employee import *
from DaysOff import *


class Instructor(Employee):

    def __init__(self, uni_id: str, password: str, first_name: str, last_name: str, faculty: Faculty,
                 office_phone: int, cpr_number: str, pay_monthly: int, title: str, list_days_off: DaysOff,
                 list_courses: [], email: str):
        Employee.__init__(self, uni_id, password, first_name, last_name, faculty,
                          office_phone, cpr_number, pay_monthly, title)
        self.__title = title
        self.__faculty = faculty
        self.list_days_off = list_days_off
        self.list_courses = list_courses
        self.email = email

    def set_email(self, new_email):
        self.email = new_email

    def get_email(self):
        return self.email

    def __str__(self):
        return Employee.__str__(self) + f"Teaches in course:{self.list_courses}, not available on {self.list_days_off}"\
                                        f"E-mail: {self.email} "
