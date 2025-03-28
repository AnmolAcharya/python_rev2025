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

# # nums = 5
# # for i in range(nums, 0, -1):

# #     print(i, end = " ")
# #     i += 1

# def printrevOrder(nums):

#     if nums == 0:
#         return 
    
#     # for i in range(nums, 0, -1): <<<<<<<<<<<<<<<<<<<<<<<<<<<- We don't need loop if we are using recursion 
#     #     printrevOrder(nums -1)
#     #     print(nums, end=" ")
#     #     i += 1

#     print(nums, end=" ")
#     printrevOrder(nums - 1)
    

# nums = 5
# printrevOrder(nums)

#############################################################################

#Count the total number of vowel occurences in a string :


# def countVowel(str):

#     count = 0

#     for char in str:
#         if char in {'a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
#             count += 1

#     return count 

# str = "AppleUmbrella"
# print(countVowel(str))


#####################################################################################################

# def greet_all(*args,**kwargs):
#     for name in args:
#         print(f"Hello {name}, role: {kwargs}")

# greet_all("Anmol", "Sam", "Lucas", role1 ="CEO", role2="worker", role="STUDENT")

#################################################################################################

def hashRev(nums):

    hash_map = {}

    for i in range(len(nums)):
        if nums[i] in hash_map:
            hash_map[nums[i]] += 1
        else:
            hash_map[nums[i]] = 1

    max_freq_val =  max(hash_map.values())s

    for key,value in hash_map.items():
        if value == max_freq_val:
            res = key

    return res 


nums = [1,2,3,1,2,3,4,5,32,3,1,1,1,1,1,1,1,1]
print(hashRev(nums))

#$$$