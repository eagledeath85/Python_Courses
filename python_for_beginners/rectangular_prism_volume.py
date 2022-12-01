length_input = int(input("Please enter the length of the prism: "))
width_input = int(input("Please enter the width of the prism: "))
height_input = int(input("Please enter the height of the prism: "))


def rectangular_prism_volume_calculation(length, width, height):
    volume = length * width * height
    return volume


print("The volume of the rectangular prism is " + str(rectangular_prism_volume_calculation(length_input, width_input, height_input)))
