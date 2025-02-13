my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9, 8, 7, 6, 5, 4, 3, 2, 1

# list[start:end:step]
#start->inclusive, end -> exclusive

print(my_list[3:8])
print(my_list[-7:-2])
print(my_list[1:-2])
print(my_list[1:])
print(my_list[5:])
print(my_list[:-1])
print(my_list[:])#copy of the list

print(my_list[2:-1])
print(my_list[2:-1:1])
print(my_list[2:-1:2])
print(my_list[-1:2])
print(my_list[-1:2:-1])
print(my_list[::-1])

#String slicing:
sample_url = 'https://srhridoy.com'
print(sample_url)

#Reverse the url:
print(sample_url[::-1]) 

#Get the top level domain:
print(sample_url[-4:])

#print the url without the https://
print(sample_url[8:])

#print the url without the https:// or hte top level domain
print(sample_url[8:-4])