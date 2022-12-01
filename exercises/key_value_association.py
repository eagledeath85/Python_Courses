from collections import defaultdict

test_dict = {"abc" : [10, 30], "bcd" : [30, 40, 10]}

result = defaultdict(list)
for key, value in test_dict.items():
    for element in value:
        result[element].append(key)
print(str(dict(result)))