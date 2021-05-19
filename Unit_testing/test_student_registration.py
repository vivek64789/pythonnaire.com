import unittest
from Model_class.student_registration import *


class TestStudentRegistration(unittest.TestCase):

    def setUp(self):
        self.stu_obj = StudentRegistration("vivek", "vivek@gmail.com", "vivek", "vivek", "kushwaha", "2002/02/04",
                                           "male",
                                           "baneshwor", 9818821313, "morning", 1, 1, "A", "2020/09/01")

    def test_set_username(self):
        actual = self.stu_obj.set_username("vivek")
        self.assertIsNone(actual)

    def test_get_username(self):
        expected = "vivek"
        actual = self.stu_obj.get_username()
        self.assertEqual(expected,actual)

    def test_set_email(self):
        actual = self.stu_obj.set_email("vivek@gmail.com")
        self.assertIsNone(actual)

    def test_get_email(self):
        expected = "vivek@gmail.com"
        actual = self.stu_obj.get_email()
        self.assertEqual(expected,actual)

    def test_set_f_name(self):
        actual = self.stu_obj.set_f_name("vivek")
        self.assertIsNone(actual)

    def test_get_f_name(self):
        expected = "vivek"
        actual = self.stu_obj.get_f_name()
        self.assertEqual(expected,actual)

    def test_set_l_name(self):
        actual = self.stu_obj.set_l_name("kushwaha")
        self.assertIsNone(actual)

    def test_get_l_name(self):
        expected = "kushwaha"
        actual = self.stu_obj.get_l_name()
        self.assertEqual(expected,actual)

    def test_set_dob(self):
        actual = self.stu_obj.set_dob("2002/02/04")
        self.assertIsNone(actual)

    def test_get_dob(self):
        expected = "2002/02/04"
        actual = self.stu_obj.get_dob()
        self.assertEqual(expected,actual)

    def test_set_gender(self):
        actual = self.stu_obj.set_gender("male")
        self.assertIsNone(actual)

    def test_get_gender(self):
        expected = "male"
        actual = self.stu_obj.get_gender()
        self.assertEqual(expected,actual)

    def test_set_address(self):
        actual = self.stu_obj.set_address("baneshwor")
        self.assertIsNone(actual)

    def test_get_address(self):
        expected = "baneshwor"
        actual = self.stu_obj.get_address()
        self.assertEqual(expected,actual)

    def test_set_contact(self):
        actual = self.stu_obj.set_contact(9818821313)
        self.assertIsNone(actual)

    def test_get_contact(self):
        expected = 9818821313
        actual = self.stu_obj.get_contact()
        self.assertEqual(expected,actual)

    def test_set_shift(self):
        actual = self.stu_obj.set_shift("morning")
        self.assertIsNone(actual)

    def test_get_shift(self):
        expected = "morning"
        actual = self.stu_obj.get_shift()
        self.assertEqual(expected,actual)

    def test_set_course_id(self):
        actual = self.stu_obj.set_course_id(1)
        self.assertIsNone(actual)

    def test_get_course_id(self):
        expected = 1
        actual = self.stu_obj.get_course_id()
        self.assertEqual(expected,actual)

    def test_set_batch_id(self):
        actual = self.stu_obj.set_batch_id(1)
        self.assertIsNone(actual)

    def test_get_batch_id(self):
        expected = 1
        actual = self.stu_obj.get_batch_id()
        self.assertEqual(expected,actual)

    def test_set_section(self):
        actual = self.stu_obj.set_section("A")
        self.assertIsNone(actual)

    def test_get_section(self):
        expected = "A"
        actual = self.stu_obj.get_section()
        self.assertEqual(expected,actual)

    def test_set_reg_date(self):
        actual = self.stu_obj.set_reg_date("2020/09/01")

        self.assertIsNone(actual)

    def test_get_reg_date(self):
        expected = '2020/09/01'
        actual = self.stu_obj.get_reg_date()
        self.assertEqual(expected,actual)
