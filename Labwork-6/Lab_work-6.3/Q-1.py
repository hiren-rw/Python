# Q.1: Raise ValueError for a negative number

n = int(input("Enter a Number : "))

if n < 0:
    raise ValueError("Number is Nagative!")

print("You Entered : ",n)