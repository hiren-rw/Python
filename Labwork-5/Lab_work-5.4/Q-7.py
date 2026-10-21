# Q.7: Method Overloading with @staticmethod

class AreaCalculator:
    @staticmethod
    def area(radius):
        return 3.14159 * radius * radius

    @staticmethod
    def area_rec(width, height):
        return width * height

print("Circle Area : ", AreaCalculator.area(5))
print("Rectangle Area : ", AreaCalculator.area_rec(4, 6))