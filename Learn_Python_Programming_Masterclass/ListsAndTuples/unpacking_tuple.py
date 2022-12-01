# Unpacking a tuple makes it a lot easier to read and understand

metallica = ("Ride the Lightning", "Metallica", 1984)

# Unpacking tuple metallica
title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)

# Unpacking table tuple
name, length, width, height, price = table
print(length * width)

x, y, z = 1, 2, 76  # what's on the right side is a tuple
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1, 2, 76  # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")
data_list = [12, 13, 14]
p, q, r = data_list
print(q)
print(r)

for index, character in enumerate("abcdefgh"):
    print(index, character)

for t in enumerate("abcdefgh"):
    print(t)

# Unpacking a tuple of tuples
countries = (("France", 65000000, 643801),
             ("Spain", 50000000, 505990),
             ("Germany", 70000000, 357588)
             )
for country in countries:
    country_name, population, area = country
    print("En {0} le nombre d'habitants au km2 est de {1}".format(country_name, int(population / area)))

albums = [
        ("Welcome to my nightmare", "Alice Cooper", 1075),
        ("Bad Company", "Bad Company", 1974),
        ("Nightflight", "Budgie", 1981),
        ("More Mayhem", "Emilda May", 2011),
        ("Ride the Lightning", "Metallica", 1984)
        ]

for name, artist, year in albums:
    print("Album: {0}, Artist: {1}, Year:{2}".format(name, artist, year))

