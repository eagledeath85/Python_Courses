# Initial array
initial_array = [1, 2, 3, 4, 5, 6, 7]

# Size of the array
n = 7

# Rotation of elements
d = 2

# Building a temporary array in which the array indexes 0 to d-1 will be stored
temp_array = []
i = 0
while (i < d):
    temp_array.append(initial_array[i])
    i = i + 1
print(temp_array)
print(initial_array)

# Shifting all the items of the initial array
i = 0
while (d < n):
    initial_array[i] = initial_array[d]
    i = i + 1
    d = d + 1
initial_array[:] = initial_array[:i] + temp_array
print(initial_array)


