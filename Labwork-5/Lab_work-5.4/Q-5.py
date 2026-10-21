# Q.5: Method Overloading using Default Arguments (Calculator)

class Calculator:
    def multiply(self,a,b,c=1):         # c is default value
        return a*b*c

c1 = Calculator().multiply(20,4)
print("Multiplication of two numbers : ",c1)

c2 = Calculator().multiply(30,3,5)
print("Multiplication of three numbers : ",c2)