list1 = ["cat", "dog", "bird"]
tup = ("cat", "dog", "bird")

print("Original List : ",list1)
print("Orogonal tuple : ",tup)

# Try changing the first item of the list
list1[0] = "lion"
print("\nUpdated list :",list1)

# Try changing the first item of the tuple
try:
    tup[0] = "lion"
except TypeError as e:
    print("\nTuple error :",e)
    print("Explanation : Lists are mutable, but tuples are immutable.")
