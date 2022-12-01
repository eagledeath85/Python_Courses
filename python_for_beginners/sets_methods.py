# .add() adds its argument to the set it is called on
set_1 = {1, 2, 3, 4}
set_1.add(5)
print(set_1)

# .remove() removes its argument from the set it is called on
# if remove() is called on an argument that's not in the set, an error message is returned
set_2 = {1, 2, 3, 4, 5}
set_2.remove(5)
print(set_2)

# .discard() performs the same action as remove()
# the only difference is when discard is called on an argument that's not in the set, it does nothing
set_3 = {"apple", "banana", "orange", "tomato"}
set_3.discard("carott")
print(set_3)

# .clear()gets rid of everything in the set it's called on
set_4 = {"Everest", "Kilimanjaro", "Fuji"}
set_4.clear()
print(set_4)

# .copy() returns a copy of a set that has its own place in memory
set_5 = {"Everest", "Kilimanjaro", "Fuji"}
backup_set = set_5.copy()
print(backup_set)

# .union() allows to combine all the items from 2 different sets into a single set
set_6 = {10, 20, 30, 40}
set_7 = {50, 60, 70, 80, 90}
set_8 = set_6.union(set_7)  #symbol | is also used: set6 | set_7
print(set_8)

# .intersection() allows to find out what items 2 sets have in common
set_9 = {4, 5, 6, 7, 8}
set_10 = {6, 7, 8, 9, 10}
print(set_9.intersection(set_10))   # symbol & is also used: set_9 & set_10

# .difference()
set_11 = {4, 5, 6, 7, 8}
set_12 = {6, 7, 8, 9, 10}
print(set_11.difference(set_12))
print(set_12.difference(set_11))
