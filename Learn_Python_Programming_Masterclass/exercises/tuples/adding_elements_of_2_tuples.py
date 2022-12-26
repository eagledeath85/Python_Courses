tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

list_from_tuples = list(zip(tuple1, tuple2, tuple3))
final_tuple = [sum(element) for element in list_from_tuples]
print(final_tuple)

print()

string_values_tuple = (('333', '33'), ('1416', '55'))
print(string_values_tuple)
string_values_tuple_to_list = list(string_values_tuple)
string_list_of_lists = []
for element in string_values_tuple_to_list:
    string_list_of_lists.append(list(element))
    for item in string_list_of_lists:
         for i in (0,len(item) - 1):
             item[i] = int(item[i])


integer_tuple_of_tuples = tuple(tuple(element) for element in string_list_of_lists)
print(integer_tuple_of_tuples)
