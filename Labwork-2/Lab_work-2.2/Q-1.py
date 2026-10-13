a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

if a>b:
    if a>c:
        print("\nA is Maximum.")
    else:
        print("\nC is Maximum.")
else:
    if b>c:
        print("\nB is Maximum.")
    else:
        print("\nC is Maximum.")
