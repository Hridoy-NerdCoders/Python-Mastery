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


