# Python Learning Journey
## What is Python?

Python is a high-level, interpreted programming language known for its readability and versatility. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is widely used for web development, data analysis, artificial intelligence, scientific computing, and more.

## Is Python a Fully Object-Oriented Programming Language?

Python is not a fully object-oriented programming language, but it supports object-oriented programming (OOP) principles such as inheritance, polymorphism, encapsulation, and abstraction. It also supports procedural and functional programming paradigms.

### Built-in Data Types and Classes

In Python, everything is an object, including built-in data types:
- **Integers**: Instances of the `int` class.
- **Strings**: Instances of the `str` class.
- **Lists**: Instances of the `list` class.
- **Tuples**: Instances of the `tuple` class.
- **Dictionaries**: Instances of the `dict` class.

### Example: Using Built-in Data Types as Classes
```python
# Integer
num = 10
print(type(num))  # Output: <class 'int'>

# String
message = "Hello, World!"
print(type(message))  # Output: <class 'str'>

# List
courses = ['Python', 'Java', 'C++']
print(type(courses))  # Output: <class 'list'>

# Dictionary
student = {'name': 'Hridoy', 'age': 23}
print(type(student))  # Output: <class 'dict'>
```

## Why Python is Not a Fully Object-Oriented Programming Language

Python supports multiple programming paradigms, not just OOP. This flexibility allows developers to choose the most appropriate paradigm for their specific use case, but it also means that Python does not enforce OOP principles as strictly as some other languages.

### Fully Object-Oriented Programming Languages

Fully object-oriented languages enforce OOP principles throughout the language:
- **Smalltalk**: Treats everything as an object, including numbers and control structures.
- **Ruby**: Designed to be fully object-oriented, enforcing OOP principles strictly.

### Characteristics of Fully Object-Oriented Languages
1. **Everything is an Object**: All entities are objects.
2. **Message Passing**: Operations are performed by sending messages to objects.
3. **Encapsulation**: Data and methods are encapsulated within objects.
4. **Inheritance and Polymorphism**: Objects can inherit properties and methods, and polymorphism allows objects to be treated as instances of their parent class.

## Are Java, C++, and C# Fully Object-Oriented Programming Languages?

### Java
- **Mostly Object-Oriented**: Enforces OOP principles but has primitive data types (e.g., `int`, `char`, `boolean`) that are not objects. Provides wrapper classes (e.g., `Integer`, `Character`, `Boolean`).

### C++
- **Not Fully Object-Oriented**: Multi-paradigm language supporting procedural, object-oriented, and generic programming. Allows procedural programming with functions and global variables.

### C#
- **Mostly Object-Oriented**: Enforces OOP principles and treats everything as an object, including primitive data types through the .NET framework's `System` namespace. Provides struct types (e.g., `Int32`, `Char`, `Boolean`).

### Summary Table

| Language | Fully Object-Oriented | Notes |
|----------|-----------------------|-------|
| Python   | No                    | Supports multiple paradigms |
| Java     | Mostly                | Has primitive data types, uses wrapper classes |
| C++      | No                    | Multi-paradigm, supports procedural programming |
| C#       | Mostly                | Has primitive data types, uses struct types |

In summary, while Python supports OOP principles, its flexibility in supporting multiple paradigms means it is not considered fully object-oriented. Java and C# are close to being fully object-oriented but have some exceptions with primitive data types. C++ is not fully object-oriented due to its support for multiple programming paradigms.


## Python String Operations

### Basic String Operations
```python
message = "Hello World"
escape = 'Hridoy\'s World'
using_single_to_handle_double = 'I am going to be a "..."'
using_double_to_handle_single = "I am going to be a '...'"
muliple_line = """
This is great to learn python 
from "Corey Shefer's" lessons and just awesome
"""
print(message)
print(escape)
print(using_single_to_handle_double)
print(using_double_to_handle_single)
print(muliple_line)
```

### String Length and Indexing
```python
print(len(message))  # Output: 11
print(message[0])    # Output: H
print(message[-1])   # Output: d
print(message[10])   # Output: d
# print(message[11]) # IndexError: string index out of range
```

### String Slicing
```python
print(message[0:5])  # Output: Hello (start is inclusive, end is exclusive)
print(message[:5])   # Output: Hello
print(message[6:])   # Output: World
```

### String Methods
```python
print(message.lower())  # Output: hello world
print(message)          # Output: Hello World
print(message.upper())  # Output: HELLO WORLD
print(message.count('l'))  # Output: 3
print(message.find('l'))   # Output: 2
print(message.count("ll")) # Output: 1
print(message.find('Universe'))  # Output: -1 (not found)
```

### String Replacement
```python
print(message.replace('World', 'Bangladesh'))  # Output: Hello Bangladesh
print(message)  # Output: Hello World
message = message.replace('World', 'Bangladesh')
print(message)  # Output: Hello Bangladesh
```

### String Concatenation
```python
greeting = 'Bye bye'
name = 'Muhammad Ali'
message = greeting + ', ' + name + '. See you!'
print(message)  # Output: Bye bye, Muhammad Ali. See you!
```

### String Formatting
```python
message = '{}, {}. See you!'.format(greeting, name.upper())
print(message)  # Output: Bye bye, MUHAMMAD ALI. See you!

message = f'{greeting}, {name.upper()}. See you!'
print(message)  # Output: Bye bye, MUHAMMAD ALI. See you!
```

### String Methods and Help
```python
print(dir(message))  # Lists all the attributes and methods of the string object
print(help(str))     # Provides help documentation for the str class
print(help(str.lower))  # Provides help documentation for the lower() method
```

## Basic Python Operations

### 1. Variable Assignment and Type Checking
Assigning integer and float values to variables, and printing the values and their types.
```python
num = 3
print(num)  # Output: 3
print(type(num))  # Output: <class 'int'>

float_num = 3.1416
print(float_num)  # Output: 3.1416
print(type(float_num))  # Output: <class 'float'>
```

### 2. Arithmetic Operations
Performing addition, subtraction, multiplication, division, floor division, exponentiation, and modulus operations. Demonstrating operator precedence with parentheses.
```python
# Arithmetic Operators
print(3 + 2)  # Output: 5
print(3 - 2)  # Output: 1
print(3 * 2)  # Output: 6
print(3 / 2)  # Output: 1.5
print(3 // 2)  # Output: 1
print(3 ** 2)  # Output: 9

# Modulus operation to observe the pattern of even and odd numbers
print(3 % 2)  # Output: 1
print(4 % 2)  # Output: 0
print(5 % 2)  # Output: 1
print(6 % 2)  # Output: 0

# Operator precedence
print(3 * 2 + 1)  # Output: 7
print(3 * (2 + 1))  # Output: 9
```

### 3. Variable Manipulation
Incrementing and multiplying variables using shorthand operators. Using the `abs()` function to get the absolute value of a number. Using the `round()` function to round a floating-point number to a specified number of decimal places.
```python
num = 1
print(num)  # Output: 1
num = num + 1
print(num)  # Output: 2
num += 1
print(num)  # Output: 3

num *= 10
print(num)  # Output: 30

num = -3
print(num)  # Output: -3
print(abs(num))  # Output: 3

print(float_num)  # Output: 3.1416
print(round(float_num))  # Output: 3
print(round(float_num, 2))  # Output: 3.14
```

### 4. Comparison Operators
Checking equality, inequality, and relational comparisons between two numbers. Demonstrating string concatenation and type conversion from string to integer for arithmetic operations.
```python
num_1 = 3
num_2 = 2

print(num_1 == num_2)  # Output: False
print(num_1 < num_2)  # Output: False
print(num_1 <= num_2)  # Output: False
print(num_1 != num_2)  # Output: True
print(num_1 > num_2)  # Output: True
print(num_1 >= num_2)  # Output: True

num_1 = '100'
num_2 = '200'
print(num_1 + num_2)  # Output: 100200
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)  # Output: 300
```

## List, Tuple, and Set Operations

### List Operations
Lists in Python are mutable, meaning they can be changed after creation. Here are some common operations you can perform on lists:

#### Creating and Accessing Lists
```python
courses = ['Algorithm', 'Python', 'Java', 'DS', 'C++']
print(courses)  # Output: ['Algorithm', 'Python', 'Java', 'DS', 'C++']
print(len(courses))  # Output: 5
print(courses[0])  # Output: Algorithm
print(courses[4])  # Output: C++
print(courses[-1])  # Output: C++
print(courses[-4])  # Output: Python
```

#### Slicing Lists
```python
print(courses[1:5])  # Output: ['Python', 'Java', 'DS', 'C++']
print(courses[:5])  # Output: ['Algorithm', 'Python', 'Java', 'DS', 'C++']
print(courses[1:])  # Output: ['Python', 'Java', 'DS', 'C++']
```

#### Modifying Lists
```python
courses.append('Django')
print(courses)  # Output: ['Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django']

courses.insert(0, 'Fundamentals')
print(courses)  # Output: ['Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django']

courses_2 = ['Dart', 'Flutter']
courses.insert(0, courses_2)
print(courses)  # Output: [['Dart', 'Flutter'], 'Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django']
print(courses[0])  # Output: ['Dart', 'Flutter']

courses.pop(0)
print(courses)  # Output: ['Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django']

courses.append(courses_2)
print(courses)  # Output: ['Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django', ['Dart', 'Flutter']]

courses.pop()
print(courses)  # Output: ['Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django']

courses.extend(courses_2)
print(courses)  # Output: ['Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django', 'Dart', 'Flutter']

courses.remove('Fundamentals')
print(courses)  # Output: ['Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django', 'Dart', 'Flutter']

popped = courses.pop()
print(popped)  # Output: Flutter
print(courses)  # Output: ['Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django', 'Dart']
```

#### Reversing and Sorting Lists
```python
courses.reverse()
print(courses)  # Output: ['Dart', 'Django', 'C++', 'DS', 'Java', 'Python', 'Algorithm']

courses.sort()
print(courses)  # Output: ['Algorithm', 'C++', 'DS', 'Dart', 'Django', 'Java', 'Python']

nums = [1, 3, 4, 2, 1, 88, 12, 9]
nums.sort()
print(nums)  # Output: [1, 1, 2, 3, 4, 9, 12, 88]

nums.sort(reverse=True)
print(nums)  # Output: [88, 12, 9, 4, 3, 2, 1, 1]

sorted_nums_ascen = sorted(nums)
print(sorted_nums_ascen)  # Output: [1, 1, 2, 3, 4, 9, 12, 88]
print(nums)  # Output: [88, 12, 9, 4, 3, 2, 1, 1]
```

#### Other List Operations
```python
print(min(nums))  # Output: 1
print(max(nums))  # Output: 88
print(sum(nums))  # Output: 120

print(courses.index('Java'))  # Output: 5
print('Art' in courses)  # Output: False
print('C++' in courses)  # Output: True

for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(index, course)

courses_str = ', '.join(courses)
print(courses_str)  # Output: Algorithm, C++, DS, Dart, Django, Java, Python

courses_str = ' $ '.join(courses)
print(courses_str)  # Output: Algorithm $ C++ $ DS $ Dart $ Django $ Java $ Python

new_list_of_courses = courses_str.split(' $ ')
print(new_list_of_courses)  # Output: ['Algorithm', 'C++', 'DS', 'Dart', 'Django', 'Java', 'Python']
```

#### List Mutability
```python
list_1 = ['Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy']
list_2 = list_1
print(list_1)  # Output: ['Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy']
print(list_2)  # Output: ['Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy']

list_1[0] = 'Unknown!'
print(list_1)  # Output: ['Unknown!', 'Tasin', 'Nova', 'Rupa', 'Hridoy']
print(list_2)  # Output: ['Unknown!', 'Tasin', 'Nova', 'Rupa', 'Hridoy']
```

### Tuple Operations
Tuples in Python are immutable, meaning they cannot be changed after creation. They are useful for fixed collections of items.

```python
tuple_1 = ('Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy')
tuple_2 = tuple_1

print(tuple_1)  # Output: ('Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy')
print(tuple_2)  # Output: ('Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy')

# tuple_1[0] = 'Unknown!'  # This will raise a TypeError
```

### Set Operations
Sets in Python are unordered collections of unique elements. They are useful for membership tests and eliminating duplicate entries.

```python
cs_courses = {'Discrete Mathematics', 'Fundamentals of Computer', 'Software Engineering', 'Computer Networks'}
print(cs_courses)  # Output: {'Discrete Mathematics', 'Fundamentals of Computer', 'Software Engineering', 'Computer Networks'}
```





## List, Tuple, and Set Operations

### List Operations
Lists in Python are mutable, meaning they can be changed after creation. Here are some common operations you can perform on lists:

#### Creating and Accessing Lists
```python
courses = ['Algorithm', 'Python', 'Java', 'DS', 'C++']
print(courses)  # Output: ['Algorithm', 'Python', 'Java', 'DS', 'C++']
print(len(courses))  # Output: 5
print(courses[0])  # Output: Algorithm
print(courses[4])  # Output: C++
print(courses[-1])  # Output: C++
print(courses[-4])  # Output: Python
```

#### Slicing Lists
```python
print(courses[1:5])  # Output: ['Python', 'Java', 'DS', 'C++']
print(courses[:5])  # Output: ['Algorithm', 'Python', 'Java', 'DS', 'C++']
print(courses[1:])  # Output: ['Python', 'Java', 'DS', 'C++']
```

#### Modifying Lists
```python
courses.append('Django')
print(courses)  # Output: ['Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django']

courses.insert(0, 'Fundamentals')
print(courses)  # Output: ['Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django']

courses_2 = ['Dart', 'Flutter']
courses.insert(0, courses_2)
print(courses)  # Output: [['Dart', 'Flutter'], 'Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django']
print(courses[0])  # Output: ['Dart', 'Flutter']

courses.pop(0)
print(courses)  # Output: ['Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django']

courses.append(courses_2)
print(courses)  # Output: ['Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django', ['Dart', 'Flutter']]

courses.pop()
print(courses)  # Output: ['Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django']

courses.extend(courses_2)
print(courses)  # Output: ['Fundamentals', 'Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django', 'Dart', 'Flutter']

courses.remove('Fundamentals')
print(courses)  # Output: ['Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django', 'Dart', 'Flutter']

popped = courses.pop()
print(popped)  # Output: Flutter
print(courses)  # Output: ['Algorithm', 'Python', 'Java', 'DS', 'C++', 'Django', 'Dart']
```

#### Reversing and Sorting Lists
```python
courses.reverse()
print(courses)  # Output: ['Dart', 'Django', 'C++', 'DS', 'Java', 'Python', 'Algorithm']

courses.sort()
print(courses)  # Output: ['Algorithm', 'C++', 'DS', 'Dart', 'Django', 'Java', 'Python']

nums = [1, 3, 4, 2, 1, 88, 12, 9]
nums.sort()
print(nums)  # Output: [1, 1, 2, 3, 4, 9, 12, 88]

nums.sort(reverse=True)
print(nums)  # Output: [88, 12, 9, 4, 3, 2, 1, 1]

sorted_nums_ascen = sorted(nums)
print(sorted_nums_ascen)  # Output: [1, 1, 2, 3, 4, 9, 12, 88]
print(nums)  # Output: [88, 12, 9, 4, 3, 2, 1, 1]
```

#### Other List Operations
```python
print(min(nums))  # Output: 1
print(max(nums))  # Output: 88
print(sum(nums))  # Output: 120

print(courses.index('Java'))  # Output: 5
print('Art' in courses)  # Output: False
print('C++' in courses)  # Output: True

for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(index, course)

courses_str = ', '.join(courses)
print(courses_str)  # Output: Algorithm, C++, DS, Dart, Django, Java, Python

courses_str = ' $ '.join(courses)
print(courses_str)  # Output: Algorithm $ C++ $ DS $ Dart $ Django $ Java $ Python

new_list_of_courses = courses_str.split(' $ ')
print(new_list_of_courses)  # Output: ['Algorithm', 'C++', 'DS', 'Dart', 'Django', 'Java', 'Python']
```

#### List Mutability
```python
list_1 = ['Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy']
list_2 = list_1
print(list_1)  # Output: ['Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy']
print(list_2)  # Output: ['Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy']

list_1[0] = 'Unknown!'
print(list_1)  # Output: ['Unknown!', 'Tasin', 'Nova', 'Rupa', 'Hridoy']
print(list_2)  # Output: ['Unknown!', 'Tasin', 'Nova', 'Rupa', 'Hridoy']
```

### Tuple Operations
Tuples in Python are immutable, meaning they cannot be changed after creation. They are useful for fixed collections of items.

```python
tuple_1 = ('Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy')
tuple_2 = tuple_1

print(tuple_1)  # Output: ('Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy')
print(tuple_2)  # Output: ('Tanha', 'Tasin', 'Nova', 'Rupa', 'Hridoy')

# tuple_1[0] = 'Unknown!'  # This will raise a TypeError
```

### Set Operations
Sets in Python are unordered collections of unique elements. They are useful for membership tests and eliminating duplicate entries.

```python
cs_courses = {'Discrete Mathematics', 'Fundamentals of Computer', 'Software Engineering', 'Computer Networks'}
print(cs_courses)  # Output: {'Discrete Mathematics', 'Fundamentals of Computer', 'Software Engineering', 'Computer Networks'}

# Membership test
print('Computer Networks' in cs_courses)  # Output: True

ece_courses = {'Digital Communication', 'Fundamentals of Computer', 'Software Engineering', 'Computer Networks', 'Digital Electronics'}
print(ece_courses)  # Output: {'Digital Communication', 'Fundamentals of Computer', 'Software Engineering', 'Computer Networks', 'Digital Electronics'}

print(cs_courses.intersection(ece_courses))  # Output: {'Fundamentals of Computer', 'Software Engineering', 'Computer Networks'}
print(cs_courses.difference(ece_courses))  # Output: {'Discrete Mathematics'}
print(cs_courses.union(ece_courses))  # Output: {'Discrete Mathematics', 'Fundamentals of Computer', 'Software Engineering', 'Computer Networks', 'Digital Communication', 'Digital Electronics'}
```

### Creating Empty Collections
```python
# Empty lists
empty_list = []
empty_list = list()

# Empty tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty sets
empty_set = set()
```
### Summary

| Feature             | Lists                                      | Tuples                                     | Sets                                      |
|---------------------|--------------------------------------------|--------------------------------------------|-------------------------------------------|
| Mutability          | Mutable (can be changed)                   | Immutable (cannot be changed)              | Mutable (can be changed)                  |
| Order               | Ordered                                    | Ordered                                    | Unordered                                 |
| Duplicates          | Allows duplicate elements                  | Allows duplicate elements                  | Does not allow duplicate elements         |
| Common Operations   | Creating, accessing, slicing, modifying, reversing, sorting, and other list-specific methods | Creating and accessing                     | Membership tests, eliminating duplicates, union, intersection, difference |
| Use Case            | General-purpose, flexible collections      | Fixed collections of items                 | Unique collections, set operations        |
| Empty Collections   | `empty_list = []` or `empty_list = list()` | `empty_tuple = ()` or `empty_tuple = tuple()` | `empty_set = set()` (not `{}` which creates a dictionary) |
```


## Dictionary Operations

Dictionaries in Python are mutable, unordered collections of key-value pairs. Keys can be any immutable data types, such as strings, numbers, or tuples.

### Creating and Accessing Dictionaries
```python
student = {'name': 'Hridoy', 'age': 23, 'courses': ['Python', 'Java'], 1: 'Islam'}
print(student)  # Output: {'name': 'Hridoy', 'age': 23, 'courses': ['Python', 'Java'], 1: 'Islam'}
print(student['name'])  # Output: Hridoy
print(student['courses'])  # Output: ['Python', 'Java']
print(student[1])  # Output: Islam
print(student.get('name'))  # Output: Hridoy
# print(student['phone'])  # KeyError: 'phone'
print(student.get('phone'))  # Output: None
print(student.get('phone', 'Not Found!'))  # Output: Not Found!
```

### Adding and Updating Dictionary Entries
```python
student['phone'] = '017XXXXXXXX'
print(student.get('phone', 'Not Found!'))  # Output: 017XXXXXXXX
student['name'] = 'SRHridoy'
print(student)  # Output: {'name': 'SRHridoy', 'age': 23, 'courses': ['Python', 'Java'], 1: 'Islam', 'phone': '017XXXXXXXX'}

# Multiple updates
student.update({'name': 'Md. Sohanur Rahman Hridoy', 'isMarried': True})
print(student)  # Output: {'name': 'Md. Sohanur Rahman Hridoy', 'age': 23, 'courses': ['Python', 'Java'], 1: 'Islam', 'phone': '017XXXXXXXX', 'isMarried': True}
```

### Removing Dictionary Entries
```python
del student[1]
print(student)  # Output: {'name': 'Md. Sohanur Rahman Hridoy', 'age': 23, 'courses': ['Python', 'Java'], 'phone': '017XXXXXXXX', 'isMarried': True}

popped = student.pop('isMarried')
print(popped)  # Output: True
print(student)  # Output: {'name': 'Md. Sohanur Rahman Hridoy', 'age': 23, 'courses': ['Python', 'Java'], 'phone': '017XXXXXXXX'}
```

### Dictionary Methods
```python
print(len(student))  # Output: 4
print(student.keys())  # Output: dict_keys(['name', 'age', 'courses', 'phone'])
print(student.values())  # Output: dict_values(['Md. Sohanur Rahman Hridoy', 23, ['Python', 'Java'], '017XXXXXXXX'])
print(student.items())  # Output: dict_items([('name', 'Md. Sohanur Rahman Hridoy'), ('age', 23), ('courses', ['Python', 'Java']), ('phone', '017XXXXXXXX')])
```

### Iterating Through a Dictionary
```python
for key, value in student.items():
    print(key, value)
    # Output:
    # name Md. Sohanur Rahman Hridoy
    # age 23
    # courses ['Python', 'Java']
    # phone 017XXXXXXXX

for key, value in student.items():
    print(f'{key} : {value}')
    # Output:
    # name : Md. Sohanur Rahman Hridoy
    # age : 23
    # courses : ['Python', 'Java']
    # phone : 017XXXXXXXX
```


## Conditional Statements and Match Statements

### Traditional Conditional Statements
Python supports traditional conditional statements using `if`, `elif`, and `else` keywords. Here are some examples:

#### Example 1: Language Check
```python
language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')
```

#### Example 2: User Authentication
```python
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

if not logged_in:
    print('Please log in')
else:
    print('Welcome')
```

### Match Statements
Python 3.10 introduced the `match` statement, which is similar to switch-case statements in other languages. It allows for more readable and concise code when dealing with multiple conditions.

#### Example 1: Language Check with Match
```python
language = 'Python'

match language:
    case 'Python':
        print('Language is Python')
    case 'Java':
        print('Language is Java')
    case 'JavaScript':
        print('Language is JavaScript')
    case _:
        print('No Match')
```

### Identity and Equality
Python provides two ways to compare objects: `==` for equality and `is` for identity.

#### Example: Comparing Lists
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True (values are equal)
print(a is b)  # Output: False (different objects)
print(id(a))   # Output: Unique id of a
print(id(b))   # Output: Unique id of b
print(id(a) == id(b))  # Output: False (different ids)

a = b
print(a == b)  # Output: True (values are equal)
print(a is b)  # Output: True (same object)
print(id(a))   # Output: Unique id of a
print(id(b))   # Output: Unique id of b
print(id(a) == id(b))  # Output: True (same ids)
```

### False Values in Python
Python considers several values as `False` in a boolean context. These include `False`, `None`, `0`, `0.0`, `''`, `()`, `[]`, and `{}`.

#### Example: Checking False Values
```python
false_values = [False, None, 0, 0.0, '', (), [], {}]

for value in false_values:
    if value:
        print(f'{value} is True')
    else:
        print(f'{value} is False')
```

### Checking for Empty Collections
You can check if a list, dictionary, or tuple is empty using the `not` keyword.

#### Example: Empty Collections
```python
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
```


# Loop through each number in the list `nums`
```python
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)
```

# Loop through each number in the list `nums` again
```python
for num in nums:
    if num == 3:
        print('Skipped!')
        continue
    print(num)
```

# Nested loop: Loop through each number in the list `nums`
```python
for num in nums:
    for letter in 'Umar':
        print(num, letter)
```

# Loop from 0 to n-1
```python
n = 10

for i in range(n):
    print(i * 5)
```

# Loop from 1 to n (inclusive)
```python
for i in range(1, n + 1):
    print(f'{5} X {i} = {5 * i}')
```

# Prompt the user to enter the number of rows and a symbol
```python
userInput = int(input('Enter the number of rows: '))
userInput2 = input('Enter a symbol: ')

for i in range(1, userInput + 1):
    for j in range(i):
        print(userInput2, end='')
    print()
```

# Loop from 0 to n-1
```python
for i in range(n):
    print(userInput2 * i)
```

# Loop while x is less than 10
```python
x = 0

while x < 10:
    print(x)
    x += 1
```


## Function Definitions and Usage

### 1. `hello_func()`
```python
def hello_func():
    """
    A placeholder function that does nothing.
    """
    pass
```
- **Description**: This function is a placeholder and does not perform any operations.

### 2. `greetings()`
```python
def greetings():
    """
    Prints a greeting message 'Good Morning!'.
    """
    print('Good Morning!')
```
- **Description**: This function prints a greeting message "Good Morning!".

### 3. `hi()`
```python
def hi():
    """
    Returns a greeting message 'Hi, Hridoy!'.
    
    Returns:
        str: A greeting message.
    """
    return 'Hi, Hridoy!'
```
- **Description**: This function returns a greeting message "Hi, Hridoy!".
- **Returns**: A string containing the greeting message.

### 4. `cus_greet(name)`
```python
def cus_greet(name):
    """
    Returns a customized greeting message.
    
    Args:
        name (str): The name to include in the greeting.
    
    Returns:
        str: A customized greeting message.
    """
    return f'Good Morning, {name}!'
```
- **Description**: This function returns a customized greeting message.
- **Arguments**:
  - `name` (str): The name to include in the greeting.
- **Returns**: A string containing the customized greeting message.

### 5. `student_info(name, std_id='2102002')`
```python
def student_info(name, std_id='2102002'):
    """
    Returns student information in a formatted string.
    
    Args:
        name (str): The name of the student.
        std_id (str, optional): The student ID. Defaults to '2102002'.
    
    Returns:
        str: Formatted student information.
    """
    return f'{name} , {std_id}'
```
- **Description**: This function returns student information in a formatted string.
- **Arguments**:
  - `name` (str): The name of the student.
  - `std_id` (str, optional): The student ID. Defaults to '2102002'.
- **Returns**: A string containing the formatted student information.

### 6. `bus_info(*args, **kwargs)`
```python
def bus_info(*args, **kwargs):
    """
    Prints positional and keyword arguments.
    
    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    """
    print(args)
    print(kwargs)
```
- **Description**: This function prints the positional and keyword arguments passed to it.
- **Arguments**:
  - `*args`: Variable length argument list.
  - `**kwargs`: Arbitrary keyword arguments.

### 7. `course_info(*args, **kwargs)`
```python
def course_info(*args, **kwargs):
    """
    Prints course information from positional and keyword arguments.
    
    Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    """
    print(args)
    print(kwargs)
```
- **Description**: This function prints course information from the positional and keyword arguments passed to it.
- **Arguments**:
  - `*args`: Variable length argument list.
  - `**kwargs`: Arbitrary keyword arguments.


### Example: Days in a Month
This example demonstrates how to determine the number of days in a given month of a specific year, accounting for leap years.

```python
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2020))  # Output: True
print(is_leap(2027))  # Output: False

print(days_in_month(2027, 2))  # Output: 28
```

print('Imported my_search_module')

test = 'Test String'

```python
'''
This script demonstrates various functionalities in Python, including custom module import, 
standard library usage, and basic operations.

Functions:
- find_index(to_search, target): Finds the index of a target value in a sequence.

Modules:
- search_module: Custom module containing the find_index function and a test variable.
- sys: Provides access to system-specific parameters and functions.
- random: Implements pseudo-random number generators for various distributions.
- math: Provides access to mathematical functions.
- datetime: Supplies classes for manipulating dates and times.
- calendar: Provides functions related to the calendar, such as checking for leap years.
- os: Provides a way of using operating system-dependent functionality.
- antigravity: A fun module that opens a web browser to the XKCD comic about Python.

Usage:
- Finds the index of 'Java' in the courses list using the find_index function.
- Prints the test variable from the search_module.
- Prints all the paths where Python searches for modules.
- Selects a random course from the list and prints it.
- Converts 90 degrees to radians and prints the sine of the angle.
- Prints today's date.
- Checks if the year 2020 is a leap year.
- Prints the current working directory.
- Prints the file location of the os module.
'''
def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1

# import search_module as sm
from modules.search_module import find_index, test
# from search_module import *

import sys

courses = ['Python', 'ML', 'Java', 'OOP', 'C++', 'C']

index = find_index(courses, 'Java')
print(index)
print(test)

# all the path where python search for modules:
print(sys.path)

import random
import math
import datetime
import calendar
import os
import antigravity

courses = ['C', 'C++', 'Java', 'Python', 'Dart']

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))
print(os.getcwd())
print(os.__file__)
```
    
## Python Script Demonstration

This script demonstrates various functionalities in Python, including custom module import, standard library usage, and basic operations.

### Importing Modules

```python
# Import the search_module with an alias 'sm' and specific functions from it
# import search_module as sm
from modules.search_module import find_index, test
# from search_module import *

import sys
```

### List of Courses

```python
# List of courses
courses = ['Python', 'ML', 'Java', 'OOP', 'C++', 'C']
```

### Finding Index

```python
# Find the index of 'Java' in the courses list using the find_index function
index = find_index(courses, 'Java')
print(index)
print(test)
```

### Python Module Search Paths

```python
# Print all the paths where Python searches for modules
print(sys.path)
```

### Additional Imports

```python
import random
import math
import datetime
import calendar
import os
import antigravity
```

### List of Courses (Updated)

```python
# List of courses
courses = ['C', 'C++', 'Java', 'Python', 'Dart']
```

### Random Course Selection

```python
# Select a random course from the list
random_course = random.choice(courses)
print(random_course)
```

### Mathematical Operations

```python
# Convert 90 degrees to radians and calculate the sine of the angle
rads = math.radians(90)
print(rads)
print(math.sin(rads))
```

### Date and Calendar Operations

```python
# Get today's date
today = datetime.date.today()
print(today)

# Check if the year 2020 is a leap year
print(calendar.isleap(2020))
```

### OS Operations

```python
# Print the current working directory
print(os.getcwd())

# Print the file location of the os module
print(os.__file__)
```





## This script demonstrates various functionalities of the `os` module in Python, including:

1. Changing the current working directory using `os.chdir()`.
2. Creating and removing directories using `os.mkdir()`, `os.makedirs()`, `os.rmdir()`, and `os.removedirs()`.
3. Renaming files or directories using `os.rename()`.
4. Retrieving and formatting file modification times using `os.stat()` and `datetime.fromtimestamp()`.

```python
import os
from datetime import datetime

# Change the current working directory
os.chdir('/media/md-sohanur-rahman-hridoy/My Files/Future Prep/Exploring Python/Mastering Python/')

# Create and remove directories
os.mkdir('DemoDir')
os.makedirs('DemoDir/Demo1')
os.rmdir('DemoDir')
os.removedirs('DemoDir/Demo1/')

# Rename files or directories
os.rename('modules', 'my_modules')

# Retrieve and format file modification times
mod_time = os.stat('07_functions.py').st_mtime
print(datetime.fromtimestamp(mod_time))

# List the current working directory and its contents
print(os.getcwd())
print(os.listdir())

# Walk through the directory tree
for dirpath, dirname, filenames in os.walk('/media/md-sohanur-rahman-hridoy/My Files/Future Prep/Exploring Python/Mastering Python/'):
    print('Current Path:', dirpath)
    print('Directories:', dirname)
    print('Files:', filenames)

# Environment variables and file paths
print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

# File and path operations
print(os.path.basename('tmp/text.txt'))
print(os.path.dirname('tmp/text.txt'))
print(os.path.exists('/tmp/text.txt'))
print(os.path.isfile('/tmp/fdkfjdk.txt'))
print(os.path.splitext('/tmp/test.txt'))
print(dir(os.path))
```


## This script demonstrates the LEGB (Local, Enclosing, Global, Built-in) rule in Python, which is the order in which Python resolves variable names.

1. **Local**: Variables defined within a function.
2. **Enclosing**: Variables defined in the local scope of enclosing functions.
3. **Global**: Variables defined at the top level of a module or declared global using the `global` keyword.
4. **Built-in**: Names preassigned in the built-in names module (e.g., `open`, `range`, `SyntaxError`).

### Examples:

- **Global Scope**:
    - `x = 'global x'`: A global variable `x` is defined.

- **Local Scope**:
    - Inside the `test` function, `x` and `y` are local variables.
    - The parameter `z` is also local to the `test` function.

- **Enclosing Scope**:
    - In the `outer` function, `x` is defined in the enclosing scope.
    - The `inner` function has access to `x` from the enclosing `outer` function.

- **Built-in Scope**:
    - The script can access built-in functions like `min` unless overridden locally.

### Functionality:

- The `test` function demonstrates local scope by defining and printing local variables.
- The `outer` function demonstrates enclosing scope by defining a variable and accessing it within an inner function.
- The script prints variables to show the scope resolution order.

### Note:
- Uncomment the `global x` line in the `test` function to see how it affects the global variable `x`.
- Uncomment the `nonlocal x` line in the `inner` function to see how it affects the enclosing variable `x`.

### Code Example:

```python
# import builtins
# print(dir(builtins))

x = 'global x'

def test(z):
    # global x
    x = 'local x'
    y = 'local y'
    # print(y)
    # print(x)
    print(z)
    
test('local z')
# print(y)
# print(x)
# print(z)

# Built-in:
# def min():
#     pass

# m = min([5,3,1,2])
# print(m)

# Enclosing:
def outer():
    x = 'outer x'
    
    def inner():
        # nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()
print(x)
```


## List Slicing in Python

List slicing allows you to access a subset of elements from a list. The syntax for slicing is `list[start:end:step]`, where:
- `start` is the index to begin the slice (inclusive).
- `end` is the index to end the slice (exclusive).
- `step` is the interval between each element in the slice.

Consider the following list:
```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
```

### Examples of List Slicing

1. **Slice from index 3 to 7:**
    ```python
    print(my_list[3:8])  # Output: [3, 4, 5, 6, 7]
    ```

2. **Slice from index -7 to -3:**
    ```python
    print(my_list[-7:-2])  # Output: [3, 4, 5, 6, 7]
    ```

3. **Slice from index 1 to -3:**
    ```python
    print(my_list[1:-2])  # Output: [1, 2, 3, 4, 5, 6, 7]
    ```

4. **Slice from index 1 to the end:**
    ```python
    print(my_list[1:])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

5. **Slice from index 5 to the end:**
    ```python
    print(my_list[5:])  # Output: [5, 6, 7, 8, 9]
    ```

6. **Slice from the beginning to index -1:**
    ```python
    print(my_list[:-1])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]
    ```

7. **Copy the entire list:**
    ```python
    print(my_list[:])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

8. **Slice from index 2 to -2:**
    ```python
    print(my_list[2:-1])  # Output: [2, 3, 4, 5, 6, 7, 8]
    ```

9. **Slice from index 2 to -2 with step 1:**
    ```python
    print(my_list[2:-1:1])  # Output: [2, 3, 4, 5, 6, 7, 8]
    ```

10. **Slice from index 2 to -2 with step 2:**
    ```python
    print(my_list[2:-1:2])  # Output: [2, 4, 6, 8]
    ```

11. **Slice from index -1 to 2 (invalid slice):**
    ```python
    print(my_list[-1:2])  # Output: []
    ```

12. **Slice from index -1 to 2 in reverse:**
    ```python
    print(my_list[-1:2:-1])  # Output: [9, 8, 7, 6, 5, 4, 3]
    ```

13. **Reverse the entire list:**
    ```python
    print(my_list[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    ```

## String Slicing in Python

String slicing works similarly to list slicing. Consider the following URL:
```python
sample_url = 'https://srhridoy.com'
print(sample_url)  # Output: https://srhridoy.com
```

### Examples of String Slicing

1. **Reverse the URL:**
    ```python
    print(sample_url[::-1])  # Output: moc.yodirhrs//:sptth
    ```

2. **Get the top-level domain:**
    ```python
    print(sample_url[-4:])  # Output: .com
    ```

3. **Print the URL without the `https://`:**
    ```python
    print(sample_url[8:])  # Output: srhridoy.com
    ```

4. **Print the URL without the `https://` or the top-level domain:**
    ```python
    print(sample_url[8:-4])  # Output: srhridoy
    ```

# Comprehensions in Python:

Comprehensions provide a concise way to create lists, dictionaries, sets, and generators. They are more readable and often more efficient than traditional loops.

## List Comprehensions

List comprehensions allow you to create lists in a single line of code.

### Examples:

1. **Basic List Comprehension:**
    ```python
    nums = [1, 2, 3, 4, 5]
    squares = [n * n for n in nums]
    print(squares)  # Output: [1, 4, 9, 16, 25]
    ```

2. **Conditional List Comprehension:**
    ```python
    even_nums = [n for n in nums if n % 2 == 0]
    print(even_nums)  # Output: [2, 4]
    ```

3. **Nested List Comprehension:**
    ```python
    pairs = [(x, y) for x in range(3) for y in range(3)]
    print(pairs)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    ```

## Dictionary Comprehensions

Dictionary comprehensions allow you to create dictionaries in a single line of code.

### Examples:

1. **Basic Dictionary Comprehension:**
    ```python
    names = ['Alice', 'Bob', 'Charlie']
    name_lengths = {name: len(name) for name in names}
    print(name_lengths)  # Output: {'Alice': 5, 'Bob': 3, 'Charlie': 7}
    ```

2. **Conditional Dictionary Comprehension:**
    ```python
    long_names = {name: len(name) for name in names if len(name) > 3}
    print(long_names)  # Output: {'Alice': 5, 'Charlie': 7}
    ```

## Set Comprehensions

Set comprehensions allow you to create sets in a single line of code.

### Example:

1. **Basic Set Comprehension:**
    ```python
    nums = [1, 2, 2, 3, 4, 4, 5]
    unique_nums = {n for n in nums}
    print(unique_nums)  # Output: {1, 2, 3, 4, 5}
    ```

## Generator Expressions

Generator expressions allow you to create generators in a single line of code.

### Example:

1. **Basic Generator Expression:**
    ```python
    nums = [1, 2, 3, 4, 5]
    squares_gen = (n * n for n in nums)
    for square in squares_gen:
        print(square)  # Output: 1 4 9 16 25
    ```

Comprehensions are a powerful feature in Python that can make your code more readable and efficient. Use them to simplify your code and improve performance.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List Comprehensions:

# I want 'n' for each 'n' in nums:
my_list = [n for n in nums]
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n*n' for each 'n' in nums:
my_list = [n*n for n in nums]
print(my_list)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Using a map + lambda:
# my_list = map(lambda n: n*n, nums)
# print(list(my_list))  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# I want 'n' for each 'n' in nums if 'n' is even:
my_list = [n for n in nums if n % 2 == 0]
print(my_list)  # Output: [2, 4, 6, 8, 10]

# Using a filter + lambda:
# my_list = filter(lambda n: n % 2 == 0, nums)
# print(list(my_list))  # Output: [2, 4, 6, 8, 10]

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123':
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)  # Output: [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]

# Dictionary Comprehensions:
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# I want a dict{'name':'hero'} for each name, hero in zip(names, heros):
my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)  # Output: {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

# If name not equal to Peter:
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)  # Output: {'Bruce': 'Batman', 'Clark': 'Superman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

# Set Comprehensions:
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = {n for n in nums}
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Generator Expressions:
# I want to yield 'n*n' for each 'n' in nums:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)
for i in my_gen:
    print(i)  # Output: 1 4 9 16 25 36 49 64 81 100

my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)  # Output: 1 4 9 16 25 36 49 64 81 100
```

# This script demonstrates various sorting techniques in Python.

```python
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
```

## Sorting Lists
- A list `li` is created and sorted using both the `sorted()` function and the `sort()` method.
- The `sorted()` function returns a new sorted list, leaving the original list unchanged.
- The `sort()` method sorts the list in place, modifying the original list.
- Both ascending and descending order sorting are demonstrated.

## Sorting Tuples
- A tuple `tup` is created and sorted using the `sorted()` function.
- Note that tuples do not have a `sort()` method, so they must be sorted using `sorted()`.

## Sorting Dictionaries
- A dictionary `dic` is created and sorted by its keys using the `sorted()` function.

## Sorting Lists with Custom Keys
- A list `li1` containing both positive and negative integers is sorted.
- The list is sorted based on absolute values using the `key` parameter in the `sorted()` function.

## Sorting Objects
- A custom `Employee` class is defined with attributes `name`, `age`, and `salary`.
- A list of `Employee` objects is created.
- The list is sorted by the `age` attribute using the `attrgetter` function from the `operator` module.




### Exception Handling in Python

When handling exceptions in Python, it's important to place more specific exceptions before more general ones. This ensures that the specific exception is caught first, and the general exception acts as a fallback.

#### Example Code
```python
try:
    f = open('test.txt')
    # var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Done!')
```

#### Explanation
- **try**: The block of code to be executed.
- **except FileNotFoundError as e**: Catches the `FileNotFoundError` if the file `test.txt` does not exist and prints the error message.
- **except Exception as e**: Catches any other exceptions that are not caught by the previous except block and prints the error message.
- **else**: Executes if the try block does not raise an exception. It reads and prints the file content and then closes the file.
- **finally**: Executes regardless of whether an exception was raised or not. It prints 'Done!'.

This structure ensures that specific exceptions are handled appropriately, and any cleanup code in the `finally` block is always executed.










## Most Asked Questions and Answers

### 1. What are the key features of Python?
- **Readability**: Python's syntax is clear and easy to understand.
- **Versatility**: It supports various programming paradigms.
- **Extensive Libraries**: Python has a rich set of libraries and frameworks.
- **Community Support**: A large and active community contributes to Python's development.

### 2. How is Python interpreted?
Python code is executed line by line by the Python interpreter, making it an interpreted language.

### 3. What is PEP 8?
PEP 8 is the style guide for writing Python code. It provides conventions for writing readable and consistent code. Following PEP 8 helps improve the readability of code and makes it more maintainable. Some key guidelines include:
- Use 4 spaces per indentation level.
- Limit lines to 79 characters.
- Use blank lines to separate functions and classes.
- Use spaces around operators and after commas.
- Use consistent naming conventions for variables, functions, and classes.
- Include docstrings for all public modules, functions, classes, and methods.

### 4. What are Python's built-in data types?
Python has several built-in data types, including:
- **Numeric**: int, float, complex
- **Sequence**: list, tuple, range
- **Text**: str
- **Mapping**: dict
- **Set**: set, frozenset
- **Boolean**: bool

### 5. What is a Python virtual environment?
A virtual environment is an isolated environment for Python projects, allowing dependencies to be managed separately for each project.

### 6. How do you handle exceptions in Python?
Exceptions in Python are handled using try-except blocks:
```python
try:
    # code that may raise an exception
except SomeException as e:
    # code to handle the exception
```

### 7. What is a lambda function?
A lambda function is an anonymous function defined using the `lambda` keyword. It can have any number of arguments but only one expression.
```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

### 8. What is the difference between `append()` and `extend()` in lists?
- `append()`: Adds a single element to the end of the list.
- `extend()`: Adds all elements of an iterable to the end of the list.

### 9. How do you install packages in Python?
Packages in Python are installed using the `pip` package manager:
```sh
pip install package_name
```

### 10. What is the use of the `with` statement in Python?
The `with` statement is used for resource management and exception handling. It ensures that resources are properly released after use.
```python
with open('file.txt', 'r') as file:
    content = file.read()
```

### 11. What is list comprehension?
List comprehension provides a concise way to create lists. It consists of brackets containing an expression followed by a for clause.
```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 12. What is the difference between `==` and `is` in Python?
- `==` checks for value equality.
- `is` checks for reference equality (whether both variables point to the same object).

### 13. How do you create a class in Python?
A class in Python is created using the `class` keyword.
```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(self.value)

obj = MyClass(10)
obj.display()  # Output: 10
```

### 14. What is the purpose of `self` in a class?
`self` represents the instance of the class. It is used to access variables and methods associated with the current object.

### 15. How do you read and write files in Python?
Files are read and written using the `open()` function.
```python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  # Output: Hello, World!
```

### 16. What is the Global Interpreter Lock (GIL) in Python?
The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This means that even in a multi-threaded Python program, only one thread can execute Python code at a time. The GIL can be a bottleneck in CPU-bound and multi-threaded code.

### 17. How do you manage memory in Python?
Python uses automatic memory management, which includes garbage collection to free up memory that is no longer in use. The garbage collector uses reference counting and a cyclic garbage collector to detect and clean up cyclic references.

### 18. What is a decorator in Python?
A decorator is a function that takes another function and extends its behavior without explicitly modifying it. Decorators are often used for logging, access control, memoization, and more.
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

### 19. What are metaclasses in Python?
Metaclasses are classes of classes that define how a class behaves. A class is an instance of a metaclass. Metaclasses allow you to modify class creation, such as adding methods or attributes dynamically.
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['greet'] = lambda self: f"Hello from {self.__class__.__name__}"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.greet())  # Output: Hello from MyClass
```

### 20. What is the difference between `deepcopy` and `copy` in Python?
The `copy` module provides two methods for copying objects:
- `copy.copy()`: Creates a shallow copy of an object. It constructs a new compound object and then inserts references into it to the objects found in the original.
- `copy.deepcopy()`: Creates a deep copy of an object. It constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
```python
import copy

original = [1, [2, 3], 4]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

original[1][0] = 'changed'
print(shallow_copy)  # Output: [1, ['changed', 3], 4]
print(deep_copy)     # Output: [1, [2, 3], 4]
```

## Additional Tricky and Critical Python Interview Questions

### 21. What is the difference between `__init__` and `__new__`?
- `__init__`: Initializes a new instance of a class.
- `__new__`: Creates a new instance of a class.

### 22. How does Python's garbage collection work?
- Uses reference counting and a cyclic garbage collector to manage memory.

### 23. Explain the concept of monkey patching in Python.
- Dynamically modifying or extending a module or class at runtime.

### 24. What is the difference between `staticmethod` and `classmethod`?
- `staticmethod`: Does not access or modify class state.
- `classmethod`: Can modify class state and takes `cls` as the first parameter.

### 25. How do you implement a singleton pattern in Python?
```python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
```

### 26. What are Python's magic methods?
- Special methods with double underscores, like `__init__`, `__str__`, etc.

### 27. How do you use the `itertools` module?
- Provides functions for creating iterators for efficient looping.

### 28. What is the purpose of the `yield` keyword?
- Used to create a generator, which returns an iterator.

### 29. How do you create a generator in Python?
```python
def generator():
    yield 1
    yield 2
    yield 3
```

### 30. Explain the difference between `map()`, `filter()`, and `reduce()`.
- `map()`: Applies a function to all items in an iterable.
- `filter()`: Filters items in an iterable based on a function.
- `reduce()`: Applies a function cumulatively to items in an iterable.

### 31. What is the purpose of the `__call__` method?
- Allows an instance of a class to be called as a function.

### 32. How do you handle circular imports in Python?
- Use import statements within functions or use `importlib`.

### 33. What is the difference between `__str__` and `__repr__`?
- `__str__`: Returns a readable string representation.
- `__repr__`: Returns an unambiguous string representation.

### 34. How do you use the `functools` module?
- Provides higher-order functions like `reduce`, `partial`, and `lru_cache`.

### 35. What is the purpose of the `__slots__` attribute?
- Limits the attributes that an instance can have, saving memory.

### 36. How do you create a context manager in Python?
- Use the `with` statement or define `__enter__` and `__exit__` methods.

### 37. Explain the difference between `deepcopy` and `copy`.
- `copy()`: Shallow copy.
- `deepcopy()`: Deep copy.

### 38. What is the purpose of the `__name__` variable?
- Indicates if a module is run as a script or imported.

### 39. How do you use the `collections` module?
- Provides specialized container datatypes like `deque`, `Counter`, `OrderedDict`.

### 40. What is the difference between `__getattr__` and `__getattribute__`?
- `__getattr__`: Called when an attribute is not found.
- `__getattribute__`: Called for every attribute access.

### 41. How do you use the `abc` module?
- Provides tools for defining abstract base classes.

### 42. What is the purpose of the `__del__` method?
- Called when an object is about to be destroyed.

### 43. How do you use the `enum` module?
- Defines enumerations, which are a set of symbolic names bound to unique values.

### 44. What is the difference between `__eq__` and `__hash__`?
- `__eq__`: Defines equality comparison.
- `__hash__`: Defines hash value for an object.

### 45. How do you use the `dataclasses` module?
- Provides a decorator and functions for creating data classes.

### 46. What is the purpose of the `__mro__` attribute?
- Shows the method resolution order for a class.

### 47. How do you use the `contextlib` module?
- Provides utilities for working with context managers.

### 48. What is the difference between `__enter__` and `__exit__`?
- `__enter__`: Called at the start of a `with` block.
- `__exit__`: Called at the end of a `with` block.

### 49. How do you use the `pathlib` module?
- Provides an object-oriented interface for filesystem paths.

### 50. What is the purpose of the `__annotations__` attribute?
- Stores type hints for function arguments and return values.

### 51. How do you use the `typing` module?
- Provides support for type hints.

### 52. What is the difference between `__dict__` and `vars()`?
- Both return the attribute dictionary of an object.

### 53. How do you use the `logging` module?
- Provides a flexible framework for emitting log messages.

### 54. What is the purpose of the `__doc__` attribute?
- Stores the docstring of a module, class, method, or function.

### 55. How do you use the `argparse` module?
- Parses command-line arguments.

### 56. What is the difference between `__file__` and `__path__`?
- `__file__`: Path to the module file.
- `__path__`: Used in package modules to specify the package search path.

### 57. How do you use the `subprocess` module?
- Allows spawning new processes, connecting to their input/output/error pipes.

### 58. What is the purpose of the `__future__` module?
- Enables new language features that are not compatible with the current interpreter.

### 59. How do you use the `multiprocessing` module?
- Supports spawning processes using an API similar to the threading module.

### 60. What is the difference between `__import__` and `importlib`?
- `__import__`: Built-in function for importing modules.
- `importlib`: Provides a more flexible way to import modules.

### 61. How do you use the `threading` module?
- Provides higher-level threading interfaces.

### 62. What is the purpose of the `__all__` attribute?
- Defines the public interface of a module.

### 63. How do you use the `weakref` module?
- Provides tools for creating weak references to objects.

### 64. What is the difference between `__slots__` and `__dict__`?
- `__slots__`: Limits attributes and saves memory.
- `__dict__`: Stores all attributes of an object.

### 65. How do you use the `pickle` module?
- Serializes and deserializes Python objects.

### 66. What is the purpose of the `__module__` attribute?
- Indicates the module in which a class was defined.

### 67. How do you use the `json` module?
- Parses JSON strings and converts Python objects to JSON.

### 68. What is the difference between `__class__` and `type()`?
- Both return the class of an object.

### 69. How do you use the `xml` module?
- Provides tools for parsing and creating XML documents.

### 70. What is the purpose of the `__bases__` attribute?
- Contains a tuple of base classes of a class.

### 71. How do you use the `csv` module?
- Reads and writes CSV files.

### 72. What is the difference between `__subclasses__` and `__mro__`?
- `__subclasses__`: Returns a list of immediate subclasses.
- `__mro__`: Shows the method resolution order.

### 73. How do you use the `sqlite3` module?
- Provides a DB-API 2.0 interface for SQLite databases.

### 74. What is the purpose of the `__weakref__` attribute?
- Holds weak references to an object.

### 75. How do you use the `configparser` module?
- Parses configuration files.

### 76. What is the difference between `__new__` and `__init__`?
- `__new__`: Creates a new instance.
- `__init__`: Initializes the instance.

### 77. How do you use the `shutil` module?
- Provides high-level file operations.

### 78. What is the purpose of the `__reduce__` method?
- Supports pickling of objects.

### 79. How do you use the `tempfile` module?
- Creates temporary files and directories.

### 80. What is the difference between `__reduce__` and `__reduce_ex__`?
- Both support pickling, but `__reduce_ex__` provides protocol-specific behavior.

### 81. How do you use the `unittest` module?
- Provides a framework for writing and running tests.

### 82. What is the purpose of the `__setattr__` method?
- Controls setting attribute values.

### 83. How do you use the `doctest` module?
- Tests interactive Python examples in docstrings.

### 84. What is the difference between `__getattr__` and `__getattribute__`?
- `__getattr__`: Called when an attribute is not found.
- `__getattribute__`: Called for every attribute access.

### 85. How do you use the `traceback` module?
- Provides utilities for extracting, formatting, and printing stack traces.

### 86. What is the difference between `__getitem__` and `__setitem__`?
- `__getitem__`: Gets an item.
- `__setitem__`: Sets an item.

### 87. How do you use the `heapq` module?
- Implements a heap queue algorithm.

### 88. What is the purpose of the `__iter__` method?
- Returns an iterator object.

### 89. How do you use the `bisect` module?
- Provides functions for manipulating sorted lists.

### 90. What is the difference between `__contains__` and `__missing__`?
- `__contains__`: Checks if an item is in a container.
- `__missing__`: Called by `dict` when a key is not found.

### 91. How do you use the `timeit` module?
- Measures execution time of small code snippets.

### 92. What is the purpose of the `__len__` method?
- Returns the length of an object.

### 93. How do you use the `sched` module?
- Implements a general-purpose event scheduler.

### 94. What is the difference between `__call__` and `__new__`?
- `__call__`: Makes an instance callable.
- `__new__`: Creates a new instance.

### 95. How do you use the `pdb` module?
- Provides an interactive debugger.

### 96. What is the purpose of the `__format__` method?
- Customizes string formatting.

### 97. How do you use the `trace` module?
- Tracks program execution and generates annotated statement coverage listings.

### 98. What is the difference between `__enter__` and `__exit__`?
- `__enter__`: Called at the start of a `with` block.
- `__exit__`: Called at the end of a `with` block.

### 99. How do you use the `profile` module?
- Provides a framework for profiling Python programs.

### 100. What is the purpose of the `__dir__` method?
- Customizes the list of attributes returned by `dir()`.