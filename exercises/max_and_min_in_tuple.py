test_tup = (3, 7, 1, 18, 9)
k = 2
test_tup= list(sorted(test_tup))

result = []

for index, value in enumerate(test_tup):
    if index < k or index >= len(test_tup) - k:
        result.append(value)

tuple(result)
print(result)