available_exits = ["north", "south", "east", "west"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please try again: ")
    if chosen_exit == "quit":
        print("Game Over")
        break
else:
    print("Good job")
