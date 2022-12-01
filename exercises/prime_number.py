user_input = int(input("Enter an integer: "))

if user_input > 1:
    for number in range(2, int(user_input / 2)+1):
        if (user_input % number) == 0:
            print(user_input, " is not a prime number")
            break
        else:
            print(user_input, " is a prime number")
else:
    print(user_input, " is not a prime number")
