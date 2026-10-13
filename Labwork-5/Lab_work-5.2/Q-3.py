# Q.3 Rectangle with Parameterized Constructor

class rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        print("Area of rectangle is : ",self.height*self.width)


h = int(input("Enter Height : "))
w = int(input("Enter Width : "))
r1 = rectangle(h,w)
r1.area()