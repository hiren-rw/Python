#  Q.11: Parent Constructor Invocation with super()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        # Call the parent class constructor to set name and salary
        super().__init__(name, salary)
        self.department = department
        
        print(f"Employee profile initialized for {self.name} with salary of : {self.salary}")
        print(f"Manager assigned to the {self.department} department")

m1 = Manager("Abc Xyz", 95000, "Engineering")