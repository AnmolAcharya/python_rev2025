def checkDuplicates(nums):

    hash_map = {}

    for num in nums:
        if num in hash_map:
            return True
        else:
            hash_map[num] =1

    return False

    
    # for value in hash_map.values():
    #     return value

    # return [True for value in hash_map.values() if value > 1]


nums = [1,2,3,4]
nums1 = [1,2,3,1]

print(checkDuplicates(nums))
print(checkDuplicates(nums1))
#     hash_map = {}

#     for num in nums:
#         if num in hash_map:
#             hash_map[num] += 1
#         else:
#             hash_map[num] =1

    
#     # for value in hash_map.values():
#     #     return value

#     return [True for value in hash_map.values() if value > 1]


# nums = [1,2,3,4]
# nums1 = [1,2,3,1]

# print(checkDuplicates(nums))
# print(checkDuplicates(nums1))


# def checkDuplicates(nums):

#     return len(nums) != len(set(nums))


# nums = [1,2,3,4]
# nums1 = [1,2,3,1]

# print(checkDuplicates(nums))
# print(checkDuplicates(nums1))
