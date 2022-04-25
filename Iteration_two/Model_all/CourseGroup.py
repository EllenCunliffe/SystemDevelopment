# In the university, the student is connected to one or multiple groups. The group could be all the students in a class,
# half the students, or students combined from different educations. These groups are important to the course, so that
# it can be registered by the system how many students will be attending the courses.
# This class is a composition of the Course --> meaning that it only exist if the course exist


class CourseGroup:

    def __init__(self, group_id: str, list_students: []):
        self.__group_id = group_id
        self.__list_students = list_students

    def set_group_id(self, new_group_id):
        self.__group_id = new_group_id

    def get_group_id(self):
        return self.__group_id

    def __str__(self):
        return f'Group: {self.__name}, Students: {self.__list_students} '
