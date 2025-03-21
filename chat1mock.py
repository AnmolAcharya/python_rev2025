def checkDuplicates(nums):

    return len(nums) != len(set(nums))


nums = [1,2,3,4]
nums1 = [1,2,3,1]

print(checkDuplicates(nums))
print(checkDuplicates(nums1))
