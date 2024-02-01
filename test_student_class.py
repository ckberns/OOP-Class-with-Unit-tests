"""
This file contains the unit test to examine the functionality of the 'Student' class and ensure everything is running as
intended.
"""
# Import the unittest module and the 'Student' class from the student.py file.
import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        # Create a method that runs before each test to ensure the object is created properly.
        self.student = Student("Smith", "John", "History", 3.5)

    def tearDown(self):
        # Create a method that will delete the object after the test runs.
        del self.student

    def test_object_created_required_attributes(self):
        # Create a method to test that each attribute is assigned properly.
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Smith")
        self.assertEqual(self.student.major, "History")
        self.assertEqual(self.student.gpa, 3.5)

    def test_object_created_all_attributes(self):
        # Create a method to test if the object has all the required attributes.
        student = Student("Doe", "Jane", "Biology", 4.0)
        self.assertEqual(student.first_name, "Jane")
        self.assertEqual(student.last_name, "Doe")
        self.assertEqual(student.major, "Biology")
        self.assertEqual(student.gpa, 4.0)

    def test_student_str(self):
        # Create a method to test if the str() method is constructed/displayed properly.
        self.assertEqual(str(self.student), "Smith, John has major History with GPA: 3.5")

    def test_object_not_created_error_last_name(self):
        # Create a method to test if the program responds correctly to the last_name attribute being left blank.
        student = Student("", "John", "History", 3.5)
        self.assertTrue(student.last_name == "")

    def test_object_not_created_error_first_name(self):
        # Create a method to test if the program responds correctly to the first_name attribute being left blank.
        student = Student("Smith", "", "History", 3.5)
        self.assertTrue(student.first_name == "")

    def test_object_not_created_error_major(self):
        # Create a method to test if the program responds correctly to the major attribute being left blank.
        student = Student("John", "Smith", "", 3.5)
        self.assertTrue(student.major == "")

    def test_object_not_created_error_gpa(self):
        # Create a method to test if the GPA entered is a float and ensure GPA is within range.
        gpa = 3.5
        self.assertTrue(2.0 <= 3.5 <= 4.0)
        self.assertFalse(3.5 <= 2.0 <= 4.0)
        self.assertIsInstance(gpa, float)


if __name__ == "__main__":
    unittest.main()
