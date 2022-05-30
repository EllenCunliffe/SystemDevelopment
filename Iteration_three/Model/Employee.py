
from datetime import date
from stdnum.dk import cpr
from User import User
from email_validator import validate_email


# Employees is a subclass of class users

class Employee(User):
    """
       Employee class holds attributes and methods for an employee and is a subclass off class User
       """

    def __init__(self, uni_id: str, password: str, first_name: str, last_name: str, office_phone: str, email: str,
                 cpr_number: str):
        User.__init__(self, uni_id, password)  # base class constructor
        self.__first_name = first_name
        self.__last_name = last_name
        self.__office_phone = office_phone
        # This validator checks if input for email exist
        try:
            self.__email = email
            validate_email(self.__email)
        except:
            raise TypeError("not an email")

        # This validator checks if cpr contains a valid birthdate
        try:
            self.__cpr_number = cpr_number
            cpr.get_birth_date(cpr.compact(self.__cpr_number))

        except:
            raise TypeError("Bad cpr_number")

    def set_office_phone(self, new_office_phone):
        self.__office_phone = new_office_phone

    def get_office_phone(self):
        return self.__office_phone

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_cpr_number(self):
        return self.__cpr_number

    def set_cpr_number(self, new_cpr):
        self.__cpr_number = new_cpr

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def get_last_name(self):
        return self.__last_name

    @property
    def get_age(self):
        """ This method return the age of the employee based on CPR information """
        __cpr_compact = cpr.compact(self.__cpr_number)  # format from ddmmyy-xxxx ([0-10]) --> ddmmyyxxxx ([0-9])
        __today = date.today()  # format yyyy-mm-dd [0,1,2,3,4,5,7,8,9,10]
        __year_today = int(str(__today)[0:4])  # yyyy
        __month_today = int(str(__today)[5:7])  # mm
        __day_today = int(str(__today)[8:10])  # dd
        # if the last two digits in birth year is higher than the last to digits of year today
        # -> you are born in 19th century fx 19(94) and 20(22)
        if int(__cpr_compact[4:6]) > int(str(__today)[2:4]):
            __birth_year = int("19" + __cpr_compact[4:6])
        else:
            __birth_year = int("20" + __cpr_compact[4:6])
        __birth_month = int(__cpr_compact[2:4])  # mm
        __birth_day = int(__cpr_compact[0:2])  # dd
        __age = __year_today - __birth_year - ((__month_today, __day_today) < (__birth_month, __birth_day))

        return f"The employees age is: {__age}"

    def get_gender(self):
        """ This method return the gender of the employee based on the last two digits in CPR"""
        __cpr_compact = cpr.compact(self.__cpr_number)
        if (int(__cpr_compact[-1]) % 2) == 0:  # [-1] is always the last position in string
            gender = "female"
        else:
            gender = "male"
        return f"The employees gender is: {gender}"

    def __str__(self):
        return User.__str__(self) + f"Office phone: {self.__office_phone}, Email: {self.__email}, {self.get_age}"
