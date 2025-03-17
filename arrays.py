# a = list((1,2,3, 'apple', 4.9))

# print(a) <<<----creating an array

# def reverese_array(arr): <<< -- find if a number exists in an array

#     reversed_array = arr[::-1]
#     return reversed_array

# arr = [1,2,3,4,5,6]

# print(reverese_array(arr))


##################################################################

# def find_number(arr, n): #<<<- finding out if a number exists in an array with linear search or simple iterations 

#     for i in range (1, len(arr)):
#         if arr[i] == n: 
#             return True
        
#     return False



# arr = [1,2,3,4,5,6]
# n = 9

# print(find_number(arr,n))


##################################################################

# def sort_array(arr):

#     # sorted_array = arr.sort() # return none as it doesn't return anything but just sorts the stuffs 

#     sorted_array = sorted

# arr = [1,2,3,4,5,6]

# print(sort_array(arr))

###########################################

# def find_first_char(strs):

#     hash_map = {}

#     for char in strs:
#         if char in hash_map:
#             hash_map[char] += 1
#         else:
#             hash_map[char] = 1

#     for index, char in enumerate(strs):
#         if hash_map[char] == 1:
#             return index
        
#     return -1 


# strs = "eetcode"
# print(find_first_char(strs))

##########################################


def find_first_char(strs):

    hash_map = {}

    for char in strs:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1

    return max(hash_map.values())


strs = "eetcode"
print(find_first_char(strs))