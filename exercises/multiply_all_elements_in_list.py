import math

list = [1, 2, 3, 4, 5, 6]

total = 1

for i in range(0, len((list))):
    total = total * list[i]
print(total)

print("######################")
print(math.prod(list))
