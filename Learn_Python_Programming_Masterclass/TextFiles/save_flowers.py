data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# There are 2 ways of writing data into a file.
# Way 1: printing data to the file with print() method

# Create a txt file to write to it
plants_filename = "flowers_print.txt"

# Writing to plants_filename with the print() method
with open(plants_filename, 'w') as plants:
    for plant in data:
        print(plant, file=plants)

# Checking the data is correctly written in the file
new_list = []
with open(plants_filename) as plants:
    for plant in plants:
        new_list.append(plant.rstrip())
print(new_list)

# ***********************************************************8
# Way 2: using the write() function
# Create a txt file to write to it
plants_filename_write = "flowers_write.txt"
with open(plants_filename_write, 'w') as plants_write:
    for plant in data:
        plants_write.write(plant)

# !!! We can only write strings to a text file with the write() method
# The print() function prints the string representation of any object you ask it to print
# The write will only write exactly what you tell it to write.
# No separators or newline characters are included, unless you explicitly tell it to write them.
# Also, no conversion is performed. If you tell write to write an integer,
# that's what it will try to send to the file. If the file is opened in text mode
# (the default), you'll get an error if you try to write numerical values to it.

filename = "test_numbers.txt"
with open(filename, 'w') as test:
    for i in range(10):
        test.write(str(i) + '\n')