"""
This file contains a class titled 'Student' that will be used to display a student's full name, the major they are
pursuing, and their overall GPA.
"""


class Student:
    """
    This class represents a student that will be used to track their personal information throughout their educational
    career. This class will require the student's name, major, and GPA.

    Attributes:
        last_name(str)      The last name of the student.
        first_name(str)     The first name of the student.
        major(str)          The major the student is currently pursuing.
        gpa(float)          The grade-point average the student currently possesses.
    """
    # Define the constructor for the 'Student' class.
    def __init__(self, lname, fname, major, gpa=0.0):
        try:
            self.last_name = lname
        except ValueError:
            print("Invalid entry! You must enter a valid last name.")
        try:
            self.first_name = fname
        except ValueError:
            print("Invalid entry! You must enter a valid first name.")
        try:
            self.major = major
        except ValueError:
            print("Invalid entry! You must enter a valid major.")
        try:
            self.gpa = gpa
        except ValueError:
            print("Invalid entry! You must enter a valid GPA.")

    def __str__(self):
        """
        Method to return a string stating the student's full name, major, and current GPA.
        :return: a formatted string displaying the student's personal information.
        """
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with GPA: " + str(self.gpa)
