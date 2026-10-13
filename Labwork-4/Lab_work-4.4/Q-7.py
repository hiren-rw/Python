# Q.7: Print first 5 elements and alternate elements

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("\nArray : ",arr)

print("\nFirst five elements : ")
for i in range(5):
    print(arr[i],end=", ")

print("\n\nAlternate elements : ")
for i in range(0, len(arr), 2):
    print(arr[i],end=", ")