# def dictStuff(nums):

#     hash_map = {}

#     for n in nums: 
#         if n in hash_map:
#             hash_map[n] += 1
#         else:
#             hash_map[n] = 1

#     return hash_map


# nums = [1, 2, 2, 3, 3, 3, 4]
# print(dictStuff(nums))

###################################################################

# def count_chars(stringer):

#     # list_count = list(stringer)
#     dict_count = {}

#     for char in stringer:
#         if char in dict_count:
#             dict_count[char] += 1
#         else:
#             dict_count[char] = 1 

#     return dict_count


# stringer = "interview"
# print(count_chars(stringer))

################################################################

# def find_duplicates(nums):

#     hash_map = {}

#     for n in nums:
#         if n in hash_map:
#             hash_map[n] += 1
#         else:
#             hash_map[n] = 1

#     # res = list()

#     return [x for x in hash_map if hash_map[x] > 1]

#     # res = list(hash_map.values())

#     # dup_res = []

#     # for r in res:
#     #     if res[r] > 1:
#     #         dup_res.append(res[r])
#     #     else:

# nums = [1, 2, 3, 4, 2, 3, 5, 6, 3]
# print(find_duplicates(nums))

###########################################################

def product_except_self(nums):

    res = []

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        res.append(product)

    return res

nums = [1,2,3,4]
print(product_except_self(nums))

########################################################