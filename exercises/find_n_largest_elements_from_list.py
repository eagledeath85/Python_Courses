input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nb_of_elements = 4

#Sort the input list
input_list.sort(reverse=True)
print("input_list:", input_list)

# Print the N largest elements from the list
#print(input_list[:nb_of_elements])


def __findNLargestElements(input_list, nb_of_elements):
    input_list.sort(reverse=True)
    return input_list[:nb_of_elements]


print("The {} largest elements from {} are {}".format(nb_of_elements, input_list, __findNLargestElements(input_list, nb_of_elements)))




