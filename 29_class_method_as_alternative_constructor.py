class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    @classmethod
    def fromStr(cls, string):
        return cls(string.split('-')[0],int(string.split('-')[1]))
        
        
e = Employee("Hridoy", 1200)

print(e.name)
print(e.salary)


e1 = "Jr-1232"
# e1 = Employee(e1.split('-')[0],e1.split('-')[1])
# print(e1.name)
# print(e1.salary)

#Erokom bivinno format e input asle cls method use korbo alternative constructor hisebe...
e1 = Employee.fromStr(e1)
print(e1.name)
print(e1.salary)
#froStr first e shaping kore nisse then init call kore intialize kore disse...