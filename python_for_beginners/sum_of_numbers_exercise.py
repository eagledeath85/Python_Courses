user_num = int(input("Please enter a positive integer: "))
int_entered = user_num
sum = 0

while user_num != 0:
    sum = sum + user_num
    user_num -= 1

print("You entered the positive integer " + str(int_entered))
print(sum)
