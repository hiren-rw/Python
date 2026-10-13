def names(*n):
    if not n:
        print("\nList is Empty")
    else:
        
        for i in n:
            print(i)


names("Abc","Pqr","Xyz")
names()                     # Empty List
