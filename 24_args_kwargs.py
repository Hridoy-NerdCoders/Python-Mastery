def summation(*numbers):
    sum = 0
    for num in numbers:
        sum += num
        
    return sum

print(summation(1,2,3,4,5,6,7,8,9))
print(summation(1,2,3,4,5))

def personal_info(**infos):
    return f"{infos['fname']} {infos['lname']} is a {infos['occupation']}"

print(personal_info(fname = 'Sohanur',occupation = 'Software Engineer',lname = 'Rahman'))