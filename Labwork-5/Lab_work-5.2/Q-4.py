# Q.4 Employee with Default Constructor and Destructor

class Employee:
    
    def __init__(self):
        self.name = "New User-1"
        self.role = "Intern"
        print("Employee session started for",self.name)

    def __del__(self):
        print("Farewell! Thank you for your service,",self.name)


e1 = Employee()
del e1