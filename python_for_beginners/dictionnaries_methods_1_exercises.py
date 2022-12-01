import math

dictionnary1 = {0: False, 1: "Welcome to the jungle", 2: math.pi, 3: 9999, 4: 'r'}

print(dictionnary1[2])
print(8 in dictionnary1)
print(10 not in dictionnary1)

print("*******************************************")

rock_groups = {"Queen": "Bohemian Rhapsody",
               "Bee Gees": "Stayin' Alive",
               "U2": "One",
               "Michael Jackson": "Billie Jean",
               "The Beatles": "Hey Jude",
               "Bob Dylan": "Like A Rolling Stone"
               }

print(len(rock_groups))
for key in rock_groups.keys():
    print(key)

print(rock_groups.values())
for key, value in rock_groups.items():
    print(key, value)

print(rock_groups.get("Promise of the Real", "Promise of the Real is not a key from rock_groups"))
