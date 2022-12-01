input_string = "hello geeks for geeks is computer science portal"
k = 7

result = []

text = input_string.split(' ')
for x in text:
    if len(x) > k:
        result.append(x)
print(result)
