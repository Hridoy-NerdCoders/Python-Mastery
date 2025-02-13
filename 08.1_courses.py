# import search_module as sm
from modules.search_module import find_index,test
#from search_module import*

import sys


courses = ['Python','ML','Java','OOP','C++','C']

index = find_index(courses,'Java')
print(index)
print(test)

#all the path where python search for modules:
print(sys.path)

