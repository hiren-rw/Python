a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))
d = int(input("Enter Fourth Number : "))

if a>b:
    if a>c:
        if a>d:
            print("\nA is Maximum.")
        else:
            print("\nD is Maximum.")
    else:
        if c>d:
            print("\nC is Maximum.")
        else:
            print("\nD is Maximum.")
else:
    if b>c:
        if b>d:
            print("\nB is Maximum.")
        else:
            print("\nD is Maximum.")
    else:
        if c>d:
            print("\nC is Maximum.")
        else:
            print("\nD is Maximum.")
