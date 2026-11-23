
# Q.1: Division by Zero

try :
    a = float(input("Enter First Number : "))
    b = float(input("Enter Second Number : "))
    result = a/b
    print("Division : ",result)
except ZeroDivisionError:
    print("Error : Cannot Divide by Zero.")