input_dict = {'a': 100, 'b':200, 'c':300}
input_list = []
for value in input_dict.values():
    nb = value
    input_list.append(value)
print(input_list)

sum = 0
for ele in input_list:
    sum += ele
print(sum)
