def countVowels(words):

    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']

    for word in words:
        if word.lower() in vowel:
            count += 1
        
    return count


print(countVowels("BANANANA"))



