# Q.5: Check if a user input number exists in the array and find index

arr = [10,22,34,59,55,40,60,77,81,95,100]

n = int(input("\nEnter number for search : "))

if n in arr:
    print(f"Number {n} is founded at index {arr.index(n)}")
else:
    print("Not Found")