# Q.7: Square Root with try, else, and finally

try:
    num = float(input("Enter a number : "))
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    root = num ** 0.5

except ValueError as e:
    print("Invalid input :", e)

else:
    print("Square root :", root)
    
finally:
    print("Execution complete.")