# Q.2: Multiple Inheritance

class teacher:
    def teach(self):
        print("I tech students.")

class administrator:
    def manage(self):
        print("I manage the school.")

class headmaster(teacher,administrator):        # Multiple Inheritance
    def head(self):
        print("I am the Headmaster.")

a1 = headmaster()
a1.teach()
a1.manage()
a1.head()