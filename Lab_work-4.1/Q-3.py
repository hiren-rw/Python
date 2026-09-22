list1 = [10,20,30,40,50]
print("Original List : ",list1)

def square(num):

    return [n**2 for n in num]

result = square(list1)
print("Squared List : ",result)
