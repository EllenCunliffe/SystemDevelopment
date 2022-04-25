from User import *


class Student(User):

    def __init__(self, uni_id: str, password: str, first_name: str, last_name: str, list_courses: [], list_group: []):
        User.__init__(self, uni_id, password, first_name, last_name)
        self.line_of_study = list_courses
        self.student_mail = uni_id + '@alumni.ku.dk'

    def get_student_mail(self):
        return self.student_mail

    def __str__(self):
        return User.__str__(self) + f"courses: {self.list_courses}, E-mail: {self.student_mail}, " \
                                    f"Groups: {self.list_group}"


