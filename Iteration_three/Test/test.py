import unittest
import classes


class Course():
    def test_course_id(self):
        self.assertEqual(classes.course_id(), 101)
        self.assertNotEqual(classes.course_id(), "101")

    def test_course_get_name(self):
        self.assertEqual(classes.get_name(), "Systemudvikling")

    def test_course_set_name(self):
        classes.set_name("Organisationsanalyse")
        self.assertEqual(classes.get_location(), "Organisationsanalyse")


class Employee():
    def test_employee_get_office_phone(self):
        self.assertEqual(classes.get_office_phone(), 33357899)
        self.assertNotEqual(classes.get_office_phone(), "33357899")

    def test_employee_set_office_phone(self):
        classes.set_office_phone(int("33357899"))
        self.assertEqual(classes.get_office_phone(), 33357899)
        self.assertNotEqual(classes.get_office_phone(), "33367899")

    def test_employee_get_first_name(self):
        self.assertEqual(classes.employee_get_first_name(), "Lone")

    def test_employee_set_first_name(self):
        classes.employee_set_first_name("Lone")
        self.assertEqual(classes.employee_get_first_name(), "Lone")

    def test_employee_get_last_name(self):
        self.assertEqual(classes.employee_get_first_name(), "Andersen")

    def test_employee_set_last_name(self):
        classes.employee_set_first_name("Andersen")
        self.assertEqual(classes.employee_get_first_name(), "Andersen")


class Instructor():
    def test_get_faculty(self):
        self.assertEqual(classes.get_faculty(), "Det Kemiske Institut")

    def test_set_faculty(self):
        classes.set_faculty("Det Kemiske Intstitut")
        self.assertEqual(classes.get_faculty(), "Det Kemiske Institut")


if _name_ == '_main_':
    unittest.main()