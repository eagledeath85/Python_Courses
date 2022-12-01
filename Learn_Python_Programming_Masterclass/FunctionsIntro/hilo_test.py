LOW = 1
HIGH = 2047


# print("Please think of a number between {0} and {1}".format(low, high))
# input("Please press ENTER to start")

def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print("\t Guessing in the range of {0} and {1}".format(low, high))
        # Formula to calculate the midpoint between the high and the low value, to split the range 1-1000 in 2
        guess = low + (high - low) // 2
        # high_low = input("My guess is {0}. Should I guess higher or lower? "
        #                  "Enter h or l, or c if I guessed correctly ".format(guess).casefold())
        # if high_low == "h":
        if guess < answer:
            # Guess higher. The low end of the range becomes 1 greater than the guess
            low = guess + 1
            # elif high_low == "l":
        elif guess > answer:
            # Guess lower. The hig end of the range becomes 1 less than the guess
            high = guess - 1
            # elif high_low == "c":
        elif guess == answer:
        # print("I guessed it in {0} guesses!".format(guesses_number))
        # break
            return guesses
        # else:
        #     print("Please enter h, l or c")

        guesses += 1

correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("I guessed without being told {0} times. Max {1} guesses."
      .format(correct_count, max_guesses))
