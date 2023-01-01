d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three",
}
# Updating key-value pair of d dictionary with the key-value pairs of d2 dictionary
d.update(d2)
for key, value in d.items():
    print(key, value)
print()

# Updating a dictionary with a tuple
d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key, value)
print()

# Getting the keys of a dictionary
keys = d.keys()
print(keys)
print()

#Getting the values of a dictionary
values = d.values()
print(values)
print()

# With the .fromkeys() method we can use the values of the list above to create a dictionary whose keys are the list values
new_dict = dict.fromkeys(pantry_items, 0)
print(new_dict)