input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = []
odd_list = []
min_range = int(input("Enter the minimum value of the range: "))
max_range = int(input("Enter the maximum value of the range: "))

for i in range(0, len(input_list)):
    if int(input_list[i]) % 2 == 0:
        even_list.append(input_list[i])

print(even_list)

for j in range(0, len(input_list)):
    if int(input_list[j] + 1) % 2 == 0:
        odd_list.append(input_list[j])

print(odd_list)

for k in range(min_range, max_range+1):
    if k % 2 ==0:
        print(set(k))

