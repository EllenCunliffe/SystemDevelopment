# Calendar Class
from datetime import *
from dateutil.relativedelta import relativedelta


class ClassroomCalendar:

    def __init__(self, number_days: int, booking_days: [], booking_start: datetime, booking_end: datetime):

        if number_days > 0:
            self.number_days = number_days
        else:
            print('Calendar must look ahead more than 1 day!, defaulting to 1 day')
            self.number_days = 1
        self.booking_days = booking_days
        self.booking_start = booking_start
        self.booking_end = booking_end

        # get all days from today to x number of month ahead
        start_date = date.today()
        end_date = start_date + relativedelta(days=self.number_days)
        delta = end_date - start_date  # Get date x number of month from now
        for i in range(delta.days + 1):
            day = start_date + timedelta(days=i)
            # since nobody is initially booked, append 'none' to each day
            x = list((day, 'none'))
            self.booking_days.append(x)

    def get_all_bookings(self):
        """ This method show a user what days, they have booked a classroom"""
        return self.booking_days

    def get_available_days_booking(self):
        """ This method will show the user what days, the rooms on a certain faculty is available"""
        return self.booking_start, self.booking_end
