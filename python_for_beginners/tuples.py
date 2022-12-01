# Tuple is a data type made up of collection of items
# !!!!!!!! Tuples are immutable !!!!!!!!
# There are 2 ways to declare a tuple
# Declaring a tuple with tuple() function implies that the argument is an iterable one (list or string)
# Tuple Declaration is as follows

tuple_1 = ("a", "b", "c", "d", "e")
tuple_2 = (2.718, False, [1, 2, 3])
tuple_3 = (1, 1, 0, 0, 0)
tuple_5 = tuple([3.14, 2.205, 10])
tuple_6 = tuple("edcba")
print(tuple_5)
print(tuple_6)

occupations = {("Angus", "Young"): "musician",
               ("Narendra", "Modi"): "prime minister",
               ("Richard", "Branson"): "entrepreneur",
               ("Quentin", "Tarantino"): "filmmaker"
               }
print(type(occupations))

# Iterating through a tuple is the same as iterating through a list
major_cities = ("Tokyo", "London", "New York", "Shangai", "Mumbay")
for element in major_cities:
    print(element)

counter = 0
while counter < len(major_cities):
    print(major_cities[counter])
    counter += 1

# How to step in a tuple
ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::3])    # stride length of 3.
print(ints[1::2])   # evens number only
print(ints[7::-1])  # backwards from 8
print(ints[8::-2])  # odds only backwards

