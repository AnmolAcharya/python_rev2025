def dictStuff(nums):

    hash_map = {}

    for n in nums: 
        if n in hash_map:
            hash_map[n] += 1
        else:
            hash_map[n] = 1

    return hash_map


nums = [1, 2, 2, 3, 3, 3, 4]
print(dictStuff(nums))