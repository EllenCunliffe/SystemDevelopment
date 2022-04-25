from enum import Enum


class Language(Enum):
    English = 1
    Dansk = 2


class ClassroomBookingStatus(Enum):
    AVAILABLE = 1
    RESERVED = 2


class ClassroomType(Enum):
    LECTURE = 1
    SAU = 2
    LABORATORY = 3


class CourseType(Enum):
    LECTURE = 1
    SAU = 2
    LABORATORY = 3


class LocationType(Enum):
    ONLINE = 1
    PHYSICAL = 2
    BOTH = 3


class Weekdays(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5

