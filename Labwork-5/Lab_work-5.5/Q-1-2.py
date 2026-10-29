from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


# A new subclass that intentionally misses one method (perimeter)
class IncompleteTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height


# ==============================================================================
# QUESTION 1: Shape, Rectangle, Circle, and Direct Instantiation Check
# ==============================================================================
print("\n--- Question 1 ---")
print("\n--- Demonstraing that making object of Shape class will raise an error ---")

try:
    s1 = Shape()
except TypeError as e:
    print("We got an Error : ",e)

print("\nComputing and Displaying Areas : ")
r1 = Rectangle(50,15)
print("Area of Rectangle is : ",r1.area())
c1 = Circle(20)
print("Area of Circle is : ",c1.area())


# ==============================================================================
# QUESTION 2: Adding perimeter() and observing Incomplete Subclass Error
# ==============================================================================
print("=" * 100)
print("\n--- Question 2 ---")
print("--- Verifying Rectangle and Circle work correctly ---")

r2 = Rectangle(4, 6)
print("Area of Rectangle : ",r2.area())
print("Perimeter : ",r2.perimeter())

c2 = Circle(3)
print(f"Area of Circle : {c2.area():.2f}")
print(f"Perimeter : {c2.perimeter():.2f}")

print("\n--- Trying to instantiate the incomplete subclass ---")
try:
    tri = IncompleteTriangle(5, 10)
except TypeError as e:
    print("Error caught successfully : ",e)