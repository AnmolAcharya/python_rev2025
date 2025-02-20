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

    word = "Python"

    lister = [char for char in word if char in "aeiou"]
    print(lister)

listComprehension()