# del statement allows to delete values from a list
planets = ["pluto", "mars", "earth", "venus"]
del planets[0]
print(planets)

# .remove() method allows to remove what you pass it as an arguent from a list
planets = ["pluto", "mars", "earth", "venus"]
planets.remove("mars")
print(planets)

# .append() method takes an argument and adds that to the end of the list
pets = ["cat", "dog", "parrot"]
pets.append("fish")
print(pets)

# .insert method allows to add an item anywhere you want to a list
pets = ["cat", "dog", "parrot"]
pets.insert(1, "turtle")
print(pets)

# .sort() method allows to sort a list made up of items that are all numbers or all strings
num_list = [2.718, 4, -19, 10000, 0]
print(num_list)
num_list.sort()
print(num_list)

star_list = ["Ringo", "John", "George", "Paul"]
print(star_list)
star_list.sort()
print(star_list)

# reverse = True sort items of a list in reverse order
star_list.sort(reverse=True)
print(star_list)

# .sort() method sorts strings in ASCIIbetical order
ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ASCIIbetical.sort()
print(ASCIIbetical)
ASCIIbetical.sort(key=str.lower)
print(ASCIIbetical)

# .index() allows you to get the index of an item from a list
metals = ["cooper", "gold", "silver", "iron"]
print(metals.index("silver"))

# .pop() method removes and returns an item from a list.
# This way, the removed item can be assigned to another variable
# When used without argument, this method removes the last item from a list
bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end = bands.pop()
print(end)
bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end = bands.pop(2)
print(end)
print(bands)
