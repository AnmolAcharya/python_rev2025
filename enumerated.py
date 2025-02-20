# def lister():

#     players = ["MaLong", "XuXin", "FZD", "ZJK", "MaLin", "WCQ", "LSD"]

#     # for index, player in enumerate(players):
#     #     print(index, player)

#     list_players = [(index,player) for index, player in enumerate(players)] #List comprehensions -> sleek and cool way to write code 
#     print(list_players)

# lister()

########Iterating over a dictioanry:

def enum_dict():

    scores={"SquidGame": 90, "MoneyHeist": 88, "BreakingBad": 99}
    for index, score in enumerate(scores.items()):
        print(index,score)

enum_dict()