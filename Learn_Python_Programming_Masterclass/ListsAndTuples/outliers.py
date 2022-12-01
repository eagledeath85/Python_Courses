# Deleting items from a list

data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
        170, 183, 185, 187, 188, 191, 350, 360]

# del data[:2]
# print(data)
# del data[14:]
# print(data)

# Removing items from a list changes its length
# So to do it, do not use a for loop

min_valid = 100
max_valid = 200

# Here is how to safely remove values from a list.
# A more efficient way is also presented in gobackwards.py

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
# delete the slice up to but not including stop from data list
del data[:stop]

# process the hgh values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    print(index)  # for debugging
    if data[index] <= max_valid:
        # We have the index of the last item to keep
        # Set 'start' to the position of the first
        # to delete, which is one after 'index'
        start = index + 1
        break

print(start)    # for debugging
del data[start:]
print(data)