# Q.5 Student Class with Attributes and Methods

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display_details(self):
        print(f"Student: {self.name} | Roll No: {self.roll}")

    def check_status(self):
        if self.marks >= 40:
            print(f"{self.name} has passed.")
        else:
            print(f"{self.name} has failed.")


s1 = Student("ABC", 101, 85)
s1.display_details()
s1.check_status()