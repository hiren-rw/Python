# Q.6: Division with Invalid Input & finally Block

try:
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    print("Division :", a / b)

except ValueError:
    print("Error : Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error : Division by zero is not allowed.")

finally:
    print("Division operation attempt finished.")