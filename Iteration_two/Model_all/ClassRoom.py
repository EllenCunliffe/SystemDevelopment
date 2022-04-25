from Institute import *
from Enumerations import ClassroomType
from Faculty import *
from Enumerations import ClassroomBookingStatus


class ClassRoom:

    reserved_status = {}
    # Available Room
    reserved_status['1'] = ClassroomBookingStatus.AVAILABLE
    # Reserved room
    reserved_status['2'] = ClassroomBookingStatus.RESERVED

    def __init__(self, classroom_id: str, address: str, classroom_type: ClassroomType, max_capacity: int,
                 faculty: Faculty,
                 classroom_number: int, building: int, level: int):
        self.classroom_id = classroom_id
        self.address = address
        self.classroom_type = classroom_type
        self.max_capacity = max_capacity
        self.faculty = faculty
        self.classroom_number = classroom_number
        self.building = building
        self.level = level

    def get_location(self):
        return f'{self.address}, {self.building}.{self.level}.{self.classroom_number}'
