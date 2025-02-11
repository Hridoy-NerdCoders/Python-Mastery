message = "Hello World"
escape = 'Hridoy\'s World'
using_single_to_handle_double = 'I am going to be a "..."'
using_double_to_handle_single = "I am going to be a '...'"
muliple_line = """
This is great to learn python 
from "Corey Shefer's" lessons and just awsome
"""
print(message)
print(escape)
print(using_single_to_handle_double)
print(using_double_to_handle_single)
print(muliple_line)
print(len(message))
print(message[0])
print(message[-1])
print(message[10])
# print(message[11])

print(message[0:5])#start is inclusive and the end is exclusive
print(message[:5])
print(message[6:])
print(message.lower())
print(message)
print(message.upper())
print(message.count('l'))
print(message.find('l'))
print(message.count("ll"))
print(message.find('Universe'))

print(message.replace('World','Bangladesh'))
print(message)
message = message.replace('World','Bangladesh')
print(message)


greeting = 'Bye bye'
name = 'Muhammad Ali'
message = greeting + ', ' + name + '.See you!'
print(message)

message = '{}, {}.See you!'.format(greeting,name.upper())
print(message)

message = f'{greeting}, {name.upper()}.See you!'
print(message)

print(dir(message))
print(help(str))
print(help(str.lower))





