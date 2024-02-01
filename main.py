"""
Program: class_unit_test.py
Author: Brandon Kerns
Last Date Modified: 12/10/23
The purpose of this program is to gain more experience writing unit tests within Python. First, a class named 'Student'
will be created. Next, a separate class will be created for the unit test. The tests will be used to verify that each
attribute of the 'Student' class is functioning as anticipated. Finally, two student objects will be created to test the
overall functionality of the program.
"""
from student import Student


if __name__ == "__main__":
    student_1 = Student("Flacco", "Joe", "Sports Medicine", 3.8)
    print(student_1)
    student_2 = Student("Kerns", "Brandon", "Computer Information Systems", 4.0)
    print(student_2)
