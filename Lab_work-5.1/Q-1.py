class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating multiple objects
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

# Calling the method for each object
p1.display()
p2.display()