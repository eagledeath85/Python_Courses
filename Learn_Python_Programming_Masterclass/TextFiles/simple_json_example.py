import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

# To serialize Python values to a file,
# we open a text file for writing, then use the json.dump function.
# The dump() function serializes the data we give it, and write the result to the file.
# The load() function allows us to read the data from the file, and decode it.

with open('test.json', 'w', encoding='utf-8') as testfile:
    # Dumping languages list to testfile
    json.dump(languages, testfile)

with open('test.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)
print(data)
print(data[4])