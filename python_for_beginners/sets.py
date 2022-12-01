# set is a data type that consist of a collection of items , like a list
# set cannot have duplicate values in it
# the items contained in a set are unordered, like in a dictionnary
# set() can hold items of different data types

# sets are useful when we want to use a collection of items without duplicates
# and the order of items doesn't matter

# set Declaration

set_1 = {1, 2, 3, 4, 5}
set_2 = set({"a", "b", "c", "d", "e"})  # set() function takes a set as an argument and returns it
set_3 = set()
set_4 = set(range(1, 12, 2))
print(set_1)
print(set_2)
print(set_3)
print(set_4)

#set elements cannot be accessed by index. To access them  a for loop is required
set_5 = {3, 6, 9, 12, 15}
for num in set_5:
    print(num)

# set comprehension is a more advanced way to create a set
# There are 3 things that make up a set comprehension
    # 1- The entire thing must be enclosed in curly brackets
    # 2- There's a for loop that goes over an iterable data type such as a range or a string
    # 3- Theres an action that is done to each item that the for loop iterates over
comp_1 = {even+2 for even in range(2, 11, 2)}
#         action       for         loop

comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)
