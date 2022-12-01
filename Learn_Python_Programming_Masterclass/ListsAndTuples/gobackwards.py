# A safer way to delete rogue values from a list is to iterate backwards through the list
# This code does it
# Code #1

data_1 = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

for index in range(len(data_1) - 1, -1, -1):
    if data_1[index] < min_valid or data_1[index] > max_valid:
        print(index, data_1)
        del data_1[index]
print(data_1)

print("********************")

# Code #2
data_2 = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
        170, 183, 185, 187, 188, 191, 350, 360]

top_index = len(data_2) - 1
# Reverse the list with reverse() function
for index, value in enumerate(reversed(data_2)):
    if value < min_valid or value > max_valid:
        print(top_index - index)
        del data_2[top_index - index]
print(data_2)