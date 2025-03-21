def findFactorial(num):

    if num == 0 or num == 1:
        return 1
    
    return num * findFactorial(num-1)
    
num = 5
print(findFactorial(num))