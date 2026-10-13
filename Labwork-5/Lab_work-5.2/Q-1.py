# Q.1 Class Objects and Destructor (del)

class sample:
    def __init__(self,name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} is being Destroyed.")

s1 = sample("A")
s2 = sample("B")

print("\nNow Deleting Objects : ")
del s1
del s2