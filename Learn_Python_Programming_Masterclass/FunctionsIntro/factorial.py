import math

def factorial(number: int) -> int:
    """
    This function calculates the factorial of the parameter number
    :param number: the number to calculate the factorial from
    :return: 1 if `number` is 0
            the factorial number
    """
    if number <= 1:
        return 1
    return math.factorial(number)


four = factorial(4)
print(four)
five = factorial(5)
print(five)
six = factorial(6)
print(six)
