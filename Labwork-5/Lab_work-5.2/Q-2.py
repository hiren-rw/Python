# Q.2 Animal Class with Method

class animal:
    def __init__(self,name):
        self.name = name

    def disp(self):
        print(f"Animal name is : {self.name}")

s1 = animal("Lion")
s1.disp()