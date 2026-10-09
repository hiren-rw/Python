class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.__name = name
        self.__marks = [mark1, mark2, mark3]

    def average(self):
        avg = sum(self.__marks) / len(self.__marks)
        return avg

    def display_average(self):
        print(f"Student: {self.__name}, Average Marks: {self.average():.2f}")

    def grade(self):
        avg = self.average()
        
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "Fail"
            
        print("Final Grade: ",grade)

student1 = Student("ABC", 85, 92, 78)
student1.display_average()
student1.grade()