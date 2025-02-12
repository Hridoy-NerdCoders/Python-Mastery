language = 'Python'
if language=='Python' :
    print('Language is Python')
elif language =='Java':
    print('Language is Java')
elif language =='JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')
    
    
user = 'Admin'
logged_in = True

if user=='Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')
    
if not logged_in:
    print('Please log in')
else:
    print('Welcome')

a = [1,2,3]
b = [1,2,3]

print(a==b)
print(a is b)
print(id(a))
print(id(b))
print(id(a)==id(b))

a = b
print(a==b)
print(a is b)
print(id(a))
print(id(b))
print(id(a)==id(b))

# False Values:
false_values = [False, None, 0, 0.0, '', (), [], {}]

for value in false_values:
    if value:
        print(f'{value} is True')
    else:
        print(f'{value} is False')
        

# Check if list, dict, or tuple is empty
sample_list = []
sample_dict = {}
sample_tuple = ()

if not sample_list:
    print('The list is empty')
else:
    print('The list is not empty')
if not sample_dict:
    print('The dictionary is empty')
else:
    print('The dictionary is not empty')
if not sample_tuple:
    print('The tuple is empty')
else:
    print('The tuple is not empty')                
            
