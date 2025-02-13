'''
LEGB
Local , Enclosing, Global, Built-in
'''

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

#Built - in:
# def min():
#     pass

# m = min([5,3,1,2])
# print(m)

#Enclosing:
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

