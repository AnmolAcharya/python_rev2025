
num_list = [4, 2, 2, 8, 3, 3, 3, 4, 4]

dict_stuff = {}


for num in num_list:
    if num in dict_stuff:
        dict_stuff[num] += 1
    else:
        dict_stuff[num] = 1

freq = tuple(dict_stuff.values())

# return [num for num in num_list if num % 2 == 0]

print(freq)
# print(lister)



