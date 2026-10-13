# Q.1: Create a 3x3 Matrix and Display in Tabular Format

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("3x3 Matrix in tabular format : ")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()