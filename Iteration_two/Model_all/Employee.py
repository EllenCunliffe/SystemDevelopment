from Faculty import *
from User import *
from datetime import date
from stdnum.dk import cpr


# Employees is a subclass of class users
class Employee(User):
    """
       employee class holds attributes and methods for an employee
       not the double underscore denoting this is a private attribute.
       An exception will be raised if your code tries to access it directly
       without the use of the setters and getters
       """

    def __init__(self, uni_id: str, password: str, first_name: str, last_name: str, title: str, faculty: Faculty,
                 office_phone: str, email: str, cpr_number: str):
        User.__init__(self, uni_id, password, first_name, last_name)  # base class constructor
        self.__office_phone = office_phone
        self.__email = email
        self.__cpr = cpr_number

    def set_office_phone(self, new_office_phone):
        self.__office_phone = new_office_phone

    def get_office_phone(self):
        return self.__office_phone

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_cpr_number(self):
        try:
            cpr.get_birth_date(cpr.compact(self.__cpr))
        except:
            raise TypeError("The number does not contain valid birth date information")
        return self.__cpr

    def set_cpr_number(self, new_cpr):
        self.__cpr = new_cpr

    #     def get_age(self):
        #         """ Return the age of the employee """
        #         __cpr_compact = cpr.compact(self.__cpr)  # format from ddmmyy-xxxx ([0-10]) --> ddmmyyxxxx ([0-9])
        #         __today = date.today()  # format yyyy-mm-dd [0,1,2,3,4,5,7,8,9,10]
        #         __year_today = int(str(__today)[0:4])  # yyyy
        #         __month_today = int(str(__today)[5:7])  # mm
        #         __day_today = int(str(__today)[8:10])  # dd
        #         # if the last two digits in birth year is higher than the last to digits of year today
        #         # -> you are born in 19th century fx 19(94) and 20(22)
        #         if int(__cpr_compact[4:6]) > int(str(__today)[2:4]):
        #             __birth_year = int("19" + __cpr_compact[4:6])
        #         else:
        #             __birth_year = int("20" + __cpr_compact[4:6])
        #         __birth_month = int(__cpr_compact[2:4])  # mm
        #         __birth_day = int(__cpr_compact[0:2])  # dd
        #         __age = __year_today - __birth_year - ((__month_today, __day_today) < (__birth_month, __birth_day))

        return f"The employees age is: {__age}"

    def get_gender(self):
        """ This method return the gender of the employee"""
        __cpr_compact = cpr.compact(self.__cpr)
        if (int(__cpr_compact[-1]) % 2) == 0:  # [-1] is always the last position in string
            gender = "female"
        else:
            gender = "male"
        return f"The employees gender is: {gender}"

    def __str__(self):
        return User.__str__(self) + f"Title: {self.__title}, Faculty: {self.__faculty}, " \
                                    f"Office phone: {self.__office_phone}, Email: {self.__email}, Age: {self.get_age()}"
