# Dictionnary is a sequence of "key-value" pairs
# Tip #1: If we know the key will be present, the use indexing
# If there's a possibility that the key won't be present, use the get method
# Tip #2: Indexing a key that's not present will crash the program, using the
# get method for a key that's not present will return 'None'
vehicles = {
    'dream': 'Honda 250 T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

# Accessing value for a given key (Indexing)
my_vehicle = vehicles['can-am']
print(my_vehicle)
commuter = vehicles['virago']
print(commuter)
print()

# Accessing value with the get method
er5 = "er5"
learner = vehicles.get(er5)
print(learner)
print()

# Iterating over a dictionary to print the keys
for key in vehicles:
    print(key)
print()

# Iterating over a dictionary to print key:value pair
for key in vehicles:
    print(key, vehicles[key], sep=': ')
print()

# Using the .items() method
for key, value in vehicles.items():
    print(key, value, sep=': ')
print()

# Adding a key-value pair in a dictionary
vehicles["starfighter"] = "Lockheed F-104"
vehicles["glider"] = "toy"
for key, value in vehicles.items():
    print(key, value, sep=': ')