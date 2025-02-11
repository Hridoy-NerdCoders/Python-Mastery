#Dictionary:
student = {'name':'Hridoy','age':23,'courses':['Python','Java'],1:'Islam'}
#keys can be any immutable datatypes
print(student)
print(student['name'])
print(student['courses'])
print(student[1])
print(student.get('name'))
# print(student['phone'])#got error
print(student.get('phone'))#safer
print(student.get('phone','Not Found!'))

student['phone'] = '017XXXXXXXX'
print(student.get('phone','Not Found!'))
student['name'] = 'SRHridoy'
print(student)

#multiple update:
student.update({'name':'Md. Sohanur Rahman Hridoy','isMarried':True})
print(student)

del student[1]
print(student)

popped = student.pop('isMarried')
print(popped)
print(student)

print(len(student))

print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
    print(key,value)
    
for key,value in student.items():
    print(f'{key} : {value}')

