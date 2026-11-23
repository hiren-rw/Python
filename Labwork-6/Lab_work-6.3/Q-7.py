# Q.7: Validate student's grade

class InvalidGradeError(Exception):
    pass

grade = input("Enter grade : ")
assert grade != "", "Input cannot be empty!"

grade = int(grade)

if grade < 0 or grade > 100:
    raise ValueError("Grade must be between 0 and 100!")

if grade < 40:
    raise InvalidGradeError("Failing grade (below 40)!")

print("Passed with grade : ", grade)