from bright_university_function import *
import unittest
class TestUniversitySystem(unittest.TestCase):

	def test_that_new_student_record_can_be_created(self):
		actual = createAStudentRecord("fathia",12,["maths","English","Computer"],{"city": "lagos", "zip": "896"},"123")
		expected = "Student record have been successfully created."
		self.assertEqual(actual,expected)


	def test_that_nothing_can_be_displayed_if_no_student_have_been_added(self):
		actual = display_student_course("111")
		expected =  "Username not found"
		self.assertEqual(actual,expected)



	def test_that_nothing_can_be_displayed_if_wrong_username_is_inputed(self):
		actual = display_student_course ("3")
		expected =  "Username not found"
		self.assertEqual(actual,expected)

	def test_that__can_right_input_can_be_added(self):
		actual = display_student_course ("123")
		expected =  "No student have been registered yet"
		self.assertEqual(actual,expected)

	
	def test_that_you_can_show_course_if_right_input_is_inputed(self):
		createAStudentRecord("fathia",12,["maths","English","Computer"],{"city": "lagos", "zip": "896"},"123")
		actual = type(display_student_course ("123"))
		expected =  tuple
		self.assertEqual(actual,expected)

	def test_that_you_can_show_zipcode_if_the_wrong_name_is_input_is_inputed(self):
		createAStudentRecord("fathia",12,["maths","English","Computer"],{"city": "lagos", "zip": "896"},"123")
		actual = display_zip_code ("12")
		expected =  "Username not found"
		self.assertEqual(actual,expected)


	def test_that_you_cant_show_zipcode_if_the_wrong__usernme_is_inputed_is_inputed(self):
		createAStudentRecord("fathia",12,["maths","English","Computer"],{"city": "lagos", "zip": "896"},"123")
		actual = display_zip_code ("13")
		expected = "Username not found"
		self.assertEqual(actual,expected)



	def test_that_you_can_display_city_if_right_input_is_inputed(self):
		createAStudentRecord("fathia",12,["maths","English","Computer"],{"city": "lagos", "zip": "896"},"123")
		actual = display_city ("123")
		expected =  "<<<City>>>","lagos"
		self.assertEqual(actual,expected)



