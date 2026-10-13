num = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original List : ", num)

square = [n**2 for n in num]
print("Squares are : ",square)
