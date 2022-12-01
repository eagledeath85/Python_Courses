user_choice = input("Enter three integers: ")
user_list = user_choice.split(',')

for index in range(len(user_list)):
    user_list[index] = int(user_list[index])

result = user_list[0] + user_list[1] - user_list[2]
print(result)