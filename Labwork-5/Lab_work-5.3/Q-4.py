# Q.4: Hierarchical Inheritance

class animal:
    def voice(self):
        print("Every animal has voice.")

class dog(animal):      # Hierarchical Inheritance
    def bark(self):
        print("Dog can bark.")

class cat(animal):
    def meow(self):
        print("Cat can meow.")

d1 = dog()
c1 = cat()
d1.voice()
d1.bark()
c1.voice()
c1.meow()