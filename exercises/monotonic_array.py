input_array = [1, 2, 3, 4, 9, 6]
i=0

# Creating 2 arrays by sorting the input_array ekements descending or ascending
ascending_array = []
descending_array = []

ascending_array.extend(input_array)
descending_array.extend(input_array)
ascending_array.sort()
descending_array.sort(reverse=True)

if ascending_array == input_array or descending_array == input_array:
    print("True")
else:
    print("False")




