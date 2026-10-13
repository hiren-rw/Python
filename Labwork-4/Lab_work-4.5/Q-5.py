# Q.5: Sort a List of Tuples in Increasing Order by the Last Element

tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_list = sorted(tuple_list, key=lambda x: x[-1])

print("Sorted List of Tuples : ")
print(sorted_list)