
from Instructor import *
from CourseWriter import CourseWriter
from CourseReader import CourseReader
from Holidays import *
from datetime import date, datetime
from InstructorWriter import InstructorWriter


def main():
    # First create some holidays
    d1: date = date(2022, 8, 6)     # define as date and not a datetime object
    d2: date = date(2022, 8, 7)
    d3: date = date(2022, 8, 8)
    d4: date = date(2022, 8, 9)
    d5: date = date(2022, 8, 10)

    # now create an empty list of 'instructor holidays' for 2 different instructors
    # add a some days to the list
    # Instructor 1
    instructor1_holidays = Holidays()
    instructor1_holidays.add_holiday(d1)
    instructor1_holidays.add_holiday(d2)
    instructor1_holidays.add_holiday(d3)
    instructor1_holidays.add_holiday(d4)
    instructor1_holidays.add_holiday(d5)

    # Instructor 2
    instructor2_holidays = Holidays()
    instructor2_holidays.add_holiday(d1)
    instructor2_holidays.add_holiday(d2)
    instructor2_holidays.add_holiday(d4)


    # Now create some course objects
    course1 = Course('1', 'System udvikling', 7.5)
    course2 = Course('2', 'Sygdomslaere', 7.5)
    course3 = Course('3', 'Humanbiologi', 7.5)

    # Create Instructor 1
    print("Creating an Instructor object")
    instructor1 = Instructor('jsw123', 'sugardaddy83', 'Jens', 'Jensen', '12345678', 'jensjensen@science.ku.dk',
                             '111082-1233', 'Ekstern lektor', 'Science', [], instructor1_holidays)
    print("First teacher is teaching at the faculty " + str(instructor1.get_faculty()) +
          " with the position: " + str(instructor1.get_title()))

    # print instructor1's holidays
    print(f"{instructor1.get_first_name()}'s holidays:")
    print(str(instructor1_holidays))

    # Create Instructor 2
    print("Creating an Instructor object")
    instructor2 = Instructor('jsw124', '1234', 'Bettina', 'Skov', '12345679', 'BettinaSkov@sund.ku.dk',
                             '121183-1234', 'lektor', 'Sund', [], instructor2_holidays)

    # print instructor2's holidays
    print(f"{instructor2.get_first_name()}'s holidays:")
    print(str(instructor2_holidays))

    # add some courses to instructor 1 and 2
    instructor1.add_course(course1)
    instructor2.add_course(course2)
    instructor2.add_course(course3)


    print("Building the XML of the Course")
    CW = CourseWriter(course1)
    print("Saving the XML of the Course in an XML file")
    CW.save()

    print("Reading XML File")
    CR = CourseReader()
    course1 = CR.get_course()
    print(course1)

    print("Building the XML of the Instructor")
    IW = InstructorWriter(instructor2)
    print("Saving the XML of the Instructor in an XML file")
    IW.save()


if __name__ == '__main__':
    main()
