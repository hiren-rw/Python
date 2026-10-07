# Q.2: Find the average of a 1D array without using built-in functions

size = int(input("Enter Array size : "))
arr = []

print("Enter Array Element : ")
for i in range(size):
    element = int(input(f"arr[{i}] = "))
    arr.append(element)

print("Array : ",arr)

total = 0
count = 0

for i in range(size):
    count += 1
    total += arr[i]

print("Total is : ",total)
print("Average is : ",total/count)