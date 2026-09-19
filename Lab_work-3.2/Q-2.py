tup = (10,50,25,40,99)
print(tup)

print("Third item :",tup[2])

# Trying to change the second value and handle the error
try:
    tup[1] = 99
except TypeError as e:
    print("Error encountered :", e)
    print("Explanation : Tuples are immutable. Once created, their values cannot be changed.")
