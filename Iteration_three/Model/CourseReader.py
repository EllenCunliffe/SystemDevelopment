from logging import root
import os
from xml.etree import ElementTree
from Course import Course


class CourseReader:
    __file_name__ = 'course.xml'

    def __init__(self) -> None:
        full_file = os.path.abspath(os.path.join(self.__file_name__))
        dom = ElementTree.parse(full_file)
        # reading general attributes
        root = dom.getroot()
        course_id = root.attrib['courseID']
        name = root.attrib['name']
        ects = float(root.attrib['ects'])

        self.__Course__ = Course(course_id, name, ects)

    def get_course(self) -> Course:
        return self.__Course__

