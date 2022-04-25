# import date to store dates
from datetime import date


# This is a list of all the days, the instructor is scheduled to do other activities, work or individual holidays
# and is not available to the University
class DaysOff:
    __days_off: list[date] = []  # a private attribute is prefixed by two underscores in Python

    def __init__(self=None):
        self.__days_off: list[date] = []  # a new object of the type Holidays is created as an empty list

    def add_day_off(self, day_off: date):  # public method to add a holiday to the list of __days_off
        if day_off not in self.__days_off:  # if it is not already in the list
            self.__days_off.append(day_off)

    def remove_holiday(self, day_off: date):  # public method to add a holiday to the list of __days_off
        if day_off in self.__days_off:  # if it is found in the list
            self.__days_off.remove(day_off)

    def contains_day(self, day_off: date):  # public method to tell if date is in the list of __days_off
        return day_off in self.__days_off

    def __str__(self):
        output = f"Number of __days_off: {len(self.__days_off)} \n"
        output = output + "The __days_off are \n"
        output += ', '.join(str(h) for h in self.__days_off)
        return output
