#List ---> Can be changed -> Mutable
courses = ['Algorithm','Python','Java','DS','C++']
print(courses)
print(len(courses))
print(courses[0])
print(courses[4])
#always be the last item: at index -1
print(courses[-1])
print(courses[-4])

#1 is inclusive but 5 is exclusive
print(courses[1:5])

print(courses[:5])
print(courses[0:5])

print(courses[1:5])
print(courses[1:])

courses.append('Django')
print(courses)

courses.insert(0,'Fundamentals')
print(courses)

courses_2 = ['Dart','Flutter']
#after inserting we get list of list:
courses.insert(0,courses_2)
print(courses)
print(courses[0])

courses.pop(0)
print(courses)

#do the same:
courses.append(courses_2)
print(courses)

courses.pop()
print(courses)



#after extending we get one list with all the items:
courses.extend(courses_2)
print(courses)

courses.remove('Fundamentals')
print(courses)

popped = courses.pop()
print(popped)
print(courses)

courses.reverse()
print(courses)

#sorting:
courses.sort()
print(courses)

nums = [1,3,4,2,1,88,12,9]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

#doesn't alter the original
sorted_nums_ascen= sorted(nums)
print(sorted_nums_ascen)
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('Java'))
print('Art' in courses)
print('C++' in courses)

for course in courses:
    print(course)

for index,course in enumerate(courses,start=1):
    print(index,course)
    
courses_str = ', '.join(courses)
print(courses_str)

courses_str = ' $ '.join(courses)
print(courses_str)

new_list_of_courses = courses_str.split(' $ ')
print(courses_str)
print(new_list_of_courses)

#List's mutability:
list_1 = ['Tanha','Tasin','Nova','Rupa','Hridoy']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Unknown!'
print(list_1)
print(list_2)

# Tuples: Can't modify-->immutable 
#if we don't change then use tuples:

tuple_1 = ('Tanha','Tasin','Nova','Rupa','Hridoy')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Unknown!'
# print(tuple_1)
# print(tuple_2)

#can't use too much method as list as many method are involved in mutating the values we can't append,remove here...But other the same...


#Sets : Remove duplicates and doesn't care about the order
cs_courses = {'Discrete Mathematics','Fundamentals of Computer','Software Engineering','Computer Networks','Discrete Mathematics','Fundamentals of Computer','Software Engineering','Computer Networks'}
print(cs_courses)

#Membership test: optimize than list and tuple
print('Computer Networks' in cs_courses)

ece_courses = {'Digital Communication','Fundamentals of Computer','Software Engineering','Computer Networks','Digital Electronics','Software Engineering','Computer Networks'}

print(ece_courses)

print(cs_courses.intersection(ece_courses))
print(cs_courses.difference(ece_courses))
print(cs_courses.union(ece_courses))



#Empty lists:
empty_lists = []
empty_lists = list()

#Empty Tuples:
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets:
empty_set = {}# This isn't right! It's a dictionary
print(type(empty_set))
empty_set = set()


