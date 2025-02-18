def find_palindrome(word):
    
     rev_word = word[::-1]
     return rev_word == word #Boolean expression (checks the values...)

    # if rev_word == word: #to print with the output 
    #     print("It's a plaindrome")
    # else:
    #     print("It's not a plaindrome")
    
print(find_palindrome("CACTUS"))