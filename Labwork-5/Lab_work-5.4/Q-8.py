# Q.8: Vehicle Start Logic (Method Overriding)

class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Bike(Vehicle):
    def start(self):        # Method Overriding
        print("Bike is starting...")

class Car(Vehicle):         # Multiple Inheritance
    def start(self):
        print("Car is starting...")

key = Vehicle(),Bike(),Car()        # Tuple

for i in key:
    i.start()