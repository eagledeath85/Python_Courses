even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
empty_list = []

#even.extend(odd)
even.sort()
print(even)
even.sort(reverse=True)
print(even)

numbers = even + odd
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Create a list of lists
numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)