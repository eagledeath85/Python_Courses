# Set declaration
farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
numbers = set("12345")
print(farm_animals)
print(numbers)

# Items in sets are unordered
for animal in farm_animals:
    print(animal)

more_animals = {'goat', 'cow', 'horse', 'hen', 'sheep'}

# Comparing the 2 sets
if farm_animals == more_animals:
    print("The 2 sets are equal")
else:
    print("The 2 sets are different")