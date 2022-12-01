# input_string = "12:05:45 AM"
# print(input_string[-2:])
# print(input_string[:2])


def convertTo24(input_string):


    # Check if last 2 elements of time are AM and first 2 elements are 12
    if input_string[-2:] == "AM" and input_string[:2] == "12":
        return "00" + input_string[2:-2]

    # remove AM
    elif input_string[-2:] == "AM":
        return input_string[:-2]

    # Check if last 2 elements of time are PM and first 2 elements are 12
    elif input_string[-2:] == "PM" and input_string[:2] == "12":
        return input_string[:-2]

    else:

        # add 12 to hours and remove PM
        return str(int(input_string[:2]) + 12) + input_string[2:8]


print(convertTo24("12:34:12 AM"))