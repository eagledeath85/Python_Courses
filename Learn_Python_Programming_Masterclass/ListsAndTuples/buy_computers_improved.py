current_choice = "-"
computer_parts = [] # Create an empty list

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "usb hub",
                   "gaming chair"
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

print(valid_choices)
while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in the cart, so remove it
            computer_parts.remove(chosen_part)
            print("Removing the item {0} to the list".format(current_choice))
        else:
            computer_parts.append(chosen_part)
            print("Adding the item {0} to the list".format(current_choice))
        print("Your list now contains {}".format(computer_parts))
    else:
        print("Please choose one the options below: ")
        # enumerate function allows to return each item with its index position
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
    current_choice = input()

print("Your list {0} is completed".format(computer_parts))
