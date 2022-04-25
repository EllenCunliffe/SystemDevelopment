# In the university, the student is connected to one or multiple groups. The group could be all the students in a class,
# half the students, or students combined from different educations. These groups are important to the course, so that
# it can be registered by the system how many students will be attending the courses.
# This class is a composition of the Course --> meaning that it only exist if the course exist
from Enumerations import CourseType
from CourseResponsible import CourseResponsible


class CourseGroup:

    def __init__(self, group_id: str, list_students: [], course_type: CourseType,
                 group_responsible: CourseResponsible):
        self.__group_id = group_id
        self.__list_students = list_students
        self.__course_type = course_type
        self.__course_responsible = group_responsible

    def __str__(self):
        return f'Group: {self.__group_id}, Students: {self.__list_students}, Type: {self.__course_type}'

    def set_group_id(self, new_group_id):
        self.__group_id = new_group_id

    def get_group_id(self):
        return self.__group_id

    def set_course_type(self, course_type: CourseType):
        self.__course_type = course_type

    def get_course_type(self):
        return self.__course_type


