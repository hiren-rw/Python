def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    print(f"The Factorial of {n} is : {f}")


n = int(input("Enter number to find Factorial : "))
fact(n)
