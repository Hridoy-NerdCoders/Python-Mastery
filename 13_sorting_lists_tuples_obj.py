li = [9,1,4,5,22,21,33,1,3,9]

s_li = sorted(li)
print('Sorted Variable: \t',s_li)
print('Original Variable: \t',li)
li.sort()
print('Original Variable: \t',li)

s_li = sorted(li, reverse=True)
print('Sorted Variable: \t',s_li)
print('Original Variable: \t',li)
li.sort(reverse=True)
print('Original Variable: \t',li)


tup = (9,1,4,5,22,21,33,1,3,9)
# tup.sort()
s_tup = sorted(tup)
print('Tuple\t:',s_tup)

dic = {'name':'Hridoy','Job':'Programming','Age':None,'OS':'Ubuntu'}
s_dic = sorted(dic)
print('Dict\t:',s_dic)


li1 = [-4,5,2,-1,0,-9]
s_li1 = sorted(li1)
print(li1)
print(s_li1)

#sorted based on absolute value:
s_li1 = sorted(li1,key=abs)
print(s_li1)

#sorting Objs:
from operator import attrgetter
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return f'{self.name},{self.age},{self.salary}'
    
e1 = Employee('Hridoy',23,100000)
e2 = Employee('Ravin',24,100000)
e3 = Employee('Ravi', 22, 100000)

employees = [e1,e2,e3]

# def e_sort(emp):
#     return emp.age

# s_employees = sorted(employees,key=e_sort)
# print(s_employees) 
    
# s_employees = sorted(employees,key=lambda e:e.name)
# print(s_employees)      

s_employees = sorted(employees,key=attrgetter('age'))
print(s_employees)