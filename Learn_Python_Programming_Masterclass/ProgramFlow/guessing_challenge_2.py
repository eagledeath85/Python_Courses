from random import randint

highest = 10
answer = randint(1, highest)
print(answer)   #TODO: remove after testing

is_answer_found = False

print("Please guess number between 1 and {0}: ".format(highest))
guess = int(input())

if guess == 0:
    print("Good bye")
elif guess == answer:
    print("You got it first time!")
    is_answer_found = True
else:
    while not is_answer_found:
            if guess < answer:
                print("Please guess higher")
                guess = int(input())
            elif guess > answer:
                print("Please guess lower")
                guess = int(input())
            elif guess == answer:
                print("You got it!")
                is_answer_found = True

