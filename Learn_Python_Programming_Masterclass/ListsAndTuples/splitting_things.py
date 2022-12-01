panagram = "The quick brown fox jumps over the lazy dog"

# split() method is called on a string and returns a list
# By default the split() method splits by whitespace, including tabs and new lines
words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split())

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7', ' '
                  ]
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

for i in range(len(values_list)):
    values_list[i] = int(values_list[i])
    print(type(values_list[i]))
print(values_list)
