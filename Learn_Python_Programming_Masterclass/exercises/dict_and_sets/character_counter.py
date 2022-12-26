# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

string = ""
for char in text.casefold():
    if char.isalnum():
        string += char.casefold()
for char in string:
    if char not in word_count:
       word_count.setdefault(char, 1)
    else:
        word_count[char] += 1



# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)