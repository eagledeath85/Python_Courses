from random import randint

# To add Docstrings, just need to tap 3 times " and then enter
def get_integer(prompt):
    """
    Get an integer from Standard Input (stdint)
    The function will continue looping, and prompting the user,
    until a valid `int` is entered.
    :param prompt: The String the user will see,
        when they're prompted to enter the value.
    :return: The integer that the user enters
    """
    # get_integer function will get input from user rand return an integer value
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("Please enter a valid number")


highest = 1000
answer = randint(1, highest)
print(answer)   #TODO: remove after testing
guess = 0   # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {0}: ".format(highest))


while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        guess = get_integer(": ")
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")
