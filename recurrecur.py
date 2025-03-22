# def findFactorial(num):

#     if num == 0 or num == 1:
#         return 1
    
#     return num * findFactorial(num-1)
    
# num = 5
# print(findFactorial(num))\

##################################################33333

# def findFibonnaciNum(num):

#     if num == 0:
#         return 0
    
#     if num == 1:
#         return 1
    
#     return findFibonnaciNum(num -1) + findFibonnaciNum(num - 2)

    
# num = 4
# print(findFibonnaciNum(num))

############Sum of digits recursively:

# def sumDigits(num):

#     if num == 0:
#         return 0
    
#     return (num%10) + sumDigits(num // 10) #get the last digit from num%10 and remove last digit by //10

# num = 123455

# print(sumDigits(num))

###############################################################################

####Reverse a string recursively :

# def revStringRecur(str):

#     if len(str) <= 1:
#         return str
    

#     return revStringRecur(str[1:]) + str[0]

# str = "abcde"
# print(revStringRecur(str))

################################################################################

# def printtillOne(num):

#     if num == 0:
#         return 
    
#     printtillOne(num -1)
#     print(num, end=" ") 

# num = 5
# (printtillOne(num))

# def printTillOne(num):

#     for i in range(1, num+1):
#     # i = 1
#     # while i < (num+1):
#         print(i, end = " ")
#         i+= 1

# num = 5
# (printTillOne(num))

############################################rev in decr########################

# nums = 5
# for i in range(nums, 0, -1):

#     print(i, end = " ")
#     i += 1

def printrevOrder(nums):

    if nums == 0:
        return 
    
    # for i in range(nums, 0, -1): <<<<<<<<<<<<<<<<<<<<<<<<<<<- We don't need loop if we are using recursion 
    #     printrevOrder(nums -1)
    #     print(nums, end=" ")
    #     i += 1

    print(nums, end=" ")
    printrevOrder(nums - 1)
    

nums = 5
printrevOrder(nums)


