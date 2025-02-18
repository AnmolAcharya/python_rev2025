# def secondLargest(num):

#     num = list(set(num))
#     num.sort()

#     return num[-2] if len(num) > 1 else None


# print(secondLargest([6,1,4,9]))

def thirdLargest(num):

    unique_num = list(set(num))
    # unique_num.sort() ?? never assign new values to sort() method as it returns none 
    sorted_unique_num = sorted(unique_num)

    return num[-3] if len(sorted_unique_num) > 1 else None

print(thirdLargest([77,55,43,22,23]))


# # def secondLargest(*num):

# #     sorted_num = num.sort()

# #     secondLargestNum = sorted_num[::-2]

# #     return secondLargestNum

# # print(secondLargest([1,5,2,8]))


# nums = [6,8,6,4,3,2,44,5]

# sorted_num = nums.sort()

# secondlargest = sorted_num[-1]

# print(secondlargest)






