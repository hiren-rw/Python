# Q.4: Find the Maximum and Minimum Values in a 2D Array

matrix = [
    [33,20,5],
    [99,45,23]
]

list1 = [element for i in matrix for element in i]

max_value = max(list1)
min_value = min(list1)

print("Maximum Value : ",max_value)
print("Minimum Value : ",min_value)