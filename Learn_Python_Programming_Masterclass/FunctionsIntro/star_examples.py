# The * character is useful to pack or unpack any sequence type

# numbers = (0, 1, 2, 3, 4, 5)
# print(numbers)  # This will print the tuple
# print(*numbers) # This will unpack the tuple numbers and print each of its values
# print(0, 1, 2, 3, 4, 5)

# Instead of unpacking the sequence that we pass as an argument,
# we can specify that a parameter is an unpacked sequence


# *args represents an unpacked tuple
def test_star(*args):
    print(args)
    for x in args:
        print(x)


# 0, 1, 2, 3, 4, 5 are treated as an unpacked
test_star(0, 1, 2, 3, 4, 5)
test_star()