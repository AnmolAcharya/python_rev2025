# def rev(words):

#     vowel_counter = 0
#     vowels = ["a", "e", "i", "o", "u"]
#     # vowels = "aeiou"

#     for char in words.lower():
#         if char in vowels:
#             vowel_counter += 1

#     return vowel_counter


# words = "Apple"
# print(rev(words))


##################################reverse an Integer##########################################################################333

# def reverse_number(n: int) -> int:

#     if n < 0: 
#         return -int(str(n)[1:][::-1])
    
#     return int(str(n)[::-1])



# print(reverse_number(-567))

##############################################Count Digits of a Number ############################################################

def count_digits(n: int) -> int:

    return len((str(abs(n))))

#     if n < 0: 
#         convert_neg_int = str(n)[1:]
#         count = len(convert_neg_int)  #<<<<<<<<<<<<<<<<<<<<<<<<<<< THIS IS THE WAY TO DO IT WITHOUT USING ABS()
#         return count
    
#     convert_dig = str(n)
#     return len(convert_dig)

print(count_digits(-567899))

