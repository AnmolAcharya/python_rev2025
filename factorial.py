# def factorial(n):

#     if n == 0 or n == 1:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(5))
# print(factorial(8))

def factorial(n):

    result = 1

    for i in range(2, n+1):
        result *= i

    return result

print(factorial(5))
