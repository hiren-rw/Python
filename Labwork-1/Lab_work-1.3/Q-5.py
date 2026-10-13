a = 10
b = 10
print("Address of a : ",id(a))
print("Address of b : ",id(b))
print("Both same? : ",id(a) == id(b))

a = a + 5
print("\nAfter Changing one value : ")
print("Address of a : ",id(a))
print("Address of b : ",id(b))
print("Both same? : ",id(a) == id(b))
