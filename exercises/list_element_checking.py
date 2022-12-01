test_list = [1, 6, 3, 5, 3, 4]
value_to_check = 36
check_bool = value_to_check in test_list
if not check_bool:
    print(value_to_check, "is not in the list", str(test_list))
else:
    print(value_to_check, "is in the list", str(test_list))
