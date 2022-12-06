input_list = [1, 2, 3, 4, 5]


def square_values(list_square_values_from: list) -> list:
    new_list = []
    for element in list_square_values_from:
        new_list.append(element ** 2)
    return new_list

print(square_values(input_list))