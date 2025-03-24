def isPrime(num):

    if num <=1:
        return False

    for i in range(2, num):
        if num % i == 1:
            return True
        else:
            return False

num = 3

print(isPrime(num))