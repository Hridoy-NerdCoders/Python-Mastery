#Python Object-Oriented Programming

# class Emplyee:
#     pass

# emp_1 = Emplyee()
# emp_2 = Emplyee()

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Sohanur'
# emp_1.last = 'Rahman'
# emp_1.email = 'sohanurrahman@gmail.com'
# emp_1.pay = 100000

# emp_2.first = 'Sonal'
# emp_2.last = 'Rahman'
# emp_2.email = 'sonalrahman@gmail.com'
# emp_2.pay = 110000


# print(emp_1.email)
# print(emp_2.email)


class Employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@nerdcoder.com"
    #we have to pass self for every methods:
    def full_name(self):
        return f'{self.first} {self.last}'.title()
        

emp_1 = Employee('sohanur','rahman',100000)
emp_2 = Employee('sonal','rahman',110000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.full_name())
#the above line transform to this below line:
print(Employee.full_name(emp_1))
print(emp_2.full_name())