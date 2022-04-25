# This class is a parent class of users of our booking-system
class User:
    def __init__(self, uni_id: str, password: str, first_name: str, last_name: str):
        self.__uni_id = uni_id
        self.__password = password
        self.first_name = first_name
        self.last_name = last_name

    def set_uni_id(self, new_uni_id):
        self.__uni_id = new_uni_id

    def get_uni_id(self):
        return self.__uni_id

    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return self.__password

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def get_last_name(self):
        return self.last_name

    def __str__(self):
        return f"User: {self.__uni_id}, Password: {self.__password}, Name: {self.first_name} + '' + {self.last_name} "
