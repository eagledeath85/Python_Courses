filename = 'Jabberwocky.txt'

with open('Jabberwocky.txt') as poem:
    first = poem.readline().rstrip()

print(first)

# How the strips() method works. They remove all from a sequence of characters, until a non-matching character is found.
chars = "' Twasebv"
for character in first:
    if character in chars:
        print(f'Removing "{character}"')
    else:
        break
print('*' * 50)

for character in reversed(first):
    if character in chars:
        print(f'Removing "{character}"')
    else:
        break

# Removing a prefix or a suffix from a string
twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removes = first.removesuffix("toves")
print(toves_removes)