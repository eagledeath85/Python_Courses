# We use the with-as statement to open files in python.
# This statement automatically closes files after running the with block, preventing from reading leaks

# Way 1 to read from a file: iterating over it with a for loop
with open('Jabberwocky.txt', 'r') as jabber:
     for line in jabber:
        print(line.rstrip())

# Way 2 to read from a file: using the readlines() method. It returns a list containing strings for each line from the file.
with open('Jabberwocky.txt', 'r') as jabber:
    lines = jabber.readlines()
print(lines)

# Way 3 to read from a file: using the read() method. It returns a single string containing all the characters in the file.
with open('Jabberwocky.txt') as jabber:
    text = jabber.read()
for character in reversed(text):
    print(character, end='')

# Way 4 to read from a file: using the readline() method. It reads one line of the file at the time
with open('Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        if 'jubjub' in line.casefold():
            break