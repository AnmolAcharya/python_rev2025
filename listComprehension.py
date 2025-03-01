# def listComprehension():

#     even_nums = [x for x in range(10) if x % 2 == 0]
#     print(even_nums)

# listComprehension()


# def listComprehension():

#     names = ["AA","AB","AC"]

#     index_names = [name for index, name in enumerate(names) if index % 2 == 0]
#     print(index_names)

# listComprehension()


def listComprehension():

    words = "Pythonoooo"
    
    
    return len([char for char in words if char in "aeiou"])

    # return len(lister)

    # lister = [char for char in word if char in "aeiou"]
    # print(lister)

    # counter = 0

    # for char in words:
    #     if char in "aeiou":
    #         counter += 1 

    # return counter



print(listComprehension())


