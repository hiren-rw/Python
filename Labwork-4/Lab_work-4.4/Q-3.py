# Q.3: Addition of two 1D arrays element by element

size = int(input("Enter size of Arrays : "))

print("Enter Array-A's Element : ")
a = []
for i in range(size):
    element = int(input(f"a1[{i}] = "))
    a.append(element)

print("\nEnter Array-B's Element : ")
b = []
for i in range(size):
    element = int(input(f"a2[{i}] = "))
    b.append(element)

print("Array A : ",a)
print("Array B : ",b)

c = []
for j in range(size):
    element = a[j] + b[j]
    c.append(element)

print("\nArray C : ",c)