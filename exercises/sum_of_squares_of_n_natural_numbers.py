user_input = int(input("Enter an integer value: "))

def __sumOfSquares(user_input):
    sum = 0
    for i in range(1, user_input + 1, 1):
        sum = sum + i**2
    return sum


print(__sumOfSquares(user_input))
