import random
import math
import datetime
import calendar
import os
import antigravity

courses = ['C','C++','Java','Python','Dart']

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
