user_string = input("Please enter a string: ")
reversed_string = ""

for letter in range(len(user_string) -1, -1, -1):
    reversed_string += user_string[letter]

print(reversed_string)


