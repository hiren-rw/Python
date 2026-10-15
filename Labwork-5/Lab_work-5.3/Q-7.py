# Q.7: dir() Function

class Sample:
    def __init__(self):
        self.name = "ABC"
        
    def my_method_1(self):
        pass
            
    def my_method_2(self):
        pass

obj = Sample()
print(dir(obj))