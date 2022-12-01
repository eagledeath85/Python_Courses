# Il existe 2 facons de trier les elements d'une liste
# sorted() function and .sort() method

# sorted() create a  new list and left the original one unchanged
pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

list_numbers = [3, 543, 21, 89, 857]
sorted_numbers = sorted(list_numbers)
print(sorted_numbers)

#.sort() sorts the list in place
list_numbers.sort()
print(list_numbers)

# To sort without taking care of capital letters, we use casefold()

missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)
print(missing_letter)

names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
names.sort(key=str.casefold)
print(names)