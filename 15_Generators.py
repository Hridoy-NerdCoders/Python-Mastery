# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result

# my_nums = square_numbers([1,2,3,4,5])

# print(my_nums)# [1, 4, 9, 16, 25]

#Generators:
def square_numbers(nums):
    for i in nums:
        yield (i*i)


my_nums = square_numbers([1,2,3,4,5])

#Generators doesn't hold the entire result in the memory it yields one result at a time.
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

for  num in my_nums:
    print(num)
    
#List Comprehensions:
my_nums = (x*x for x in [1,2,3,4,5])
# for  num in my_nums:
#     print(num)
    
print( list (my_nums))
#Generator have much performance as itn't hold all memory.But when we cast to list then the performance is lost...


