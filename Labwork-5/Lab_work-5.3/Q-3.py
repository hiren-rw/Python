# Q.3: Multilevel Inheritance

class grandparent:
    def grandrole(self):
        print("Role : Grandparents")

class parent(grandparent):
    def parentrole(self):
        print("Role : Parents")

class child(parent):        # Multilevel Inheritance
    def childrole(self):
        print("Role : Child")

a1 = child()
a1.grandrole()
a1.parentrole()
a1.childrole()