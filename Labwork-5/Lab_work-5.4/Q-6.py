# Q.6: Method Overriding (Animal Sounds)

class Animal:
    def speak(self):
        print("All animal's have different sound.")

class Dog(Animal):
    def speak(self):
        print("Dog can Bark...")

class Cat(Animal):
    def speak(self):
        print("Cat can Meow...")        # Method Overriding

sound = Animal(),Dog(),Cat()     # Tuple

for i in sound:
    i.speak()