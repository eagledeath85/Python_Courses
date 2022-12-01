LOW = 1
HIGH = 100


def fizz_buzz(value_to_check: int) -> str:
    """
    Get an integer and checks if it's divisible by 3 or 5 or both
    :param value_to_check: The value to check. Must be `int` .
    :return: "fizz" if `value_to_check` is divisible by 3
        "buzz" if `value_to_check` is divisible by 5
        "fizz buzz" if `value_to_check` is divisible by 3 and 5
    """
    # for num in integers:
    if (value_to_check % 3) == 0 and (value_to_check % 5) == 0:
        return "fizz buzz"
    elif (value_to_check % 3) == 0:
        return "fizz"
    elif (value_to_check % 5) == 0:
        return "buzz"
    else:
        return str(value_to_check)


# for number in range(LOW, HIGH + 1):
#     value_returned = fizz_buzz(number)
#     print(value_returned)

# Initialize the counter to be checked
next_number = 0
while next_number < 99:
    next_number += 1
    # Print the result of fizz_buzz for the next number (ie computer's turn)
    print(fizz_buzz(next_number))
    # Incrementing next_number t
    next_number += 1
    # Calculate the correct answer for this next number
    correct_answer = fizz_buzz(next_number)
    # Asking user to enter the next value
    players_number = input("Your turn: ")
    # Check the value entered by user is correct
    if players_number != correct_answer:
        print("You lose! Correct answer was {0}".format(correct_answer))
        break
else:
    print("Well done! you reached {0}".format(next_number))

