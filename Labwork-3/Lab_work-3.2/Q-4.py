# 1. Squares of 1 to 10
squares = []
print("Original First List :",squares)

for i in range(1,11):
    sq = i*i
    squares.append(sq)

print("Squared List :", squares)

# 2. Extract even numbers from a list of 1 to 20
list2 = list(range(1, 21))
print("\nOriginal Second List : ",list2)

even_num = [num for num in list2 if num % 2 == 0]
print("Even numbers :", even_num)

# 3. Convert all strings to lowercase
list3 = ["hello", "WORLD", "PyThOn"]
print("\nOriginal Third List : ",list3)

lower = [text.lower() for text in list3]
print("Lowercase list :", lower)
