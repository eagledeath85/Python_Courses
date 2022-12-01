word = input("Please enter a string: ")
num_of_characters = 0

for letter in word:
    print(letter)
    num_of_characters += 1

print("\nYou entered " + word)
print("There are " + str(num_of_characters) + " characters in the word " + word)
