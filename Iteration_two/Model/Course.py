from CourseResponsible import CourseResponsible


# define a class course
class Course:
    """
       a University course
       """

    def __init__(self, course_id: str, name: str, list_topic: [], responsible: CourseResponsible):
        self.__course_id: str = course_id
        self.__name: str = name
        self.__list_topics: list_topic
        self.__course_responsible = responsible

    def __str__(self):
        return f"Name: {self.__name}, Topics: {self.list_topic}, " \
               f"Responsible Instructor: {self.__course_responsible}"

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name


