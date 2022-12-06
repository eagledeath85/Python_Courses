from random import random, randint

# Defining input_list size
input_list = []
for i in range(randint(0, 10)):
    # Populating input_list with random values from 1 to 30
    n = randint(1, 30)
    input_list.append(n)
print(input_list)

def square_values(list_square_values_from: list) -> list:
    new_list = []
    for element in list_square_values_from:
        new_list.append(element ** 2)
    return new_list

print(square_values(input_list))