# Q.5: Hybrid Inheritance

class School:
    def __init__(self):
        print("School initialized")

class Teacher(School):
    def __init__(self):
        super().__init__()
        print("Teacher initialized")

class Administrator(School):
    def __init__(self):
        super().__init__()
        print("Administrator initialized")

class Headmaster(Teacher, Administrator):
    def __init__(self):
        super().__init__()
        print("Headmaster initialized")

hm = Headmaster()