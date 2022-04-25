from Course import *
from Enumerations import LocationType, Weekdays
from datetime import *


class Preference:

    def __init__(self, course: Course,  timeslot_preferred_start: time, timeslot_preferred_end: time,
                 weekdays_preferred: Weekdays, location_type: LocationType, requirements_list: []):
        self.course = course
        self.timeslot_preferred_start = timeslot_preferred_start #før slut og min 1 t imellem
        self.timeslot_preferred_end = timeslot_preferred_end
        self.weekdays_preferred = weekdays_preferred    # monday/tuesday/wednesday/thursday/friday
        self.location_type: location_type   # online/physical/both
        self.requirements_list = requirements_list


#    def add_blocker(self):
#        """This method allow the instructor to block out a periode off time, in the preference module"""

#    def add_online_link(self):
#        """This method adds an online link to a course timeslot"""