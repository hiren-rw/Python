# Q.2: Transpose a 2x3 Matrix into a 3x2 Matrix

matrix = [
    [1,2,3],
    [4,5,6]
]

transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("Original 2x3 Matrix : ")
for i in matrix:
    print(i)

print("\nTransposed 3x2 Matrix : ")
for i in transpose:
    print(i)