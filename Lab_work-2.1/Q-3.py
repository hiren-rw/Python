a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

print()

if(a>b and a>c):
    print(a,"is Maximum")
elif(b>c):
    print(b,"is Maximum")
else:
    print(c,"is Maximum")
