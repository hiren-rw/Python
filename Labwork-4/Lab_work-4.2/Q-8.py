a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
c = float(input("Enter third number : "))

# lambda function
find_max = lambda a, b, c: max(a, b, c)

result = find_max(a,b,c)
print("The largest number is :", result)
