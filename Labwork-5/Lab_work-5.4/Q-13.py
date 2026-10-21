# Q.13: super() inside an Overridden Method

class Base:
    def display(self):
        print("Message from the Base class!")

class Derived(Base):
    def display(self):
        # Call the parent class display method first
        super().display()
        # Add extra functionality specific to Derived class
        print("Message from the Derived class!")

obj = Derived()
obj.display()