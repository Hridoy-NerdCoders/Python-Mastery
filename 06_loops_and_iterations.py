nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)
    

for num in nums:
    if num == 3:
        print('Skipped!')
        continue
    print(num)
        
        


for num in nums:
    for letter in 'Umar':
        print(num,letter)
        

n = 10     
for i in range(n):
    print(i*5)
    
for i in range(1,n+1):
    print(f'{5} X {i} = {5*i}')
    

userInput = int(input('Enter the number of rows: '))
userInput2 = input('Enter a symbol: ')

for i in range(1, userInput + 1):
    for j in range(i):
        print(userInput2, end='')
    print()

for i in range(n):
    print(userInput2*i)
    
x = 0
while x < 10:
    print(x)
    x+=1