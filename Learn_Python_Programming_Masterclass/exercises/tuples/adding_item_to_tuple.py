tuple1 = ("one", "two", "three",)
tuple1 += "four",
print(tuple1)

string1 = str(tuple1)
print(string1)
print(type(string1))


tuple3 = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
tuple31, tuple32, tuple33 = tuple3
print('White' in tuple31 or 'White' in tuple32 or 'White' in tuple33)
print('Olive' in tuple31 or 'Olive' in tuple32 or 'Olive' in tuple33)
print('Purple' in tuple31 or 'Purple' in tuple32 or 'Purple' in tuple33)
