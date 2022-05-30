from Course import *
from datetime import *
from datatest import validate


class Preference:
    """
    Represents the preferences a teacher adds to course. Request for a weekday and timeslot for a given course
    """
    __preference_id = 0

    def __init__(self, course: Course, weekday: str, timeslot_start: time,
                 timeslot_end: time):
        self.__course = course
        self.__weekday = weekday
        self.__timeslot_start = timeslot_start
        self.__timeslot_end = timeslot_end
        self.__preference_id += 1

    def __str__(self):
        return f"Request: {str(self.request_id)}, course, {str(self.__course)}," \
                f" weekday: {str(self.__weekday)}, start-time: {str(self.__timeslot_start)}," \
                f" end-time {str(self.__timeslot_end)}"

    def set_weekday(self, weekday: str):
        self.__weekday = weekday

    @staticmethod
    def time_validator(time_string, time_format: str = "%H:%M"):
        while True:  # a loop that require the input to work
            try_time = time_string  # This variable is used for validation and can be changed to different input methods
            try:
                # strptime() is a method in DateTime used to format the string format to date-time object.
                # This can only be possible when the date format and the booking date (try) is the same format
                datetime.strptime(try_time, time_format)
                print("This is the correct date string format.")
                break  # Break the loop if the input is the true format
            except ValueError:  # exception made if the loop catches an error
                print(f"This is the incorrect date string format. It should be {time_format}")
        return try_time

    def set_end_time(self, timeslot_end: time):
        try:
            self.__timeslot_end = timeslot_end
            time_validator(self.__timeslot_end)
        except:
            raise TypeError("not an email")


    def set_start_time(self, timeslot_start: time):
        self.__timeslot_start = timeslot_start

    # def add_weekday(self, new_weekday):
    # self.weekdays_preferred.append(Weekdays(new_weekday))

    # def add_location_type(self, new_location_type):
    # self.location_type.append(LocationType(new_location_type))

#    def add_blocker(self):
#        """This method allow the instructor to block out a one time"""

#    def add_online_link(self):
#        """This method adds an online link to a course timeslot"""
