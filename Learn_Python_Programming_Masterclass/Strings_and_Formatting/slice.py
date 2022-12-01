parrot = "Norwegian Blue"

# Slicing string
print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[:9])   # Norwegian
print(parrot[10:])  # Blue
print(parrot[:])    # Norwegian Blue

print("##################")

# Slicing string with negative values

print(parrot[5:-5])     # gian
print(parrot[-4:-2])    # Bl
print(parrot[:-8])      # Norweg
print(parrot[-11:-9])   # we
print(parrot[:-5])      # Norwegian
print(parrot[-4:])      # Blue
print(parrot[-14:])     # Norwegian Blue

# Slicing string using step

print(parrot[0:10:2])   # Nrein
print(parrot[::3])      # Nwi u

number = "9,223;317:067 854;184,623"
separators = number[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print(values)
print([int(val) for val in values])