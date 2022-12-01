low = 1
high = 1000
guesses_number = 1

print("Please think of a number between {0} and {1}".format(low, high))
input("Please press ENTER to start")

while True:
    print("\t Guessing in the range of {0} and {1}".format(low, high))
    # Formula to calculate the midpoint between the high and the low value, to split the range 1-1000 in 2
    guess = low + (high - low) // 2
    high_low = input("My guess is {0}. Should I guess higher or lower? "
                     "Enter h or l, or c if I guessed correctly ".format(guess).casefold())
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The hig end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I guessed it in {0} guesses!". format(guesses_number))
        break
    else:
        print("Please enter h, l or c")

    guesses_number += 1
