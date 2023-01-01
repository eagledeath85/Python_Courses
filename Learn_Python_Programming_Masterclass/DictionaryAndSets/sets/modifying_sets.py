# numbers = set()
#
# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     # Adding values to the set
#     numbers.add(next_value)
# print(numbers)


# Create a set from a list, to remove duplicates
data = ["blue", "red", "blue", "green", "red", "blue", "white"]
unique_data = set(data)
print(unique_data)

print()
# Create a list of unique colors, keeping the order they appeared
# How does it work: fromkeys() method creates a dictionary, and gets the keys from the iterable we pass to it
# When a value already appears in the dictionary, the new one replaces the existing one, but the insertion order is preserved
# We then convert the dictionary to a list
print(dict.fromkeys(data))
unique_data = list(dict.fromkeys(data))
print(unique_data)