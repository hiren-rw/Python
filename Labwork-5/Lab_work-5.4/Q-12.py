# Q.12: issubclass() in Multilevel Inheritance

class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

# Checking relationships
print("Is Child a subclass of Parent? : ", issubclass(Child, Parent))
print("Is Child a subclass of Grandparent? : ", issubclass(Child, Grandparent))
print("Is Parent a subclass of Grandparent? : ", issubclass(Parent, Grandparent))
print("Is Grandparent a subclass of Child? : ", issubclass(Grandparent, Child))