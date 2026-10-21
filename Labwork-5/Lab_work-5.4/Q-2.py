# Q.2: Polymorphism in Class Inheritance (Shape)

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radious):        # Constructor
        self.r = radious
        
    def area(self):
        print("Area of Circle : ",3.14 * self.r ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.l = length
        self.w = width
        
    def area(self):
        print("Area of Rectangle : ",self.l * self.w)

shapes = Circle(5), Rectangle(4, 6)     # Stores as a tuple

for s in shapes:
    s.area()