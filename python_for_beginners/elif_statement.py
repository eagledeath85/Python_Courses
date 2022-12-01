user_num = int(input("Please enter an integer: "))

if user_num < 0:
    print("The number you entered is less than 0.")
elif user_num == 0:
    print("The number you entered is equal to 0.")
elif 0 < user_num <= 100:
    print("The number you enter is either 1, 100 or anything in between")
else:
    print("The number you entered is greater than 100.")
