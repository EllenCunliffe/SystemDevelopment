# This class is a parent class of users of our booking-system
class User:
    """ This class holds attributes and methods for the users of the system, and is the parent class"""

    def __init__(self, uni_id: str, password: str):
        self.__uni_id = uni_id
        self.__password = password

    def __str__(self):
        return f"Name: {self.__first_name} {self.__last_name} "

    def set_uni_id(self, new_uni_id):
        self.__uni_id = new_uni_id

    def get_uni_id(self):
        return self.__uni_id

    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return self.__password

