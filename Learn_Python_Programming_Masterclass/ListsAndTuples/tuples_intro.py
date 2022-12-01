# a tuple is a mathematical name for an ordered set of data
# its syntax is a set of data in parenthesis ("string", variable, integer)
# tuples differ from lists because they are immutables,
# meaning they can't be changed once they're created - just like strings

# Tuple advantage 1: tuples are immutable, meaning the integrity of the data is protected
# Tuple advantage 2: because tuple is immutable, it can always be unpacked successfully

t = ("a", "b", "c")
print(t)

# Parenthesis must be used whe we pass a tuple literal as an argument to a function
name = "Tim"
age = 32
print(name, age, "Python", 2020)
print((name, age, "Python", 2020))


welcome = ("Welcome to my nightmare", "Alice Cooper", 1075)
bad = ("Bad Company", "Bad Company", 1974)
budgie = ("Nightflight", "Budgie", 1981)
imelda = ("More Mayhem", "Emilda May", 2011)
metallica = ("Ride the Lightning", "Metallica", 1984)

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

title, artist, year = metallica
print(title)
print(artist)
print(year)