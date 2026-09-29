def fact(n):
    if n<0:
        print("\nNegetive numbers not allowed.")
    else:

        if n==1 or n==0:
            return 1
        
        return n*fact(n-1)

n = int(input("Enter number to find Factorial : "))
result = fact(n)
print("Factorial is :",result)
