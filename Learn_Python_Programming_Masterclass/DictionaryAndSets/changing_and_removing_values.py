vehicles = {
    'dream': 'Honda 250 T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'starfighter': 'Lockheed F-104',
    'learjet': 'Bombardier Learjet 75',
}

# Updating the value of 'virago' key
vehicles["virago"] = "Yamaha XV535"

# Removing a key-value pair from a dictionary by indexing method
del vehicles["starfighter"]

# .pop() method removes and returns a key-value pair from a dictionary
planes = vehicles.pop("learjet")
print("planes: ", planes)
print()

# We can print a default value if the key is not found
result = vehicles.pop("f1", "f1 is not a key of this dictionary")

for key, value in vehicles.items():
    print(key, value, sep=': ')
print()

print(result)


