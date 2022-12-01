current_choice = "-"
computer_parts = []  # Create an empty list
ITEM = 0
ITEM_PRICE = 1
total_to_pay = 0
available_parts = [("computer", 700),
                   ("monitor", 300),
                   ("keyboard", 80),
                   ("mouse", 30),
                   ("mouse mat", 20),
                   ("hdmi cable", 10),
                   ("usb hub", 15),
                   ("gaming chair", 250),
                   ]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

print(valid_choices)
while current_choice != '0':
    if current_choice in valid_choices:

        index = int(current_choice) - 1
        chosen_part = available_parts[index][ITEM]
        if chosen_part in computer_parts:
            # it's already in the cart, so remove it
            computer_parts.remove(chosen_part)
            print("Removing the item {0} to the list".format(current_choice))
        else:
            computer_parts.append(chosen_part)
            print("Adding the item {0} to the list".format(current_choice))
            total_to_pay = total_to_pay + available_parts[index][ITEM_PRICE]
        print("Your list now contains {}".format(computer_parts))
    else:
        print("Please choose one the options below: ")
        # enumerate function allows to return each item with its index position
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
    current_choice = input()

print("Your list {0} is completed".format(computer_parts))
print("Total to pay: $ {0}".format(total_to_pay))
