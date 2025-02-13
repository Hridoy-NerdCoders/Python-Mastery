def hello_func():
    pass

hello_func()
print(hello_func)
print(hello_func())

def greetings():
    print('Good Morning!')
    
greetings()
print(greetings)
print(greetings())


#DRY
hello_func()
greetings()

def hi():
    return 'Hi, Hridoy!'

hi()
print(hi())
print(hi().upper())

print(len('Hridoy'))


def cus_greet(name):
    return f'Good Morning, {name}!'

print(cus_greet('Hridoy'))

def student_info(name,std_id='2102002'):
    return f'{name} , {std_id}'

print(student_info(name='Hridoy'))
#doen't matter:
print(student_info(std_id='2102002',name='Hridoy'))


#got error:
# def teacher_info(ta_id = '102',name):
#     return f'{ta_id}, {name}'

def bus_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
bus_info('Suihari','College Mor',name = 'Raju',age = 30)


courses = ['ML','Python','Java']
info = {'name':'Hridoy','age':23}

def course_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
course_info(courses,info)
course_info(*courses,**info)
