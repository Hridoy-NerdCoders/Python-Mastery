class Employee:
    no_of_employees = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@nerdcoder.com"
        
        Employee.no_of_employees += 1

    def full_name(self):
        return f'{self.first} {self.last}'.title()
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('sohanur','rahman',100000)
emp_2 = Employee('sonal','rahman',110000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(emp_1.__dict__)
print(Employee.__dict__)

Employee.raise_amount = 1.05

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

emp_1.raise_amount = 1.06

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(emp_1.__dict__)
print(Employee.no_of_employees)
