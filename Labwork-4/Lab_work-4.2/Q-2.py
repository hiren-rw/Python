def fibo(n):

    if n<0:
        print("\nNegative not Allowed.")
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

n = int(input("Enter Last value : "))
print(f"{n}th Fibbonacci :{fibo(n)}")
