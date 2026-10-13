a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

if a<b:
    if a<c:
        print("\nA is Minimum.")
    else:
        print("\nC is Minimum.")
else:
    if b<c:
        print("\nB is Minimum.")
    else:
        print("\nC is Minimum.")
