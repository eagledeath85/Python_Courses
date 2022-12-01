input_list = [12, 67, 98, 34]
result = []

for element in input_list:
    sum = 0
    print(element)
    for digit in str(element):
        sum = sum + int(digit)
        #print(digit)
    result.append(sum)

print(result)
