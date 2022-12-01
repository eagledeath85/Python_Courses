# The if-else statement

name1 = input("Please enter your name: ")
age1 = int(input("How old are you, {0} ?".format(name1)))
if age1 >= 18:
    print("You're eligible to vote")
else:
    print("Please come back in {0} years".format(18 - age1))


# The elif statement
name2 = input("Please enter your name: ")
age2 = int(input("How old are you, {0} ?".format(name2)))

if age2 < 18:
    print("Please come back in {0} years".format(18 - age2))
elif age2 == 900:
    print("Sorry Yoda, you're not from here")
else:
    print("You're old enough to vote")
    print("Please put an X in the box")

# Structure of if / elif / else block

# if condition:
#     do some code
# elif condition:
#     do some code
# else:
#     do some default code