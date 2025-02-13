#We have to put more specific exception on top otherwise that more general exception will hit first...
try:
    f = open('test.txt')
    #var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Done!')