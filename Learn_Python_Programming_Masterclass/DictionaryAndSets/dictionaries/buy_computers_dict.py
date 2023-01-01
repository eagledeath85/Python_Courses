available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "mouse mat",
                   "6": "hdmi cable",
                   "7": "usb hub",
                   "8": "gaming chair"
                   }

computer_parts = {}  # Create an empty dictionary to store user's choices

# We have to initialize current_choice to anything that's not in
# valid choices of available_part nor equal to 0
current_choice = None
while current_choice != "0":
    # We need to decide if the user's choice is valid
    # If it is we print a message that we're adding the part
    # We display back the menu otherwise
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {current_choice}")
            computer_parts.pop(current_choice)
        else:
            computer_parts[current_choice] = chosen_part
            print(f"Adding {chosen_part}")
        print(f"Your dictionary now contains {computer_parts}")
    else:
        print("Please choose items from the list below:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
    current_choice = input("> ")