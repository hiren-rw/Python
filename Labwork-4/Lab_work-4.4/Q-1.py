# Q.1: Find the length of a 1D array without using any built-in function

size = int(input("Enter Array size : "))
arr = []

print("Enter Array Element : ")
for i in range(size):
    element = int(input(f"arr[{i}] = "))
    arr.append(element)

print("Array : ",arr)

c = 0
for i in arr:
    c += 1

print("Length of array is : ",c)