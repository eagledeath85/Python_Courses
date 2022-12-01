test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]
             }

test_list = []

for key in test_dict.keys():
    test_list.extend(test_dict[key])

test_list = list(set(test_list))
test_list.sort()
print(test_list)
