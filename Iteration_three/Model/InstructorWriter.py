from xml.etree.ElementTree import tostring
import xml.etree.cElementTree as ET
from xml.dom import minidom
from Instructor import *


class InstructorWriter:
    def __init__(self, instructor: Instructor) -> None:
        print("Writing root nodes")
        self.__root__ = ET.Element("Instructor")  # define root of the document
        self.__root__.set("uniID", instructor.get_uni_id())
        self.__root__.set("password", instructor.get_password())
        self.__root__.set("first name", instructor.get_first_name())
        self.__root__.set("last name", instructor.get_last_name())
        self.__root__.set("phone number", instructor.get_office_phone())
        self.__root__.set("e-mail", instructor.get_email())
        self.__root__.set("cpr", instructor.get_cpr_number())
        self.__root__.set("title", instructor.get_title())
        self.__root__.set("faculty", instructor.get_faculty())

        # If we were to define many elements of the type course we would do as follows:
        self.__courses__ = ET.SubElement(self.__root__, "courses")
        for course in instructor.get_list_courses():
            ET.SubElement(self.__courses__, "course", name=str(course))
        print(tostring(self.__root__))

        # If we were to define many elements of the type holidays we would do as follows:
        self.__holidays__ = ET.SubElement(self.__root__, "holidays")
        for holiday in instructor.get_holidays():
            ET.SubElement(self.__holidays__, "holiday", date=str(holiday))
        print(tostring(self.__root__))

    def save(self) -> None:
        tree = ET.ElementTree(self.__root__)
        print(tree)
        tree.write("instructor.xml")


def prettify(elem):
    """Return a pretty-printed XML string for the element.
    """
    elem.getroot()
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
