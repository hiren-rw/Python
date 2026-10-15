# Q.8: isinstance() Function

class Animal:
    pass

class Dog(Animal):
    pass

my_dog = Dog()

print("Is my_dog an instance of Dog? : ", isinstance(my_dog, Dog))
print("Is my_dog an instance of Animal? : ", isinstance(my_dog, Animal))
print("Is my_dog an instance of str? : ", isinstance(my_dog, str))