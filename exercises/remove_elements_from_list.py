input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in input_list:
    if i % 2 == 0:
        #del input_list[i]
        input_list.remove(i)
print(input_list)
