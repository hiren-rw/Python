class AgeValid:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)  # Validates during initialization

    # Setter with validation logic
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Error: Age must be greater than 0! Setting default age to 1.")
            self.__age = 1

    # Getter method
    def get_age(self):
        return self.__age

p1 = AgeValid("Abc", 21)
print(f"{p1.name}'s Age: {p1.get_age()}")

p2 = AgeValid("Xyz", -5)  # Triggers validation warning
print(f"{p2.name}'s Age: {p2.get_age()}")