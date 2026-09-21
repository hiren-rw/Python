string = "123"
print("String :",string)
list_1 = [1,2,3]
print("List-1 :",list_1)
tup = (4,5,6)
print("Tuple : ",tup)
list_2 = [(1,'A'),(2,'B')]
print("List-2 : ",list_2)

# Conversion :
a = int(string)         # String to Integer
print("\nString to Integer : ",a)

b = tuple(list_1)       # List to Tuple
print("List to Tuple : ",b)

c = list(tup)           # Tuple to List
print("Tuple to List : ",c)

d = dict(list_2)        # List to Dictionary
print("List to Dictionary : ",d)
