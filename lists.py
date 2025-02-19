def lists(scores):

    mutab = list(scores)

    print(mutab[0])
    print(mutab[1:4])
    print(len(mutab))
    print(mutab.append(6))
    print(mutab)
    mutab.pop()
    print(mutab)

    mutab.pop(-2)
    print(mutab)


print(lists([1,2,3,4,5])) 

