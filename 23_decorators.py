

    
#Decorator ফাংশানকে মডিফাই করে। 
def greet(fx):
    def mfx(*a,**k):
        print('Good Morning')
        fx(*a,**k)
        print('Thanks for using this function')
    return mfx

@greet  
def hello():
    print('Hello World')
# @greet   
def add(a, b):
    print(a + b)
    
hello()
# greet(hello())()
add(3,4)
greet(add)(1,2)


