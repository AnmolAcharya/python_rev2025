def squareNum(num):

    start, end = 1, num

    if num < 2:
        return True

    while start <= end:
        mid = start + (end - start)//2

        if num == mid*mid:
            return True
        elif num < mid*mid:
            end = mid - 1
        else:
            start = mid + 1

    return False

num = 18

print(squareNum(num))



#     i = 1
#     while i*i <= num:
#         if i*i == num:
#             return True
#         i += 1

#     return False

# num = 4
# print(squareNum(num))

