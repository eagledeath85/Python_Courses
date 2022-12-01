# While loop is used when we need to keep looking as long as some condition is True
# and stop when it becomes False
# Syntax is

# while <condition>:
#     execute some code


# for i in range(10):
#     print("i is now {0}".format(i))

i = 0
while i < 10:
    print("i is now {0}".format(i))
    i += 1

# break keyword allows to get out of the while loop
available_exits = ["north", "south", "east", "west"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please try again: ")
    if chosen_exit.casefold() == "quit":
        print("good bye")
        break