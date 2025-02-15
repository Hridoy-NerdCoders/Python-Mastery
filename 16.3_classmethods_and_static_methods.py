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
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
    #Alternative Constructor:    
    @classmethod
    def from_string(cls,emp_str):
        first, last , pay = emp_str.split('_')
        return cls(first,last,pay)
    
    #Don't operate on instance or class:
    @staticmethod
    def is_workday(day):
        if day == 'Friday' or day == 'Saturday':
            return False
        return True
        

emp_1 = Employee('sohanur','rahman',100000)
emp_2 = Employee('sonal','rahman',110000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.set_raise_amt(1.06)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_n = Employee.from_string('John_DOE_70000')
print(emp_n.email)


print(Employee.is_workday('Friday'))
print(Employee.is_workday('Saturday'))