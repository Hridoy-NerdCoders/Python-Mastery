class Employee:
    company_name = "DJ"
    noOfEmployees = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1
        
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.company_name} is {self.raise_amount}")
        


emp1 = Employee("Hridoy")
emp1.raise_amount = 0.3
emp1.company_name = 'DJuo'# Eta na thakle orthat instant var ta na thakle class var tai call hoto..
emp1.showDetails()
# Employee.showDetails(emp1)#These two lines are same. The above line is interpreted as this line...
emp2 = Employee('Rai')
emp2.showDetails()

print(Employee.company_name)
Employee.company_name = "Apple"
emp2.showDetails()


        