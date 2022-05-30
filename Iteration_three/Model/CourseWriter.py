from xml.etree.ElementTree import tostring
import xml.etree.cElementTree as ET
from xml.dom import minidom
from Course import Course


class CourseWriter:
    def __init__(self, course: Course) -> None:
        print("Writing root nodes")
        self.__root__ = ET.Element("Course")  # define root of the document
        self.__root__.set("courseID", course.get_id())
        self.__root__.set("name", course.get_name())
        self.__root__.set("ects", str(course.get_ects()))
        # If we were to define many elements of the type ects we would do as follows:
        # self.__ects__ = ET.SubElement(self.__root__, "ects", {"value": str(course.get_ects())})  # define ects subelement
        print(tostring(self.__root__))

    def save(self) -> None:
        tree = ET.ElementTree(self.__root__)
        print(tree)
        # prettyTree = prettify(tree)
        # print (prettyTree)
        tree.write("course.xml")


def prettify(elem):
    """Return a pretty-printed XML string for the element.
    """
    elem.getroot()
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
