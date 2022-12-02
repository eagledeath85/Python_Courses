def sum_numbers(*args: float) -> float:
    """
    Calculate the sum of the numbers `float` passed as arguments
    :param args: The numbers `float` to be added
    :return: the sum of the numbers passed. `float`
    """
    return sum(args)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))