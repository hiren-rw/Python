# Q.1: Single Inheritance

class parent:
    def display(self):
        print("This is parent class method called by child class.")

class child(parent):        # single inheritance
    def call_display(self):
        self.display()

c1 = child()
c1.call_display()           # calling child class