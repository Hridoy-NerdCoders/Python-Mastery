def factorial(i:int)->int:
    if i < 0:
        return None
    if i == 0:
        return 1
    return i * factorial(i-1)

print(factorial(5.01))

#run using mypy then filename.py...
#Python ignore the hint....