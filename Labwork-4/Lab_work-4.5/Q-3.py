# Q.3: Calculate the Sum of All Elements in a 2D Array Separately

matrix = [
    [5,10,15],
    [20,25,30]
]

for i, row in enumerate(matrix):
    print(f"Sum of elements in Row {i + 1}: {sum(row)}")

total_sum = sum(sum(row) for row in matrix)
print("Total overall sum : ",total_sum)