# Q.6: Print even and odd numbers from a user-defined array

size = int(input("Enter array size : "))
arr = []
for i in range(size):
    element = int(input(f"a{[i]} = "))
    arr.append(element)

print("\nOdd Numbers are : ")
for i in arr:
    if i%2!=0:
        print(i,end=",")

print("\nEven Numbers are : ")
for i in arr:
    if i%2==0:
        print(i,end=",")