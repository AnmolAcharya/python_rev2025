# def findFactorial(num):

#     if num == 0 or num == 1:
#         return 1
    
#     return num * findFactorial(num-1)
    
# num = 5
# print(findFactorial(num))\

##################################################33333

def findFibonnaciNum(num):

    if num == 0:
        return 0
    
    if num == 1:
        return 1
    
    return findFibonnaciNum(num -1) + findFibonnaciNum(num - 2)

    
num = 6
print(findFibonnaciNum(num))

