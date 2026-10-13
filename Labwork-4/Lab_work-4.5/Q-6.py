# Q.6: Sort a Tuple (or Convert to List to Sort and Back)

original_tuple = (45, 12, 89, 5, 23)

sorted_asc = tuple(sorted(original_tuple))

sorted_desc = tuple(sorted(original_tuple, reverse=True))

print("Original Tuple : ",original_tuple)
print("Sorted (Ascending) : ",sorted_asc)
print("Sorted (Descending) : ",sorted_desc)