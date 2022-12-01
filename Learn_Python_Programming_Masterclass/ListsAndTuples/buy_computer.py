current_choice = "-"
computer_parts = [] # Create an empty list

while current_choice != '0':
    if current_choice in "123456":
        print("adding the item {0} to the list".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("mouse mat")
        elif current_choice == '6':
            computer_parts.append("HDMI cable")
    else:
        print("Please choose one the options below: "
              "\n1: computer"
              "\n2 monitor"
              "\n3: keyboard"
              "\n4: mouse"
              "\n5: mouse mat"
              "\n6. HDMI cable"
              "\n0: to finish")
    current_choice = input()
print("You list", str(computer_parts), "is completed")