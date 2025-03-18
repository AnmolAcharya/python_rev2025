# def sortArraybyParity(nums):

#     odd_array = []
#     even_array = []

#     n = len(nums)

#     for i in range(n):
#         if nums[i] % 2 == 1:
#             odd_array.append(nums[i])
#         else:
#             even_array.append(nums[i])

#     final_array = odd_array + even_array

#     return final_array


# nums = [2,4,3,1]

# print(sortArraybyParity(nums))

#########################################
def transformArray(nums):

        n = len(nums)

        res_array = []

        for i in range(n):
            if nums[i] % 2 == 1:
                nums[i] = 1
                res_array.append(nums[i])
            elif nums[i] % 2 == 0:
                nums[i] = 0
                res_array.append(nums[i])
            else:
                if nums[i] == 0:
                    res_array.append(nums[i])

        sorted_res_array = sorted(res_array)
        return sorted_res_array
