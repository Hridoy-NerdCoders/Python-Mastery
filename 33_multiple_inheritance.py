class Employee:
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"The name is {self.dance}")
    
class DancerEmployee(Employee,Dancer):
    def __init__(self, dance,name):
        self.dance = dance
        self.name = name
        
o = DancerEmployee("Uradhura","Rai")
print(o.name)
print(o.dance)
# Ekhane Employee er show() method call hobe karon employee age inherit hoise...
o.show()

print(DancerEmployee.mro())