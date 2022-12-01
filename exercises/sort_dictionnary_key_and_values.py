test_dict = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4]
             }

result = dict()

#print(sorted(test_dict))
for key in sorted(test_dict):
    result[key] = test_dict[key]

print(result)
