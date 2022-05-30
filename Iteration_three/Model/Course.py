
# define a class course
class Course:
    """
    a University course
    """
    def __init__(self, course_id: str, name: str, ects: float):
        self.__course_id: str = course_id
        self.__name: str = name
        #self.__list_topics: list_topic
        self.__ects: float = ects

    def __str__(self):
        return f"Name: {self.__name}, ects: {self.__ects}"

    def get_id(self):
        return self.__course_id

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def get_ects(self):
        return self.__ects

    #     def erase(self) -> None:
    #         self.__name__ = ' '
    #         self.__address__ = ' '
    #         self.__manager__ = ' '
    #         self.__drugs__ = []
    #         self.__stock__ = []

    #     def update(self, d: Dispensary) -> None:
    #         self.__name__ = d.getName()
    #         self.__address__ = d.getAddress()
    #         self.__manager__ = d.getManager()
    #         self.__drugs__ = d.getDrugs()
    #         self.__stock__ = d.getStock()
