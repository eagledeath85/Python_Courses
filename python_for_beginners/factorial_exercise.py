from random import randint


def factorial(factorial_number):
    fact = 1
    for num in range(factorial_number, 1, -1):
        fact *= num
    return fact


print(factorial(3))
print(factorial(4))
print(factorial(5))
