def sortArraybyParity(nums):

    odd_array = []
    even_array = []

    n = len(nums)

    for i in range(n):
        if nums[i] % 2 == 1:
            odd_array.append(nums[i])
        else:
            even_array.append(nums[i])

    final_array = odd_array + even_array

    return final_array


nums = [2,4,3,1]

print(sortArraybyParity(nums))
