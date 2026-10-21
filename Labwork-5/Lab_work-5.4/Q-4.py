# Q.4: Interface Polymorphism (Transport)

class Transport:
    def travel(self):
        pass

class Train(Transport):
    def travel(self):
        print("Transporting by Train.")

class Plane(Transport):     # Multiple Inheritance
    def travel(self):
        print("Transporting by Plane.")

t1 = Train()
t1.travel()

p1 = Plane()
p1.travel()