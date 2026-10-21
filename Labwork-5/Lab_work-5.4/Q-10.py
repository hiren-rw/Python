# Q.10: Subclass Verification using issubclas
 
class Person:
    pass

class Student(Person):
    pass

result = issubclass(Student, Person)

print("Is sudent class is subclass of person class ? : ",result)