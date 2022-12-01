answer = 5
correct_guess = False

while not correct_guess:
    print("Please guess number between 1 and 10: ")
    guess = int(input())

    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("You got it!")
        correct_guess = True
