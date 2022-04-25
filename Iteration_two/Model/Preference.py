from Course import *
from datetime import *
from Enumerations import Weekdays
from Enumerations import LocationType


class Preference:
    """
    Represents the preferences a teacher adds to course
    """
    # weekdays = Weekdays()
    # weekdays_preferred = []

    # locations = LocationType()
    # location_type = [locations]

    def __init__(self, timeslot_preferred_start: time, timeslot_preferred_end: time,
                 weekdays_preferred: [], location_type, requirements_list: []):
        self.timeslot_preferred_start = timeslot_preferred_start
        self.timeslot_preferred_end = timeslot_preferred_end
        self.location_type = location_type  # online/physical/both
        self.requirements_list = requirements_list  # can this be done better?
        self.weekdays_preferred = weekdays_preferred

    # def add_weekday(self, new_weekday):
        # self.weekdays_preferred.append(Weekdays(new_weekday))

    # def add_location_type(self, new_location_type):
        # self.location_type.append(LocationType(new_location_type))

#    def add_blocker(self):
#        """This method allow the instructor to block out a one time"""

#    def add_online_link(self):
#        """This method adds an online link to a course timeslot"""
