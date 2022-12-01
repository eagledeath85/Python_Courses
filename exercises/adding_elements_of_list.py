import math

list = [54, 979, 23, 5, 86]
print(sum(list))

total = 0

for i in range(0, len(list)):
    #total = total + list[i]
    print(i)
    print(list[i])
print(total)

for i, element in enumerate(list):
    print(element)

element = 0
sum = 0
while element < len(list):
    sum = sum + list[element]
    element + 1
print(sum)
