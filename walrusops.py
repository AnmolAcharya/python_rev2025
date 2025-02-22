names = ["Malong", "XuXin", "FZD", "WCQ", "LSD"]

# namesLst = [name for name in names if name == "Mashort"]

# print(namesLst)

if(name := input("Enter a name: ")) in names:
    print(f"Goat, {name}")
else:
    print("Not Found!")

