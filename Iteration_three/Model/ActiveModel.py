from Course import Course
from Instructor import Instructor


class ActiveModel(object):
    """
    This is the system model that allows a teacher to set a preference from a course
    that is choosen
    """

    list_courses: list = []
    current_course: Course = None
    current_instructor: Instructor = None


def add_course(cls, course):
    cls.list_course.append(course)


def set_current_course(cls, course):
    cls.current_course = course


def get_current_course(cls):
    return cls.current_course


def get_course_list(cls):
    return cls.list_course


def set_current_instructor(cls, i):
    cls.current_instructor = i


def get_current_instructor(cls):
    return cls.current_instructor
