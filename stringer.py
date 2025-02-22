# def stringer(word):

#     print(word[4])
    
#     # return word.split(' ')
#     return word.replace('Nepal', 'Argentina')

# word = "Vamos Nepal"

# print(stringer(word))

# num = 9

# str_num = str(num)
# print(str_num)

def stringer():
    
    names = ["AI", "ML", "NN", "HCI"]
    return [name for name in names if len(name) == 3]

print(stringer())


