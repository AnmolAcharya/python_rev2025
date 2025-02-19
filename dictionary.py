# def dictionary(dict):

#     # dict = {"red":3,
#     #         "bluw": 4,
#     #         "green": 5,
#     #         "purple":6}
    

#     # return dict.keys()
#     # return list(dict.keys())[0] 


#     # we coulkd use iter as well for this --->
#     return next(iter(dict))

# print(dictionary({"red":3,
#                   "blue":4,
#                   "green":5
#                   }))

####################################################################################################################
# # from itertools import islice
# from itertools import islice


# def dictionary(dic):
#     dic = {"gasvd": 2}

#################Get the second element

# def dictionary(d):

#     # iterator = iter(d)

#     # next(iterator)
#     # return next(iterator)

#     secondKey = iter(d)
#     next(secondKey)
#     next(secondKey)

#     return next(secondKey)


# print(dictionary({"red":4,
#                   "blue":5,
#                   "green":6}))


########################################################

# def dictionary(dics):

#     #return list(dics.keys())[2] #starightforward way--->


#     iterators = iter(dics)
#     next(iterators)
#     next(iterators)
#     return next(iterators)

# print(dictionary({"red":5,
#                   "blue":8,
#                   "yellow":9,
#                   "green":10
#                   }))

####################################################################
###########################IMPORTANT$###############################

# Skillsets = {"React": 1,
#              "Node": 2,
#              "Firebase": 3,
#              "MongoDB": 4,
#              "Express": 5,
#             }

# Skillsets['Next.js'] = 6
# Skillsets['Nest.js'] = 7
# Skillsets['Supabase'] = 8 #add to the dictionary

# print(Skillsets)

# del Skillsets['Supabase'] #delete from the hashmap/dictionary
# Skillsets['Node'] = 3     #we can change the value and it won't matter much!!!!

# print(Skillsets)

# print(Skillsets.values()) #get the values list  --> all together though
 

# print(len(Skillsets))

#####################################################################

def dictionary(dics):

    return dics.values()


print(dictionary({"red":1,
                  "blue":2}))

