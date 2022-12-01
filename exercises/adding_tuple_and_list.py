test_list = [5, 6, 7]
test_tup = (9,10)

test_list.extend(list(test_tup))
print(str(test_list))

test_list = [1,2,3,4]
test_tup=(5,6)

test_tup = list(test_tup)
test_tup.extend(test_list)
test_tup = tuple(test_tup)
print(str(test_tup))